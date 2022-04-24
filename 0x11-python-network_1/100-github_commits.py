#!/usr/bin/python3
"""
Write a Python script that takes your
GitHub credentials and uses the GitHub
API to display your id
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    html = requests.get(url)
    commits = html.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
