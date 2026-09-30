import pandas as pd
from asreml import asreml, define_categorical_variables

d003 = pd.read_csv("SEMICOND.txt", sep=r"\s+", na_values=["NA"])

d003 = define_categorical_variables(d003, variables=["source", "lot", "wafer"])

asr005 = asreml(
    response="thick", 
    fixed="source",
    random="at(source):lot + lot:wafer", 
    residual="units",
    predict={"classify": "source"},
    options={"wald": {"den_df": "numeric"}},
    data=d003
)

print(asr005.wald(display=False))

print(asr005.predict(display=False))

print(asr005.variance_components(display=False))
