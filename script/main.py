#!/usr/local/bin/python3
                        
                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: main.py                                                            #
                        #   created: 2022-10-28                                                          #
                        #   system: Darwin                                                               #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#

import speech_recognition as sr


#variables

rec = sr.Recognizer()




def choice_mic():
    list_mic = sr.Microphone().list_microphone_names() #bring the list of mic inside you compute
    list_mic_def = []
    for i in enumerate(list_mic):
        choice_format = f"{i[0]} - {i[1]}"
        list_mic_def.append(choice_format)
    return list_mic_def

lang = int(input("""Choice your language: 

[1] - English
[2] - Portuguese
 """))

if lang == 1:

    def choiceMic():
        choice = str(choice_mic())
        choice = choice.replace(',','\n').replace(']','').replace("'",'')[1:]
        choiceMic = int(input(f"""Below are listed the microphones of your computer, choose (by typing the corresponding number)
        which you want to use:
        {choice}
        Answer: """))
        return choiceMic

    with sr.Microphone(choiceMic()) as mic:
        rec.adjust_for_ambient_noise(mic) #adjust noise
        print("Speak now: ")
        audio = rec.listen(mic)
        text = rec.recognize_google(audio)
        print(text)

elif lang == 2:

    def choiceMic():
        choice = str(choice_mic())
        choice = choice.replace(',','\n').replace(']','').replace("'",'')[1:]
        choiceMic = int(input(f"""Below are listed the microphones of your computer, choose (by typing the corresponding number)
        which you want to use:
        {choice}
        Answer: """))
        return choiceMic

    with sr.Microphone(choiceMic()) as mic:
        rec.adjust_for_ambient_noise(mic) #adjust noise
        print("Speak now: ")
        audio = rec.listen(mic)
        text = rec.recognize_google(audio, language='pt-BR')
        print(text)
else:
    print("choose one about")