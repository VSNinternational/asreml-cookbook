import pandas as pd
from asreml import asreml, define_categorical_variables

d004 = pd.read_csv("RAIL.txt", sep=r"\s+", na_values=["NA"])

d004 = define_categorical_variables(d004, variables=["rail"])

asr006 = asreml(
    response="travel", 
    fixed="mu", 
    random="rail", 
    residual="units",
    data=d004
)

print(asr006.variance_components(display=False))

BLUP = asr006.coefficients(display=False)
print(BLUP[BLUP.index.str.startswith("rail_")])
