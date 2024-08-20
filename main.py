import requests
import concurrent.futures
import time

cooldown_option = True # If you are not using proxies set this to true.
reverse_option = False; # Set to true if you want to run wordlist in reverse. HELP would become PLEH

url = "https://codes.thisisnotawebsitedotcom.com/"
validcodeurl = "https://haykam.com/notawebsite/submit"

# Load the list of common words. If it doesn't work try "ISO-8859-1" encoding. Usually "UTF-8" will work always.
with open('words.txt', 'r', encoding="UTF-8") as file:
    words = file.read().splitlines()


def try_code(code, reverse_words, cooldown):
    if cooldown:
        time.sleep(0.01)
    if reverse_words:
        code = code[::-1]

    files = {
        'code': (None, code),
    }
    response = requests.post(url, files=files)

    if response.status_code == 200:
        with open('valid_codes.txt', 'a') as valid_file: # Saves all valid words to a file...
            valid_file.write(f"{code}\n")
        data = {"code": code}
        haykamrequest = requests.post(validcodeurl, json=data) # ... and sends it to Haykam's endpoint
        print(f"{response.status_code}: Valid code found: {code}, Haykam's endpoint check: {haykamrequest.status_code}")
        return True
    elif response.status_code == 429:
        print(f"{response.status_code}, Failed to send code {code} , too many requests! Make sure you are using proxies or cooldown?")
        time.sleep(0.01)
    elif response.status_code == 404:
        print(f"{response.status_code}: Attempted code: {code} - Incorrect")
        return False


with concurrent.futures.ThreadPoolExecutor(max_workers=2500) as executor: # If you experience problems you may need to decrease the max workers amount, but you can also increase it!
    futures = {executor.submit(try_code, word, reverse_option, cooldown_option): word for word in words}
    for future in concurrent.futures.as_completed(futures):
        future.result()