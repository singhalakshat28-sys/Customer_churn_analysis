import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"./project_customer_churn.csv")
df.head(10)

import matplotlib.pyplot as plt

# Histogram of numerical columns
df.hist(figsize=(12, 8), bins=20, edgecolor='black')

plt.tight_layout()
plt.show()