import gtts
from django.utils.text import slugify
import phrases
import winsound as w

def tts_con(text: str, lang: str, name: str):
    tts = gtts.gTTS(text=text, lang=lang)
    file = slugify(name.lower())
    tts.save(f'audios/{file}.mp3')
    print(f'✅ "{file}.mp3" has been created!')

for phrase in phrases.numbers_words:
    tts_con(text=phrase, lang='en', name=phrase)

# for en in phrases.numbers_translation:
#     # print(en + " " + phrases.numbers_translation[en])
#     ru = phrases.numbers_translation[en]
#     tts_con(text=ru, lang='ru', name=en)

# Success!
w.MessageBeep(w.MB_OK)
print('SUCCESSFULLY!')