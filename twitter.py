import speech_recognition as sr
import time



from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


r = sr.Recognizer()


while True:
	with sr.Microphone() as source:
		print("say something")
		audio = r.listen(source)
		print("time over, thanks")


	try:
		message = (r.recognize_sphinx(audio))
		twitter.update_status(status=message+" #DM_OpenStudio")
		print("Tweeted: %s" % message)
		sleep(10)
	except:
		pass;