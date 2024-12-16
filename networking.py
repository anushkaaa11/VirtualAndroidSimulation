import requests

url = "http://127.0.0.1:5000/add-app"

mock_data = {
    "device_id": "virtual_device_001",
    "os_version": "Android 12",
    "device_model": "Pixel_4_API_35",
    "memory": "4GB"
}

try:
    # Sending mock data to the backend
    response = requests.post(url, json=mock_data)

    # Logging the response from the server
    print("Server Response:", response.status_code, response.json())
except Exception as e:
    print("Error connecting to the server:", str(e))
