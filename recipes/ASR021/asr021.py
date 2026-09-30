import pandas as pd
from asreml import asreml, define_categorical_variables

d017 = pd.read_csv("PRESSURE.txt", sep=r"\s+", na_values=["NA"])

dcv = define_categorical_variables(d017, variables=["drug","biofeed","diet"])

full = asreml(
    response="pressure",
    fixed="drug*biofeed*diet",
    residual="units",
    predict={"classify": "drug:biofeed:diet"},
    options={"wald": {"den_df": "numeric"}},
    data=dcv
)

partial = asreml(
    response="pressure",
    fixed="drug:biofeed:diet",
    residual="units",
    predict={"classify": "drug:biofeed:diet"},
    options={"wald": {"den_df": "numeric"}},
    data=dcv
)

print(full.predict(display=False))

print(partial.predict(display=False))

print(full.wald(display=False))

print(partial.wald(display=False))
