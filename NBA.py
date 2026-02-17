# Import libraries
import numpy as np
import os
 
# Get the current script directory (not currently used)
os.path.join(os.path.dirname(__file__))
 
# Alternative: change working directory to Downloads folder (currently disabled)
#os.chdir('/Users/vaishnav/Library/Mobile Documents/com~apple~CloudDocs/Python/')
 
# Load NBA player statistics from a TSV (tab-separated values) file
# The file is expected to contain columns: Player, Season, FGA, FGM, 3PA, 3PM, FTA, FTM, 
# MIN, PTS, GP, BLK, STL, and others
data = np.genfromtxt(
     'NBA_Player_Stats.tsv', delimiter='\t', names=True, dtype=None,
 )
 
# Extract player names and seasons from the dataset
player_names = data['Player']
seasons = data['Season']
 
# Calculate shooting accuracy metrics (avoid division by zero with np.where)
# Field Goal Accuracy: made field goals / attempted field goals
fg_acc = np.where(data['FGA'] > 0, data['FGM'] / data['FGA'], 0)
# Three-Point Accuracy: made 3-pointers / attempted 3-pointers
tp_acc = np.where(data['3PA'] > 0, data['3PM'] / data['3PA'], 0)
# Free Throw Accuracy: made free throws / attempted free throws
ft_acc = np.where(data['FTA'] > 0, data['FTM'] / data['FTA'], 0)
# Stack results for field goal, 3-point, and free throw accuracy
results1 = np.column_stack((player_names, seasons, fg_acc, tp_acc, ft_acc))
 
# Calculate average points per minute played (avoid division by zero)
avg_pts_min = np.where(data['MIN'] > 0, data['PTS'] / data['MIN'], 0)
# Stack results for points per minute
results2 = np.column_stack((player_names, seasons, avg_pts_min))
 
# Calculate overall shooting accuracy across all shot types
overall_acc = np.where(data['FGA'] + data['3PA'] + data['FTA'] > 0,
                         (data['FGM'] + data['3PM'] + data['FTM']) /
                         (data['FGA'] + data['3PA'] + data['FTA']), 0)
# Stack results for overall accuracy
results3 = np.column_stack((player_names, seasons, overall_acc))
 
# Calculate defensive metrics: blocks and steals per game
blocks = np.where(data['GP'] > 0, data['BLK'] / data['GP'], 0)
steals = np.where(data['GP'] > 0, data['STL'] / data['GP'], 0)
# Stack results for blocks and steals per game
results4 = np.column_stack((player_names, seasons, blocks, steals))
 
# Function to print the top 100 players for a given metric
# Reduces code repetition by consolidating the printing logic
def top100(metric, label=""):
    # Sort indices in descending order and get the top 100
    # argsort returns indices; [-100:] gets last 100 (highest values); [::-1] reverses to descending order
    indices = np.argsort(metric)[-100:][::-1]
    pos = 1
 
    # Print each player with their rank, name, season, and metric value
    for i in indices:
        print(f"Player {pos}: {player_names[i]}, Season: {seasons[i]}, {label}: {metric[i]}")
        pos += 1
 
# Print top 100 players for each statistical metric
top100(fg_acc, "FG Accuracy")
top100(tp_acc, "3PT Accuracy")
top100(ft_acc, "FT Accuracy")
top100(avg_pts_min, "Average Points per Minute")
top100(overall_acc, "Overall Shooting Accuracy")
top100(blocks, "Blocks per Game")
top100(steals, "Steals per Game")
