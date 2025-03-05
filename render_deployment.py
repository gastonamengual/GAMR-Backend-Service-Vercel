import requests  # type: ignore
from gamr_backend_api_service.settings import Settings


def get_service_id() -> requests.Response:
    url = "https://api.render.com/v1/services?includePreviews=true&limit=20"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {Settings.RENDER_API_TOKEN}",
    }

    response = requests.get(url, headers=headers)
    return response


def deploy_service(service_id: str) -> requests.Response:
    url = f"https://api.render.com/v1/services/{service_id}/deploys"

    payload = {"clearCache": "do_not_clear"}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {Settings.RENDER_API_TOKEN}",
    }

    response = requests.post(url, json=payload, headers=headers)

    return response


response = get_service_id()
service_id = response.json()[0]["service"]["id"]
print(f"Retrieved service with id: {service_id}")
response = deploy_service(service_id)
if response.ok:
    print("Render deployment triggered successfully")
