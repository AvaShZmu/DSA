import time


def show_stack(s1, s2, s3, numdisks):
    max_height = numdisks

    stack1 = [""] * (max_height - len(s1)) + s1
    stack2 = [""] * (max_height - len(s2)) + s2
    stack3 = [""] * (max_height - len(s3)) + s3
    print("Tower 1    Tower 2    Tower 3")
    for i in range(max_height):
        print(f" {stack1[i]:^5}      {stack2[i]:^5}      {stack3[i]:^5}")


def valid_move(move_dict, start, end):
    if len(move_dict[end]) == 0:
        return True
    disc = move_dict[start][0]
    if len(disc) > len(move_dict[end][0]):
        return False
    return True


def win_check(s3, numdisks):
    if len(s3) != numdisks:
        return False
    for i in range(1, len(s3)):
        if s3[i - 1] > s3[i]:
            return False
    return True


def TowerOfHanoi(n):
    ans = []
    temp_dict = {'s1': 1, 's2': 2, 's3': 3}

    def subfunc(n, from_tower, to_tower, aux_tower):
        if n == 0:
            return
        subfunc(n - 1, from_tower, aux_tower, to_tower)
        ans.append((temp_dict[from_tower], temp_dict[to_tower]))
        subfunc(n - 1, aux_tower, to_tower, from_tower)

    subfunc(n, 's1', 's2', 's3')
    return ans


print("\nLet's play tower of Hanoi")

# Create the stacks
stack1 = []
stack2 = []
stack3 = []
move_dict = {1: stack1, 2: stack2, 3: stack3}

total_moves = 0
numdisks = 0
while numdisks <= 1 or numdisks >= 12:
    try:
        numdisks = int(input("How many disks?\n"))
        if numdisks <= 1 or numdisks >= 12:
            print("Please enter an integer greater than 1 and smaller than 12 (anything after that sucks)")
    except ValueError:
        print("Please enter a valid number")

# Set up:
for i in range(1, numdisks + 1):
    stack1.append('=' * i)

show_stack(stack1, stack2, stack3, numdisks)

selection = input("Do you want to play? Or do you want me to solve?\n1 = play\n2 = solve\n")

if selection == "1":
    # Play the game:
    print(r"////////// BEGIN \\\\\\\\\\")
    show_stack(stack1, stack2, stack3, numdisks)
    print("Type x y to indicate that you want to move the disk from tower x to tower y.")
    while not win_check(stack3, numdisks):
        print("-" * 25)
        try:
            move = list(map(int, input("Move:\n").split(' ')))
            start, end = move[0], move[1]
            if valid_move(move_dict, start, end):
                disc = move_dict[start].pop(0)
                move_dict[end].insert(0, disc)
                total_moves += 1
            else:
                print("Invalid move.")
            show_stack(stack1, stack2, stack3, numdisks)
        except ValueError:
            print("Please enter the correct format")
        except IndexError:
            print("Invalid move")
        except KeyError:
            print("Invalid move")
    print(f'Congrats! Total moves: {total_moves}')

elif selection == "2":
    ans = TowerOfHanoi(numdisks)
    show_stack(stack1, stack2, stack3, numdisks)
    for start, end in ans:
        disc = move_dict[start].pop(0)
        move_dict[end].insert(0, disc)
        show_stack(stack1, stack3, stack2, numdisks)
        time.sleep(1.4)
    print(f"Total moves: {len(ans)}")
