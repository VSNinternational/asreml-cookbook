
library(asreml)

d005 <- read.table("RATPUP.txt", header = TRUE,na.strings='NA')

d005$sex <- as.factor(d005$sex)
d005$litter <- as.factor(d005$litter)
d005$treatment <- as.factor(d005$treatment)

asr007 <- asreml(
  fixed= weight ~ lsize + treatment + sex + treatment:sex,
  random = ~litter,
  residual = ~units,
  data = d005
)

plot(asr007)

res <- residuals(asr007)
d005$weight[which.min(res)] <- NA

asr007 <- update(asr007)

wald(asr007, denDF = 'numeric')$Wald

summary(asr007, coef=TRUE)$coef.fixed

BLUP <- summary(asr007, coef=TRUE)$coef.random
head(BLUP)
