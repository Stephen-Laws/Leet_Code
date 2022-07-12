import sys
import os

try:
    import argparse
    import validators
    from urllib.parse import urlparse
    import urllib
    from urllib.request import urlopen
    import json
    import re
    import subprocess
    from datetime import date
    from bisect import bisect
    from sys import platform
except ImportError as e:
    print(f"ERROR: {e}")
    sys.exit()

import requests


PROBLEMS_API_LINK = "https://leetcode.com/api/problems/algorithms"
COMMAND_LINE = True
difficulty_dict = {1: "Easy", 2: "Medium", 3: "Hard"}
algorithms_problem_json = requests.get(PROBLEMS_API_LINK).content
algorithms_problem_json = json.loads(algorithms_problem_json)

python_str = None
if COMMAND_LINE:
    parser = argparse.ArgumentParser(description = "Import Leetcode Problem URL", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("url", help = "Leet code problem URL")
    parser.add_argument("-p", "--python_string", help = "Optional name for python file")
    args = vars(parser.parse_args())

    url = args["url"]
    if args["python_string"]:
        python_str = args["python_string"]

else:
    url = "https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/"
    python_str = "special_array"

#Check URL is valud
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

#Extract problem info from json api
problem_name = os.path.basename(os.path.normpath(parsed_url.path))
if python_str == None:
    python_str = problem_name.replace("-","_")
for el in algorithms_problem_json['stat_status_pairs']:
    if el['stat']['question__article__slug'] == problem_name or el['stat']['question__title_slug'] == problem_name:
        problem_number= el['stat']['question_id']
        problem_title = el['stat']['question__title']
        difficulty = difficulty_dict[el['difficulty']['level']]
        break

python_file_name = f"{problem_number:04d}_{python_str}.py"
updated_url = parsed_url.scheme + "://oj." + parsed_url.hostname + parsed_url.path

# Get today's date
today = date.today()
today = today.strftime("%y/%m/%d")

#Readme rows to add
table_row = f"|{problem_number}|[{problem_title}][{problem_number}]|{python_file_name}|{today}|{difficulty}|\n"
url_row = f"[{problem_number}]:{updated_url}\n"

# Update Readme
if platform == "win32":  
    with open('C:\\Users\\sglaw\\Documents\\GitHub\\Leet_Code\\python\\README.md','r') as f:
        rme = f.read()
else:
    p = subprocess.Popen(["cat",os.path.join('python','README.md')], stdout=subprocess.PIPE)
    rme = p.stdout.read().decode('utf-8')

#Find list of problems already done in readme
current_nums = re.findall(r'\|\d+\|',rme)
current_nums_start_idx = [m.start(0) for m in re.finditer(r'\|\d+\|', rme)]
url_start_idx = [m.start(0) for m in re.finditer(r'\[\d+\]\:', rme)]

#Append end of insertion lists with last line of readme
current_nums_start_idx.append([m.start(0) for m in re.finditer('\n\n\[\d+\]',rme)][0]+1)
url_start_idx.append(len(rme))

current_nums = [int(num[1:-1]) for num in current_nums]
if problem_number in current_nums:
    print(f"README already contains problem {problem_number}")
    sys.exit()

#Find where to insert new table row
insertion_point = bisect(current_nums,problem_number)

#Add new table row
updated_rme = rme[:current_nums_start_idx[insertion_point]] + table_row \
                + rme[current_nums_start_idx[insertion_point]:url_start_idx[insertion_point]]  \
                    + url_row + rme[url_start_idx[insertion_point]:]
    

#Create new python file
hi = 99
while problem_number > hi:
    hi += 100
lo = hi - 99
folder_name = f"/python/{lo:04d}-{hi:04d}"

#Make folder if it doesn't exist
if not os.path.exists(os.getcwd()+ folder_name):
    os.mkdir(os.getcwd() + folder_name)

python_file_path = os.getcwd() + folder_name + "/" + python_file_name
pyf = open(python_file_path, "a")
pyf.write(f"# {updated_url}")
pyf.close()


#Write new readme contents
f = open("python/README.md", 'w')
f.write(updated_rme)
f.close()




