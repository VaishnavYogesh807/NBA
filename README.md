# NBA

#Purpose
In order to assess player performance over the course of several seasons, this project analyzes NBA player data. To determine the best player-season arrangement, important performance metrics including shooting accuracy, scoring efficiency, and defense effect are computed using numerical techniques.

#Design and Implementation
The project is implemented entirely using NumPy, without external libraries.

#Data and Attributes
Each row in the dataset represents a player-season. The following metrics are computed:
  Field goal accuracy (FGM / FGA)
  Three-point accuracy (3PM / 3PA)
  Free throw accuracy (FTM / FTA)
  Average points per minute (PTS / MIN)
  Overall shooting accuracy ((FGM + 3PM + FTM) / (FGA + 3PA + FTA))
  Average blocks per game (BLK / GP)
  Average steals per game (STL / GP)

#Functions
Utilizes top100(metric, label="") to display top 100 players under each metric. Ultimately, this avoids repitition and improves efficiency

#Limitations
Rankings are based solely on box-score statistics
