import json

def save_quote(quote, author):

    try:

        with open("quotes.json", "r") as file:
            data = json.load(file)

    except:

        data = []

    data.append({"quote": quote, "author": author})

    with open("quotes.json", "w") as file:
        json.dump(data, file, indent=4)