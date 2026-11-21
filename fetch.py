import requests
import json
import time
import os

BASE_URL = "https://ll.thespacedevs.com/2.3.0/launches/previous/?limit=100"
FILE_NAME = "launches_raw.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        all_launches = json.load(f)
    print(f"Resuming from {len(all_launches)} launches already downloaded.")
else:
    all_launches = []

current_offset = len(all_launches)
if current_offset > 0:
    current_url = f"{BASE_URL}&offset={current_offset}"
else:
    current_url = BASE_URL

print("Starting to fetch launch data.")

while current_url:
    response = requests.get(current_url, timeout=60)
    
    if response.status_code == 429:
        wait_seconds = int(response.headers.get("retry-after", 300))
        print(f"Rate limit reached. Waiting {wait_seconds} seconds (~{wait_seconds // 60} mins)...")
        time.sleep(wait_seconds)
        continue

    response.raise_for_status()
    data = response.json()

    for launch in data.get("results", []):
        status = launch.get("status") or {}
        provider = launch.get("launch_service_provider") or {}
        rocket = launch.get("rocket") or {}
        config = rocket.get("configuration") or {}
        pad = launch.get("pad") or {}
        country = pad.get("country") or {}
        mission = launch.get("mission") or {}
        orbit = mission.get("orbit") or {}

        launch_info = {
            "Launch ID": launch.get("id"),
            "Name": launch.get("name"),
            "Status": status.get("name"),
            "Date": launch.get("net"),
            "Provider": provider.get("name"),
            "Rocket": config.get("full_name"),
            "Pad": pad.get("name"),
            "Country": country.get("alpha_3_code"),
            "Country Name": country.get("name"),
            "Mission Type": mission.get("type"),
            "Orbit": orbit.get("name")
        }
        all_launches.append(launch_info)

    print(f"Fetched {len(all_launches)} / {data.get('count', '?')} records...")

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(all_launches, f, indent=2)

    current_url = data.get("next")

    if current_url:
        time.sleep(2)

print("All launch data successfully downloaded and saved to launches_raw.json!")
