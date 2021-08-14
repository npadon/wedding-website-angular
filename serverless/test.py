import requests
import json
import os

def main():
    url = 'http://localhost:3000/local/v1/rsvp'
    
    payload = {
        'firstName':'Nick',
        'lastName':'Padon',
        'email':'npadon@gmail.com',
        'attending':'yes',
        'numberAttending':5
        }
    
    requests.post(url,json=payload)

if __name__=='__main__':
    main()