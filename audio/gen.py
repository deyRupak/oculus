from gtts import gTTS
import os

language = 'en'
texts = "Welcome to Oculus testing platform. 1. This page is playing audio. Kindly keep the volume 🔊 turned on." + " 2. Click on the left tab for 'ADHD' Test & on the right tab for AUTISM' Test." + "3. After you click on the tabs you'll be shown a set of running images." + "4. Click on the START TEST button to begin." + "5. After you're done with the tests, hit 'SPACEBAR' to stop." + "6. Observe those images while trying to distinguish between them."


# for text in texts:
speech = gTTS(text = texts, lang = language, slow = False)
speech.save("instruction.mp3")
