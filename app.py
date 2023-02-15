import os
import requests
import json
from datetime import datetime, timezone, timedelta

# Set up Github API endpoint and user
API_ENDPOINT = "https://api.github.com"
GITHUB_USER = "<GITHUB_USERNAME>"  # replace with your Github username

# Set up authentication using a Github personal access token
GITHUB_TOKEN = "<GITHUB_TOKEN>"  # replace with your Github personal access token
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# Set up file to store timestamp of last run
TIMESTAMP_FILE = "last_run_timestamp.txt"

# Load last run timestamp if it exists, otherwise use current time
if os.path.isfile(TIMESTAMP_FILE):
    with open(TIMESTAMP_FILE, "r") as f:
        last_run_timestamp = datetime.fromisoformat(f.read())
else:
    last_run_timestamp = datetime.now(timezone.utc) - timedelta(days=1)

# Send GET request to Github API to retrieve list of user's gists
response = requests.get(f"{API_ENDPOINT}/users/{GITHUB_USER}/gists", headers=headers)

# Parse response JSON to extract list of gists and their timestamps
gists = json.loads(response.content)
new_gists = []
for gist in gists:
    gist_timestamp = datetime.fromisoformat(gist["created_at"].replace("Z", "+00:00"))
    if gist_timestamp > last_run_timestamp:
        new_gists.append(gist)

# Display list of all gists or new gists depending on whether any new ones were found
if len(new_gists) == 0:
    print("No new gists found.")
else:
    print("New gists found:")
    for gist in new_gists:
        print(f"- {gist['html_url']} ({gist['description']})")

# Save current timestamp to file for next run
with open(TIMESTAMP_FILE, "w") as f:
    f.write(datetime.now(timezone.utc).isoformat())
