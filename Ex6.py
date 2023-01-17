import requests

response = requests.get ("https://playground.learnqa.ru/api/long_redirect")
redir = response.history[0]
redir2 = response.history[1]

print(redir.url)
print(redir2.url)
