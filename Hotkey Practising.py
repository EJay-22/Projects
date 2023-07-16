import time
import random
from threading import Thread


def importTest():
    time.sleep(10)
    print(random.randint(1,10))
    print("10 second is over")

    
def check():
    time.sleep(2)
    if answer != None:
        return
    print("Too Slow")
    lives -= 1

def Hotkey():
    changeHotkey = "C"
    while changeHotkey.casefold() != "b":
        page = "Hotkey"
        pageName = f"[ {page} ]"
        num = len(pageName)
        print()
        for pasteEqual in range(num):
            print("=",end="")
        print(f"\n{pageName}")
        for pasteEqual in range(num):
            print("=",end="")
        print("\n")
        for i in range(0,9):
            print(str(f"Hotkey Slot {i+1}: [{hotkeyNum[i]}]"))
        print("Press [N] to Enter new Hotkey\nPress [B] to Return")
        changeHotkey = input("Enter: ")
        if changeHotkey.casefold() == "n":
            print("Enter the slot number")
            hotkey = 0
            while hotkey < 1 or hotkey > 9:
                hotkey = int(input("Hotkey Slot: "))
                if hotkey > 0 and hotkey < 10:
                    while True:
                        hotkeyCheck = input(f"Enter Hotkey for Slot {hotkey}: ")
                        if len(str(hotkeyCheck)) != 1:
                            print("Please Enter only ONE Key")
                        elif len(str(hotkeyCheck)) == 1:
                            error = 0
                            for checkHotkey in range(0,9):
                                if hotkeyNum[checkHotkey] == hotkeyCheck:
                                    error += 1
                            if error > 0:
                                print("Please Enter a Different Key")
                            elif error <= 0:
                                hotkeyNum[hotkey - 1] = hotkeyCheck
                                break
                elif changeHotkey.casefold() == "b":
                            print("Going Back....")
                else:
                    print("Please Enter ONLY Slot Number 1 to 9")

def Inventory():
    changeInv = "C"
    while changeInv.casefold() != "b":
        page = "Inventory"
        pageName = f"[ {page} ]"
        num = len(pageName)
        print()
        for pasteEqual in range(num):
            print("=",end="")
        print(f"\n{pageName}")
        for pasteEqual in range(num):
            print("=",end="")
        print("\n")
        print("=================================================")
        for n in range(0,9):
            print("|",end="")
            print(Inv[n],end="")
        print("|")
        print("=================================================")
        print("Press [A] to Arrange Inventory\nPress [B] to Return")
        changeInv = input("Enter: ")
        if changeInv.casefold() == "a":
            print("Choose Two Inv Slot to Swap")
            FirstInvSwap = 0
            SecondInvSwap = 0
            while FirstInvSwap < 1 or FirstInvSwap > 9:
                FirstInvSwap = int(input("Enter First Inv Slot to Swap: "))
                if FirstInvSwap > 0 and FirstInvSwap < 10:
                    InvStorage1 = Inv[FirstInvSwap - 1]
                else:
                    print("Please Enter ONLY Slot Number 1 to 9")
            while SecondInvSwap < 1 or SecondInvSwap > 9:
                SecondInvSwap = int(input("Enter Second Inv Slot to Swap: "))
                if SecondInvSwap == FirstInvSwap:
                    SecondInvSwap = 0
                    print("Please Enter a Different Inv Slot Number")
                elif SecondInvSwap > 0 and SecondInvSwap < 10:
                    InvStorage2 = Inv[SecondInvSwap - 1]
                else:
                    print("Please Enter ONLY Slot Number 1 to 9")
            print(f"Swapping Inv Slot {FirstInvSwap} with {SecondInvSwap}...")
            Inv[FirstInvSwap - 1] = InvStorage2
            Inv[SecondInvSwap - 1] = InvStorage1
        elif changeInv.casefold() == "b":
            print("Going Back....")
        else:
            print("Please Enter Correct Input")

def Scenario():
    SceneNum = 1
    PrevScene = 7
    NextScene = 2
    changeScene = "C"
    while changeScene.casefold() != "b":
        page = "Scenario"
        pageName = f"[ {page} ]"
        num = len(pageName)
        print()
        for pasteEqual in range(num):
            print("=",end="")
        print(f"\n{pageName}")
        for pasteEqual in range(num):
            print("=",end="")
        print("\n")
        print(f"Scene {SceneNum}: {Scene[SceneNum - 1]}\n")
        print(f"Type [Prev] to go back to Scene {PrevScene}\nType [Next] to continue to Scene {NextScene}\nPress [B] to return")
        changeScene = input("Enter: ")
        if changeScene.casefold() == "prev":
            if SceneNum == 1: 
                SceneNum = 7
                PrevScene = SceneNum - 1
                NextScene = 1
            else:
                SceneNum -= 1
                PrevScene = SceneNum - 1
                NextScene = SceneNum + 1
        elif changeScene.casefold() == "next":
            if SceneNum == 7:
                SceneNum = 1
                PrevScene = 7
                NextScene = SceneNum + 1
            else:
                SceneNum += 1
                PrevScene = SceneNum - 1
                NextScene = SceneNum + 1
        elif changeScene.casefold() == "b":
            print("Going Back....")
        else:
            print("Please Enter Correct Input")


hotkeyNum = [1,2,3,4,5,6,7,8,9]
Inv = ["SWORD","PICK","AXE","SHEAR","WOOL","GOLD","IRON","EMPTY","EMPTY"]
Scene = ["Bridging","Player started attacking","Got stuck by a wool block","wood defence","endstone defence","iron in the inv","gold in the inv"]
start = "C"
while start.casefold() != "y":
    page = "Main"
    pageName = f"[ {page} ]"
    num = len(pageName)
    print()
    for pasteEqual in range(num):
        print("=",end="")
    print(f"\n{pageName}")
    for pasteEqual in range(num):
        print("=",end="")
    print("\n")
    print("Press [S] to start")
    print("Press [O] to view options")
    start = input("Input: ")
    if start.casefold() == "":
        startInput = "C"
    if start.casefold() == "o":
        optionInput = "c"
        while optionInput.casefold() != "b":
            page = "Options"
            pageName = f"[ {page} ]"
            num = len(pageName)
            print()
            for pasteEqual in range(num):
                print("=",end="")
            print()
            print(pageName)
            for pasteEqual in range(num):
                print("=",end="")
            print("\n")
            print("Press [H] for Hotkey")
            print("Press [I] for Inventory")
            print("Press [S] for Scenario")
            print("Press [B] to go Back")
            optionInput = input("Input: ")
            if optionInput.casefold() == "h":
                Hotkey()
            if optionInput.casefold() == "i":
                Inventory()
            if optionInput.casefold() == "s":
                Scenario()
