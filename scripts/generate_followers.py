# scripts/generate_followers.py
import requests
import os
import sys

USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

if not USERNAME:
    print("Error: GITHUB_USERNAME environment variable is required")
    sys.exit(1)

if not TOKEN:
    print("Error: GITHUB_TOKEN environment variable is required")
    sys.exit(1)

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def fetch_followers(username):
    url = f"https://api.github.com/users/{username}/followers"
    followers = []
    page = 1
    
    print(f"Fetching followers for {username}...")
    
    while True:
        print(f"Fetching page {page}...")
        resp = requests.get(f"{url}?page={page}&per_page=100", headers=headers)
        
        if resp.status_code == 404:
            print(f"Error: User '{username}' not found")
            sys.exit(1)
        elif resp.status_code == 403:
            print("Error: API rate limit exceeded or insufficient permissions")
            sys.exit(1)
        elif resp.status_code != 200:
            print(f"Error: API request failed with status {resp.status_code}")
            print(f"Response: {resp.text}")
            sys.exit(1)
            
        data = resp.json()
        if not data:
            break
            
        followers.extend(data)
        page += 1
        
    print(f"Found {len(followers)} followers")
    return followers

def generate_html(followers, columns=6):
    rows = []
    for i in range(0, len(followers), columns):
        row = followers[i:i+columns]
        row_html = "  <tr>\n"
        for user in row:
            row_html += f"""    <td align="center">
      <a href="{user['html_url']}" aria-label="{user['login']}">
        <img src="{user['avatar_url']}" width="50px" alt="{user['login']}"/><br />
        <sub><b>{user['login']}</b></sub>
      </a>
    </td>\n"""
        for _ in range(columns - len(row)):
            row_html += "    <td></td>\n"
        row_html += "  </tr>\n"
        rows.append(row_html)
    return "<div align=\"center\">\n<table>\n" + "\n".join(rows) + "</table>\n</div>"

def save_html(content, path="followers.html"):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root
    project_root = os.path.dirname(script_dir)
    # Create the full path to the HTML file
    full_path = os.path.join(project_root, path)
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"HTML file saved to: {full_path}")

if __name__ == "__main__":
    try:
        followers = fetch_followers(USERNAME)
        if not followers:
            print("No followers found or unable to fetch followers")
            sys.exit(0)
            
        html = generate_html(followers)
        save_html(html)
        print("Successfully generated followers grid!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
