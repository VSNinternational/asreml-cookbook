import pandas as pd
from asreml import asreml, define_categorical_variables

d018 = pd.read_csv("ATP.txt", sep=r"\s+", na_values=["NA"])

dcv = define_categorical_variables(d018, variables=["heart","A","B","time"])

asr022 = asreml(
    response="ATP",
    fixed="A + B + A:B + A:time + B:time",
    random="heart",
    residual="heart:ante(time,1)",
    predict={"classify": "A:B:time"},
    options={
        "varscale": 1.0,
        "wald": {"den_df": "numeric", "ss_type": "incremental"}
        },
    data=dcv
)

print(asr022.variance_components(display=False).head(6))

print(asr022.wald(display=False))

print(asr022.predict(display=False).head(6))

print(asr022.predict(display=False).tail(6))
