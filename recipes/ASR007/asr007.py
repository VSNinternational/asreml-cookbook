import numpy as np, pandas as pd
from asreml import asreml, define_categorical_variables

d005 = pd.read_csv("RATPUP.txt", sep=r"\s+", na_values=["NA"])

d005 = define_categorical_variables(d005, variables=["sex", "litter", "treatment"])

MODEL = dict(
  response="weight", 
  fixed="lsize + treatment + sex + treatment:sex",
  random="litter", 
  residual="units"
)
  
asr007 = asreml(
  **MODEL,
  data=d005
)

from asreml.plotting import residual_plot
residual_plot(asr007)

res = np.asarray(asr007.residuals(display=False)).ravel()
d005["data"].loc[int(np.nanargmin(res)), "weight"] = np.nan

# refit the same model on the edited data.
asr007 = asreml(
  **MODEL, 
  options={"wald": {"den_df": "numeric"}},
  data=d005
)

print(asr007.wald(display=False))

c = asr007.coefficients(display=False)
print(c[~c.index.str.startswith("litter_")])

BLUP = c[c.index.str.startswith("litter_")]
print(BLUP.head(6))
