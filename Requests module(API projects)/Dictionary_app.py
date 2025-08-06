import requests

API_KEY = "/5ho6RJtSw+PVgmsV/TcmA==kSicTOa6lsHKYZFU"  
API_URL = "https://api.api-ninjas.com/v1/dictionary?word="

def get_meaning(word):
    try:
        response = requests.get(API_URL + word, headers={"X-Api-Key": API_KEY})
        if response.status_code == 200:
            data = response.json()
            if data.get("definition"):
                return data["definition"]
            else:
                return "No meaning found for this word."
        else:
            return f"Error {response.status_code}: Unable to fetch meaning."
    except Exception as e:
        return f"Error: {str(e)}"


while True:
    word= input("\nEnter a word ('exit' to quit): ").strip().lower()
    if word == "exit":
        print("Goodbye")
        break
    if not word:
        print("Please enter a word.")
        continue
    if len(word) < 3:
        print("Word must be at least 3 characters long.")
        continue
    if not word.isalpha():
        print("Word must contain only alphabets (no numbers or symbols).")
        continue

    meaning = get_meaning(word)
    print(f"\nMeaning of '{word}':\n{meaning}")


