from functools import wraps
import requests


def error_handler(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            response = f(*args, **kwargs)
        except:
            return {"error": True, "message": "Something went wrong!"}
        try:
            data = {"error": False, "result": response.json()}
        except:
            data = {"error": True, "message": response.text}
        return data

    return decorated_function


class API:
    def __init__(self, login, token):
        self.login = login
        self.token = token

    @property
    def base_url(self):
        """
        Базовая url для обращения к api
        """
        return f"https://spoyer.com/api/get.php?login={self.login}&token={self.token}"

    @error_handler
    def get_game_info_spoyer(self, game_id):
        response = requests.get(self.base_url + f'&task=eventdata&game_id={game_id}')
        return response

    @error_handler
    def get_prematch_games_bet365(self, sport_name):
        response = requests.get(self.base_url + f'&task=pre&bookmaker=bet365&sport={sport_name}')
        return response

    @error_handler
    def get_game_prematch_odds_bet365(self, game_id):
        response = requests.get(self.base_url + f'&task=preodds&bookmaker=bet365&game_id={game_id}')
        return response


zap = API("timurka", "57758-XfDsV1ZtuLR9wtP")
print(zap.get_prematch_games_bet365('icehockey'))
