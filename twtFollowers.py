import tweepy
import time
import json

# KEYFILE = "config/twkey.json"

"""
def get_key(keyfile):
	try:
		with open(keyfile) as fin:
			key = json.load(fin)
	except FileNotFoundError as e:
		sys.exit(1)
	return key

def authenticate(key):
	auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
	auth.set_access_token(key['access_token'], key['access_secret'])
	api = tweepy.API(auth)
	#return auth
	"""

key1 = ""
key2 = ""
key3 = ""
key4 = ""


print("Twitter Followers Importer V0.5")
accountvar = input ("Account name: ")


list = open (accountvar + ".csv", 'w')
list.write("Source,Target" +' \n')
print("Getting followers from: " + accountvar)


auth = tweepy.OAuthHandler(key1, key2)
auth.set_access_token(key3, key4)
api = tweepy.API(auth)

# Use the Cursor API parameter to look for the followers from the account stored in screen_name
users = tweepy.Cursor(api.followers, screen_name=accountvar).items()

while True:
	try:
		user = next(users)
		list.write(user.screen_name + "," + accountvar + '\n')
		time.sleep(5.5*1)
	except tweepy.TweepError:
		print ("Getting a time out, wait 15 minutes :)")
		time.sleep(60*15)
		print ("Startting again")
		user = next(users)
		list.write(user.screen_name + "," + accountvar + '\n')
		time.sleep (5.5*1)
	except StopIteration:
		break
	print (user.screen_name)