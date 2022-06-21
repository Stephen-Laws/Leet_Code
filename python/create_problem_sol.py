import sys
import os

try:
    import argparse
    import validators
    from urllib.parse import urlparse
    import urllib
    from urllib.request import urlopen
    import json
except ImportError as e:
    print(f"ERROR: {e}")
    sys.exit()

import requests


problems_api = "https://leetcode.com/api/problems/algorithms"
algorithms_problem_json = requests.get(problems_api).content
algorithms_problem_json = json.loads(algorithms_problem_json)
print(algorithms_problem_json)
parser = argparse.ArgumentParser(description = "Import Leetcode Problem URL", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("url", help = "Leet code problem URL")
args = vars(parser.parse_args())

url = args["url"]

if not validators.url(url):
    print("Needs a valid URL (https:// ...)" )
    sys.exit()

parsed_url= urlparse(url)
url_base_path = parsed_url.path
while os.path.dirname(url_base_path) != '/':
    url_base_path = os.path.dirname(url_base_path)

if (parsed_url.netloc != "leetcode.com") or (url_base_path != "/problems"):
    print("Ensure url is of form https://leetcode.com/problems/A_PROBLEM")
    sys.exit()



