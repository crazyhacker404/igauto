from os import name, system
try:
 from requests import session
 from json import load
 from random import choice
 from user_agent import generate_user_agent 
 import pyfiglet
except:
 system("pip install requests user_agent pyfiglet")
 from requests import session
 from json import load
 from random import choice
 from user_agent import generate_user_agent 
 import pyfiglet
bbin = pyfiglet.figlet_format("followers")
adet = 0
UserAgents = [generate_user_agent()]
banner = f"""\033[96m
{bbin}
\033[93mCoded By \033[94m→\033[2;31;5m @crazy_hacker404\033[0;m  
\033[93mChannel \033[94m→ \033[2;31;5m@xSPY_BACKUP\033[0;m
"""
def clear(): 
    if name == 'nt':system('cls')
    elif name == 'posix':system('clear')
def Login1(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcizen.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcizen.com/login"})
    login = Session.post("https://takipcizen.com/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login1(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcizen.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})
   
    
def Login2(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcikrali.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcikrali.com/login"})
    login = Session.post("https://takipcikrali.com/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login2(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcikrali.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login3(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://bayitakipci.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://bayitakipci.com/memberlogin"})
    login = Session.post("https://bayitakipci.com/memberlogin?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login3(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://bayitakipci.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login4(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcigir.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcigir.com/login"})
    login = Session.post("https://takipcigir.com/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        Login4(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcigir.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login5(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://canlitakipci.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://canlitakipci.com/login"})
    login = Session.post("https://canlitakipci.com/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login5(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://canlitakipci.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})

def Login6(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipciking.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipciking.com/member"})
    login = Session.post("https://takipciking.com/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login6(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipciking.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login7(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcitime.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcitime.com/login"})
    login = Session.post("https://takipcitime.com/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login7(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcitime.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})
    



def Login8(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://birtakipci.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://birtakipci.com/member"})
    login = Session.post("https://birtakipci.com/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login8(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://birtakipci.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})



def Login9(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipstar.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipstar.com/login"})
    login = Session.post("https://takipstar.com/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login9(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipstar.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login10(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://followersize.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://followersize.com/member"})
    login = Session.post("https://followersize.com/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login10(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://followersize.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login11(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcimx.net/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcimx.net/member"})
    login = Session.post("https://takipcimx.net/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login11(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcimx.net/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})




def Login12(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcimx.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcimx.com/member"})
    login = Session.post("https://takipcimx.com/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login12(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcimx.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})




def Login13(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcibase.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcibase.com/login"})
    login = Session.post("https://takipcibase.com/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login13(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcibase.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})




def Login14(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://instamoda.org/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://instamoda.org/login"})
    login = Session.post("https://instamoda.org/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login14(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://instamoda.org/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login15(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://fastfollow.in/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://fastfollow.in/member"})
    login = Session.post("https://fastfollow.in/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login15(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://fastfollow.in/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login16(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcikutusu.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcikutusu.com/member"})
    login = Session.post("https://takipcikutusu.com/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login16(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcikutusu.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})



def Login17(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://bigtakip.net/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://bigtakip.net/login"})
    login = Session.post("https://bigtakip.net/login?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login17(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://bigtakip.net/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login18(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://gramtakipci.xyz/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://gramtakipci.xyz/959f6ba24150ee69eea1361a8b85a5c1c36c42f2"})
    login = Session.post("https://gramtakipci.xyz/959f6ba24150ee69eea1361a8b85a5c1c36c42f2?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login18(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://gramtakipci.xyz/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})

def Login19(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://hepsitakipci.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://hepsitakipci.com/member"})
    login = Session.post("https://hepsitakipci.com/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login19(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://hepsitakipci.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def Login20(Session,username,password):
    Session.headers ={"User-Agent": choice(UserAgents)}
    data = Session.get("https://takipcimax.com/")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m")
    Session.headers.update({"Referer": "https://takipcimax.com/member"})
    login = Session.post("https://takipcimax.com/member?",data={"username":username,"password":password}).json()    
    if login['status'] == "success":
        print("\033[93m[\033[32m+\033[93m] \033[32mSuccessFul\033[91m☑️")
    else:
        print("\033[93m[\033[91m-\033[93m] \033[91mCheck App Instagram To Verified Login(\033[0m")
        clear_session()
        Login20(Session,username,password)
    cockies = data.cookies.items()[0]
    data = Session.get("https://takipcimax.com/tools/send-follower")
    print(f"\033[32m[\033[94m*\033[32m] \033[96mSTATUS \033[93m→ \033[91m{data.status_code}\033[0m") 
    Session.headers.update({cockies[0]: cockies[1]})


def FindeNumId(sesnumid,username):
    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(username)
    head2={                'accept':'*/*',                            'accept-language':'en-US,en;q=0.9,ar;q=0.8',                'cookie':'ig_nrcb=1; mid=ZlyXRQALAAGB-IZLxY-vGMkPHpVw; ig_did=0C859344-F210-412E-A7E6-48BEC7A5CF14; datr=RpdcZpY36yQcYftcaDR-_cyV; ps_n=1; ps_l=1; csrftoken=Ai7EsLi0pBt8VsmtkQnEWCVBmoZgYKtZ; wd=1028x730; dpr=1.25',                'priority':'u=1, i',                'referer':'https://www.instagram.com/gzik/',                'sec-ch-prefers-color-scheme':'light',                'sec-ch-ua':'"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',                'sec-ch-ua-full-version-list':'"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.74", "Chromium";v="127.0.6533.74"',                'sec-ch-ua-mobile':'?0',                'sec-ch-ua-model':'""',                'sec-ch-ua-platform':'"Windows"',                'sec-ch-ua-platform-version':'"15.0.0"',                            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',                'x-asbd-id':'129477',                'x-csrftoken':'Ai7EsLi0pBt8VsmtkQnEWCVBmoZgYKtZ',                'x-ig-app-id':'936619743392459',                'x-ig-www-claim':'0',                'x-requested-with':'XMLHttpRequest'                }
    ge = sesnumid.get(url2,headers=head2).json()
    id = ge['data']['user']['id']
    return id




def Sender1(Session,User,Number,numId):
    global adet
    
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 1\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcizen.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcizen.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")

def Sender2(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 2\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcikrali.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcikrali.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender3(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 3\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://bayitakipci.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://bayitakipci.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender4(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 4\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcigir.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcigir.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender5(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 5\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://canlitakipci.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://canlitakipci.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender6(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 6\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipciking.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipciking.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender7(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 7\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcitime.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcitime.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender8(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 8\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://birtakipci.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://birtakipci.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender9(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 9\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipstar.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipstar.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender10(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 10\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://followersize.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://followersize.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender11(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 11\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcimx.net").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcimx.net/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender12(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 12\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcimx.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcimx.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender13(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 13\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcibase.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcibase.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender14(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 14\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://instamoda.org").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://instamoda.org/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender15(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 15\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://fastfollow.in").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://fastfollow.in/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender16(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 16\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcikutusu.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcikutusu.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender17(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 17\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://bigtakip.net").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://bigtakip.net/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender18(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 18\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://gramtakipci.xyz").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://gramtakipci.xyz/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender19(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 19\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://hepsitakipci.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://hepsitakipci.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")
def Sender19(Session,User,Number,numId):
    global adet
    adet += Number
    print("\n\033[96m──────────────\033[93m[ \033[91mInFo FolloWer 20\033[93m]\033[96m───────────────")
    while(adet >= 0 ):
      try:
        limited = Session.get(f"https://takipcimax.com").text.split('href="/tools/send-follower">')[1].split('class="text"')[1].split('>')[1].split('<')[0]
        print(f"\033[32m[\033[94m*\033[32m] \033[96mCOINS HAVE \033[93m→ \033[91m{limited}\033[0m")
        data = Session.post(f"https://takipcimax.com/tools/send-follower/{numId}?formType=send" ,data={"adet":Number,"userID":numId,"userName":User}).json()
        if data['status'] == "success":
            for user in data['users']:
                print(f"\033[91m[ \033[32mUser \033[93m→ \033[96m{user['userNick']} \033[94m| \033[32mStatus \033[93m→ \033[96m{user['status']}\033[91m]")
        else:
            print(f"\033[93m[\033[91m-\033[93m] \033[91m{data['status']}")
            
            
        if adet == 1:
            adet -= 1
        else :
            adet -= 2
        if int(limited)==0:
            break 
      except:
        print(f"\033[93m[\033[91m-\033[93m] \033[91mDone Followers Amount")
    print("\033[96m──────────────────────────────────────────────")



def clear_session():
    Session.headers.clear()
    Session.cookies.clear()

clear()
Session = session()
sesnumid = session()
print(banner)
username = input("Fake Account\033[2;31;5m( UserName )\033[0;m > \033[96m") 
password = input("\033[0;mFake Account\033[2;31;5m( PassWord )\033[0;m > \033[96m") 
User = input("\033[93mTarGet \033[32m→\033[96m ")
Number = int(input("\033[93mAmount \033[32m→\033[96m "))
Login1(Session,username,password)
numId = FindeNumId(sesnumid,User)
Sender1(Session,User,Number,numId)
clear_session()
Login2(Session,username,password)
Sender2(Session,User,Number,numId)
clear_session()
Login3(Session,username,password)
Sender3(Session,User,Number,numId)
clear_session()
#Login4(Session,username,password)
#Sender4(Session,User,Number,numId)
#clear_session()
Login5(Session,username,password)
Sender5(Session,User,Number,numId)
clear_session()
Login6(Session,username,password)
Sender6(Session,User,Number,numId)
clear_session()
Login7(Session,username,password)
Sender7(Session,User,Number,numId)
clear_session()
Login8(Session,username,password)
Sender8(Session,User,Number,numId)
clear_session()
Login9(Session,username,password)
Sender9(Session,User,Number,numId)
clear_session()
Login10(Session,username,password)
Sender10(Session,User,Number,numId)
clear_session()
Login12(Session,username,password)
Sender12(Session,User,Number,numId)
clear_session()
Login13(Session,username,password)
Sender13(Session,User,Number,numId)
clear_session()
Login14(Session,username,password)
Sender14(Session,User,Number,numId)
clear_session()
Login15(Session,username,password)
Sender15(Session,User,Number,numId)
clear_session()
Login16(Session,username,password)
Sender16(Session,User,Number,numId)
clear_session()
Login17(Session,username,password)
Sender17(Session,User,Number,numId)
clear_session()
Login19(Session,username,password)
Sender19(Session,User,Number,numId)
clear_session()
