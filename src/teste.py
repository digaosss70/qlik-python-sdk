from dotenv import load_dotenv
import os
from qlik_sdk import Auth, AuthType, Config
import json

# Carrega as variáveis de ambiente
load_dotenv()

QLIK_HIOST = os.getenv("host")
QLIK_API_KEY = os.getenv("api_key")
QLIK_APP_ID = os.getenv("app_id")

auth = Auth(config=Config(host=QLIK_HIOST, auth_type=AuthType.APIKey, api_key=QLIK_API_KEY))

app_id ="abb9560b-60cc-4e56-bb8c-1b0b91105b44"
rpc_session = auth.rpc(app_id=app_id)

with rpc_session.open() as rpc_client:
    app = rpc_client.send("OpenDoc", -1, app_id)
    handle = app["qReturn"]["qHandle"]
    slist_object = rpc_client.send("GetObject", handle,"SheetList")
    slist_handle = slist_object["qReturn"]["qHandle"]
    slist_layout = rpc_client.send("GetLayout", slist_handle)
    print(slist_layout["qLayout"])