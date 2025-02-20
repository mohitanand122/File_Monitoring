# File_Monitoring
*Comapny*: CODTECH IT SOLUTION
*NAME*: MOHIT ANAND
*INTERN ID*: 
*DOMAIN*: CYBER SECURITY
*DURATION*: 4 WEEKS
*MENTOR*: NEELA SANTOSH

## Introduction
The Directory Monitoring System is an advanced file integrity monitoring tool designed to track changes within a specified directory. This project ensures that any modifications, additions, or deletions within a directory are logged and notified in real-time. The system utilizes cryptographic hashing to detect unauthorized file changes, making it a valuable asset for security-conscious users and organizations.

## Features
- **Real-time File Monitoring:** Continuously monitors a directory for any changes.
- **SHA-256 Hashing:** Ensures data integrity by computing file hashes.
- **Change Detection:** Identifies new files, modifications, and deletions.
- **Cross-Platform Compatibility:** Works on Windows and Linux.
- **Automatic Directory Setup:** Creates a default test directory if no valid directory is provided.
- **Minimal Resource Usage:** Efficiently monitors files without excessive CPU or memory usage.

## How It Works
1. **Directory Selection:** The user specifies a directory to monitor, or the system defaults to a predefined test directory.
2. **Initial Hashing:** The system calculates SHA-256 hashes for all files in the directory.
3. **Continuous Monitoring:** The program runs in an infinite loop, checking the directory every 10 seconds.
4. **Change Detection:**
   - If a new file appears, it is logged as a new entry.
   - If a file is modified, its previous hash is compared with the new one, and changes are reported.
   - If a file is deleted, it is logged as removed.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/CODTECH-IT-SOLUTION/Directory-Monitor.git
   cd Directory-Monitor
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script:
   ```sh
   python monitor.py
   ```

## Usage
1. When prompted, enter the directory path to monitor.
2. If no directory is entered, the script will create and use a default test directory.
3. Any detected changes will be displayed in the console.

## Security & Use Cases
- **Security Audits:** Helps track unauthorized modifications in critical directories.
- **Data Integrity Verification:** Ensures files remain unchanged unless intended.
- **System Monitoring:** Detects suspicious activity in system logs or configurations.

## Future Enhancements
- **Email Notifications:** Alert users of detected changes via email.
- **Log File Generation:** Store change logs for future analysis.
- **GUI Interface:** Provide a user-friendly dashboard for monitoring changes.

## License
This project is open-source under the MIT License.
## Output
![image](https://github.com/user-attachments/assets/582086fb-1ff0-42f9-8f6a-231566ef31cd)
