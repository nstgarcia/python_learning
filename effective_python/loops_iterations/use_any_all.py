import random

def flip_coin():
    if random.randint(0,1)==0:
        return "heads"
    else:
        return "tails"

def flip_is_heads():
    return flip_coin() == "heads"

flips = [flip_is_heads() for _ in range(20)]
all_heads = False not in flips
print(all_heads)

all_heads = all(flip_is_heads() for _ in range(20))
print(all_heads)

print("************ Using any *******")

def flip_is_tails():
    return flip_coin()=="tails"


all_heads = not any(flip_is_tails() for _ in range(20) )
print(all_heads)