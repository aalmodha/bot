
from flask import Flask, request, jsonify
from webexteamssdk import WebexTeamsAPI
import os

# get environment variables
WT_BOT_TOKEN = os.environ['WT_BOT_TOKEN']

app = Flask(__name__)
api = WebexTeamsAPI(access_token=WT_BOT_TOKEN)
#message = "Hi, I am a Webex Teams bot. Have a great day ☀! "
#api.messages.create(toPersonEmail='aalmodha@cisco.com', markdown=message)

@app.route('/', methods=['POST'])
def alert_received():
    raw_json = request.json()
    message = api.messages.get(raw_json['data']['id'])
    #print(raw_json)


    if message.personEmail != 'aalmodha@webex.bot':
        api.messages.create(toPersonId=message.personId, markdown='Hi, i can talk now')

 
    return jsonify({'success': True})

if __name__=="__main__":
    app.run()