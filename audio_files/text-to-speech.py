from gtts import gTTS
import os

language = 'en'
texts = [
    "Welcome to Oculus testing platform.",
    "We have provide 3 diagnostics test",
]

for text in texts:
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save(text+".mp3")