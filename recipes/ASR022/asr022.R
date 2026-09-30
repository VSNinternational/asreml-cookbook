
library(asreml)

d018 <- read.table("ATP.txt", header = TRUE,na.strings='NA')

d018$heart <- as.factor(d018$heart)
d018$A <- as.factor(d018$A)
d018$B <- as.factor(d018$B)
d018$time <- as.factor(d018$time)

asr022 <- asreml(
  fixed = ATP ~ A + B + A:B + A:time + B:time, 
  random = ~heart, 
  residual = ~heart:ante(time,1),
  data = d018
)
asr022 <- update(asr022)

varcomp <- summary(asr022)$varcomp
head(varcomp)

wald(asr022, denDF = 'numeric', ssType = 'incremental')$Wald

pp <- predict(asr022, classify = 'A:B:time')$pvals
head(pp)
tail(pp)
