import random
import time

def voting():
    voting = True
    while voting == True:
        vote_someone = int(input("Who do you want to vote out:\nPlayer: "))
        if vote_someone == 2:
            ready = False
            while ready == False:
                readyOrNot = input("Are you ready to roll the dice?[Y/N]")
                if readyOrNot.casefold() == "y" or readyOrNot.casefold() == "yes":
                    dice = random.randint(1,6)
                    ready = True
                    break
                elif readyOrNot.casefold() == "n" or readyOrNot.casefold() == "no":
                    print("Bruh\nJUST SAY YOU ARE READY\nTAKING SO LONG FOR WHAT?!")
                else:
                    print("JUST ANSWER YES OR NO")
            if dice == 2 or 5:
                print("Player",vote_someone,"was snuck up by someone and got hung and died...")
                player2 = "Dead"
                print("Game Ended\nThe surviver wins!!!")
                voting = False
                game = 0
                break
            else:
                print("Player",vote_someone,"survived")
                turn = 2
                voting = False
                break
        else:
            print("There is no Player",vote_someone)
            
def killing():
    kill_someone = int(input("Who do want you to kill:\nPlayer: "))
    killing = True
    while killing == True:
        if kill_someone == 2:
            dice = random.randint(1,6)
            if dice == 3 or 4:
                print("Player",kill_someone,"got backstabbed")
                player2 = "Dead"
                print("Game Ended\nThe killer win!!!")
                killing = False
                break
            else:
                print("Player",kill_someone,"survived")
                turn = 2
                killing = False
                break
        else:
             print("There is no Player",kill_someone)

def fighting():
    fighting = True
    while fighting == True:
        dice = random.randint(1,6)
        if dice == 3 or 4:
            print("Player 1 lost a fight to the killer")
            player1 = "Dead"
            print("Game Ended\nThe killer win!!!")
            fighting = False
            break
        else:
            print("Player 1 won the fight against the killer!!!\nBut he was scared so he ran...")
            turn = 2
            fighting = False
            break

