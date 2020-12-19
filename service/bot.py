import requests
import configparser as cfg
import json

class TelegramBot:
    def __init__(self):
        self.token = self.GetBotToken()
        self.host = "https://api.telegram.org/bot{}".format(self.token)

    def GetUpdate(self, offset=None):
        url = self.host + "/getUpdates?timeout=100"
        if offset:
            url += "&offset={}".format(offset + 1)
        print(url)
        r = requests.get(url)
        return json.loads(r.content)

    def SendMessage(self, msg, chatID):
        url = self.host + "/sendMessage?chat_id={}&text={}".format(chatID, msg)
        if msg is not None:
            requests.get(url)

    def GetBotToken(self):
        parser = cfg.ConfigParser()
        parser.read("config.cfg")
        return parser.get("creds", "token")