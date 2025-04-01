from fastapi import APIRouter, Response
from prometheus_client import CONTENT_TYPE_LATEST

from gamr_backend_api_service.monitoring import PROMETHEUS_MONITOR

router = APIRouter()


@router.get("/metrics")
async def metrics() -> Response:
    return Response(
        PROMETHEUS_MONITOR.collect_metrics(), media_type=CONTENT_TYPE_LATEST
    )
