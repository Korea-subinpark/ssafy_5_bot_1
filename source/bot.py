from slacker import Slacker
from flask import Flask, request, make_response
import json
import requests
import crawling_module
import pascucci_scrap
import random
import multiprocessing
from threading import Thread

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

slack_token = "xoxb-503818135714-507655945173-nirvXFLZ5okONQNcqnqPPgiE"
slack_client_id = "503818135714.507653967109"
slack_client_secret = "f3f1ed75759311aef663a80e0b7c883f"
slack_verification = "hN9lJABBCfl37mBeUs9jVjWY"

slack = Slacker(slack_token)


# Send a message to #general channel
# slack.chat.post_message('#day4', 'Slacker Test')


# Get users list
# response = slack.users.list()
# users = response.body['members']

# Upload a file
# slack.files.upload('hello.txt')


def identifyintents(text, user_key):
    data_send = {
        'query': text,
        'sessionId': user_key,
        'lang': 'ko',
    }

    data_header = {
        'Authorization': 'Bearer c4c99af895fa4b2384ca79d8fcb6a9eb',
        'Content-Type': 'application/json; charset=utf-8'
    }

    dialog_flow_url = 'https://api.dialogflow.com/v1/query?v=20150910'
    res = requests.post(dialog_flow_url, data=json.dumps(data_send), headers=data_header)

    if res.status_code != requests.codes.ok:
        return '오류가 발생했습니다.'

    data_receive = res.json()
    result = {
        "speech": data_receive['result']['fulfillment']['speech'],
        "intent": data_receive['result']['metadata']['intentName']
    }

    return result


# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        event_queue.put(slack_event)
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

def deffered_event_processing(queue):
    while True:
        # 큐가 비어있지 않은 경우 로직 실행
        if not queue.empty():
            slack_event = queue.get()

            channel = slack_event["event"]["channel"]
            text = slack_event["event"]["text"]

            user_text = text.split("> ")[1]

            # identifyIntents
            intent_identifier = identifyintents(user_text, "session")  # intent = {speech, intent}

            message = ""
            # Event Handle (data, intent)
            if intent_identifier["intent"] == "coffeebean":
                slack.files.upload('../img/coffeebean.jpg', channels=channel)
                message = intent_identifier["speech"] + "\n"
                message += crawling_module.coffeebean()
            elif intent_identifier["intent"] == "hollys":
                slack.files.upload('../img/hollyscoffee.gif', channels=channel)
                message = intent_identifier["speech"] + "\n"
                message += crawling_module.hollys()
            elif intent_identifier["intent"] == "pascucci":
                slack.files.upload("../img/pascucci.jpg", channels=channel)
                message = intent_identifier["speech"] + "\n"
                message += pascucci_scrap.passcucci()
            elif intent_identifier["intent"] == "menu":
                path = "../coffeeMenu/" + str(random.randint(1, 12)) + ".PNG"
                slack.files.upload(path, channels=channel)
                message = intent_identifier["speech"] + "\n"
            else:
                message = intent_identifier["speech"]

            # message = "Slacker Test"

            # slack.chat.post_message(channel, message)
            slack.chat.post_message(channel, message)


@app.route('/', methods=['POST', 'GET'])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    event_queue = multiprocessing.Queue()

    p = Thread(target=deffered_event_processing, args=(event_queue,))
    p.start()
    print("thread start!")

    app.run(host='0.0.0.0', port=8080)
    p.join()
