# downloading the subreddit CSV here
!wget -q https://raw.githubusercontent.com/almayor/reddit-mods-dataset/master/subreddits.csv -O subreddits_redditmods.csv

import pandas as pd
df = pd.read_csv('subreddits_redditmods.csv', dtype=str, low_memory=False)
print("Rows:", len(df))
df.head()
