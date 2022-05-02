import requests
from config import *
from colorama import Style, Fore

def danger(msg):
    return f"{Fore.RED}{msg}{Style.RESET_ALL}"

def check_trello(username=""):

    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{TRELLO_REQUEST}/{username}/?invitationTokens=")

    status = r.status_code

    if status == 200:
        return f"{TRELLO_RESPONSE}/{username}"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_pinterest(username=""):
    if not username:
        return "No Username Entered"

    r = requests.get(f"{PINTEREST_REQUEST}/{username}")

    status = r.status_code    

    if status==200:
        return f"{PINTEREST_REQUEST}/{username}"
    elif status==404:
        return danger("Not Found") 
    else:
        return "Error"

def check_github(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{GITHUB_REQUEST}/{username}")

    status = r.status_code

    if status == 200:
        return f"{GITHUB_REQUEST}/{username}"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_quora(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{QUORA_REQUEST}/{username}")

    status = r.status_code

    if status == 200:
        return f"{QUORA_RESPONSE}/{username}"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_vk(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{VK_REQUEST}/{username}")

    status = r.status_code

    if status == 200:
        return f"{VK_REQUEST}/{username}"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_tumblr(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"https://{username}.tumblr.com/")

    status = r.status_code

    if status == 200:
        return f"https://{username}.tumblr.com/"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_slideshare(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{SLIDESHARE_REQUEST}/{username}")

    status = r.status_code

    if status == 200:
        return f"{SLIDESHARE_REQUEST}/{username}"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_reddit(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{REDDIT_REQUEST}/{username}/about/.json")

    status = r.status_code

    if status == 200:
        return f"{REDDIT_REQUEST}/{username}"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_patreon(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{PATREON_REQUEST}/{username}")

    status = r.status_code

    if status == 200:
        return f"{PATREON_REQUEST}/{username}"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_ebay(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{EBAY_REQUEST}/{username}")

    result = r.text.find("The User ID you entered was not found")

    if result == -1:
        return f"{EBAY_REQUEST}/{username}"
    else:
        return danger("Not Found") 
        
def check_docker(username=""):
    if not username:
        return "No Username Entered"
    
    r = requests.get(f"{DOCKER_REQUEST}/{username}/")

    status = r.status_code

    if status == 200:
        return f"{DOCKER_RESPONSE}/{username}"
    elif status == 404:
        return danger("Not Found") 
    else:
        return "Error"

def check_social(username):
    result = []
    res = ""

    print("Analysing the internet...")
    
    print("Checking Pinterest: ", end=" ")
    res = f"Pinterest: {check_pinterest(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking VK:", end=" ")
    res = f"VK: {check_vk(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Tumblr:", end=" ")
    res = f"Tumblr: {check_tumblr(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Reddit:", end=" ")
    res = f"Reddit: {check_reddit(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Docker:", end=" ")
    res = f"Docker: {check_docker(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Ebay:", end=" ")
    res = f"Ebay: {check_ebay(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Slideshare:", end=" ")
    res = f"Slideshare: {check_slideshare(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Patreon:", end=" ")
    res = f"Patreon: {check_patreon(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Quora:", end=" ")
    res = f"Quora: {check_quora(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Github:", end=" ")
    res = f"Github: {check_github(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    print("Checking Trello:", end=" ")
    res = f"Trello: {check_trello(username)}"
    print(res[res.find(":")+1:])
    result.append(res)

    found = list(filter(lambda x: x.find("Not Found")==-1 and x.find("Error")==-1,result))

    print("\nHere's what I found online: ")
    for f in found:
        print(f)

username = input("Enter username: ")

check_social(username)

