import pandas as pd
import numpy as np

DATA = np.random.randint(1, 100, 100).reshape(10,10)

random_data = pd.DataFrame(data=DATA)
random_data.to_csv('data/random_data.csv', index=False)