import os
import keyboard

print("system online, type the name of the bat file you want to run, then press print scrn. Press print scrn+esc to exit")
def run_neg():
    print("launching neg")
    os.startfile('neg.bat')

def run_pho():
    print("launching pho")
    os.startfile('pho.bat')

keyboard.add_word_listener(word="pho", callback=run_pho, triggers=['print scrn'], match_suffix=True)
keyboard.add_word_listener(word="neg", callback=run_neg, triggers=['print scrn'], match_suffix=True)
keyboard.wait('print scrn + esc')