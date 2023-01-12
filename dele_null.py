import pandas as pd
data = pd.read_csv("./comments/北京.csv")
res = data.dropna(how="all")
res.to_csv("clean.csv", index=False)
