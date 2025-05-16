# 9 positions
# 3 players
# Player can cut each other
# Store positions and winners
import random as r

players_postion = {
    "p1": 0,
    "p2": 0,
    "p3": 0
}

grid_size = 9 # 3x 3

current_player = "p1"
history = []

def move_player(player):
    dice_roll = r.randint(1, 6)
    final_pos = players_postion[player] + dice_roll
    if final_pos > grid_size:
        final_pos = final_pos - dice_roll
    
    elif final_pos == grid_size:
        final_pos = grid_size
    
    return final_pos, dice_roll


def check_cut(player):
    cut = []
    for p, coord in players_postion:
        if p != player:
            if coord == players_postion[player]:
                players_postion[p] = 0
                cut.append(p)
    return cut


def play():
    somebody_won = False
    winner = None
    while not somebody_won:
        for player in players_postion:
            is_winner = False
            prev_pos = players_postion[player]
            pos, roll = move_player(player)
            players_postion[player] = pos
            players_cut = []
            
            for p in players_postion:
                coord = players_postion[p]
                if p != player and coord == pos:
                    players_postion[p] = 0
                    players_cut.append(p)
            if pos == grid_size:
                winner = player
                somebody_won = True
                is_winner = True
            
            history.append(
                {
                    "Player": player,
                    "Previous position": prev_pos,
                    "New Position": pos,
                    "Dice roll": roll,
                    "is winner": is_winner
                }
            )
            print(f"""
"Player": {player},
"Previous position": {prev_pos},
"New Position": {pos},
"Dice roll": {roll},
"is winner": {is_winner},
"Players who were cut: {players_cut}

""")
            if somebody_won:
                break
    

play()
# print(history)
