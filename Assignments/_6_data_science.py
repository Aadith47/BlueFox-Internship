import pandas as pd

import numpy as np

df = pd.read_csv("student-data.csv")

#student is study is effective or not

df["Study"] = np.where((df["studytime"] >= 2) & (df["traveltime"] < 2), "Effective" , "Not Effective")

#Students who need to be physically more active

df["Physially Active"] = np.where(df["freetime"] > 2 & (df["internet"] == "yes") & (df["activities"] == "no"), "Need to be active", "Active Enough" )

#Need guidance

df["Guidance"] = np.where((df["studytime"] >= 2) & (df["passed"] == "no"), "Need Guidance", "On Track")

print(df.shape)

print(df)

