import yaml
import os

# Path to config file relative to client.py
current_dir = os.path.dirname(__file__)
config_file_path = os.path.join(current_dir, '..', 'config.yaml')

# Ensure the path is correct
if not os.path.exists(config_file_path):
    raise FileNotFoundError(f"Configuration file not found at {config_file_path}")

# Load YAML configuration from file
with open(config_file_path, 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)
if config['settings']['logging']['username']:
    print("You are logged in.")
else:
    print("You are not logged in.")