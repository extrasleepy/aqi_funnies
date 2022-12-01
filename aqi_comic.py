#!/usr/bin/env python3
#best orange from procreate is around 255,106,0
#aqi eink comic
#copyright akleindolph/extrasleepy.com 2002. Attribution required.

import time
import traceback
from PIL import Image, ImageFont, ImageDraw
import json
import requests
from requests import get
from inky import Inky7Colour as Inky
import sys
import os
import datetime
#import pytz
#from datetime import date
#import calendar
import random

inky = Inky()
inky.h_flip = True
inky.v_flip = True
saturation = 1.0

font_size = 50
med_font = ImageFont.truetype('playtime.ttf', font_size)
font_size = 35
sm_font = ImageFont.truetype('playtime.ttf', font_size)

url = 'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94114&distance=10&API_KEY=B309BA58-1608-45E6-BB0A-BBF427C99D14'

g_adj = ['superb', 'lovely', 'fresh', 'crisp', 'dreamy']
m_adj = ['okay', 'decent','so-so', 'fair','fine']
ufsf_adj=['murky', 'dirty', 'somber', 'smoky', 'gloomy']
ufaf_adj=['filthy','gross','yucky','choky','grimy']
vuh_adj=['harmful', 'risky', 'poision','unsafe','sad']
h_adj=['deadly','noxious', 'toxic', 'grim','septic']

while True:
    time.sleep(20)
    try:
        air_today = get(url).json()
        time.sleep(5)
        

        x = (air_today[0]['AQI'])
        print(x)
        
        try:
            day = datetime.datetime.now()
            #day = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
            #day=curr_date = date.today()
            #y = calendar.day_name[curr_date.weekday()]
            y=str(day.strftime("%A"))
            #y=str(datetime.datetime.today().weekday())
        except:
            y="day!"
        print(y)

        
        adj = random.randint(0,4)
        #x= 145 #for testing
        
        if (x<=25):
            message = "Noe Valley AQI is " + str(x)
            part2 = ("on this "+ str(g_adj[adj])+" "+ y)
            part3 = ("THAT'S")
            part4 = ("GREAT!")
            image = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
            image2 = Image.open("below_25.jfif") 
            image.paste(image2, (0, 0))
            draw = ImageDraw.Draw(image)
            draw.multiline_text((48,35),message,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((48,87),part2,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((375,265),part3,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((375,315),part4,fill=(0,0,0), font=med_font, align="center")
                
        if (x>25 and x<=50):
            message = "Noe Valley AQI is " + str(x)
            part2 = ("on this "+ str(g_adj[adj])+" "+ y)
            part3 = ("THAT'S")
            part4 = ("GOOD!")
            image = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
            image2 = Image.open("26_to_50.jfif") 
            image.paste(image2, (0, 0))
            draw = ImageDraw.Draw(image)
            draw.multiline_text((48,35),message,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((48,87),part2,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((375,265),part3,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((375,315),part4,fill=(0,0,0), font=med_font, align="center")
            
        if (x>50 and x<=100):
            message = "Noe Valley AQI is " + str(x)
            part2 = ("on this "+ str(m_adj[adj])+" "+ y)
            part3 = ("At least it's")
            part4 = ("MODERATE!")
            image = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
            image2 = Image.open("51_to_100.jfif") 
            image.paste(image2, (0, 0))
            draw = ImageDraw.Draw(image)
            draw.multiline_text((50,35),message,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((50,85),part2,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((50,290),part3,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((50,340),part4,fill=(0,0,0), font=sm_font, align="center")
            
        if (x>100 and x<=150):
            message = "Noe Valley AQI is " + str(x)
            part2 = ("on this "+ str(ufsf_adj[adj])+" "+ y)
            part3 = ("This is UN-")
            part4 = ("HEALTHY")
            part5 = ("for")
            part6 = ("SENSITIVE")
            part7 = ("FOLX!")
            image = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
            image2 = Image.open("100_to_150.jfif") 
            image.paste(image2, (0, 0))
            draw = ImageDraw.Draw(image)
            draw.multiline_text((50,35),message,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((50,85),part2,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((410,210),part3,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((410,250),part4,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((450,285),part5,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((405,325),part6,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((435,365),part7,fill=(0,0,0), font=sm_font, align="center")

        if (x>150 and x<=200):
            message = "Noe Valley AQI is " + str(x)
            part2 = ("on this "+ str(ufaf_adj[adj])+" "+ y)
            part3 = ("The air")
            part4 = ("is UN-")
            part5 = ("HEALTHY")
            image = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
            image2 = Image.open("151_to_200.jfif") 
            image.paste(image2, (0, 0))
            draw = ImageDraw.Draw(image)
            draw.multiline_text((50,305),message,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((50,350),part2,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((40,60),part3,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((40,100),part4,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((35,140),part5,fill=(0,0,0), font=sm_font, align="center")

        if (x>200 and x<=300):
            message = "Noe Valley AQI is " + str(x)
            part2 = ("on this "+ str(vuh_adj[adj])+" "+ y)
            part3 = ("That air is")
            part4 = ("VERY UN-")
            part5 = ("HEALTHY!")
            image = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
            image2 = Image.open("201_to_300.jfif") 
            image.paste(image2, (0, 0))
            draw = ImageDraw.Draw(image)
            draw.multiline_text((50,40),message,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((50,90),part2,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((50,197),part3,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((50,237),part4,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((50,277),part5,fill=(0,0,0), font=sm_font, align="center")

        if (x>300):
            message = "Noe Valley AQI is " + str(x)
            part2= ("on this "+ str(h_adj[adj])+" "+ y)
            part3 = ("Don't")
            part4 = ("inhale! It's")
            part5 = ("HAZARD-")
            part6 = ("OUS!!")
            image = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
            image2 = Image.open("300_and_up.jfif") 
            image.paste(image2, (0, 0))
            draw = ImageDraw.Draw(image)
            draw.multiline_text((50,300),message,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((50,350),part2,fill=(0,0,0), font=med_font, align="center")
            draw.multiline_text((50,60),part3,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((50,100),part4,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((50,145),part5,fill=(0,0,0), font=sm_font, align="center")
            draw.multiline_text((50,190),part6,fill=(0,0,0), font=sm_font, align="center")
    except:      
        traceback.print_exc()
        message = "AQI data unavailable"
        print("error")
        part2 = ("on this fine day")
        part3 = ("CHECK")
        part4 = ("BACK!")
        image = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
        image2 = Image.open("26_to_50.jfif") 
        image.paste(image2, (0, 0))
        draw = ImageDraw.Draw(image)
        draw.multiline_text((50,25),message,fill=(0,0,0), font = med_font, align="center")
        draw.multiline_text((50,85),part2,fill=(0,0,0), font = med_font, align="center")
        draw.multiline_text((375,265),part3,fill=(0,0,0), font=med_font, align="center")
        draw.multiline_text((375,315),part4,fill=(0,0,0), font=med_font, align="center")

    inky.set_image(image, saturation=saturation)
    inky.show()
    time.sleep(5)
    os.system("sudo shutdown -h now")
    time.sleep(20)
