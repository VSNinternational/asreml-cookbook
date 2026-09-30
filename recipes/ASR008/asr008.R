
library(asreml)

d005 <- read.table("RATPUP.txt", header = TRUE,na.strings='NA')

d005$sex <- as.factor(d005$sex)
d005$litter <- as.factor(d005$litter)
d005$treatment <- as.factor(d005$treatment)

asr008 <- asreml(
  fixed = weight ~ lsize + treatment + sex + treatment:sex,
  random = ~litter,
  residual = ~dsum(~units|treatment),	
  data = d005
)

wald(asr008, denDF = 'numeric')$Wald

summary(asr008, coef = TRUE)$coef.fixed

summary(asr008)$varcomp

summary(asr008, coef = TRUE)$coef.random
