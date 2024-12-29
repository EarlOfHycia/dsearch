import sys
import argparse as ap
import requests
import json
import socket

parser = ap.ArgumentParser()

parser.add_argument('--header',action='store_true',help='To include header information')
parser.add_argument('-d','--dict', action = 'store_true',help='To get site information in dictionary form')
parser.add_argument('-D','--detailed',action = 'store_true',help='To get detailed information of the site')
parser.add_argument('url', help='Give <domain> of the site to be investigated')

args = parser.parse_args()

try:
	ip_address = socket.gethostbyname(args.url)
except:
	sys.exit("No site exists for given url")

try:
	req = requests.get("https://"+args.url)
except:
	sys.exit("No site exists for given url")

if(args.header):
	print("\n")
	print(req.headers)
	print("\n")
try:
	req2 = requests.get("https://ipinfo.io/"+ip_address+"/json")
except:
	print("No site exists for given url")

resp = json.loads(req2.text)

if(args.dict):
	print(req2.text)

elif(args.detailed):
	print(f'IP Address: {resp["ip"]}')

	try:
		print(f'Hostname: {resp["hostname"]}')
	except:
		print("No hostname exists")

	print(f'Location: {resp["loc"]}')
	print(f'City: {resp["city"]}')
	print(f'Region: {resp["region"]}')
	print(f'Country: {resp["country"]}')
	print(f'Organisation: {resp["org"]}')
	print(f'Time Zone: {resp["timezone"]}')
	print(f'Postal Code: {resp["postal"]}')

else:
	print(f'IP Address: {resp["ip"]}\n')
	print("for more options, view help page using command:")
	print("python3 dsearch --help\n")
