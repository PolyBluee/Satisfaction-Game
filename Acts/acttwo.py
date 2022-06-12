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

def post_inv_trial():
    clear()
    print("You:  That was really fun! ⏎")
    p()
    print("I know right. Also, investigation segments are meant to find hints, but are optional. However, it is recommended to investigate. ⏎")
    p()
    print("Gotta utilize the powers you are given, kid. ⏎")
    p()
    print("You:  Yeah I know. I've got this.")
    p()
    print("Also, you will find achievements once in a while. They don't count towards anything, they are just for fun. You can check 'achievements.txt' in the 'Misc' folder for achievement hunting! ⏎")
    p()
    print("You:  Cool.")


# INVESTIGATION TRIAL

def inv_trial():

    print("-- INVESTIGATION START --                <-- This marks the investigation beginning.")
    print("It doesn't hurt to take a look.          <-- This is your motto! How sweet...")
    print("")
    print("Location: Hospital                       <-- This shows your current location.")
    print("")
    print("")
    print("Choose something to INVESTIGATE.")
    print("1 - Exit door")
    print("2 - Stretchers                           <-- These three are the things you can look at right now. These differ at locations.")
    print("3 - Dustbins")
    print("E - Exit INVESTIGATION                   <-- Use 'E' to exit investigating and progress through the game.")

    inv_trial_c = input("Enter a number or 'E' to INVESTIGATE/End INVESTIGATION > ")

    if inv_trial_c == "1":
        print("INVESTIGATING: Exit Door")
        print("This is the exit door through which you can exit the hospital. It's better not to leave now. ⏎")
        p()
        clear()
        inv_trial()
    elif inv_trial_c == "2":
        print("INVESTIGATING: Stretchers")
        print("These are used to carry patients around. Brendan was carried on one of them... ⏎")
        p()
        clear()
        inv_trial()
    elif inv_trial_c == "3":
        print("INVESTIGATING: Dustbins")
        print("There are dustbins that are shaded red and blue. They are used to store medical things, not flowers. The blue dustbin isn't sad either. ⏎")
        p()
        print("Wanna take a look inside the blue dustbin? (y/n)")

        inv_trial_c_bludust = input("> ")

        if inv_trial_c_bludust == "y":
            print("")
            print("There's a sunflower with the initials A.B. inscribed carefully on one of the petals. ⏎")
            p()
            print("")
            print("ACHIEVEMENT GET! -- Oh, broken heart... [Task: Find a remain of love in the hospital.] ⏎")
            p()
            print("Oh look, you got an achievement! These don't count towards anything, they are just for fun. You can check 'achievements.txt' in the 'Misc' folder for achievement hunting! ⏎")
        else:
            print("Decided not to look inside the dustbin. Disgusting! ⏎")
            p()
            clear()
            inv_trial()
        inv_trial()

    else:
        clear()
        print("-- INVESTIGATION END --                  <-- Marks the end of an investigation.")
        print("That was a good trial!                   <-- Your ending line, how sweet... ⏎")
        p()
        post_inv_trial()

# Act 2 - Me and My Friends (Part II)

