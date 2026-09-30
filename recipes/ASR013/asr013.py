import numpy as np, pandas as pd
from asreml import ainverse, sparse_to_full

ped = pd.read_csv("AINVERSE_PED.txt", sep=r"\s+", na_values=["NA"],
                  dtype={"indiv": str, "sire": str, "dam": str, "grand_sire": str})

ainv = ainverse(ped)

# ainverse() returns a dict {"inverse", "ids"}, not a data frame: "inverse" is
# the sparse triplet form (rowid, colid, vals) and "ids" the individual labels.
print(ainv["inverse"].head())

print(ainv["ids"])

def nrm(ainv):
    full = sparse_to_full(ainv["inverse"])
    A = np.linalg.inv(np.asarray(full, dtype=float))
    # + 0.0 turns IEEE negative zeros into plain zeros, as R's print() shows them
    return pd.DataFrame(np.round(A, 2) + 0.0, index=ainv["ids"], columns=ainv["ids"])

print(nrm(ainv).to_string())

ainv = ainverse(ped, missing_values=["ID15", "*"])

print(ainv["ids"])

ainv = ainverse(ped, missing_values=["*"], selfing_levels=["f_gen", 0.5])

print(nrm(ainv).to_string())

ped_selfing = ped.iloc[:, [0, 2, 1, 3, 4, 5]]

ainv = ainverse(ped_selfing, missing_values=["*"], selfing=0.3)

print(nrm(ainv).to_string())

ped_mgs = ped.iloc[:, [0, 1, 4, 2, 3, 5]]

ainv = ainverse(ped_mgs, missing_values="*", maternal_grand_sire=True)

print(nrm(ainv).to_string())

ped_sorted = ped.iloc[[0, 7, 1, 2, 11, 4, 5, 13, 6, 8, 9, 10, 12]]

print(ainverse(ped_sorted, missing_values="*", return_pedigree=True))
