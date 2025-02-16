import json
import os

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample-data.json")

# Load the JSON file
with open(file_path, "r") as file:
    data = json.load(file)

# Print Header
print("Interface Status")
print("=" * 90)
print(f"{'DN':<55} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 90)

# Extract and print required data
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "N/A") if attributes.get("descr", "").strip() else "N/A"
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<55} {descr:<20} {speed:<8} {mtu:<6}")
