from slacker import Slacker
from flask import Flask, request, make_response
import json

app = Flask(__name__)

slack_token = "xoxb-503818135714-507655945173-yuzdJQ4x8erVXPDw31lfVj4X"
slack_client_id = "503818135714.507653967109"
slack_client_secret = "f3f1ed75759311aef663a80e0b7c883f"
slack_verification = "hN9lJABBCfl37mBeUs9jVjWY"

slack = Slacker(slack_token)

# Send a message to #general channel
slack.chat.post_message('#day4', 'Slacker Test')


# Get users list
# response = slack.users.list()
# users = response.body['members']

# Upload a file
# slack.files.upload('hello.txt')

# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]

        # funcName(text)
        message = " "

        # slack.chat.post_message(channel, message)
        slack.chat.post_message(channel, "Slacker Test")

        return make_response("App mention message has been sent", 200, )

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                                 "application/json"
                                                             })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


@app.route('/', methods=['POST', 'GET'])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
