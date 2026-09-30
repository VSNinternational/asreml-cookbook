import pandas as pd
from asreml import asreml, define_categorical_variables

d001 = pd.read_csv("BESAG_ELBATAN.txt", sep=r"\s+", na_values=["NA"])

d001["row"] = d001["row"].astype(float)
d001["col"] = d001["col"].astype(float)
d001 = define_categorical_variables(d001, variables=["gen"])

asr002 = asreml(
    response="yield", 
    fixed="col + row", 
    random="gen",
    residual="units",
    vpredict={"h2": "V1/(V1+V2)"},
    options={"wald": {"den_df": "numeric"}},
    data=d001
)

print(asr002.wald(display=False))

c = asr002.coefficients(display=False)
print(c[~c.index.str.startswith("gen_")])

print(asr002.variance_components(display=False))

print(asr002.vpredict(display=False))
