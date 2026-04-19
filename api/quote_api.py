import requests

class QuoteAPI:

    def __init__(self):

        self.url = "https://zenquotes.io/api/quotes"

    def quote(self):

        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data[10]['q'], data[10]['a']
        else:
            return "Error", 404