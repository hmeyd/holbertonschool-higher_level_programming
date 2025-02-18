#!/usr/bin/python3
"""
a basic Python script to fetch posts from
JSONPlaceholder using requests
"""


import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print their titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("status_code:{}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("failed")


def fetch_and_save_posts():

    """Fetch posts and save them into a CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        posts = reponse.json()
        fieldnames = ["id", "title", "body"]
        with open('posts.csv', mode="w", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for post in posts:
                writer.writerow({"id": post["id"], "title":
                                 post["title"], "body": post["body"]})
        print("posts have been saved")
    else:
        print("failed")
