
library(asreml)

d015 <- read.table("WEIGHT_LOSS.txt", header = TRUE,na.strings='NA')

d015$trt <- as.factor(d015$trt)

asr019 <- asreml(
  fixed = loss ~ trt + weight + trt:weight, 
  residual = ~units,
  data = d015
)

wald(asr019, denDF = 'numeric', ssType = 'conditional')$Wald

predict(asr019, classify = 'trt:weight')$pvals

predict(asr019, classify = 'trt:weight', levels = list(weight = c(190, 230, 270)))$pvals

