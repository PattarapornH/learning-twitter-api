## split json
import json
import glob

all_json = glob.glob("../jsons/*.json")

for json_file in all_json:
    input_file = open(json_file)
    json_arr = json.load(input_file)
    for tweet in json_arr:
        with open('all_tweet.json', 'a') as f:
            json.dump(tweet,f)
            f.write('\n')