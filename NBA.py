import numpy as np

data = np.genfromtxt(
    '/Users/vaishnav/Downloads/NBA_Player_Stats.tsv', delimiter='\t', names=True, dtype=None,
)

player_names = data['Player']
seasons = data['Season']

FG_acc = np.where(data['FGA'] > 0, data['FGM'] / data['FGA'], 0)
TP_acc = np.where(data['3PA'] > 0, data['3PM'] / data['3PA'], 0)
FT_acc = np.where(data['FTA'] > 0, data['FTM'] / data['FTA'], 0)
results1 = np.column_stack((player_names, seasons, FG_acc, TP_acc, FT_acc))

avg_pts_mid = np.where(data['MIN'] > 0, data['PTS'] / data['MIN'], 0)
results2 = np.column_stack((player_names, seasons, avg_pts_mid))

overall_acc = np.where(data['FGA'] + data['3PA'] + data['FTA'] > 0,
                        (data['FGM'] + data['3PM'] + data['FTM']) /
                        (data['FGA'] + data['3PA'] + data['FTA']), 0)
results3 = np.column_stack((player_names, seasons, overall_acc))

blocks = np.where(data['GP'] > 0, data['BLK'] / data['GP'], 0)
steals = np.where(data['GP'] > 0, data['STL'] / data['GP'], 0)
results4 = np.column_stack((player_names, seasons, blocks, steals))

# Function to avoid repition to print top 100 players for each given metric
def top100(metric, label=""):
    indices = np.argsort(metric)[-100:][::-1] # CHATgpt suggested [::-1] to reverse the order
    pos = 1

    for i in indices:
        print(f"Player {pos}: {player_names[i]}, Season: {seasons[i]}, {label}: {metric[i]}")
        pos += 1

top100(FG_acc, "FG Accuracy")
top100(TP_acc, "3PT Accuracy")
top100(FT_acc, "FT Accuracy")
top100(avg_pts_mid, "Average Points per Minute")
top100(overall_acc, "Overall Shooting Accuracy")
top100(blocks, "Blocks per Game")
top100(steals, "Steals per Game")