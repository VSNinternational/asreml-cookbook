import pandas as pd
from asreml import asreml, define_categorical_variables

d005 = pd.read_csv("RATPUP.txt", sep=r"\s+", na_values=["NA"])

d005 = define_categorical_variables(d005, variables=["sex", "litter", "treatment"])

asr008 = asreml(
    response="weight",
    fixed="lsize + treatment + sex + treatment:sex",
    random="litter", 
    residual="dsum(units, treatment)",
    options={"wald": {"den_df": "numeric"}},
    data=d005
)

print(asr008.wald(display=False))

c = asr008.coefficients(display=False)
print(c[~c.index.str.startswith("litter_")])

print(asr008.variance_components(display=False))

print(c[c.index.str.startswith("litter_")])
