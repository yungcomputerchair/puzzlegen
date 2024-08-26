import random
import sys

def get_suffixed(num):
    suffixed = str(num)
    num = num % 10
    if num == 1:
        return suffixed + "st"
    if num == 2:
        return suffixed + "nd"
    if num == 3:
        return suffixed + "rd"
    return suffixed + "th"

def get_random_cup(num_cups):
    return random.randint(1, num_cups)

def do_cups(num_cups, num_switches):
    cups = []
    for i in range(1, num_cups + 1):
        cups.append(f"Cup {i}")
    print(", ".join(cups))
    ball = get_random_cup(num_cups)
    print(f"The ball is under the {get_suffixed(ball)} Cup")
    for i in range(num_switches):
        cup1 = get_random_cup(num_cups)
        cup2 = get_random_cup(num_cups)
        while cup1 == cup2:
            cup2 = get_random_cup(num_cups)
        print(f"The {get_suffixed(cup1)} and {get_suffixed(cup2)} Cups are switched")
        if cup1 == ball:
            ball = cup2
        elif cup2 == ball:
            ball = cup1
    print("Which cup is the ball under?")
    guess = int(input())
    if guess == ball:
        print("Correct")
    else:
        print(f"Wrong, the ball was under the {get_suffixed(ball)} Cup")
    
    again = input("Play again? (y/n)")
    if again == "y":
        return True
    return False

if __name__ == "__main__":
    num_cups = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    num_switches = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    playing = True
    while playing:
        playing = do_cups(num_cups, num_switches)
        print()