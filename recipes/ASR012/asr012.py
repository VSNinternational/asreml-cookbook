import pandas as pd
from asreml import asreml, ainverse, define_categorical_variables

d008 = pd.read_csv("SALMON.txt", sep=r"\s+", na_values=["NA"], dtype={"indiv": str})
d008ped = pd.read_csv("SALMON_PED.txt", sep=r"\s+", na_values=["NA"],
                      dtype={"indiv": str, "sire": str, "dam": str})

ainv = ainverse(d008ped)

dcv = define_categorical_variables(d008, variables=["indiv"])

asr012 = asreml(
    response="amoebic_load",
    fixed="mu",
    random="vm(indiv, ainv)",
    residual="units",
    vpredict={"h2": "V1/(V1+V2)"},
    predict={"classify": "indiv"},
    data={"data": dcv, "ainv": ainv}
)

from asreml.plotting import residual_plot
residual_plot(asr012)

print(asr012.variance_components(display=False))

print(asr012.vpredict(display=False))

c = asr012.coefficients(display=False)
print(c[~c.index.str.contains("indiv")])

print(c[c.index.str.contains("indiv")].head(6))

p = asr012.predict(display=False)
print(p.head(6) if hasattr(p, "head") else p)
