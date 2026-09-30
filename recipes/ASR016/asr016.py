import pandas as pd
from asreml import asreml, define_categorical_variables

d013 = pd.read_csv("ARCHBOLD_APPLE.txt", sep=r"\s+", na_values=["NA"])

d013["wplot"]   = d013["row"].astype(str) + "_" + d013["spacing"].astype(str)
d013["subplot"] = (d013["row"].astype(str) + "_" + d013["spacing"].astype(str)
                   + "_" + d013["stock"].astype(str))
                   
dcv = define_categorical_variables(
    d013, variables=["rep","spacing","stock","gen","wplot","subplot"])

asr016 = asreml(
    response="yield", 
    fixed="spacing*stock*gen",
    random="rep + rep:wplot + rep:wplot:subplot", 
    residual="units",
    predict=[{"classify": "spacing"}, {"classify": "stock:gen"}],
    options={"wald": {"den_df": "numeric", "ss_type": "incremental"}},
    data=dcv
)

print(asr016.wald(display=False))

print(asr016.predict(display=False)[0])

print(asr016.predict(display=False)[1])

print(asr016.variance_components(display=False))
