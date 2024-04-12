import json
import os
def lambda_handler(event, context):
    return os.getenv("ENV_NAME")
