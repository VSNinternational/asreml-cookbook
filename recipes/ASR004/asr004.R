
library(asreml)

d003 <- read.table("SEMICOND.txt", header = TRUE,na.strings='NA')

d003$source <- as.factor(d003$source)
d003$lot <- as.factor(d003$lot)
d003$wafer <- as.factor(d003$wafer)

asr004 <- asreml(
  fixed = thick ~ source,
  random = ~lot + lot:wafer,
  residual = ~units,
  data = d003
)

wald(asr004, denDF='numeric')$Wald

predict(asr004, classify = 'source')$pvals

summary(asr004)$varcomp

BLUP <- summary(asr004, coef = TRUE)$coef.random
head(BLUP, 12)
