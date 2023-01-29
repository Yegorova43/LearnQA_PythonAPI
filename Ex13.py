import pytest
import requests
import json

class TestUserAgent:
    user_agents = [
      'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
      'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
      'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
      'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    ]

    expected_values = [
      {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
      {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
      {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
      {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
      {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    ]

    @pytest.mark.parametrize('user_agent, expected_value', zip(user_agents, expected_values))
    def test_user(self, user_agent, expected_value):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        user_agent = {'User-agent': user_agent}
        response = requests.get(url, headers=user_agent)

        platform = json.loads(response.text)['platform']
        device = json.loads(response.text)['device']
        browser = json.loads(response.text)['browser']

        expected_platform = expected_value['platform']
        expected_browser = expected_value['browser']
        expected_device = expected_value['device']

        response_dict = response.json()

        assert response.status_code == 200, "Wrong response code"
        assert 'platform' in response_dict, 'There is no field "platform" in the response'
        assert platform == expected_platform, f'Actual platform {platform} is not equal to expected platform {expected_platform}'
        assert browser == expected_browser, f'Actual browser {browser} is not equal to expected browser {expected_browser}'
        assert device == expected_device, f'Actual device {device} is not equal to expected device {expected_device}'




