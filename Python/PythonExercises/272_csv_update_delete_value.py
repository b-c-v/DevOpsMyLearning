import pandas as pd

row_to_update = 1
col_to_update = "Name"  # Always use column labels when updating values with df.at
new_value = "Test"

# Load the CSV
df = pd.read_csv("tmp.csv")
print(f"Before update\n{df}")

# Update value
df.at[row_to_update, col_to_update] = new_value

print(f"After update\n{df}")

# Save changes back to the CSV
df.to_csv("tmp.csv", index=False)

# delete cell value
import numpy as np

row_to_clear = 1
col_to_clear = "Age"

df = pd.read_csv("tmp.csv")
print(f"Before update\n{df}")


df.at[row_to_clear, col_to_clear] = np.nan
print(f"After update\n{df}")

df.to_csv("tmp.csv", index=False)
