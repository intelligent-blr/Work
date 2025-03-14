import requests
from time import sleep

response = requests.get("https://api.github.com/users/SciWake")
data = response.json()
for k, v in data.items():
    print(f"{k}: {v}")

followers_data = requests.get(data["followers_url"]).json()

print(followers_data)

base_url = "https://api.github.com/users/"

all_followers = 0
for follower in followers_data:
    follower_data = requests.get(base_url + follower["login"]).json()
    print(f"{follower_data["login"]} = {follower_data['followers']}")
    sleep(0.5)
