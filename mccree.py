import os
import time
from slackclient import SlackClient
# starterbot's ID as an environment variable
BOT_ID = os.environ.get("MCCREE_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">:"
THE_QUESTION = "what time is it"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('MCCREE_BOT_TOKEN'))


def handle_command(command, channel):
    if THE_QUESTION in command:
        response = "It's High Noon. . ."
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    if "what time it is" in command :
        response = "It's High Noon. . ."
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    if "when" in command:
        response = "High Noon"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output:
                # return text after the @ mention, whitespace removed
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
