import pandas as pd
import numpy as np

DATA = np.random.randint(1, 100, 100).reshape(10,10)

df = pd.DataFrame(data=DATA)
df.to_csv('data/df.csv', index=False)