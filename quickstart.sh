curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: SOME_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Write a text 1000 characters long using words with Cyrillic letters asdfghjkl. Do not use punctuation marks, capital letters, or any other characters other than those allowed. Do not use words longer than 10 characters."
          }
        ]
      }
    ]
  }'