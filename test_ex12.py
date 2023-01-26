import requests
class TestHeaders:
    def test_check_headers(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        print(response.headers)


        assert response.status_code == 200, "Wrong response code"
        assert 'x-secret-homework-header' in response.headers, 'There is no x-secret-homework-header in response'

