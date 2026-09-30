
library(asreml)

d001 <- read.table("BESAG_ELBATAN.txt", header = TRUE,na.strings='NA')

d001$gen <- as.factor(d001$gen)
d001$row <- as.numeric(d001$row)
d001$col <- as.numeric(d001$col)

asr002 <- asreml(
  fixed = yield ~ col + row,
  random = ~gen,
  residual = ~units,
  data = d001
)

wald(asr002, denDF = 'numeric')$Wald

summary(asr002, coef = TRUE)$coef.fixed

summary(asr002)$varcomp

vpredict(asr002, h2 ~ V1/(V1+V2))
