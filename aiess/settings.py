import os
import json

with open("settings.json", mode="r") as settings_file:
    json_str = settings_file.read()
    json_str = os.path.expandvars(json_str)
    settings = json.loads(json_str)

# WEB
API_KEY           = settings["api-key"]
API_RATE_LIMIT    = settings["api-rate-limit"]
PAGE_RATE_LIMIT   = settings["page-rate-limit"]
BNSITE_RATE_LIMIT = settings["bnsite-rate-limit"]

# APIV2
APIV2_CLIENT_ID     = settings["apiv2-client-id"]
APIV2_CLIENT_SECRET = settings["apiv2-client-secret"]

# STORAGE
ROOT_PATH = settings["root-path"]
DB_CONFIG = settings["db-config"]

# 3RD PARTY
BNSITE_MONGODB_URI = settings["bnsite-mongodb-uri"]
BNSITE_HEADERS     = settings["bnsite-headers"]
BNSTATS_HEADERS    = settings["bnstats-headers"]
BNPLANNER_HEADERS  = settings["bnplanner-headers"]
