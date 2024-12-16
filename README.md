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

## Using Android Studio in This Assignment

### Purpose of Android Studio in the Assignment
Android Studio was utilized in this assignment to:
- Build and generate the APK file for testing and installation in the virtual Android system.
- Manage and simulate a virtual Android environment (via the AVD Manager).
- Debug and manage the Android application lifecycle.

### Prerequisites
Before using Android Studio, ensure:
1. **System Requirements** are met:
   - Minimum 4 GB RAM (8 GB recommended).
   - Java Development Kit (JDK) installed.
   - Sufficient disk space for Android Studio and the Android SDK.
2. **Android Studio Installed**
   - [Download here](https://developer.android.com/studio).
3. **Android Virtual Device (AVD)** setup in the SDK Manager.

---

### How Android Studio Was Used

#### 1. **Creating the Project**
1. Open Android Studio and create a new project:
   - Select **Empty Activity** template.
   - Configure the project settings (e.g., name, location, minimum SDK).
2. The project structure was generated automatically, with the main files located in:
   - `app/src/main/java/` for source code.
   - `app/src/main/res/` for resources like layouts and strings.

#### 2. **Building the APK File**
1. Open the project in Android Studio.
2. Navigate to the menu:
   - **Build > Build Bundle(s)/APK(s) > Build APK(s).**
3. After the build completes, the APK is generated at:
   - `app/build/outputs/apk/debug/app-debug.apk`
4. This APK was used for testing in the virtual Android system simulation.

#### 3. **Setting Up the Emulator**
1. Open **AVD Manager** in Android Studio:
   - Tools > Device Manager > Create Device.
2. Configure the virtual device:
   - Choose a device model (e.g., Pixel 4).
   - Select a system image (e.g., Android 13).
   - Configure settings like RAM, storage, etc.
3. Launch the emulator from Android Studio or via the command line using `emulator -avd <avd_name>`.

#### 4. **Debugging the Application**
1. Use Android Studio’s debugger to identify issues in the application.
2. Install the APK directly from Android Studio:
   - Connect the emulator and click **Run** to deploy and test the app.

---

### How to Use Android Studio for This Assignment

#### Step 1: Install Android Studio
- Download and install Android Studio from the [official site](https://developer.android.com/studio).
- During setup, ensure you download the required SDK components.

#### Step 2: Clone or Create Your Project
- Open Android Studio.
- If cloning, choose **File > New > Project from Version Control > Git**, and provide the repository URL.

#### Step 3: Build the APK
1. Open the project.
2. Navigate to **Build > Build Bundle(s)/APK(s) > Build APK(s).**
3. Note the path where the APK is saved (e.g., `app/build/outputs/apk/debug/app-debug.apk`).

#### Step 4: Set Up the Emulator
1. Open **AVD Manager** (Tools > Device Manager).
2. Create a virtual device with your preferred configurations.
3. Start the emulator using the play button in **AVD Manager** or via the command line:
   ```bash
   emulator -avd <avd_name>
   ```

#### Step 5: Install and Test the APK
1. Install the APK using Android Studio or `adb` command:
   ```bash
   adb install <path_to_apk>
   ```
2. Run the app in the emulator to verify its functionality.

---

### Common Issues and Solutions
- **Emulator not booting**: Ensure the AVD settings are compatible with your system’s hardware.
- **APK installation failed**: Check if the emulator is running and ensure the APK path is correct.
- **Build errors**: Resolve dependencies or Gradle issues in the `build.gradle` file.

---

By following these steps, you can replicate or extend the work done in this assignment using Android Studio.

---

## **Notes**
- Ensure all scripts are in the same project directory.
- Test Flask API endpoints before running the networking script.
- For any errors, check:
  - Flask server logs.
  - HTTP error messages in the client script.
- Modify paths and configurations as needed for your environment.

---

