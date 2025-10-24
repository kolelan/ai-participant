import requests
API_KEY = "AIzNSyCHjRWAYIeXjS3hjaSW-sOj2Fz2tXuP70M"
LETTERS_COUNT = 1000
LATIN_LETTERS = "a s d f g h j k l"
LATIN_LETTERS_NOT_USE = "q w e r t y u i o p z x c v b n m"
CIRILLIC_LETTERS = "ф ы в а п р о л д ж"
CIRILLIC_LETTERS_NOT_USE = "й ц у к е н г ш щ з х я ч с м и т ь б ю"
MIN_LETTERS_IN_WORD = 2
MAX_LETTERS_IN_WORD = 7
print('hello');

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
print(url)
prompt = f"Write a text {LETTERS_COUNT} characters long using words with Cyrillic letters {CIRILLIC_LETTERS}. Do not use punctuation marks, capital letters, or any other characters other than those allowed. Don't use the letters from the next set {CIRILLIC_LETTERS_NOT_USE}. Use words with a word length of {MIN_LETTERS_IN_WORD} to {MAX_LETTERS_IN_WORD} characters. Don't repeat phrases. Use as many unique words as possible."
promptLatin = f"Write a text {LETTERS_COUNT} characters long using words with Latin letters {LATIN_LETTERS}. Do not use punctuation marks, capital letters, or any other characters other than those allowed. Don't use the letters from the next set {LATIN_LETTERS_NOT_USE}. Use words with a word length of {MIN_LETTERS_IN_WORD} to {MAX_LETTERS_IN_WORD} characters. Don't repeat phrases. Use as many unique words as possible. Each word is either a noun, a verb, an adjective, or another part of speech. Make sure that the same parts of speech do not stand next to each other."
print(promptLatin)
data = {
    "contents": [{
        "parts": [{
            "text": promptLatin
        }]
    }]
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    # Extract the generated text
    try:
        generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
        print(generated_text)
    except KeyError as e:
        print("Unexpected JSON structure:", e)
        print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)