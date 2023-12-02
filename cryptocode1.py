import requests
import time
from bs4 import BeautifulSoup 

def price():
    r=requests.get("https://cryptowat.ch/")
    r=BeautifulSoup(r.content)
    
    try:
        p=float(r.find_all("span", {"class":"price"})[5].text)
    except:
        p=0
    
    return(p)

def max(lis):
    a=0
    for i in lis:
        if i>a:
            a=i
    return a

alltime=[0] #list for storing list of btc prices of each day
today=[] #list of btc prices of each day
diff=0
buy=0
vrn=0
while(True):

    k=price()
    print( k)
    if k!=0: #ie when theres no error
        today.append( k )

        if (buy==0 and max(today)-k<(max(today)*0.05)) or (buy==0 and max(today)-k<(max(alltime[-1])*0.075)):
            buy=k
            vrn=buy


        if buy!=0 and k>buy:
            vrn=buy #vrn stores highest value of btc after buying 

        if vrn-k> (vrn*0.01):
            sell=k
            diff+=sell-buy
            print("buy",buy)
            print("sell",sell)
            print("yes"+str(sell-buy))
            buy=0 #resetting buy and sell variables
            vrn=0
            sell=0





        if len(today)==1440: #1440 minutes in a day
            alltime.append(today)
            today=[]
        
    time.sleep(58) #2 seconds lesser than a minute accounting for time to run the script
