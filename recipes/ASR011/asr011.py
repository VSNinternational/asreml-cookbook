import numpy as np, pandas as pd
from asreml import asreml, ainverse, define_categorical_variables

# pedigree ids look numeric but are labels: read them as str, or 203 becomes 203.0
d007 = pd.read_csv("LIZARD.txt", sep=r"\s+", na_values=["NA"],
                   dtype={"indiv": str, "dam": str, "sire": str})

ainv = ainverse(d007[["indiv", "dam", "sire"]])

dcv = define_categorical_variables(d007, variables=["indiv", "cohort", "sex"])
DATA = {"data": dcv, "ainv": ainv}

asr011 = asreml(
  response="p_yellow",
  fixed="cohort + sex",
  random="vm(indiv, ainv)",
  residual="units",
  data=DATA
)

from asreml.plotting import residual_plot
residual_plot(asr011)

d007["p_yellow_log"] = np.log((d007["p_yellow"] + 1) / (100 - d007["p_yellow"] + 1))
print(d007["p_yellow_log"])

# the transformed column was added after define_categorical_variables(), so the
# categorised frame has to be rebuilt before the second fit
dcv = define_categorical_variables(d007, variables=["indiv", "cohort", "sex"])
DATA = {"data": dcv, "ainv": ainv}

asr011_transfo = asreml(
  response="p_yellow_log",
  fixed="cohort + sex",
  random="vm(indiv, ainv)",
  residual="idv(units)",
  vpredict={"h2": "V1/(V1+V2)"},
  options={"wald": {"den_df": "numeric"}},
  data=DATA
)

print(asr011_transfo.wald(display=False))

print(asr011_transfo.variance_components(display=False))

print(asr011_transfo.vpredict(display=False))

c = asr011_transfo.coefficients(display=False)
BLUP = c[c.index.str.contains("indiv")].copy()
print(BLUP.head(6))

BLUP["Mean"] = d007["p_yellow_log"].mean()
BLUP["Preds"] = BLUP["Mean"] + BLUP["estimate"]
print(BLUP.head(6))

BLUP["BT_Preds"] = ((100 + 1) * np.exp(BLUP["Preds"]) - 1) / (1 + np.exp(BLUP["Preds"]))
print(BLUP.head(6))

print(BLUP.tail(6))
