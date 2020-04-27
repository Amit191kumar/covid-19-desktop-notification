from plyer import notification
import requests
from bs4 import BeautifulSoup
import time



def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\Amit\Desktop\covid-19 notification\pic.ico",
        timeout = 10
    )

def getdata(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    #while True:
        #notifyMe("Ahir_boy","Lets Stop THe spread of this virus together")
        myhtmldata= getdata('https://www.mohfw.gov.in/')

        #print(myhtmldata)
        soup = BeautifulSoup(myhtmldata, 'html.parser')
        #print(soup.prettify())
        mydatastr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mydatastr += tr.get_text()
        mydatastr = mydatastr[1:]
        itemlist = mydatastr.split("\n\n")

        states = ['Uttar Pradesh','Uttarakhand']

        for item in itemlist[0:32]:
            datalist = (item.split('\n'))
            if datalist[1] in states:
                print(datalist)
                ntitle = 'Live Covid-19 Updates'
                ntext = f" {datalist[1]} \nCases : {datalist[2]}\n Cured : {datalist[3]}\nDeaths : {datalist[4]}"
                notifyMe(ntitle,ntext)
                time.sleep(1)
        #time.sleep(3600)