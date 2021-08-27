"""
A simple network moniter that just sends a request to a
website. This script dosnt use the ICMP ping protocol for verifing 
whether the connection is up or not, instead it uses a simple 
"""

import requests
import time
list_of=["https://google.com"]                        #More websites can be added     
def check_net(url):                                   #this fuction sends a requsts to
    try:                                              #given website if the internet is 
        resp=requests.get(url)                        #down the error will notify it.
        resp.close()
    except requests.exceptions.ConnectionError:
        return True

def log():                                            #function that logs the result to
	with open("log.csv","a") as f:                    #a file named log.csv
		for i in list_of:
			if check_net(i)==True:
				f.write("{t},{we},\n".format(t=i,we=time.ctime()))

def main():
    while True:
        log()
        time.sleep(30)

if __name__=="__main__":
    main()
		
		
 


