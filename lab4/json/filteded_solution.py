import json
import os

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample-data.json")

# Load the JSON file
with open(file_path, "r") as file:
    data = json.load(file)

# List of required interfaces
required_interfaces = {
    "topology/pod-1/node-201/sys/phys-[eth1/33]",
    "topology/pod-1/node-201/sys/phys-[eth1/34]",
    "topology/pod-1/node-201/sys/phys-[eth1/35]"
}

# Print Header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<55} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

# Extract and print only required data
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]

    # Print only if DN is in the required interfaces list
    if dn in required_interfaces:
        descr = attributes.get("descr", "N/A") if attributes.get("descr", "").strip() else "N/A"
        speed = attributes["speed"]
        mtu = attributes["mtu"]

        print(f"{dn:<55} {descr:<20} {speed:<8} {mtu:<6}")
