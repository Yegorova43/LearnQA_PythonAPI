import requests
class TestHeaders:
    def test_check_headers(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        print(response.text)


        assert response.status_code == 200, "Wrong response code"
        assert 'success' in response.text, 'There is no success in response'