import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(25, size=(4, 4)), index=["1", "2", "3", "4"], columns=["A", "B", "C", "D"])
df2 = pd.DataFrame(np.random.randint(25, size=(6, 4)), index=["5", "6", "7", "8", "9", "10"],
                   columns=["A", "B", "C", "D"])
df3 = pd.DataFrame(np.random.randint(25, size=(4, 4)), columns=["A", "B", "C", "D"])
df4 = pd.DataFrame(np.random.randint(25, size=(4, 4)), columns=["E", "F", "G", "H"])


def display(df1, df2, df3, df4):
    # Perform some actions or return the DataFrames
    # For example, you can print them:
    print("DataFrame 1:")
    print(df1)

    print("\nDataFrame 2:")
    print(df2)

    print("\nDataFrame 3:")
    print(df3)

    print("\nDataFrame 4:")
    print(df4)


display(df1, df2, df3, df4)