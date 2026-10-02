
library(asreml)

d014 <- read.table("MAIZE_HYBRIDS.txt", header = TRUE, na.strings='NA')

d014$sire <- as.factor(d014$sire)
d014$dam <- as.factor(d014$dam)


asr028 <- asreml(
  fixed = rdm ~ 1, 
  random = ~sire + and(dam) , 
  residual = ~units,
  equate.levels = c('sire','dam'),
  data = d014
)


asr028_b <- asreml(
  fixed = cbind(rdm, srl) ~ trait, 
  random = ~corgh(trait):sire + and(corgh(trait):dam),
  residual = ~id(units):corgh(trait),
  equate.levels = c('sire','dam'),
  data = d014
)


summary(asr028)$varcomp

BLUP<-as.data.frame(summary(asr028, coef = TRUE)$coef.random)
head(BLUP)

vpredict(asr028, h2 ~ 4*V1/(2*V1+V2))


summary(asr028_b)$varcomp

BLUP<-as.data.frame(summary(asr028_b, coef = TRUE)$coef.random)
head(BLUP)

vpredict(asr028_b, h2_rdm ~ 4*V2/(2*V2+V6))


