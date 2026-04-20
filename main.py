from quote_api import QuoteAPI

def main():

    api = QuoteAPI()

    quote_collection = []

    while True:

        print("\n1. Generate Quote")
        print("2. View Quote Collection")

        selection = input("\n>> ")

        if selection == "1":

            response = api.quote()

            print("")

            print(response)

            quote_collection.append(response)

        elif selection == "2":

            for quote in quote_collection:
                print(quote)

if __name__ == "__main__":
    main()