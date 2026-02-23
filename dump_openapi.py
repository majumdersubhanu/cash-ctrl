from app.main import app
import json

with open("openapi_dump.json", "w") as f:
    json.dump(app.openapi(), f, indent=2)
