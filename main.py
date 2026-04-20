from api.quote_api import QuoteAPI
from data_handling import file_handler

def main():

    api = QuoteAPI()

    while True:

        print("\n1. Generate Quote")
        print("2. View Quote Collection")

        selection = input("\n>> ")

        if selection == "1":

            response = api.quote()

            for item in response:
                print(item)

if __name__ == "__main__":
    main()