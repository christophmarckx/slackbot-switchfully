import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

with open("test.txt", "r") as a_file:
    words = []

    for line in a_file:
        for word in line.split():
            words.append(word)

    i: int = 0
    x = len(words)
    while i < x:
        response = client.conversations_open(users=["UK99TQ0G6", words[i]])
        tempvar = response.get(["channel"][0])
        channelid = tempvar["id"]
        client.chat_postMessage(channel=channelid, text="Testing Python " + words[i + 1] + " your link is: " + words[i + 2] + " :art:")
        i += 3

