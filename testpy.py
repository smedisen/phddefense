import matplotlib.pyplot as plt

import pandas as pd

def test(a,b):
    print(a,b)

test(50,1)

df = pd.DataFrame()

df['x'] = [1,2,3]
df['y'] = [1,2,3]

plt.scatter([1,2,3], [1,2,3])

plt.show()

df.plot()

plt.show()
