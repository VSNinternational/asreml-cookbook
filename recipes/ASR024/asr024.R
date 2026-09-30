
library(asreml)

d020 <- read.table("EPILEPSY.txt", header = TRUE,na.strings='NA')

d020$trt <- as.factor(d020$trt)
d020$time <- as.factor(d020$time)
d020$patient <- as.factor(d020$patient)

asr024 <- asreml(
  fixed = seizure ~ base + trt + time + trt:time, 
  residual = ~dsum(~id(patient):corv(time)|trt),
  data = d020
)

d020$trans <- log(d020$seizure + 1)

asr024t <- asreml(
  fixed = trans ~ base + trt + time + trt:time, 
  residual = ~dsum(~id(patient):corv(time)|trt),
  data = d020
)

res <- data.frame(asr024$residuals)
rest <- data.frame(asr024t$residuals)
par(mfrow = c(1, 2))
hist(res$e, breaks = 15, xlab = "residuals", main = "asr024")
hist(rest$e, breaks = 20, xlab = "residuals", main = "asr024t")

wald(asr024, denDF = 'numeric')$Wald

summary(asr024t)$varcomp

preds <- predict(asr024t, classify = 'trt')$pvals
as.data.frame(preds)
preds$back_trans <- exp(preds$predicted.value) - 1
preds
