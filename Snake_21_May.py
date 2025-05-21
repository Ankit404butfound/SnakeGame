# 9 positions
# 3 players
# Player can cut each other
# Store positions and winners
import random as r

players_postion = {
    "p1": -1,
    "p2": -1,
    "p3": -1
}

grid_size = 9 # 3x 3
grid_size_2d = (3, 3)

grid = []
multiplier = 1
counter = 0
for y in range(grid_size_2d[1]):
    if y %2 == 0:
        counter = 0
    else:
        counter = grid_size_2d[0]+1
    for x in range(grid_size_2d[0]):
        counter = counter + (1*multiplier)
        grid.append([counter-1, y])
    multiplier *= -1

# print(grid)
current_player = "p1"
history = []

def move_player(player):
    dice_roll = r.randint(1, 6)
    final_pos = players_postion[player] + dice_roll
    if final_pos > grid_size-1:
        final_pos = final_pos - dice_roll
    
    elif final_pos == grid_size-1:
        final_pos = grid_size-1
    
    return final_pos, dice_roll


def check_cut(player):
    cut = []
    for p, coord in players_postion.items():
        if p != player:
            if coord == players_postion[player]:
                players_postion[p] = -1
                cut.append(p)
    return cut


def play():
    somebody_won = False
    while not somebody_won:
        for player in players_postion:
            is_winner = False
            prev_pos = players_postion[player]
            pos, roll = move_player(player)
            players_postion[player] = pos
            cut = check_cut(player)
            if pos == grid_size-1:
                somebody_won = True
                is_winner = True
            
            history.append(
                {
                    "Player": player,
                    "Previous position": grid[prev_pos] if prev_pos >= 0 else "Outside",
                    "New position": grid[pos] if pos >= 0 else "Outside",
                    "Dice roll": roll,
                    "is winner": is_winner,
                    "pos": pos
                }
            )
#             print(f"""
# Player: {player},
# Dice roll: {roll},
# Previous position: {grid[prev_pos] if prev_pos >= 0 else "Outside"},
# New Position: {grid[pos]},
# Is winner: {is_winner},
# Players who were cut: {cut}

# """)
            if somebody_won:
                break
    

play()

for player in players_postion:
    dice_roll = []
    prev_position = []
    new_position = []
    coords = []
    pos_history = []
    for h in history:
        if h["Player"] == player:
            dice_roll.append(h["Dice roll"])
            prev_position.append(h["Previous position"])
            new_position.append(h["New position"])
            pos_history.append(h["pos"]+1)
    print("Player: ", player)
    print("Dice Roll history: ", dice_roll)
    print("Previous Position History", prev_position)
    print("New Position History", new_position)
    print("Position History", pos_history)
    print()

# print(history)
