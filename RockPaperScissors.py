
import random
moves = ['r','p','s']


def winner(um,cm):
    if um==cm:
        print("The moves were the same")
    else:
        if um=="r":
            if cm=="p":
                print(":::::You lose:::::")
            else:
                print(":::::You Win!!!!:::::")
        elif um=="p":
            if cm=="s":
                print(":::::You lose:::::")
            else:
                print(":::::You Win!!!!:::::")
        elif um=="s":
            if cm=="r":
                print(":::::You lose:::::")
            else:
                print(":::::You Win!!!!:::::")        
        


for i in range(0,5):
    cm=random.choice(moves)
    um=input("\nChoose a move out of 'r,p,s': ")
    if um not in moves:
        print("INVALID MOVE")
    else:    
        print("Computer move:",cm)
        winner(um,cm)

