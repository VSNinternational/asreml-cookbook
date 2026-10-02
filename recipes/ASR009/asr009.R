
library(asreml)

d001 <- read.table("BESAG_ELBATAN.txt", header = TRUE,na.strings='NA')

d001$gen <- as.factor(d001$gen)
d001$row <- as.factor(d001$row)
d001$col <- as.factor(d001$col)

asr009 <- asreml(
  fixed = yield ~ 1 + col,
  random = ~gen,
  residual = ~ar1v(col):ar1(row),
  data = d001
)

summary(asr009, coef = TRUE)$coef.fixed

summary(asr009)$varcomp

vpredict(asr009, H2 ~ V1/(V1+V4))

BLUP <- summary(asr009, coef = TRUE)$coef.random
head(BLUP)
