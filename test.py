
import json

with open('/Users/sigurdrolfsnes/Documents/Discord bot/Discord bot/Bank.json') as f:
    data = json.load(f)
    print(f.read())
    print(data)
    print(data['323911793110371630']["wallet"])