import pandas as pd
import plotly.express as go
import numpy

# My new method
df = pd.read_csv("./data.csv")

mean = df.groupby("level")["attempt"].mean()

fig  = go.scatter(x=mean, y=['Level 1', "Level 2", "Level 3", "Level 4"], orientation="h")

fig.show()