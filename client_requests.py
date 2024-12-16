import requests
import json

BASE_URL = "http://127.0.0.1:5000"

mock_data = {
    "app_name": "TestApp",
    "version": "1.0.0",
    "description": "A test application."
}

def add_app():
    endpoint = f"{BASE_URL}/add-app"
    try:
        response = requests.post(endpoint, json=mock_data)
        if response.status_code == 200:
            print("App added successfully:", response.json())
        else:
            print(f"Failed to add app: {response.status_code}, {response.text}")
    except Exception as e:
        print("Error during POST request:", e)

def get_app(app_id):
    endpoint = f"{BASE_URL}/get-app/{app_id}"
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            print("App details retrieved successfully:", response.json())
        else:
            print(f"Failed to retrieve app: {response.status_code}, {response.text}")
    except Exception as e:
        print("Error during GET request:", e)

def delete_app(app_id):
    endpoint = f"{BASE_URL}/delete-app/{app_id}"
    try:
        response = requests.delete(endpoint)
        if response.status_code == 200:
            print("App deleted successfully:", response.json())
        else:
            print(f"Failed to delete app: {response.status_code}, {response.text}")
    except Exception as e:
        print("Error during DELETE request:", e)

if __name__ == "__main__":
    print("Adding an app...")
    add_app()

    print("\nRetrieving the app with ID 1...")
    get_app(1)

    print("\nDeleting the app with ID 1...")
    delete_app(1)
