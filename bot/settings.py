import os
import json

with open("settings.json", mode="r") as settings_file:
    json_str = settings_file.read()
    json_str = os.path.expandvars(json_str)
    settings = json.loads(json_str)

# DISCORD
API_KEY = settings["discord-api-key"]