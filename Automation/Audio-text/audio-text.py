import json

import speech_recognition as sr
import datetime as dt

r = sr.Recognizer()
run = True

with open("notepad.json", "r") as f:
    data = json.load(f)

while run:
    with sr.Microphone() as source:
        print("Working...")
        audio_text = r.listen(source)
        print("Done")
        try:
            text = r.recognize_google(audio_text)
            print(json.dumps(data, indent=4))
            # create json file

            now = dt.now()
            timestamp = dt.timestamp(now)
            data["notes"].append({
                str(timestamp): text
            })

            with open("notepad.json", "w") as outputfile:
                outputfile.write(json.dumps(data, indent=4))

        except KeyboardInterrupt:
            print("Stopping")
        except:
            print("Error")
            run = False
