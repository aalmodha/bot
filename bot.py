
from flask import Flask, request, jsonify
from webexteamssdk import WebexTeamsAPI
import os

# get environment variables
WT_BOT_TOKEN = os.environ['WT_BOT_TOKEN']

# uncomment next line if you are implementing a notifier bot
#WT_ROOM_ID = os.environ['WT_ROOM_ID']

# uncomment next line if you are implementing a controller bot
#WT_BOT_EMAIL = os.environ['WT_BOT_EMAIL']

# start Flask and WT connection
app = Flask(__name__)
api = WebexTeamsAPI(access_token=WT_BOT_TOKEN)
#message = "Hi, I am a Webex Teams bot. Have a great day ☀! "
#api.messages.create(toPersonEmail='aalmodha@cisco.com', markdown=message)

# defining the decorater and route registration for incoming alerts
@app.route('/', methods=['POST'])
def alert_received():
    raw_json = request.json()
    message = api.messages.get(raw_json['data']['id'])
    #print(raw_json)


    if message.personEmail != 'aalmodha@webex.bot':
        api.messages.create(toPersonEmail=messages.p, markdown='Hi, i can talk now')



    # uncomment if you are implementing a controller bot
    '''
    WT_ROOM_ID = raw_json['data']['roomId']
    personEmail_json = raw_json['data']['personEmail']
    if personEmail_json != WT_BOT_EMAIL:
        api.messages.create(roomId=WT_ROOM_ID, markdown=message)
    '''

    return jsonify({'success': True})

if __name__=="__main__":
    app.run()