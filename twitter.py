import tweepy
import os
import json

consumer_key = 'YKgrgU3hwQMwJnSzSfdIFNDO5'
consumer_secret = 'F2XDedxzwXsEy7uUMeoQVK1y65Q6kgjVuBTVsD1ofUeCefBlVE'
access_token = '1100219361371906054-v75OhPayXaJZoxIo1bMHIRohq6Gcsu'
access_secret = 'nazL1RQYfVMLS9QRdaOxBH8wWrdWelCZEUftav79fqQYh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

followers = api.followers_ids(screen_name='StampApiwat')

TWEET_COUNT = 1000
python_file_dir = os.path.dirname(__file__)
for fol_id in followers:
    try:
        user_info = api.get_user(fol_id)
        if user_info.statuses_count >= TWEET_COUNT:
            print("Found: {0} ({1})", user_info.screen_name, user_info.statuses_count)
            save_count = 0
            tweet_storage = []
            tweet_result = api.user_timeline(id=user_info.screen_name, count=200)
            cur_file_dir = os.path.join(python_file_dir, './jsons/{0}.json'.format(user_info.screen_name))
            if (os.path.exists(cur_file_dir)):
                continue
            
            while save_count < TWEET_COUNT:
                if len(tweet_result) <= 0:
                    break
                print("Save: {0} ({1})", user_info.screen_name, len(tweet_result))
                for tweet in tweet_result:
                    tweet_storage.append(tweet._json)
                    save_count += 1

                with open(cur_file_dir, 'w') as json_file:
                    json_file.write(json.dumps(tweet_storage))
                
                if save_count < TWEET_COUNT:
                    tweet_result = api.user_timeline(id=user_info.screen_name, max_id=tweet_result[-1].id - 1, count=200)
        else:
            print("Skip: {0} ({1})", user_info.screen_name, user_info.statuses_count)
    except tweepy.TweepError:
        print("Error")