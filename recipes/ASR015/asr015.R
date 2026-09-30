
library(asreml)

d010 <- read.table("DURBAN_ROWCOL.txt", header = TRUE,na.strings='NA')

d010$rep <- as.factor(d010$rep)
d010$row <- as.factor(d010$row)
d010$gen <- as.factor(d010$gen)
d010$bed <- as.factor(d010$bed)

asr015 <- asreml(
  fixed = yield ~ rep,
  random = ~gen + rep:row + rep:bed,
  residual = ~units,
  data = d010
)

wald(asr015)

summary(asr015)$varcomp

vpredict(asr015, h2 ~ V3/(V1+V2+V3+V4))

summary(asr015,coef=TRUE)$coef.fixed

BLUP<-as.data.frame(summary(asr015,coef=TRUE)$coef.random)
head(BLUP)
