import pandas as pd
from asreml import asreml, define_categorical_variables

d019 = pd.read_csv("LUNG.txt", sep=r"\s+", na_values=["NA"])

# R's `subset=` argument has no Py equivalent -- filter the frame.
before = d019[d019["time"] == "Before"].copy()

asr023_before = asreml(
  response="resp",
  fixed="mu",
  data=define_categorical_variables(before, variables=["rat","time"])
)

print(asr023_before.variance_components(display=False))

after = d019[d019["time"] == "After"].copy()

asr023_after = asreml(
  response="resp",
  fixed="mu",
  data=define_categorical_variables(after, variables=["rat","time"])
)

print(asr023_after.variance_components(display=False))

initR = [0.5, 0.266, 0.975]

d019 = d019.sort_values("time", kind="stable").reset_index(drop=True)
dcv = define_categorical_variables(d019, variables=["rat","time"])

# corgh already supplies its own variances; without varscale=1.0 Py adds a
# redundant Residual!SCA_V and the fit goes singular. R uses the sigma
# parameterization here ("Model fitted using the sigma parameterization").
asr023 = asreml(
  response="resp",
  fixed="time",
  residual="corgh(time, init=initR):id(rat)",
  predict={"classify": "time"},
  options={"varscale": 1.0, "wald": {"den_df": "numeric"}},
  data={"data": dcv, "initR": initR}
)

print(asr023.variance_components(display=False))

print(asr023.wald(display=False))

print(asr023.predict(display=False))
