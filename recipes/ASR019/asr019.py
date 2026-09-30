import pandas as pd
from asreml import asreml, define_categorical_variables

d015 = pd.read_csv("WEIGHT_LOSS.txt", sep=r"\s+", na_values=["NA"])

dcv = define_categorical_variables(d015, variables=["trt"])

asr019 = asreml(
    response="loss", 
    fixed="trt + weight + trt:weight", 
    residual="units",
    predict=[{"classify": "trt:weight"},
             {"classify": "trt:weight", "levels": {"weight": [190, 230, 270]}}],
    options={"wald": {"den_df": "numeric", "ss_type": "conditional"}},
    data=dcv
)

print(asr019.wald(display=False))

print(asr019.predict(display=False)[0])

print(asr019.predict(display=False)[1])
