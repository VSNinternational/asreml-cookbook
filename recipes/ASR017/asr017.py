import matplotlib.pyplot as plt
import numpy as np, pandas as pd
from asreml import asreml, ainverse, define_categorical_variables

d021 = pd.read_csv("PINE_CLONES.txt", sep=r"\s+", na_values=["NA"],
                   dtype={"clone": str})
d021ped = pd.read_csv("PINE_CLONES_PED.txt", sep=r"\s+", na_values=["NA"], dtype=str)

print(sorted(d021["location"].unique()))
d021_r = d021[d021["location"] == "Rail"].copy()

print(d021_r.describe(include="all").T)

with pd.option_context("display.max_columns", None, "display.width", 88):
    print(pd.crosstab(d021_r["block"], d021_r["clone"]).head())

plt.figure(figsize=(5, 3.5))
plt.hist(d021_r["height_8"].dropna())
plt.xlabel("height_8")
plt.show()

ainv = ainverse(d021ped)
dcv = define_categorical_variables(d021_r, variables=["clone", "block", "location"])

asr017 = asreml(
    response="height_8",
    fixed="mu",
    random="block + vm(clone, ainv)",
    data={"data": dcv, "ainv": ainv}
)

from asreml.plotting import residual_plot
residual_plot(asr017)

res = np.asarray(asr017.residuals(display=False)).ravel()
# +1 because pandas positions start at 0, whereas R's which.max() starts at 1
print("which.max:", int(np.nanargmax(res)) + 1)
print("which.min:", int(np.nanargmin(res)) + 1)

outliers = [int(np.nanargmax(res)), int(np.nanargmin(res))]
d021_r.iloc[outliers, d021_r.columns.get_loc("height_8")] = np.nan
