from quote_api import QuoteAPI

def main():

    api = QuoteAPI()

    quote_collection = []

    while True:

        print("\n1. Generate Quote")
        print("2. View Quote Collection")

        selection = input("\n>> ")

        if selection == "1":

            try:

                quote, author = api.quote()

                output = f"\n'{quote}'\n\n - {author}"

                print(output)

                print("\nWould you like to add this quote to your quote collection? (y/n)")

                yes_or_no = input("\n>> ").lower()

                if yes_or_no == "y":

                    quote_collection.append(output)

                    print("\nQuote added!")

                else:

                    pass

            except:

                print("Too many quotes! Try again later.")

        elif selection == "2":

            for output in quote_collection:
                print(output)

if __name__ == "__main__":
    main()