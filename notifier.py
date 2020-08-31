
"""
This code gives the count of Covid 19 cases as Notification
@author: rhitc
"""
import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup as bs

country='us'
url='https://www.worldometers.info/coronavirus/country/'+country+'/'
req=requests.get(url)
html=req.text
obj=bs(html,"html.parser")

l1=obj.find_all('div',{'class':'maincounter-number'})
total_cases=l1[0].span.text
deaths=l1[1].span.text
recovered=l1[2].span.text

message="Total Cases:"+total_cases+'\nTotal Deaths:'+deaths+"\nTotal Recovered:"+recovered


notifier=ToastNotifier()
notification=notifier.show_toast(title='Covid 19 Counts',
                                 msg=message,
                                 duration=10)

