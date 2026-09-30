import pandas as pd
from asreml import asreml, define_categorical_variables

d001 = pd.read_csv("BESAG_ELBATAN.txt", sep=r"\s+", na_values=["NA"])

d001 = define_categorical_variables(d001, variables=["gen", "row", "col"])

asr009 = asreml(
    response="yield", 
    fixed="mu + col", 
    random="gen",
    residual="ar1v(col):ar1(row)",
    vpredict={"h2": "V1/(V1+V2)"},
    data=d001
)

c = asr009.coefficients(display=False)
print(c[~c.index.str.startswith("gen_")])

print(asr009.variance_components(display=False))

print(asr009.vpredict(display=False))

print(c[c.index.str.startswith("gen_")].head(6))
