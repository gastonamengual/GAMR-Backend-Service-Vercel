import time
from dataclasses import dataclass, field

from prometheus_client import Counter, Gauge, Histogram, generate_latest


@dataclass
class PrometheusMonitor:
    requests_total: Counter = field(init=False)
    request_duration_seconds: Histogram = field(init=False)
    memory_usage_bytes: Gauge = field(init=False)
    cpu_usage_seconds: Counter = field(init=False)

    def __post_init__(self) -> None:
        self.requests_total = Counter(
            "requests_total",
            "Total number of requests",
            labelnames=["method", "endpoint"],
        )
        self.request_duration_seconds = Histogram(
            "request_duration_seconds",
            "Histogram of request duration in seconds",
            labelnames=["endpoint"],
        )

        self.memory_usage_bytes = Gauge(
            "memory_usage_bytes", "Memory usage of the service in bytes"
        )

        self.cpu_usage_seconds = Counter(
            "cpu_usage_seconds_total", "Total CPU usage time in seconds"
        )

    def start_time(self) -> float:
        return time.time()

    def get_duration(self, start_time: float) -> float:
        return time.time() - start_time

    def observe_request(self, method: str, endpoint: str, duration: float) -> None:
        self.requests_total.labels(method=method, endpoint=endpoint).inc()
        self.request_duration_seconds.labels(endpoint=endpoint).observe(duration)

    def update_memory_usage(self, memory_usage: float) -> None:
        self.memory_usage_bytes.set(memory_usage)

    def update_cpu_usage(self, cpu_usage: float) -> None:
        self.cpu_usage_seconds.inc(cpu_usage)

    def collect_metrics(self) -> bytes:
        return generate_latest()  # type: ignore


PROMETHEYS_MONITOR = PrometheusMonitor()
