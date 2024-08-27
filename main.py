import requests

websites = {
    "Github": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "YouTube": "https://youtube.com/@{}",
    "LinkedIn": "https://linkedin.com/in/{}",
    "Chess": "https://chess.com/member/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Reddit": "https://reddit.com/user/{}",
    "Telegram": "https://t.me/{}"
}

def check_username_on_website(website_name, url_pattern, username):
    # Format the URL with the username
    url = url_pattern.format(username)
    
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        
        # Check the status code to determine if the username exists
        if response.status_code == 200:
            print(f"[+] {website_name}: Username '{username}' found!")
        else:
            print(f"[-] {website_name}: Username '{username}' not found.")
    
    except requests.RequestException as e:
        print(f"[!] Error checking {website_name}: {e}")

def main():
    # Take username input from the user
    username = input("Enter the username to search for: ")
    
    # Check the username on all websites
    for website_name, url_pattern in websites.items():
        check_username_on_website(website_name, url_pattern, username)

if __name__ == "__main__":
    main()