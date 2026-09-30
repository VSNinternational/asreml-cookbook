
library(asreml)

d021 <- read.table("PINE_CLONES.txt", header=TRUE,na.strings='NA')

d021ped <- read.table("PINE_CLONES_PED.txt", header = TRUE,na.strings='NA')

d021$clone <- as.factor(d021$clone)
d021$block <- as.factor(d021$block)
d021$location <- as.factor(d021$location)

ainv<- ainverse(d021ped)

d021 <- d021[order(d021$location),]
asr018 <- asreml(
  fixed = height_8 ~ location,
  random = ~at(location):block + vm(clone, ainv) + idv(location):vm(clone, ainv),
  residual = ~dsum(~units|location),
  data = d021
)

summary(asr018)$varcomp

vpredict(asr018, h2 ~ V4/((V1+V2+V3)/3+V4+V5+(V6+V7+V8)/3))

wald(asr018, denDF = 'numeric')$Wald

BLUP <- as.data.frame(summary(asr018, coef = TRUE)$coef.random)
head(BLUP)
tail(BLUP)
