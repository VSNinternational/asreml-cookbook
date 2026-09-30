import pandas as pd
from asreml import asreml, define_categorical_variables

d006 = pd.read_csv("PIXEL.txt", sep=r"\s+", na_values=["NA"])

d006["daysq"] = d006["day"] ** 2
d006 = define_categorical_variables(d006, variables=["dog", "side"])

asr010 = asreml(
    response="pixel", 
    fixed="side + day + daysq",
    random="str(dog + dog:day, corgh(2):id(dog))",
    options={"wald": {"den_df": "numeric"}},
    data=d006
)

print(asr010.wald(display=False))

c = asr010.coefficients(display=False)
print(c[~c.index.str.startswith("dog")])

print(asr010.variance_components(display=False))

blup = c[c.index.str.startswith("dog")]
print(blup.head(6))

print(blup.tail(6))
