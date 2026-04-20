import requests

class QuoteAPI:

    def __init__(self):

        self.url = "https://zenquotes.io/api/quotes"

    def quote(self):

        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            quote = data[10]['q']
            author = data[10]['a']
            return quote, author
        else:
            return "Error, too many quotes are being generated! Wait a while."