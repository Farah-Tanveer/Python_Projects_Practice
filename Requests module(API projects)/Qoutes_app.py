import requests

API_KEY = "/5ho6RJtSw+PVgmsV/TcmA==kSicTOa6lsHKYZFU"  
API_URL = "https://api.api-ninjas.com/v1/quotes"

favorites = []

def get_quote(): 
    try:
        response = requests.get(API_URL, headers={"X-Api-Key": API_KEY})
        if response.status_code == 200:
            data = response.json()
            if data and "quote" in data[0]:
                return data[0]["quote"], data[0]["author"]
            else:
                return None, None
        else:
            return None, None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

def show_favorites():
    if not favorites:
        print("\nNo favorites saved yet.")
    else:
        print("\nYour Favorite Quotes")
        for i, (quote, author) in enumerate(favorites, 1):
            print(f"{i}. \"{quote}\" — {author}")
 

while True:
    quote, author = get_quote()
    if quote:
        print("\nQuote of the Moment")
        print(f"\"{quote}\"")
        print(f" — {author}\n")

        choice = input("Options: [Enter] New Quote | [S] Save Quote | [F] Favorites | [Q] Quit: ").strip().lower()
        if choice == "q":
            print("\nGoodbye!")
            break
        elif choice == "s":
            favorites.append((quote, author))
            print("Quote saved to favorites!")
        elif choice == "f":
                show_favorites()
    else:
        print("Could not fetch quote. Try again later.")
        break

if favorites:
    print("\nYour Favorite Quotes Before Exit:")
    for i, (q, a) in enumerate(favorites, 1):
        print(f"{i}. \"{q}\" — {a}")


