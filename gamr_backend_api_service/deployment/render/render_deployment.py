from dataclasses import dataclass
import requests  # type: ignore
from gamr_backend_api_service.settings import Settings


@dataclass
class RenderDeployment:

    def get_service_id(self):
        url = "https://api.render.com/v1/services?includePreviews=true&limit=20"

        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {Settings.RENDER_API_TOKEN}",
        }

        response = requests.get(url, headers=headers)
        return response

    def deploy_service(self, service_id: str):
        url = f"https://api.render.com/v1/services/{service_id}/deploys"

        payload = {"clearCache": "do_not_clear"}
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {Settings.RENDER_API_TOKEN}",
        }

        response = requests.post(url, json=payload, headers=headers)

        return response


def trigger_render_deployment():
    render_deployment = RenderDeployment()
    response = render_deployment.get_service_id()
    service_id = response.json()[0]["service"]["id"]
    render_deployment.deploy_service(service_id)
