from bs4 import BeautifulSoup
import requests
import json
import time

print("Enter below, what you want to search ?")
search = input()

searchSplit = search.split()

if(len(searchSplit) > 1 ):
    search = '+'.join(searchSplit)

url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+ search + '&btnG=&oq=java+'
res = requests.get(url, timeout=5)
content = BeautifulSoup(res.content , "html.parser")

feedArr= []

for data in content.find_all("div",attrs={"class":"gs_r gs_or gs_scl"}) :
    AuthorInfo = data.find("div" , attrs={ "class":"gs_a" }).text
    heading = data.find("h3" , attrs={"class":"gs_rt"} ).text
    
    splitted = AuthorInfo.split("-")
    author = splitted[0]
    date = splitted[1]
    webAddress = splitted[2] 


    if(date.isdigit() == False ):
        splitDate = date.split()

        for x in splitDate:
            if(x.isdigit()):
                date = x
        


    Obj = {
            "Heading"    : heading    ,
            "Author"     : author     , 
            "Date"       : date       , 
            "WebAddress" : webAddress
            }
    print("\n")
    print(Obj)

    feedArr.append(Obj)

moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())

with open('Json-' + moment + '.json' , 'w') as outfile:
    json.dump(feedArr , outfile)
