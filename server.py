from service.bot import TelegramBot
from service.translator import TranslateIndoToEnglish

newBot = TelegramBot()
updateID = None

def MakeReply(msg):
    return TranslateIndoToEnglish(msg)

while True:
    print("...")
    updates = newBot.GetUpdate(updateID)
    print(updates)
    updates = updates["result"]
    if updates:
        for item in updates:
            updateID = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = MakeReply(message)
            newBot.SendMessage(reply, from_)