
library(asreml)

d006 <- read.table("PIXEL.txt", header = TRUE,na.strings='NA')

d006$dog <- as.factor(d006$dog)
d006$side <- as.factor(d006$side)
str(d006)

d006$daysq <- d006$day^2

asr010 <- asreml(
  fixed = pixel ~ side + day + daysq,
  random = ~str(~dog + dog:day, ~ corgh(2):id(dog)),
  data = d006
)

wald(asr010, denDF = 'numeric')$Wald

summary(asr010, coef = TRUE)$coef.fixed

summary(asr010)$varcomp

BLUP <- summary(asr010, coef = TRUE)$coef.random
head(BLUP)

tail(BLUP)
