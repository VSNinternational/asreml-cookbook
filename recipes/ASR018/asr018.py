import pandas as pd
from asreml import asreml, ainverse, define_categorical_variables

d021 = pd.read_csv("PINE_CLONES.txt", sep=r"\s+", na_values=["NA"], dtype={"clone": str})
d021ped = pd.read_csv("PINE_CLONES_PED.txt", sep=r"\s+", na_values=["NA"], dtype=str)

ainv = ainverse(d021ped)

# dsum needs the data in section order
d021 = d021.sort_values("location", kind="stable").reset_index(drop=True)
dcv = define_categorical_variables(d021, variables=["clone", "block", "location"])

asr018 = asreml(
    response="height_8",
    fixed="location",
    random="at(location):block + vm(clone, ainv) + idv(location):vm(clone, ainv)",
    residual="dsum(units, location)",
    vpredict={"h2": "V4/((V1+V2+V3)/3+V4+V8+(V5+V6+V7)/3)"},
    options={"wald": {"den_df": "numeric"}},
    data={"data": dcv, "ainv": ainv}
)

print(asr018.variance_components(display=False))

print(asr018.vpredict(display=False))

print(asr018.wald(display=False))

c = asr018.coefficients(display=False)
blup = c[c.index.str.contains("clone|block")]
print(blup.head(6))

print(blup.tail(6))
