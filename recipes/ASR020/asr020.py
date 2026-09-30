import pandas as pd
from asreml import asreml, define_categorical_variables

d016 = pd.read_csv("ALZHEIMER.txt", sep=r"\s+", na_values=["NA"])

dcv = define_categorical_variables(d016, variables=["id", "trt"])

asr020 = asreml(
    response="score",
    fixed="trt + visit",
    random="str(id + id:visit, corgh(2):id(id))",
    residual="units",
    options={"wald": {"den_df": "numeric"}},
    data=dcv
)

print(asr020.wald(display=False))

c = asr020.coefficients(display=False)
print(c[~c.index.str.startswith("id")])

print(asr020.variance_components(display=False))

b = c[c.index.str.startswith("id")]
print(b.head(6))

print(b.tail(6))
