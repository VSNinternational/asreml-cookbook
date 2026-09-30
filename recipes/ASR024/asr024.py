import matplotlib.pyplot as plt
import numpy as np, pandas as pd
from asreml import asreml, define_categorical_variables

d020 = pd.read_csv("EPILEPSY.txt", sep=r"\s+", na_values=["NA"])

dcv = define_categorical_variables(d020, variables=["trt","time","patient"])

# alternative to dsum(...corv...)
RES = ("at(trt,1):id(patient):corv(time) + at(trt,2):id(patient):corv(time)")

asr024 = asreml(
  response="seizure",
  fixed="base + trt + time + trt:time",
  residual=RES,
  options={"wald": {"den_df": "numeric"}},
  data=dcv
)

# use NumPy for the log transformation
d020["trans"] = np.log(d020["seizure"] + 1)

# the transformed column is added after define_categorical_variables(), so the
# categorised frame has to be rebuilt before this second fit
dcv = define_categorical_variables(d020, variables=["trt","time","patient"])

asr024t = asreml(
  response="trans",
  fixed="base + trt + time + trt:time",
  residual=RES,
  predict={"classify": "trt"},
  options={"wald": {"den_df": "numeric"}},
  data=dcv
)

res = np.asarray(asr024.residuals(display=False)).ravel()
rest = np.asarray(asr024t.residuals(display=False)).ravel()

fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
axes[0].hist(res, bins=15)
axes[0].set_xlabel("residuals")
axes[0].set_title("asr024")
axes[1].hist(rest, bins=20)
axes[1].set_xlabel("residuals")
axes[1].set_title("asr024t")
fig.tight_layout()
plt.show()

print(asr024t.wald(display=False))

print(asr024t.variance_components(display=False))

preds = asr024t.predict(display=False).copy()
preds["back_trans"] = np.exp(preds.iloc[:, 1]) - 1
print(preds)
