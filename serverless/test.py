import requests
import json

def main():
    url = 'http://localhost:3000/dev/v1/rspv'
    
    payload = {
        'first_name':'Nick',
        'last_name':'Padon',
        'email':'npadon@gmail.com',
        'attending':'yes',
        'number_attending':4
        }
    
    requests.post(url,json=payload)

if __name__=='__main__':
    main()