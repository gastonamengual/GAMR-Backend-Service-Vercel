from dataclasses import dataclass

import firebase_admin
from firebase_admin import firestore

from app.models.user import User
from app.settings import Settings

def get_credentials() -> dict[str, str]:
    CREDENTIALS_DICT = {
        "type": "service_account",
        "project_id": Settings.PROJECT_ID,
        "private_key": Settings.PRIVATE_KEY,
        "private_key_id": Settings.PRIVATE_KEY_ID,
        "client_email": Settings.CLIENT_EMAIL,
        "client_id": Settings.CLIENT_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40imagerecognitionapp-15216.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com",
    }
    return CREDENTIALS_DICT

@dataclass
class FirestoreConnector:
    def __post_init__(self):
        if not firebase_admin._apps:
            credentials = get_credentials()
            cred = firebase_admin.credentials.Certificate(credentials)
            firebase_admin.initialize_app(cred)

    @property
    def _db(self):
        return firestore.client()

    def add_user(self, username):
        doc_ref = self._db.collection("users").document()
        doc_ref.set(
            {
                "username": username,
            }
        )

    def get_all_users(self) -> list[User]:
        users = []
        docs = self._db.collection("users").stream()
        for doc in docs:
            user = User(username=doc.to_dict()["username"])
            users.append(user)
        return users
