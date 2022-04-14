import json

string_json_data = open("auth.json")
json_data = json.load(string_json_data)

with open("syslog", "r") as file:
    for line in file.readlines():
        if("SerialNumber:" in line):
            serial = line.split(" ")[-1].strip()
            if(serial not in json_data['serial']):
                print("Found serial number: ", serial)
