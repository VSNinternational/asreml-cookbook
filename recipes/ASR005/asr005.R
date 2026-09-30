
library(asreml)

d003 <- read.table("SEMICOND.txt", header = TRUE,na.strings='NA')

d003$source <- as.factor(d003$source)
d003$lot <- as.factor(d003$lot)
d003$wafer <- as.factor(d003$wafer)

asr005 <- asreml(
  fixed = thick ~ source,
  random = ~at(source):lot + lot:wafer,
  residual = ~units,
  data = d003
)

wald(asr005, denDF = 'numeric')$Wald

predict(asr005, classify = 'source')$pvals

summary(asr005)$varcomp
