import pandas as pd
from scipy.stats import chi2
from asreml import asreml, define_categorical_variables

d002 = pd.read_csv("TWINLONG.txt", sep=r"\s+", na_values=["NA"])

dcv = define_categorical_variables(d002, variables=["pair","twin"])

full = asreml(
    response="iq",
    fixed="twin",
    residual="id(pair):corv(twin)",
    data=dcv
)

nested = asreml(
    response="iq",
    fixed="twin",
    residual="id(pair):idv(twin)",
    data=dcv
)

# ASReml-Python has no lrt(): compute d = 2*(logL_MC - logL_MI) and the chi2 tail
llf = full.summary(display=False)["loglik"]; lln = nested.summary(display=False)["loglik"]
stat = 2 * (llf - lln); df = 1
p = chi2.sf(stat, df)
print(f"LR statistic = {stat:.6f}  df = {df}  p = {p:.6g}")

print(f"loglik full={llf:.6f} nested={lln:.6f}")
print(full.variance_components(display=False))