def kill_game():
    num_playing = int(input("How many people are playing (MAX:5): "))
    turn = 0
    dice = random.randint(1,6)
    kill = 1 or 2
    death = 4
    survive = 3 or 5 or 6
    
    if num_playing < 2:
        print("YOU NEED AT LEAST TWO PLAYERS TO PLAY THIS GAME!!!")
        game = 0
        
    elif num_playing == 2:
        player_num = random.randint(44,45)
        game = 1
        fullyknow = 0
        if player_num == 44:
            player1 = "Killer"
            player2 = "Surviver"
        else:
            player1 = "Surviver"
            player2 = "Killer"

        while fullyknow == 0:
            players_role = int(input("(Put 0 if no more players left to show the role)Player: "))
            if players_role == 1:
                print("Your role is",player1)
            elif players_role == 2:
                print("Your role is",player2)
            elif players_role == 0:
                fullyknow = 1
                break
            else:
                print("There is no player",players_role)
            
    elif num_playing == 3:
        player_num = random.randint(41,43)
        game = 2
        fullyknow = 0
        if player_num == 41:
            player1 = "Killer"
            player2 = "Surviver"
            player3 = "Surviver"
        elif player_num == 42:
            player1 = "Surviver"
            player2 = "Killer"
            player3 = "Surviver"
        else:
            player1 = "Surviver"
            player2 = "Surviver"
            player3 = "Killer"

        while fullyknow == 0:
            players_role = int(input("(Put 0 if no more players left to show the role)Player: "))
            if players_role == 1:
                print("Your role is",player1)
            elif players_role == 2:
                print("Your role is",player2)
            elif players_role == 3:
                print("Your role is",player3)
            elif players_role == 0:
                fullyknow = 1
            else:
                print("There is no player",players_role)
        
    elif num_playing == 4:
        player_num = random.randint(41,44)
        game = 3
        fullyknow = 0
        if player_num == 41:
            player1 = "Killer"
            player2 = "Surviver"
            player3 = "Surviver"
            player4 = "Surviver"
        elif player_num == 42:
            player1 = "Surviver"
            player2 = "Killer"
            player3 = "Surviver"
            player4 = "Surviver"
        elif player_num == 43:
            player1 = "Surviver"
            player2 = "Surviver"
            player3 = "Killer"
            player4 = "Surviver"
        else:
            player1 = "Surviver"
            player2 = "Surviver"
            player3 = "Surviver"
            player4 = "Killer"
            

        while fullyknow == 0:
            players_role = int(input("(Put 0 if no more players left to show the role)Player: "))
            if players_role == 1:
                print("Your role is",player1)
            elif players_role == 2:
                print("Your role is",player2)
            elif players_role == 3:
                print("Your role is",player3)
            elif players_role == 4:
                print("Your role is",player4)
            elif players_role == 0:
                fullyknow = 1
            else:
                print("There is no player",players_role)
        
    elif num_playing == 5:
        player_num = random.randint(41,45)
        game = 4
        fullyknow = 0
        if player_num == 41:
            player1 = "Killer"
            player2 = "Surviver"
            player3 = "Surviver"
            player4 = "Surviver"
            player5 = "Surviver"
        elif player_num == 42:
            player1 = "Surviver"
            player2 = "Killer"
            player3 = "Surviver"
            player4 = "Surviver"
            player5 = "Surviver"
        elif player_num == 43:
            player1 = "Surviver"
            player2 = "Surviver"
            player3 = "Killer"
            player4 = "Surviver"
            player5 = "Surviver"
        elif player_num == 44:
            player1 = "Surviver"
            player2 = "Surviver"
            player3 = "Surviver"
            player4 = "Killer"
            player5 = "Surviver"
        else:
            player1 = "Surviver"
            player2 = "Surviver"
            player3 = "Surviver"
            player4 = "Surviver"
            player5 = "Killer"

        while fullyknow == 0:
            players_role = int(input("(Put 0 if no more players left to show the role)Player: "))
            if players_role == 1:
                print("Your role is",player1)
            elif players_role == 2:
                print("Your role is",player2)
            elif players_role == 3:
                print("Your role is",player3)
            elif players_role == 4:
                print("Your role is",player4)
            elif players_role == 5:
                print("Your role is",player5)
            elif players_role == 0:
                fullyknow = 1
            else:
                print("There is no player",players_role)
        
    else:
        print("...")
        game = 0

    turn = random.randint(1,1)
    while game == 1:
        print(turn)
        while turn == 1:
            ready = False
            while ready == False:
                readyOrNot = input("Are you ready to roll the dice?[Y/N]")
                if readyOrNot.casefold() == "y" or readyOrNot.casefold() == "yes":
                    dice = random.randint(1,6)
                    ready = True
                    continue
                elif readyOrNot.casefold() == "n" or readyOrNot.casefold() == "no":
                    print("Bruh\nJUST SAY YOU ARE READY\nTAKING SO LONG FOR WHAT?!")
                else:
                    print("JUST ANSWER YES OR NO")
            print("Number Rolled:",dice)
            if player1 == "Killer" and dice == (1 or 2):
                killing()
                break
            elif player1 == "Killer" and dice == 4:
                player1 = "Dead"
                print("Player",turn,"Suicided")
                print("Game Ended\nThe surviver wins!!!")
                game = 0
                break
            elif player1 == "Killer" and dice == (3 or 5 or 6):
                print("You fail to find anyone to kill")
                turn = 2
                break
            elif player1 == "Surviver" and dice == 4 or 3:
                if dice == 3:
                    fighting()
                    break
                elif dice == 4:
                    print("Player",turn,"cannot take it anymore\nSo,He just ended his own life...")
                    player1 = "Dead"
                    print("Game Ended\nThe killer win!!!")
                    break
            elif player1 == "Surviver" and dice == (1 or 2):
                voting()
                break
            elif player1 == "Surviver" and dice == 5 or 6:
                print("You are lucky!\nYou survive...")
                turn = 2
                break
            
        while turn == 2:
            print("finally, it work ig")
