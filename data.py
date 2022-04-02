import requests

def get_data(url):
    try:
        response = requests.get(url)
        print(response.status_code)
        return response.json()
    except:
        print(response.status_code)
        return "Error".encode("json")