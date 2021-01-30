#Project 2: Web scraper

import requests
from bs4 import BeautifulSoup
import pandas
import connect
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--dbname",help="Enter the name of the DB",type=str)
args=parser.parse_args()

hotel_url="https://www.oyorooms.com/search?location=Bangalore%2C%20Karnataka%2C%20India&city=Bangalore&searchType=city&coupon=&checkin=30%2F01%2F2021&checkout=31%2F01%2F2021&roomConfig%5B%5D=1&showSearchElements=false&country=india&guests=1&rooms=1&filters%5Bcity_id%5D=4"
info=[]
connect.connect(args.dbname)

req=requests.get(hotel_url)
content=req.content
soup=BeautifulSoup(content,"html.parser")

all_hotels=soup.find_all("div",{"class":"hostelCardListing"})

for hotel in all_hotels:
    hotel_dict={}
    hotel_dict["hotel_name"]=hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
    hotel_dict["hotel_address"]=hotel.find("span",{"itemprop": "streetAddress"}).text
    hotel_dict["hotel_price"]=hotel.find("span",{"class": "listingPrice_finalPrice"}).text

    try:
        hotel_dict["hotel_rating"]=hotel.find("span",{"class": "hotelRating_ratingSummary"}).text
    except AttributeError:
        hotel_dict["hotel_rating"]=0

    parent_amenities_element=hotel.find("div",{"class": "amenityWrapper"})
    amenities_list=[]
    for amenity in parent_amenities_element.findall("div",{"class":"amenityWrapper__amenity"}):
        amenitites_list.append(amenity,find("span",{"class":"d-bofy-sm"}).text.strip())
    hotel_dict["amenities"]=','.join(amenities_list)

    info.append(hotel_dict)

    connect.insert_into_table(args.dbname,tuple(hotel_dict.values()))

dataFrame=pandas.DataFrame(info)
dataFrame.to_csv("Oyo.csv")
connect.hotel_info(args.dbname)

