import os
import time
import schedule
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = '_kaorikondo_'
insta_password = 'zv!~8y?$7N7^'

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
		session.set_use_clarifai(enabled=True, api_key='f56aa5af66994d4f92eaf5e8e7db8e03')
		session.set_use_clarifai(enabled=True)
   	 	session.set_relationship_bounds(enabled=True,
						 potency_ratio=-1.21,
				  		delimit_by_numbers=True,
				   		max_followers=4590,
				    		max_following=5555,
				     		min_followers=45,
				      		min_following=77)
   	 	session.set_do_comment(True, percentage=10)
    		session.set_comments([u'Nice shot! :thumbsup:', 'Where is that?', 'Need to do that too!'], media='Photo')
    		session.set_comments(['Great Video!', u'How artful :sparkles:'], media='Video')
    		session.set_comments(['Nice shot! @{}', 'Couldnt have done it any better! @{}'], media='Photo')
    		session.set_comments(['Cool!', 'Awesome!', 'Nice!', 'Super!', u'Sugoi! :trollface:', u':raised_hands: Automation Collective (Social Flux) :raised_hands:'])
   		session.set_dont_include(['random_user'])
    		session.set_dont_like(['pizza', 'girl', 'raciscme', 'pro trump'])
		session.set_user_interact(amount=5, random=True, percentage=50, media='Photo')

		 # session clarifai actions
		session.clarifai_check_img_for(['food'], comment=True, comments=['Tasty!', 'Yum!'])
   		 # actions
    		session.like_by_tags(['designer', 'webdesign', 'UX', 'design', 'ceramics', 'architecture', 'design art' ], amount=50)
		session.like_by_users(usernames=['random_user'], amount=10, random=True)
		session.like_by_feed(amount=10, randomize=True)
		session.interact_user_followers(['natgeo', 'charity', 'design'], amount=10, random=True)
		session.unfollow_users(amount=2)
		

	except Exception as exc:
   		# if changes to IG layout, upload the file to help us locate the change
   		if isinstance(exc, NoSuchElementException):
       		 file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        	with open(file_path, 'wb') as fp:
          	 fp.write(session.browser.page_source.encode('utf8'))
        	print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
           	 '*' * 70, file_path))
    		# full stacktrace when raising Github issue
    		raise

	finally:
    # end the bot session
    	 	session.end()
	
schedule.every().day.at("6:35").do(job)
schedule.every().day.at("16:22").do(job)
schedule.every().day.at("18:42").do(job)
schedule.every().day.at("20:22").do(job)
schedule.every().day.at("22:22").do(job)
schedule.every().day.at("00:22").do(job)
schedule.every().day.at("04:22").do(job)


while True:
    schedule.run_pending()
time.sleep(1)
