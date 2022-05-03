import requests,sys
from config import *
from colorama import Style, Fore

def danger(msg):
    return f"{Fore.RED}{msg}{Style.RESET_ALL}"

def default_return(request, res_url):
    status = request.status_code

    if not status or not res_url:
        return danger("[!] Error. Request status or response URL is wrong")

    if status == 200:
        return res_url
    elif status == 404:
        return danger("[-] Not Found")
    else:
        return danger(f"[!] Error. Status Code: {status}")

def check_trello(username=""):
    
    r = requests.get(f"{TRELLO_REQUEST}/{username}/?invitationTokens=")

    return default_return(r, f"{TRELLO_RESPONSE}/{username}")

def check_pinterest(username=""):

    r = requests.get(f"{PINTEREST_REQUEST}/{username}")

    return default_return(r, f"{PINTEREST_REQUEST}/{username}")

def check_github(username=""):
    
    r = requests.get(f"{GITHUB_REQUEST}/{username}")

    return default_return(r, f"{GITHUB_REQUEST}/{username}")

def check_quora(username=""):
    
    r = requests.get(f"{QUORA_REQUEST}/{username}")

    return default_return(r, f"{QUORA_RESPONSE}/{username}")

def check_vk(username=""):
    
    r = requests.get(f"{VK_REQUEST}/{username}")

    return default_return(r, f"{VK_REQUEST}/{username}")

def check_tumblr(username=""):
    
    r = requests.get(f"https://{username}.tumblr.com/")

    return default_return(r, f"https://{username}.tumblr.com/")

def check_slideshare(username=""):
    
    r = requests.get(f"{SLIDESHARE_REQUEST}/{username}")

    return default_return(r, f"{SLIDESHARE_REQUEST}/{username}")

def check_reddit(username=""):
     
    r = requests.get(f"{REDDIT_REQUEST}/{username}/about/.json")

    return default_return(r, f"{REDDIT_REQUEST}/{username}")

def check_patreon(username=""):
     
    r = requests.get(f"{PATREON_REQUEST}/{username}")

    return default_return(r, f"{PATREON_REQUEST}/{username}")

def check_ebay(username=""):
     
    r = requests.get(f"{EBAY_REQUEST}/{username}")

    result = r.text.find("The User ID you entered was not found")

    if result == -1:
        return f"{EBAY_REQUEST}/{username}"
    else:
        return danger("Not Found") 
        
def check_docker(username=""):
    
    r = requests.get(f"{DOCKER_REQUEST}/{username}/")

    return default_return(r, f"{DOCKER_RESPONSE}/{username}")

def check_dribbble(username=""):

    r = requests.get(f'{DRIBBBLE_REQUEST}/{username}')

    return default_return(r, f"{DRIBBBLE_REQUEST}/{username}")

def check_disqus(username=""):

    r = requests.get(f'{DISQUS_REQUEST}/{username}')

    return default_return(r, f"{DISQUS_REQUEST}/{username}")

def check_aboutme(username=""):

    r = requests.get(f'{ABOUTME_REQUEST}/{username}')

    return default_return(r, f"{ABOUTME_REQUEST}/{username}")

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
        print(f"{Fore.GREEN}Bye!")
        sys.exit(0)
    check_social(username)
    username = input("\nEnter username (or \"q\" to exit): ")

if not username: 
    print(f"{Fore.RED}[!] You didn't enter a username. Try again. Bye!")