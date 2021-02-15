import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

with open("github-student-packs.txt", "r", encoding='utf-8') as a_file:
    words = []

    for line in a_file:
        for word in line.split():
            words.append(word)

    i: int = 0
    amountofwords = len(words)

    while i < amountofwords:
        response = client.conversations_open(users=["UK99TQ0G6", words[i]])
        tempvar = response.get(["channel"][0])
        channelid = tempvar["id"]
        client.chat_postMessage(channel=channelid, text="Hey " + words[i+1] + "! Are you ready to start your Switchfully Java adventure? \n"
                                                        "One of the final preparations we have for you is to upgrade your Github account! \n"
                                                        "_*Why?*_ As a Java developer you need some tools that are usually not free (_IntelliJ Ultimate Edition costs € 499 / year_ :heavy_dollar_sign:) ... "
                                                        "Luckily Switchfully is a recognized codeschool - and we get this for free! (yah! :gift:) \n"
                                                        "_*How?*_ Upgrading your Github account (and receiving the Github Student Pack goodies) is easy: \n"
                                                        "1. Log in into your Github account \n"
                                                        "2. Visit this link: :link: <" + words[i+2] + "> :link: \n"
                                                        "3. Done! Celebrate! :tada: \n"
                                                        "_*Problems/Questions?*_ If you run into any issues, just let us know and we'll help you out. :sos: \n"
                                                        "Looking forward to seeing you the 1st of February! :wave:")
        i += 3




