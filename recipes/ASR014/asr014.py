import pandas as pd
from asreml import asreml, define_categorical_variables

d011 = pd.read_csv("OATS.txt", sep=r"\s+", na_values=["NA"])

dcv = define_categorical_variables(d011, variables=["variety","nitrogen","block","wplot"])

asr014 = asreml(
    response="yield",
    fixed="variety + nitrogen + variety:nitrogen",
    random="block + block:wplot",
    residual="units",
    predict=[{"classify": "variety:nitrogen"}, {"classify": "nitrogen"}],
    options={"wald": {"den_df": "numeric"}},
    data=dcv
)

asr014 = asreml(
    response="yield",
    fixed="variety*nitrogen",
    random="block/wplot",
    residual="units",
    predict=[{"classify": "variety:nitrogen"}, {"classify": "nitrogen"}],
    options={"wald": {"den_df": "numeric"}},
    data=dcv
)

print(asr014.wald(display=False))

print(asr014.variance_components(display=False))

print(asr014.predict(display=False)[0])

print(asr014.predict(display=False)[1])
