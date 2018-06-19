import os
import time
import schedule
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'lijung84'
insta_password = '_%ot5ZPe'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'
def job():
	try:
		session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

    		session.login()

    		# settings
		# default enabled=False , enables the checking with the clarifai api (image tagging)
		# if secret and proj_id are not set, it will get the environment Variables
		# 'CLARIFAI_API_KEY'
		session.set_use_clarifai(enabled=True, api_key='f58bf3c3d55e46929c4ffdc83da8864a')
		session.set_use_clarifai(enabled=True)
   	 	session.set_relationship_bounds(enabled=True,
						 potency_ratio=-1.21,
				  		delimit_by_numbers=True,
				   		max_followers=4590,
				    		max_following=5555,
				     		min_followers=45,
				      		min_following=77)
   	 	session.set_do_comment(True, percentage=10)
    		session.set_comments([u'Interesting stuff! :thumbsup:', 'where did you get the inspiration from?', 'Nice photograph!'], media='Photo')
    		session.set_comments(['Great Video, nicely made!', u'very professional! :sparkles:'], media='Video')
    		session.set_comments(['Nice shot! @{}', 'Couldnt have done it any better! @{}'], media='Photo')
    		session.set_comments(['Cool!', 'Awesome!', '喜欢它', 'Super!', u'冷静 :trollface:', u':raised_hands: Automation Collective (Social Flux) :raised_hands:'])
   		session.set_dont_include(['random_user'])
    		session.set_dont_like([ 'girl', 'raciscme', 'pro trump'])
		session.set_user_interact(amount=5, random=True, percentage=50, media='Photo')

		 # session clarifai actions
		session.clarifai_check_img_for(['writing'], comment=True, comments=['Beautiful!', 'Inspiring!'])

   		 # actions
    		session.like_by_tags(['writing', 'poetry', 'writing artist', 'romance', 'shakespeare', 'russian writers', 'literature' ], amount=50)
		session.like_by_users(usernames=['random_user'], amount=10, random=True)
		session.like_by_feed(amount=10, randomize=True)
		session.interact_user_followers(['writing', 'writers', 'markov'], amount=10, random=True)
		session.unfollow_users(amount=2)
		

	
	finally:
    # end the bot session
    	 	session.end()
	
schedule.every().day.at("6:35").do(job)
schedule.every().day.at("12:15").do(job)
schedule.every().day.at("13:50").do(job)
schedule.every().day.at("20:22").do(job)
schedule.every().day.at("23:32").do(job)
schedule.every().day.at("00:22").do(job)
schedule.every().day.at("04:22").do(job)


while True:
    schedule.run_pending()
time.sleep(1)
