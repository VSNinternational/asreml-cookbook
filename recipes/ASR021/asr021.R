
library(asreml)

d017 <- read.table("PRESSURE.txt", header = TRUE,na.strings='NA')

d017$drug <- as.factor(d017$drug)
d017$biofeed <- as.factor(d017$biofeed)
d017$diet <- as.factor(d017$diet)

asr021_full <- asreml(
  fixed = pressure ~ drug*biofeed*diet, 
  residual = ~units,
  data = d017
)

asr021_partial <- asreml(
  fixed = pressure ~ drug:biofeed:diet, 
  residual = ~units,
  data = d017
)


preds_full <- predict(asr021_full, classify = 'drug*biofeed*diet')$pvals
preds_full

preds_partial <- predict(asr021_partial, classify = 'drug:biofeed:diet')$pvals
preds_partial

wald(asr021_full, denDF = 'numeric')$Wald

wald(asr021_partial, denDF = 'numeric')$Wald

