from email.policy import default
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
        return danger("[-] Not Found") 
        
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

def check_7cups(username=""):
    r = requests.get(f"{CUPS7_REQUEST}/@{username}")

    return default_return(r, f"{CUPS7_REQUEST}/@{username}")

def check_artistsnclients(username=""):
    r = requests.get(f"{ARTISTSNCLIENTS_REQUEST}/{username}")

    return default_return(r, f"{ARTISTSNCLIENTS_REQUEST}/{username}")

def check_ameblo(username=""):
    r = requests.get(f"{AMEBLO_REQUEST}/{username}")

    return default_return(r, f"{AMEBLO_REQUEST}/{username}")

def check_aminoapps(username=""):
    r = requests.get(f"{AMINOAPPS_REQUEST}/{username}")

    return default_return(r, f"{AMINOAPPS_REQUEST}/{username}")

def check_cloudflare(username=""):
    r = requests.get(f"{CLOUDFLARE_REQUEST}/{username}")

    return default_return(r, f"{CLOUDFLARE_REQUEST}/{username}")

def check_cnet(username=""):
    r = requests.get(f"{CNET_REQUEST}/{username}")

    return default_return(r, f"{CNET_REQUEST}/{username}")

def check_devto(username=""):
    r = requests.get(f"{DEVTO_REQUEST}/{username}")

    return default_return(r, f"{DEVTO_REQUEST}/{username}")

def check_kickstarter(username=""):
    r = requests.get(f"{KICKSTARTER_REQUEST}/{username}")

    return default_return(r, f"{KICKSTARTER_REQUEST}/{username}")

def check_animeplanet(username=""):
    r = requests.get(f"{ANIMEPLANET_REQUEST}/{username}")

    status = r.status_code

    if status == 200:
        return f"{ANIMEPLANET_REQUEST}/{username}"
    elif status == 302:
        return danger("[-] Not Found")
    else:
        return danger(f"[!] Error. Status Code: {status}")

def check_notabug(username=""):
    r = requests.get(f"{NOTABUG_REQUEST}/{username}")

    return default_return(r, f"{NOTABUG_REQUEST}/{username}")

def check_openstreetmap(username=""):
    r = requests.get(f"{OPENSTREETMAP_REQUEST}/{username}")

    return default_return(r, f"{OPENSTREETMAP_REQUEST}/{username}")

def check_pastebin(username=""):
    r = requests.get(f"{PASTEBIN_REQUEST}/{username}")

    return default_return(r, f"{PASTEBIN_REQUEST}/{username}")

def check_plurk(username=""):
    r = requests.get(f"{PLURK_REQUEST}/{username}")

    return default_return(r, f"{PLURK_REQUEST}/{username}")

def check_scratch(username=""):
    r = requests.get(f"{SCRATCH_REQUEST}/{username}")

    return default_return(r, f"{SCRATCH_REQUEST}/{username}")

def check_tripadvisor(username=""):
    try: 
        r = requests.get(f"{TRIP_ADVISOR_REQUEST}/{username}", timeout=3)
    except requests.ReadTimeout as e:
        return danger("[!] Request timeout")
    else:
        return default_return(r, f"{TRIP_ADVISOR_REQUEST}/{username}")
    
def check_twitter(username=""):
    r = requests.get(f"{TWITTER_REQUEST}/{username}")

    return default_return(r, f"{TWITTER_REQUEST}/{username}")

def check_vimeo(username=""):
    r = requests.get(f"{VIMEO_REQUEST}/{username}")

    return default_return(r, f"{VIMEO_REQUEST}/{username}")

def check_vine(username=""):
    r = requests.get(f"{VINE_REQUEST}/{username}")

    return default_return(r, f"{VINE_REQUEST}/{username}")

def check_vivino(username=""):
    r = requests.get(f"{VIVINO_REQUEST}/{username}")

    return default_return(r, f"{VIVINO_REQUEST}/{username}")

def check_social(username):
    result = []

    def print_each(social, func):
        print(f"Checking {social}:", end=" ")
        res = f"{social}: {func}"
        print(f"{Fore.GREEN}{res[res.find(':')+1:]}{Style.RESET_ALL}")
        result.append(res)

    print("Analysing the internet...")

    print_each("TripAdvisor", check_tripadvisor(username))
    print_each("Vivino", check_vivino(username))
    print_each("Vine", check_vine(username))
    print_each("Vimeo", check_vimeo(username))
    print_each("Twitter", check_twitter(username))
    print_each("Plurk", check_plurk(username)) 
    print_each("Scratch", check_scratch(username)) 
    print_each("PasteBin", check_pastebin(username))
    print_each("OpenStreetMap", check_openstreetmap(username))
    print_each("NotaBug", check_notabug(username))
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
    print_each("7Cups", check_7cups(username))
    print_each("ArtistsNClients", check_artistsnclients(username))
    print_each("Ameblo", check_ameblo(username))
    print_each("AminoApps", check_aminoapps(username))
    print_each("Anime-Planet", check_animeplanet(username))
    print_each("CNet", check_cnet(username))
    print_each("CloudFlare", check_cloudflare(username))
    print_each("dev.to", check_devto(username))
    print_each("Kickstarter", check_kickstarter(username))

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