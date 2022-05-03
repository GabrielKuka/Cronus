import requests,sys
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

def check_dribbble(username=""):
    if not username: return "No Username Entered"

    r = requests.get(f'{DRIBBBLE_REQUEST}/{username}')

    status = r.status_code

    if status == 200:
        return f"{DRIBBBLE_REQUEST}/{username}"
    elif status == 404:
        return danger("Not Found")
    else:
        return "Error"

def check_disqus(username=""):
    if not username: return "No Username Entered"

    r = requests.get(f'{DISQUS_REQUEST}/{username}')

    status = r.status_code

    if status == 200:
        return f"{DISQUS_REQUEST}/{username}"
    elif status == 404:
        return danger("Not Found")
    else:
        return "Error"

def check_aboutme(username=""):
    if not username: return "No Username Entered"

    r = requests.get(f'{ABOUTME_REQUEST}/{username}')

    status = r.status_code

    if status == 200:
        return f"{ABOUTME_REQUEST}/{username}"
    elif status == 404:
        return danger("Not Found")
    else:
        return "Error"

def check_social(username):
    result = []

    def print_each(social, func):
        print(f"Checking {social}:", end=" ")
        res = f"{social}: {func}"
        print(f"{Fore.GREEN}{res[res.find(':')+1:]}{Style.RESET_ALL}")
        result.append(res)

    print("Analysing the internet...")
    
    print_each("Pinterest", check_pinterest(username))
    print_each("VK", check_vk(username))
    print_each("Tumblr", check_tumblr(username))
    print_each("Reddit", check_reddit(username))
    print_each("Docker", check_docker(username))
    print_each("Github", check_github(username))
    print_each("Ebay", check_ebay(username))
    print_each("Slideshare", check_slideshare(username))
    print_each("Patreon", check_patreon(username))
    print_each("Quora", check_quora(username))
    print_each("Trello", check_trello(username))
    print_each("Disqus", check_disqus(username))
    print_each("AboutMe", check_aboutme(username))


    found = list(filter(lambda x: x.find("Not Found")==-1 and x.find("Error")==-1,result))

    print("\nHere's what I found online: ")
    for f in found:
        print(f)

username = input("Enter username (or \"q\" to exit): ")

while username:
    if username == "q":
        sys.exit(0)
    check_social(username)
    username = input("\nEnter username (or \"q\" to exit): ")