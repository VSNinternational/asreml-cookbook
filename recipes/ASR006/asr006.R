
library(asreml)

d004 <- read.table("RAIL.txt", header = TRUE,na.strings='NA')

d004$rail <- as.factor(d004$rail)

asr006 <- asreml(
  fixed = travel ~ 1,
  random = ~rail,
  residual = ~units,
  data = d004
)

summary(asr006)$varcomp

BLUP <- summary(asr006, coef = TRUE)$coef.random
BLUP
