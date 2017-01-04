import pandas as pd

df = pd.read_csv('match.csv')

seasons = set(df.Years)

for s in seasons:

        df[df.Years == s].to_csv(s+'.csv', index=False)

