
library(asreml)

d016 <- read.table("ALZHEIMER.txt", header = TRUE,na.strings='NA')

d016$id <- as.factor(d016$id)
d016$trt <- as.factor(d016$trt)

asr020 <- asreml(
  fixed = score ~ trt + visit, 
  random = ~str(~id + id:visit, ~corgh(2):id(id)), 
  residual = ~units,
  data = d016
)

wald(asr020, denDF = 'numeric')$Wald

summary(asr020, coef = TRUE)$coef.fixed

summary(asr020)$varcomp

BLUP <- summary(asr020, coef = TRUE)$coef.random
head(BLUP)

tail(BLUP)
