
library(asreml)

d001 <- read.table("BESAG_ELBATAN.txt", header = TRUE,na.strings='NA')

d001$gen <- as.factor(d001$gen)
d001$col <- as.factor(d001$col)

asr001 <- asreml(
  fixed = yield ~ col,
  random = ~gen,
  residual = ~units,
  data = d001
)

wald(asr001, denDF = 'numeric')$Wald

summary(asr001)$varcomp

vpredict(asr001, h2 ~ V1/(V1+V2))

BLUP <- summary(asr001, coef = TRUE)$coef.random
head(BLUP)
