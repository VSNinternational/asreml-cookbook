import pandas as pd
from asreml import asreml, define_categorical_variables

d003 = pd.read_csv("SEMICOND.txt", sep=r"\s+", na_values=["NA"])

d003 = define_categorical_variables(d003, variables=["source", "lot", "wafer"])

asr004 = asreml(
    response="thick", 
    fixed="source", 
    random="lot + lot:wafer",
    residual="units",
    predict={"classify": "source"},
    options={"wald": {"den_df": "numeric"}},
    data=d003
)

print(asr004.wald(display=False))

print(asr004.predict(display=False))

print(asr004.variance_components(display=False))

BLUP = asr004.coefficients(display=False)
print(BLUP[BLUP.index.str.startswith("lot")].head(12))
