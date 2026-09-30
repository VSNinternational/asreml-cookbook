
library(asreml)

d011 <- read.table("OATS.txt", header = TRUE,na.strings='NA')

d011$variety <- as.factor(d011$variety)
d011$nitrogen <- as.factor(d011$nitrogen)
d011$block <- as.factor(d011$block)
d011$wplot <- as.factor(d011$wplot)

asr014 <- asreml(
  fixed = yield ~ variety + nitrogen + variety:nitrogen, 
  random = ~block + block:wplot, 
  residual = ~units,
  data = d011
)

asr014 <- asreml(
  fixed = yield ~ variety*nitrogen, 
  random = ~block/wplot,
  residual = ~units,
  data = d011
)

wald(asr014, denDF = 'numeric')$Wald

summary(asr014)$varcomp

predict(asr014, classify = 'variety:nitrogen')$pvals

preds <- predict(asr014, classify = 'nitrogen')$pvals
preds