def acttwo():
    print("This act expects that you have finished 'Act 0' and 'Act 1'.")
    print("If you haven't yet finished 'Act 0' and 'Act 1', it is expected you finish them.")
    print("You may not understand the story if you do not finish the acts in order.")
    print("")
    print("Pressing a button will continue this act, or close this act if you haven't finished the aforementioned act(s). ⏎")

    p()
    clear()

    time.sleep(3)
    print("ACT 2 - ME AND MY FRIENDS (PART II)")
    time.sleep(1)
    print("BEGIN")
    time.sleep(3)
    clear()

    print("...")
    time.sleep(2)
    print("Hey...")
    time.sleep(2)
    print("You there...?")
    time.sleep(2)
    print("Andrew, can you listen to me?")
    time.sleep(2)
    print("You (Andrew):  WAHHHHH!!!")
    time.sleep(1)
    clear()
    

    print("...")
    time.sleep(2)
    print("Stop freaking out already, you know what's up. ⏎")
    p()
    print("You:  Wh- who is talking to me? ⏎")
    p()
    print("Oh come on, Brendan never questioned the voices in his head, why should you? ⏎")
    p()
    print("You:  Oh... Brendan... ⏎")
    p()
    print("You:  BRENDAN WHY?! ⏎")
    p()
    print("It's okay, things like these happen all the time. ⏎")
    p()
    print("You:  I don't know who I am talking to, but YOU CAN SHUT THE HELL UP! ⏎")
    p()
    print("You:  Brendan was my BEST FRIEND! Do you even know what that means?! ⏎")
    p()
    print("Oh please, not with that 'bEsT fRiEnD' thing again. He's DEAD. Okay? ⏎")
    p()
    clear()
    print("You:  ... You seem awfully happy that Brendan's gone, are you hiding something from me?   (Narr: E- Eh?) ⏎")
    p()
    print("What is there to h- hide? I am just a voice, you know. I'm totally neutral.")
    p()
    print("You:  But why are you in my head now? And how do you know about Brendan? Were you with him before? And if you were, why are you here now-")
    time.sleep(0.5)
    print("HOLD IT! CUT YOUR BULLCRAP ALREADY. ⏎")
    p()
    print("You:  Eh?? ⏎")
    p()
    clear()
    print("It's just how this world is, okay kid? People come, people make you special, people go. They return to make things right, they again leave. ⏎")
    p()
    print("That's the way the world is. Your 'bEsT fRiEnD' Brendan, was no one, but just another person you knew. ⏎")
    p()
    print("Many come, many go. He's gone, someone else will come for you. Now stop repenting, will you? ⏎")
    p()
    clear()
    print("You:  ... ⏎")
    p()
    print("You:  Alright, I'll stop. ⏎")
    p()
    print("You:  But I swear on Brendan's grave, if his departure has something to do with you, I'll find you. ⏎")
    p()
    print("Is that supposed to be a threat? If yes, it won't work on me. ⏎")
    p()
    print("Let us now continue with the story, shall we? ⏎")
    p()
    print("You:  What story? ⏎")
    p()
    print("Umm... I mean, let me introduce myself! Where are my manners... ⏎")
    p()
    clear()
    print("I am your NARRATOR! I will narrate things you see, observe, and feel! ⏎")
    p()
    print("You:  I'm not sure why I'd need that, but sounds pretty neat. ⏎")
    p()
    print("It sure is! Also, you are Andrew. Andrew what? ⏎")
    p()
    print("You:  Andrew Joe. ⏎")
    p()
    print("Joe... Joe who? ⏎")
    p()
    print("You:  Please no... Just... no... ⏎")
    p()
    print("That name doesn't quite fit right, so I'll call you Andrew Stilth from now on! ⏎")
    p()
    print("You:  St- Still- what? WHY'D YOU CHANGE MY SURNAME?! ⏎")
    p()
    print("Oh for no reason... it's just that the word 'Joe' induces a very bad joke, and that your new surname has the letter 'S'! ⏎")
    p()
    print("You:  What does the letter 'S' have to do with anything...? ⏎")
    p()
    print("Nothing really! It is another one of my gimmicks! Let us just continue. ⏎")
    p()
    print("You:  Okay...? ⏎")
    p()
    clear()

    print("Er hem... so where was I? ⏎")
    p()
    print("Oh yes! Andrew, you have a *special* power...! ⏎")
    p()
    print("You:  Special power? What is it? ⏎")
    p()
    print("You can interact with objects! It's called INVESTIGATION! ⏎")
    p()
    print("You: Oh really? What does it do though? ⏎")
    p()
    print("You learn more about your surroundings, and probably unravel new mysteries! Wanna give it a shot? ⏎")
    p()
    print("You:  Sure! ⏎")
    p()
    
    print("Alrighty, here we go! ⏎")
    p()
    clear()
    inv_trial()

    

    



acttwo()