# scan-gspread-targets
A script to take targets from a google spreadsheet and run a Nessus vulnerability scan

It calls out to google docs and pulls the info from the spreadsheet, extracts the first column, parses it and then executes the scan.

Google docs has its own API, I used gspread as I found it easier. Follow the install directions ["here"](https://github.com/burnash/gspread).


### Dependencies

* nessrest
* gspread
* oauth2client
* pycrypto
* requests


### Installation of requirements

$ cd [your directory] $ pip install -r requirements.txt 
