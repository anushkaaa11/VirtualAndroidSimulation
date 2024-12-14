# Virtual Android System Simulation

This project involves creating a Python-based virtual Android system capable of running basic tasks and communicating with a backend server. Below are the step-by-step instructions for each task, requirements, and an explanation of networking scripts.

---

## **Requirements**
1. **Python** (version 3.8 or later)
2. **pip** (Python package manager)
3. Libraries:
   - `os`
   - `subprocess`
   - `requests`
   - `Flask`
4. **Android Studio** (optional, for creating and managing Android Virtual Devices).
5. **QEMU** or any emulator capable of running Android systems (optional, based on task implementation).
6. **Basic Understanding of Networking** (optional, for Task 4).

---

## **Setup Instructions**

1. **Install Required Libraries:**
   ```bash
   pip install flask requests
   ```

2. **Prepare Your Virtual Environment:**
   - Install Android Studio or QEMU as needed for creating the virtual Android system.

3. **Clone or Download the Repository:**
   Save the Python scripts for each task in the same folder for easier management.

---

## **Tasks Overview and Instructions**

### **Task 1: Backend Development**
This task involves setting up a backend server using Flask to handle app data.

**Steps to Run:**
1. Save the `flask_api.py` script in your project folder.
2. Run the Flask server:
   ```bash
   python flask_api.py
   ```
3. The server will start running on `http://127.0.0.1:5000`.
4. Test the endpoints using Postman or directly through your Python client script (Task 4).

---

### **Task 2: Database Management**
This script launches a virtual Android system and performs basic tasks.

**Steps to Run:**
1. Save the `simulate_android.py` script in your project folder.
2. Ensure the Android emulator (e.g., QEMU) is installed and configured.
3. Run the script:
   ```bash
   python simulate_android.py
   ```
4. The script will:
   - Create a virtual Android environment.
   - Display basic system information.

---

### **Task 3: Virtual Android System Simulation**
This script installs a sample APK into the virtual Android system.

**Steps to Run:**
1. Save the `install_apk.py` script in your project folder.
2. Place a sample APK file in the project directory.
3. Update the APK path in the script:
   ```python
   apk_path = "path/to/sample.apk"
   ```
4. Run the script:
   ```bash
   python install_apk.py
   ```

---

### **Task 4: Basic Networking**
This task involves connecting the virtual Android system to the Flask backend server created in Task 1.

**Steps to Run:**
1. Ensure the Flask server (from Task 1) is running.
2. Save the `client_requests.py` script in your project folder.
3. Run the client script:
   ```bash
   python client_requests.py
   ```
4. The script will:
   - Add a mock app to the server.
   - Retrieve app details from the server.
   - Delete the app from the server.

---

## **Networking Scripts Explanation**

### **1. Networking in This Project**
Networking enables communication between the client script and the Flask server using HTTP protocols.

### **2. How HTTP Requests Work**
- **POST Request:** Sends data to the server (e.g., app details).
- **GET Request:** Retrieves specific data from the server (e.g., app info).
- **DELETE Request:** Removes specific data from the server (e.g., deleting an app).

### **3. Key Components in the Scripts**
- **`requests` Library:** Simplifies sending HTTP requests.
- **Error Handling:** Ensures graceful handling of errors like server disconnection.

### **4. Flow of Execution**
1. **Adding an App:** Sends a `POST` request with app details.
2. **Retrieving App Details:** Sends a `GET` request with the app ID.
3. **Deleting the App:** Sends a `DELETE` request with the app ID.

For example:
```python
response = requests.post("http://127.0.0.1:5000/add-app", json=data)
if response.status_code == 200:
    print("App added successfully.")
else:
    print("Error adding app.")
```

---

## **Notes**
- Ensure all scripts are in the same project directory.
- Test Flask API endpoints before running the networking script.
- For any errors, check:
  - Flask server logs.
  - HTTP error messages in the client script.
- Modify paths and configurations as needed for your environment.

---

