#!/usr/bin/env python

# A python script to take targets from a google spreadsheet and run a Nessus vulnerability scan.

import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from nessrest import ness6rest
import getpass

# Login with your Google account's API key
json_key = json.load(open('API-xxxxxxxxxx.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

gc = gspread.authorize(credentials)

# Open worksheet from spreadsheet
wks = gc.open("hosts").sheet1

# Get all values from the first column
host_list = wks.col_values(1)

temp_hosts=[]

for i in host_list:
  # ignore the first entry as it's just header information
  # del host_list[0]
  if i != 'IP':
    # iterate through all rows and add to a temp array
    temp_hosts.append(i)

print(temp_hosts)

# scan

# Scan Settings
#nessus_url = "https://nessus.example.com:8834"
nessus_url = "https://192.168.111.10:8834"
scan_policy = "Basic Network Scan";
scan_name = "My Scan";

# Scanner Credentials
user = getpass._raw_input('User: ')
password = getpass.getpass()
#login = "username";
#password = "password";

scan = ness6rest.Scanner(url=nessus_url,login=user,password=password, insecure=True)

# Set scan policy that should be used
scan.policy_set(name=scan_policy)

# alt_targets on edit can take an array otherwise a new scan expects a string
hosts = ','.join(temp_hosts)
# Set target and scan name
scan.scan_add(targets=hosts, name=scan_name)
#scan.scan_exists(targets=hosts, name=scan_name)

# Run Scan
scan.scan_run()

# Download results
#scan.action(action="scans", method="get")
#for s in scan.res['scans']:
#  scan.scan_name = s['name']
#  scan.scan_id = s['id']
#  xml_nessus = scan.download_scan(export_format='nessus')
#  fp = open('%s_%s.nessus'%(scan.scan_name,scan.scan_id),"w")
#  fp.write(xml_nessus)
#  fp.close()
