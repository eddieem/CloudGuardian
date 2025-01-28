# CloudGuardian - Cloud Security Configuration Analyzer
## Overview
CloudGuardian is a web application that helps users identify and mitigate potential security vulnerabilities in their cloud infrastructure by analyzing uploaded JSON configuration files and generating a security report.

## Features
- File Upload: Upload JSON configuration files containing your cloud resources and security settings.

- Configuration Analysis: Parse the uploaded JSON file and analyze the configuration for common security issues.

- Report Generation: Generate and display a security report that includes:

  - A summary of the identified security issues

  - Detailed descriptions of each issue

  - Recommendations for mitigating each issue
 
## Technology Stack
- Flask: Web framework for building the application

- Werkzeug: For file upload handling (used internally by Flask)

- jsonschema: For validating the JSON configuration files

## Assumptions
- Users will upload correctly formatted JSON files.

- The application will run in a local environment or a simple web server setup.

- Basic security checks (e.g., file size limit) are implemented for file uploads.

## Project Structure
```
CloudGuardian/
├── app/
│   ├── __init__.py
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── report.html
│   │   ├── error.html
│   │   ├── about.html
│   │   ├── help.html
│   ├── uploads/
│   │   └── .gitkeep
│   ├── app.py
│   └── security_analyzer.py
├── requirements.txt
├── README.md
└── run.py

 ```

## Setup and Running
1. **Clone the repository**
   ```sh
   git clone https://github.com/eddieem/CloudGuardian.git
   pwd # to confirm you're on the CloudGuardian repo
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```
   python run.py
   ```

4. **Open the web application:** Open your web browser and navigate to
   `http://127.0.0.1:5000`

## Usage
1. **Upload** a JSON file containing your cloud configuration.
2. The application will **analyze** the configuration and **generate a report** highliting any security issues and recommendations

## Example JSON Configuration
Here is an example of a valid JSON configuration file:
```
{
  "resources": [
    {
      "type": "virtual_machine",
      "name": "vm1",
      "open_ports": [22, 80, 443],
      "password": "weakpassword",
      "encryption": false,
      "mfa_enabled": false,
      "azure_specific": {
        "resource_group": "rg1",
        "location": "eastus",
        "vm_size": "Standard_DS1_v2"
      }
    },
    {
      "type": "storage_account",
      "name": "storage1",
      "encryption": false,
      "azure_specific": {
        "resource_group": "rg1",
        "location": "eastus",
        "account_tier": "Standard",
        "replication": "LRS"
      }
    },
    {
      "type": "database",
      "name": "db1",
      "open_ports": [],
      "password": "supersecurepassword",
      "encryption": true,
      "mfa_enabled": true,
      "azure_specific": {
        "resource_group": "rg2",
        "location": "westus",
        "db_service": "Azure SQL Database"
      }
    },
    {
      "type": "virtual_machine",
      "name": "vm2",
      "open_ports": [22, 8080],
      "password": "anotherweakpassword",
      "encryption": false,
      "mfa_enabled": false,
      "azure_specific": {
        "resource_group": "rg2",
        "location": "westus",
        "vm_size": "Standard_B2s"
      }
    },
    {
      "type": "storage_account",
      "name": "storage2",
      "encryption": true,
      "azure_specific": {
        "resource_group": "rg3",
        "location": "centralus",
        "account_tier": "Premium",
        "replication": "GRS"
      }
    }
  ]
}
```

## Screenshots
### Home Page
- This is the main page where users can upload their JSON configuration file.
  ![Home Page](https://github.com/user-attachments/assets/1ee49bff-f95c-4590-afa5-7d86eeaecaa7)
### File Upload
- Users can choose their JSON file and upload it for analysis.
  ![File Upload Form](https://github.com/user-attachments/assets/970b0896-5a46-47b0-8db2-d0c33c01024e)
### Security Report
- The security report provides a summary and detailed analysis of potential issues found in the configuration with recommendations to address the issues.
  ![Security Report](https://github.com/user-attachments/assets/82c41176-7e09-4ba4-950b-a97ffba19d21)
### Error Handling Page
- A screenshot of an error page
  ![Error Handling Page](https://github.com/user-attachments/assets/a5bc018d-142c-43bc-adf3-3ac3f780d3d1)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
