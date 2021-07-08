import random
import string
import win32clipboard

lowers = string.ascii_letters
numbs = string.digits
sym = string.punctuation
print("How many chars.?")
length = input()
pwdlength = int(length)
pwd = (''.join(random.choice(numbs + lowers + sym) for i in range(pwdlength)))
print(pwd)

def gen():
    lowers = string.ascii_letters
    numbs = string.digits
    sym = string.punctuation
    print("How many chars.?")
    length = input()
    pwdlength = int(length)
    pwd = (''.join(random.choice(numbs + lowers + sym) for i in range(pwdlength)))
    print(pwd)
    ok = input("Generate different password.?" + "\n" "Yes or No" + "\n")
    if ok == "yes":
        gen()
    else:
        # set clipboard data
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(pwd)
        win32clipboard.CloseClipboard()
        print("DONE")


ok = input("Generate different password.?" + "\n" "Yes or No" + "\n")
if ok == "yes":
    gen()
else:
    # set clipboard data
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(pwd)
    win32clipboard.CloseClipboard()
    print("DONE")
