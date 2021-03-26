#Checking out meat and birth data
from pandasql import sqldf
from pandasql import load_meat, load_births

def test_basic_import():
    meat = load_meat()
    births = load_births()
    print (meat.head())
    print (births.head())

# Let's make a graph to visualize the data
# Bet you haven't had a title quite like this before
import matplotlib.pyplot as plt
from pandasql import *
import pandas as pd
from libdefinitions import *

pysqldf = lambda q: sqldf(q, globals())

q = """
SELECT m.date,
       m.beef,
       b.births
FROM   meat m
LEFT JOIN births b ON m.date = b.date
WHERE  m.date > '1974-12-31';
"""

meat = load_meat()
births = load_births()

df = pysqldf(q)

printSectionHead("meat/beef join")
print(df.head())
df.births = df.births.fillna(method='backfill')

fig = plt.figure()
ax1 = fig.add_subplot(111)
# ax1.plot(pd.rolling(12).mean(df['beef']), color='b')
ax1.plot(df['beef'].rolling(12).mean(), color='b')
ax1.set_xlabel('months since 1975')
ax1.set_ylabel('cattle slaughtered', color='b')

ax2 = ax1.twinx()
# ax2.plot(pd.rolling(12).mean(df['births']), color='r')
ax2.plot(df['births'].rolling(12).max(), color='r')
ax2.set_ylabel('babies born max', color='r')
plt.title("Beef Consumption and the Birth Rate")
plt.show()