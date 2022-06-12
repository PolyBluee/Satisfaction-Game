# Modules

import time
import os
import platform

# Clear Function

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

def p():
    os.system("pause >nul")

# Act 0 - Prologue

def actzero():
    print("???:  ...")
    time.sleep(3)
    print("???:  Where am I?")
    time.sleep(3)
    print("You see nothing but darkness. ⏎")
    p()
    print("From now on, I will be the narrator. I will keep narrating what you see. ⏎")
    p()
    print("I know it's a tedious task, but that's the best I can do for you. ⏎")
    p()
    print("Oh, I know! I will show you some mechanics and things that will help you with this adventure. ⏎")
    p()
    print("Within 5 seconds, the controls and mechanics shall appear...!")
    time.sleep(5)
    clear()
    print("""
    1. Lines with no "⏎" symbol at the end proceed automatically. It is recommended not to press any key, think of it like a 
       "reflex test".
    2. Lines with "⏎" symbol at the end need a keypress to continue. Please use 'ENTER' / 'RETURN', it is the preferred key.
    3. Sometimes the narrator can interrupt while talking, which will be shown in brackets using the keyword 'Narr'. Other 
       characters can interrupt too, but their keyword will be different.
       For example,
       You:   Lorem Ipsum Dolor!    (Narr: Yeah, type in filler text now... That's all you have.)
    4. New rules and clues may appear as time goes by.

    You can view these basic rules in the 'rules.txt' file in the 'Misc' folder.
    ⏎
    """)
    p()
    clear()
    print("But please, do not get ahead of yourself. I may not be present everywhere. ⏎")
    p()
    print("You cannot believe anyone these days, can you? ⏎")
    time.sleep(1)
    clear()
    print("???:  It's so dark... It's very dark.")
    time.sleep(3)
    print("???:  Can anyone hear me?")
    time.sleep(3)
    print("???:  Someone, anyone, if you can hear me...")
    time.sleep(3)
    print("???:  PLEASE!")
    time.sleep(2)
    print("???:  Please say something...!")
    time.sleep(3)
    print("???:  I'm so scared...")
    print("You were screaming on the top of your lungs when suddenly...! ⏎")
    p()
    clear()

    print("Mom:  Wake up Brendan! You're late for school! ⏎")
    p()
    print("You (Brendan):  Sch... school? ⏎")
    p()
    print("You thought to yourself as you slowly opened your eyes. ⏎")
    p()
    print("There you were in your bed, staring at the fan that was hanging from the ceiling. ⏎")
    p()
    print("You:  Oh, it's just another day. ⏎")
    p()
    clear()
    print("Mom:  Just another day?! Today is your exam you idiot! ⏎")
    p()
    print("Mom:  You have to get ready quickly! Here, I've got your goods ready, and for breakfast I-")
    time.sleep(0.5)
    print("You:  Mom chill! ⏎")
    p()
    print("You:  It's still 7 A.M., what's the hurry?! ⏎")
    p()
    print("")
    print("Mom:  Your exam starts from 8! Did you forget? ⏎")
    p()
    print("Mom:  Oh sweet summer child, when will you grow up? ⏎")
    p()
    print("")
    print("You heard as your mom uttered those words and physically felt pain. ⏎")
    p()
    print("She started to pull your sleeves when you finally gave up, and got off of the bed. ⏎")
    p()
    clear()
    print("Your name is Brendan Dees. ⏎")
    p()
    clear()
    print("You:  My name is Brendan Dees.")
    time.sleep(3)
    print("I am a teenager and sixteen years old.   (Narr: Yeah, I guess you can do the talking.)")
    time.sleep(3)
    print("I currently am in 11th standard. Today my exams start which will decide if I continue to next grade or not...")
    time.sleep(3)
    print("...and I'm late for the first exam, that's my life.")
    time.sleep(3)
    clear()
    time.sleep(3)
    print("ACT 0 - PROLOGUE")
    time.sleep(1)
    print("END")
    time.sleep(1)
    print("")
    print("To continue the story, please go into the 'Acts' folder and run 'actone.py'. Please press any key to exit.")
    p()
    exit()