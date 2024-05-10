# Uncomment the imports below before you add the function code
import os
import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    """function"""

    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print(f"GET from {request_url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except requests.RequestException as e:
        # If any error occurs
        print(f"Network exception occurred : {e}")


def analyze_review_sentiments(text):
    """function"""

    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except requests.RequestException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    """function"""

    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except requests.RequestException as e:
        print(f"Network exception occurred : {e}")


# Add code for posting review
