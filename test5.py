import requests
import json




response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"})
response_dict = response.json()
#platform = response_dict['platform']
#browser = response_dict['browser']
#device = response_dict['device']
#user_agent = response_dict['user_agent']
print(response_dict)
#print(platform, browser, device)
