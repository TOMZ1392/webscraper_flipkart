from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
from time import time, sleep

setpoint_price=14000
wait_time_since_last_check=5
def  wait_seconds(delay_sec):
    start_time=time()
    #print(start_time)
    diff=0
    while diff < delay_sec:
        diff= time() - start_time
        #print(diff)
        sleep(1)

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

URL = "https://www.flipkart.com/oppo-k1-piano-black-64-gb/p/itmfdy9keddxqvbt?pid=MOBFDY9KSZFK5RDZ&srno=s_1_1&otracker=search&otracker1=search&lid=LSTMOBFDY9KSZFK5RDZOMBJRD&fm=organic&iid=4d924c88-1613-428d-b09e-73b4ce5ed81a.MOBFDY9KSZFK5RDZ.SEARCH&ssid=b0xl2mqpxc0000001569685786453&qH=476bf930ffe1fdda"
last_price=0
while True:
    r = requests.get(URL) 
    #print(r.content)
    soup = BeautifulSoup(r.content, 'html5lib')
    msgs=client.messages.list(from_='+919999999999')
    for msg in msgs:
        print(msg.sid)

    price_str=soup.find('div', attrs={'class','_1vC4OE _3qQ9m1'}).get_text().replace(',','')
    price_int=int(price_str[1:])
    print(setpoint_price)
    #wait_seconds(2)
    sleep(wait_time_since_last_check)
    #setpoint_price=setpoint_price + 300
    if last_price != price_int:
        if price_int <= setpoint_price:
            product_name=soup.find('span',attrs={'class','_35KyD6'}).get_text()
            info_msg='Price slashed!!\n' + product_name[0:20] + '...: \nCurrent Price:'+ price_str + '\nVisit:' + URL
            print(info_msg)
            last_price=price_int
            
            #print(priceInt)
            message = client.messages.create(
                             body=info_msg,
                             from_='whatsapp:+1466666',
                             to='whatsapp:+919999999999'
				 #,media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80']
                          )
            print(message.sid)
            message = client.messages.create(
                             body=info_msg,
                             from_='whatsapp:+14666666666666',
                             to='whatsapp:+919999999999'
				 #,media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80']
                          )
            print(message.sid)
