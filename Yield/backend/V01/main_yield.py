""" Карта урожайности c системы """
import requests as requests

LOGIN = 'login'
PASSWORD = 'password'
PATCH = 'D:\DataBase\Сartography\Yield\\'   # Путь куда сохраняем

def main():
    """ Точка входа """


def Authorization_claas():
    """ Авторизация в системе Claas """
url = 'https://www.claas-telematics.com/Telematics/TheLogin.app'
response = requests.get(url, auth=(LOGIN, PASSWORD))
print(response.text)

if __name__ == '__main__':
    Authorization_claas()

