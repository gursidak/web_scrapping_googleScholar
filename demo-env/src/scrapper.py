from bs4 import BeautifulSoup
import requests
import json
import time

#Taking search input :::>

print("Enter below, what you want to search ?")
search = input()

#split the user input into words and rejoin it by inserting + inbetween each word to make it a query str eg: ('java+programming+language') ::::>

searchSplit = search.split()

if(len(searchSplit) > 1 ):
    search = '+'.join(searchSplit)

#makking http request to fetch data :::::>

url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+ search + '&btnG=&oq=java+'
res = requests.get(url, timeout=5)
content = BeautifulSoup(res.content , "html.parser")

# filtering the required data and storing in an object and storing each object in an array of object, such that at the end of forLoop we will be having an array of objects containing required information ::::::>

feedArr= []

for data in content.find_all("div",attrs={"class":"gs_r gs_or gs_scl"}) :
    AuthorInfo = data.find("div" , attrs={ "class":"gs_a" }).text
    heading = data.find("h3" , attrs={"class":"gs_rt"} ).text

    #in google scholar the format of authorInfo is 'authorName - data -webAddress', we will destructure data to get seprate feilds  

    splitted = AuthorInfo.split("-")
    author = splitted[0]
    date = splitted[1]
    webAddress = splitted[2] 

    #double check to avoid any mistake

    if(date.isdigit() == False ):
        splitDate = date.split()

        for x in splitDate:
            if(x.isdigit()):
                date = x
    #storing whole data in an object    


    Obj = {
            "Heading"    : heading    ,
            "Author"     : author     , 
            "Date"       : date       , 
            "WebAddress" : webAddress
            }
    #Printing the created object just for debugging purposes
    
    print("\n")
    print(Obj)
    
    #Storing the created object in an array named feedArray

    feedArr.append(Obj)

#In this section we will store all the objects we have stored in array to a Json file

#this moment variable will get a new JsonFile name using the time function that will return the current time and date to moment variable
moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())

#creating a new file and writing array of objects in file(each time the new file will be created with unique name beacuse of time function that will return the time at which time.localtime() will be called)

with open('Json-' + moment + '.json' , 'w') as outfile:
    json.dump(feedArr , outfile)


#Now the scrapped data is stored in a Jsonfile with name(date_time.json) in the src directory. You can go and access that data by importing in apython file and perfrom the required operations.

#TO explain how to use data stored in json file a sample program named demo_using_scrapped_data.py
