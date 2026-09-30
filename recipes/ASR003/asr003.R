
library(asreml)

d002 <- read.table("TWINLONG.txt", header = TRUE,na.strings='NA')

d002$pair <- as.factor(d002$pair)
d002$twin <- as.factor(d002$twin)

asr003 <- asreml(
  fixed = iq ~ twin,
  random = ~pair,
  residual = ~units,
  data = d002
)

wald(asr003, denDF = 'numeric')$Wald

predict(asr003, classify = 'twin')$pvals

summary(asr003)$varcomp

vpredict(asr003, r2 ~ V1/(V1+V2))


BLUP <- summary(asr003, coef = TRUE)$coef.random
head(BLUP)

