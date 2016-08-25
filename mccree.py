# -*- coding: utf-8 -*-
import os
import time
import string

from slackclient import SlackClient
# starterbot's ID as an environment variable
BOT_ID = os.environ.get("MCCREE_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">:"
THE_QUESTION = "what time is it"
HIGH_NOON = "High Noon"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('MCCREE_BOT_TOKEN'))

def handle_command(command, channel):
    if THE_QUESTION in command or "what time it is" in command :
        response = "It's High Noon. . ."
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    elif HIGH_NOON.lower() in command:
        response = "You're damn right"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    elif command.startswith(("what time")) or string.replace(command, "whenever", "").startswith(("when")):
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=HIGH_NOON, as_user=True)
    elif command.lower().startswith((AT_BOT.lower()+" fuck you")):
        slack_client.api_call("chat.postMessage", channel=channel, text="What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.", as_user=True)
#    elif command.startswith(("who are you")):
#        slack_client.api_call("chat.postMessage", channel=channel,
#                          text="/giphy mccree", as_user=True)

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output:
                if output['user'] == BOT_ID:
                    return None, None
                return output['text'].lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("mccree is here!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
