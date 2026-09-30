
library(asreml)

d008 <- read.table("SALMON.txt", header=TRUE,na.strings='NA')

d008ped <- read.table("SALMON_PED.txt", header = TRUE,na.strings='NA')

ainv <- ainverse(d008ped)

d008$indiv <- as.factor(d008$indiv)

asr012 <- asreml(
  fixed = amoebic_load ~ 1,
  random = ~vm(indiv, ainv),
  residual = ~units,
  data = d008
)

plot(asr012)

summary(asr012)$varcomp

vpredict(asr012, h2 ~ V1/(V1+V2))

summary(asr012, coef=TRUE)$coef.fixed

BLUP <- as.data.frame(summary(asr012, coef=TRUE)$coef.random)
head(BLUP)

preds <- predict(asr012, classify='vm(indiv,ainv)')$pvals
head(preds)
