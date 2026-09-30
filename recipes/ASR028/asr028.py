import pandas as pd
from asreml import asreml, define_categorical_variables

d014 = pd.read_csv("MAIZE_HYBRIDS.txt", sep=r"\s+", na_values=["NA"],
                   dtype={"indiv": str, "sire": str, "dam": str})

dcv = define_categorical_variables(d014, variables=["indiv", "sire", "dam"],
                                   equate_levels=["sire", "dam"])

asr028 = asreml(
    response="rdm",
    fixed="mu",
    random="sire + and(dam)",
    residual="units",
    vpredict={"h2": "V1/(V1*0.5+V2*0.25)"},
    data=dcv
)

asr028_b = asreml(
    response=["rdm", "srl"], 
    fixed="trait",
    random="corgh(trait):sire + and(corgh(trait):dam)",
    residual="id(units):corgh(trait)",
    options={"asuv": True, "varscale": 1.0},
    vpredict={"h2_rdm": "V5/(V5*0.5+V2*0.25)"},
    data=dcv
)

print(asr028.variance_components(display=False))

c = asr028.coefficients(display=False)
print(c[c.index.str.startswith("sire")].head(6))

print(asr028.vpredict(display=False))

print(asr028_b.variance_components(display=False))

cb = asr028_b.coefficients(display=False)
print(cb[cb.index.str.contains("sire")].head(6))

print(asr028_b.vpredict(display=False))
