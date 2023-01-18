import requests
import json
import time


#создаем задачу
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(response1.text)
token = obj['token']
seconds = obj['seconds']

#запрос с token ДО того, как задача готова
payload = {"token": token}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = payload)

#убеждаемся в правильности поля status
obj2 = json.loads(response2.text)
status2 = obj2['status']
try:
    status2 = "Job is NOT ready"
except:
    print("Неправильный токен")

#ждем нужное количество секунд
time.sleep(int(seconds))

#запрос c token ПОСЛЕ того, как задача готова
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = payload)

#убеждаемся в правильности поля status и наличии поля result
obj3 = json.loads(response3.text)
status3 = obj3['status']
result3 = obj3['result']
try:
    status3 = "Job is ready"
    result3 is not None
    print(status3)
except:
    print("Что-то пошло не так")



