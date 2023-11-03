# This program imports test.json into the program

import json, os

if os.path.exists("./test.json"):
    with open("./tests_data/test.json") as f:
        json_file = json.load(f)
        f.close
        print(json_file)
else:
    print("The test.json file does not exist. Please create one and run the program again.")
