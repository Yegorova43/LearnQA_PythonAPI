import requests
#1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
#2
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
#3
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = 'post')

#4
                                      #проверяем метод GET
method_lst = ['get', 'post', 'put', 'delete']

get_not_200 = []
not_get_200 = []
for method in method_lst:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
    code = response.status_code
    if method =='get' and code !=200:
        get_not_200.append(method)
    if method !='get' and code ==200:
        not_get_200.append(method)

print('Ошибки по методу GET: Метод GET, статус не 200:'+ str(get_not_200))
print('Ошибки по методу GET: Метод не GET, но статус 200:'+ str(not_get_200))

                                      #проверяем метод POST
post_not_200 = []
not_post_200 = []
for method in method_lst:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    code = response.status_code
    if method =='post' and code !=200:
        post_not_200.append(method)
    if method !='post' and code ==200:
        not_post_200.append(method)

print('Ошибки по методу POST: Метод POST, статус не 200:'+ str(post_not_200))
print('Ошибки по методу POST: Метод не POST, но статус 200:'+ str(not_post_200))

                                     #проверяем метод PUT
put_not_200 = []
not_put_200 = []
for method in method_lst:
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    code = response.status_code
    if method =='put' and code !=200:
        put_not_200.append(method)
    if method !='put' and code ==200:
        not_put_200.append(method)

print('Ошибки по методу PUT: Метод PUT, статус не 200:'+ str(put_not_200))
print('Ошибки по методу PUT: Метод не PUT, но статус 200:'+ str(not_put_200))

                                    #проверяем метод DELETE
delete_not_200 = []
not_delete_200 = []
for method in method_lst:
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    code = response.status_code
    if method =='delete' and code !=200:
        delete_not_200.append(method)
    if method !='delete' and code ==200:
        not_delete_200.append(method)

print('Ошибки по методу DELETE: Метод DELETE, статус не 200:'+ str(delete_not_200))
print('Ошибки по методу DELETE: Метод не DELETE, но статус 200:'+ str(not_delete_200))