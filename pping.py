import requests
import time

"""
ip="https://google.com"

output=requests.get(ip)

print(output)
"""
list_of=["https://google.com","https://wikipedia.org"]

def check_net(url):
    try:
        resp=requests.get(url)
        resp.close()
    except:
        return True

def log():
	with open("log.csv","a") as f:
		for i in list_of:
			if check_net(i)==True:
				f.write("{t}:{we} down\n".format(t=i,we=time.ctime()))

def main():
    while True:
        log()
        print("i\n")
        time.sleep(30)

if __name__=="__main__":
    main()
		
		
 


