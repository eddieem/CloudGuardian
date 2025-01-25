import json
import logging
from jsonschema import validate, ValidationError

# Configure logging
logging.basicConfig(filename='security_analyzer.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# JSON schema for validation
schema = {
    "type": "object",
    "properties": {
        "resources": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "name": {"type": "string"},
                    "open_ports": {"type": "array", "items": {"type": "integer"}},
                    "password": {"type": "string"},
                    "encryption": {"type": "boolean"},
                    "mfa_enabled": {"type": "boolean"},
                    "azure_specific": {
                        "type": "object",
                        "properties": {
                            "resource_group": {"type": "string"},
                            "location": {"type": "string"},
                            "vm_size": {"type": "string"},
                            "account_tier": {"type": "string"},
                            "replication": {"type": "string"},
                            "db_service": {"type": "string"}
                        },
                        "required": ["resource_group", "location"]
                    }
                },
                "required": ["type", "name"]
            }
        }
    },
    "required": ["resources"]
}

def analyze_configuration(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Validate JSON schema
        validate(instance=data, schema=schema)
        
        issues = []
        
        for resource in data['resources']:
            resource_issues = []
            recommendations = []

            if resource['type'] == 'virtual_machine':
                if 'weakpassword' in resource['password']:
                    resource_issues.append('Weak password detected.')
                    recommendations.append('Use a strong, complex password.')
                if not resource['encryption']:
                    resource_issues.append('Data encryption is disabled.')
                    recommendations.append('Enable data encryption to protect sensitive information.')
                if not resource['mfa_enabled']:
                    resource_issues.append('Multi-Factor Authentication is not enabled.')
                    recommendations.append('Enable Multi-Factor Authentication to enhance security.')
            
            elif resource['type'] == 'storage_account':
                if not resource['encryption']:
                    resource_issues.append('Data encryption is disabled.')
                    recommendations.append('Enable data encryption to protect stored data.')
            
            elif resource['type'] == 'database':
                if 'supersecurepassword' not in resource['password']:
                    resource_issues.append('Password might not be secure.')
                    recommendations.append('Ensure the database password is strong and complex.')
            
            if resource_issues:
                issues.append({
                    'resource': resource['name'],
                    'type': resource['type'],
                    'issues': resource_issues,
                    'recommendations': recommendations
                })
        
        report = generate_report(issues)
        return report
    
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in file: %s", file_path)
        raise
    except ValidationError as e:
        logging.error("JSON validation error: %s", e.message)
        raise
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e))
        raise

def generate_report(issues):
    report = {
        'summary': f"{len(issues)} security issues found.",
        'details': issues
    }
    return report
