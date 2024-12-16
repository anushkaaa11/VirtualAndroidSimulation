import requests
import platform
import json

BACKEND_URL = "http://127.0.0.1:5000/add-app"

def get_mock_device_data():
    return {
        "app_name": "VirtualAndroid",
        "version": platform.version(),
        "description": f"OS: {platform.system()} {platform.release()}, Device: {platform.node()}, RAM: 2GB"
    }

def send_data_to_server():
    data = get_mock_device_data()
    
    try:
        response = requests.post(BACKEND_URL, json=data)
        
        if response.status_code == 200:
            print("Data sent successfully!")
            print("Server Response:", response.json())
        else:
            print(f"Failed to send data. HTTP Status Code: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print("Error occurred while connecting to the server:", e)

if __name__ == "__main__":
    send_data_to_server()
