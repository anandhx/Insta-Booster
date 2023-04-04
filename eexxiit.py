# Importing Modules...
import os
import json
import random
import time
from pathlib import Path
from tqdm import tqdm
from termcolor import colored
from instagrapi import Client

# Create an instance of the Instagram client
client = Client()

# Login to your Instagram account
#.........Enter username and password 
username = input("Enter the username of the fake acccount ")
password = input("Enter the passsword of the fake acccount ")


path_to_file = f"{username}.json"
path = Path(path_to_file)

if path.is_file():
    print(f"Loading Conf of {path_to_file}")
    client.load_settings(path_to_file)
else:
    print("Please wait! Logging In!")
    client.login(username, password)
    client.dump_settings(path_to_file)
print("Logged In Successfully!!")


def console_clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')
        
        

# The username of the user whose followers you want to scrape
target_username = input("Enter The username of the user whose followers you want to scrape ")
# Get the user ID of the target user
target_user = client.user_info_by_username(target_username)
target_user_id = target_user.pk

# Get the list of the target user's followers
followers_ids = client.user_followers(target_user_id)

# Convert the user IDs to user objects
followers = []
for follower_id in tqdm(followers_ids, desc=colored("Scraping followers", "green"), unit="followers", leave=False):
    follower = client.user_info(follower_id)
    followers.append(follower)
    time.sleep(random.uniform(1, 2))

# Extract the usernames from the followers list
usernames = [follower.username for follower in followers]

# Create a dictionary containing the list of usernames
data = {"users": usernames}

# Save the dictionary to a JSON file
with open("followers.json", "w") as file:
    json.dump(data, file)

# Print the success message
print(colored("Followers successfully scraped and saved to followers.json!", "green"))
