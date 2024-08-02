from dotenv import load_dotenv
import os
from qlik_sdk import Apps, AuthType, Config

# Carrega as variáveis de ambiente
load_dotenv()

QLIK_HIOST = os.getenv("host")
QLIK_API_KEY = os.getenv("api_key")

apps = Apps(Config(host=QLIK_HIOST, auth_type=AuthType.APIKey, api_key=QLIK_API_KEY))

# app is fetched from the REST /v1/apps/{app_id}
app = apps.get("e927666f-2878-4ea9-b099-cadcf183177a")

# opens a websocket connection against the Engine API and gets the app layout
with app.open():
    app_info = app.get_app_layout()
    #app_info = app.get_variables()
    print(app_info)