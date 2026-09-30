import pandas as pd
from asreml import asreml, define_categorical_variables

d010 = pd.read_csv("DURBAN_ROWCOL.txt", sep=r"\s+", na_values=["NA"])

dcv = define_categorical_variables(d010, variables=["rep","row","gen","bed"])

asr015 = asreml(
    response="yield",
    fixed="rep",
    random="gen + rep:row + rep:bed",
    residual="units",
    vpredict={"h2": "V3/(V1+V2+V3+V4)"},
    data=dcv
)

print(asr015.wald(display=False))

print(asr015.variance_components(display=False))

print(asr015.vpredict(display=False))

c = asr015.coefficients(display=False)
print(c[c.index.str.startswith(("rep_","mu"))])

print(c[c.index.str.startswith("gen_")].head(6))
