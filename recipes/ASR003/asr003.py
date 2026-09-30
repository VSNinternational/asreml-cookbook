import pandas as pd
from asreml import asreml, define_categorical_variables

d002 = pd.read_csv("TWINLONG.txt", sep=r"\s+", na_values=["NA"])

d002 = define_categorical_variables(d002, variables=["pair", "twin"])

asr003 = asreml(
    response="iq", 
    fixed="twin", 
    random="pair", 
    residual="units",
    predict={"classify": "twin"},
    vpredict={"r2": "V1/(V1+V2)"},
    options={"wald": {"den_df": "numeric"}},
    data=d002
)

print(asr003.wald(display=False))

print(asr003.predict(display=False))

print(asr003.variance_components(display=False))

print(asr003.vpredict(display=False))

BLUP = asr003.coefficients(display=False)
print(BLUP[BLUP.index.str.startswith("pair_")].head(6))
