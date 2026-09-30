import pandas as pd
from asreml import asreml, define_categorical_variables

d001 = pd.read_csv("BESAG_ELBATAN.txt", sep=r"\s+", na_values=["NA"])

d001 = define_categorical_variables(d001, variables=["gen", "col"])

asr001 = asreml(
    response="yield",
    fixed="col",
    random="gen",
    residual="units",
    vpredict={"H2": "V1/(V1+V2)"},
    options={"wald": {"den_df": "numeric"}},
    data=d001
)

print(asr001.wald(display=False))

print(asr001.variance_components(display=False))

print(asr001.vpredict(display=False))

BLUP = asr001.coefficients(display=False)
BLUP = BLUP[BLUP.index.str.startswith("gen_")]
print(BLUP.head(6))
