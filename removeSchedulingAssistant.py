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
	cli_delegate_email = sys.argv[2]

	baseURL="https://api.zoom.us/v2/users/"
	token = generateToken()
	headers = {'authorization': 'Bearer %s' %token,
				'content-type': 'application/json'}

	getDelegateInfo = requests.get(baseURL+"%s" %cli_delegate_email, headers=headers)
	delegateID = getDelegateInfo.json()["id"]

	getUserInfo = requests.get(baseURL+"%s" %cli_user_email, headers=headers)
	userID = getUserInfo.json()["id"]

	checkPosted=requests.delete(baseURL+"%s/assistants/%s" %(userID, delegateID), headers=headers)
	print(checkPosted)
	getUserInfo = requests.get(baseURL+"%s/assistants" %cli_user_email, headers=headers, data=cli_user_email)
	print(getUserInfo.json())

if __name__ == '__main__':
	main()
