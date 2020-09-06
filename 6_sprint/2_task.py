"""
Implement function parse_user(output_file, *input_files) for creating file that will contain
 only unique records (unique by key "name") by merging information from all input_files argument
  (if we find user with already existing name from previous file we should ignore it).


If the function cannot find input files we need to log information with error level

root - ERROR - File <file name> doesn't exists
For example:
user1.json :
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
]

user2.json :
[{"name": "Bob1", "rate": 25, “languages": ["French"]},
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

If we execute parse_user(user3.json, user1.json, user2.json)
then file user3.json should contain information:
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

"""
import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    output_list = []
    unique_key = "name"
    for files in input_files:
        try:
            with open(files) as file:
                json_data = json.load(file)
                if len(json_data) > 1:
                    for x in json_data:
                        count = 0
                        for item in output_list:
                            if x.get(unique_key, None) == item.get(unique_key, None):
                                count += 1
                                continue
                        if count == 0:
                            output_list.append(x)
        except FileNotFoundError as error:
                    logging.error(f"File {files} doesn't exists")
    try:
        with open(output_file, "w") as wrie_file:
            json.dump(output_list, wrie_file, indent=4)
    except FileNotFoundError as error:
        logging.error(f"File {output_file} doesn't exists")


parse_user("user4.json", "user_without_name.json")
