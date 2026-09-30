# ASReml Cookbook — scripts and datasets

Code and data for the recipes in the [ASReml Cookbook for R and Python](https://cookbook.asreml.vsni.co.uk/).

One folder per recipe. Each folder is self-contained: the scripts and the
datasets they read sit side by side, so a recipe runs from its own folder with
no path changes. `ASRNNN.zip` holds the same files, for a single-click download.

Running the recipes needs a licensed ASReml-R or ASReml-Python; see the
[installation instructions](https://cookbook.asreml.vsni.co.uk/instructions.html).

| Recipe | Title | Scripts | Datasets |
|---|---|---|---|
| [ASR001](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR001) | LMM for a randomized complete block design - Wheat varieties | R, py | BESAG_ELBATAN.txt |
| [ASR002](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR002) | LMM for a randomized complete block design with covariates - Wheat varieties | R, py | BESAG_ELBATAN.txt |
| [ASR003](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR003) | Simple LMM - Twins' IQ | R, py | TWINLONG.txt |
| [ASR004](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR004) | Hierarchical LMM with nested factors - Silicon wafers | R, py | SEMICOND.txt |
| [ASR005](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR005) | Hierarchical LMM with nested factors and heterogeneous variances - Silicon wafers | R, py | SEMICOND.txt |
| [ASR006](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR006) | One-way classification LMM - Railways rails | R, py | RAIL.txt |
| [ASR007](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR007) | LMM with fixed effect interaction - Rat pups | R, py | RATPUP.txt |
| [ASR008](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR008) | LMM with fixed effect interaction and heterogeneous residual variances - Rat pups | R, py | RATPUP.txt |
| [ASR009](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR009) | LMM for a randomized complete block design with spatial analysis - Wheat varieties | R, py | BESAG_ELBATAN.txt |
| [ASR010](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR010) | Random coefficient LMM for longitudinal data (random intercept and slope) - Dog scans | R, py | PIXEL.txt |
| [ASR011](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR011) | LMM with log transformation of the response and pedigree - Tawny dragon lizards | R, py | LIZARD.txt |
| [ASR012](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR012) | LMM with pedigree information - Atlantic salmon | R, py | SALMON.txt, SALMON_PED.txt |
| [ASR013](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR013) | Exploring the options to obtain a relationship matrix based on a pedigree | R, py | AINVERSE_PED.txt |
| [ASR014](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR014) | LMM for a split-plot design with covariates - Oats varieties | R, py | OATS.txt |
| [ASR015](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR015) | LMM for a row-column design with nested effects - Spring barley varieties | R, py | DURBAN_ROWCOL.txt |
| [ASR016](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR016) | LMM for a split-split-plot design with a three-way factorial - Apple cultivars | R, py | ARCHBOLD_APPLE.txt |
| [ASR017](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR017) | Exploring phenotypic data at each site individually before fitting an MET model - Pine clones | R, py | PINE_CLONES.txt, PINE_CLONES_PED.txt |
| [ASR018](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR018) | LMM for a multi-environmental trial - Pine clones | R, py | PINE_CLONES.txt, PINE_CLONES_PED.txt |
| [ASR019](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR019) | Obtaining predictions for specific values of an explanatory variable - Synthetic weight loss data | R, py | WEIGHT_LOSS.txt |
| [ASR020](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR020) | Random coefficient LMM for longitudinal data (random intercept and slope) - Treatment of Alzheimer's disease | R, py | ALZHEIMER.txt |
| [ASR021](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR021) | Three-way interaction linear models - Treating hypertension | R, py | PRESSURE.txt |
| [ASR022](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR022) | Mixed linear model for repeated measures using an antedependence residual structure - Dog hearts' enzyme content | R, py | ATP.txt |
| [ASR023](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR023) | LMM specifying a generalized unstructured correlation matrix - Effect of ozone on lung capacity | R, py | LUNG.txt |
| [ASR024](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR024) | LMM with transformed response - Epilepsy treatment | R, py | EPILEPSY.txt |
| [ASR025](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR025) | LMM with correlated residuals and model comparison using the LRT - Twins' IQ | R, py | TWINLONG.txt |
| [ASR026](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR026) | Using SNP markers to obtain a genomic relationship matrix - Spring barley lines | R | SPRING_BARLEY_SNP.txt |
| [ASR027](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR027) | Run a quality control check on a genomic relationship matrix - Spring barley lines | R | SPRING_BARLEY_SNP.txt |
| [ASR028](https://github.com/VSNinternational/asreml-cookbook/tree/main/recipes/ASR028) | Univariate and bivariate parental LMMs - Maize hybrids | R, py | MAIZE_HYBRIDS.txt |

*Generated from the cookbook sources by `build-github-repo.py`; do not edit by hand.*
