import requests
import os
from dotenv import load_dotenv

edinet_url = "https://api.edinet-fsa.go.jp/api/v2/documents.json"

req_param = {
    "date": "2021-01-01",
    "type": 2,
    "Subscription-Key":
}