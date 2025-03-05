FROM python:3.12-slim

ARG PACKAGE_VERSION

WORKDIR /app

RUN pip install --upgrade pip && pip install gamr-backend-api-service==${PACKAGE_VERSION}

EXPOSE 8080

CMD ["python", "-m", "gamr_backend_api_service"]

# docker build --build-arg PACKAGE_VERSION=1.0.4 -t gamr_backend_api_service .

# docker run -p 8080:8080 --env-file=.env -e HOST=0.0.0.0 -e PORT=8080 gamr_backend_api_service
