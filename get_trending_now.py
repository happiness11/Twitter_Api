import json
from auth import get_api

api = get_api()


DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print (json.dumps(dub_trends, indent=1))