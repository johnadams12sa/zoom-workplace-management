import jwt
from time import time
import requests
import config
import sys

def generateToken():
	token = jwt.encode(
		{"iss": config.API_KEY, "exp": time() + 6000},
		config.API_SECRET,
		algorithm='HS256'
	)
	return token

def main():

    cli_user_email = sys.argv[1]
    baseURL="https://api.zoom.us/v2/users/"
    token = generateToken()
    headers = {'authorization': 'Bearer %s' %token,
                'content-type': 'application/json'}

    getUserInfo = requests.get(baseURL+"%s" %cli_user_email, headers=headers)
    userID = getUserInfo.json()["id"]
    getUserInfo = requests.get(baseURL+"%s/assistants" %cli_user_email, headers=headers, data=cli_user_email)
    print(getUserInfo.json())

if __name__ == '__main__':
    main()
