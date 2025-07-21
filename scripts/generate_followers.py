# scripts/generate_followers.py
import requests
import os

USERNAME = os.getenv("GITHUB_USERNAME", "your-username")
TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def fetch_followers(username):
    url = f"https://api.github.com/users/{username}/followers"
    followers = []
    page = 1
    while True:
        resp = requests.get(f"{url}?page={page}&per_page=100", headers=headers)
        if resp.status_code != 200:
            print("Error:", resp.text)
            break
        data = resp.json()
        if not data:
            break
        followers.extend(data)
        page += 1
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
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    followers = fetch_followers(USERNAME)
    html = generate_html(followers)
    save_html(html)
