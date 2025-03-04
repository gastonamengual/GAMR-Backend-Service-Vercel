import uvicorn

from gamr_backend_api_service.api import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "gamr_backend_api_service.api:create_app",
        factory=True,
        host="0.0.0.0",
        port=8080,
        reload=True,
    )

# uvicorn gamr_backend_api_service.api:create_app --host 0.0.0.0 --port 8000 --reload
