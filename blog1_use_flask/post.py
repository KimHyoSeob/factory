import requests


class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.blog_response = requests.get(url=self.blog_url)
        self.blog_data = self.blog_response.json()
