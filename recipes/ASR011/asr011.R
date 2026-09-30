
library(asreml)

d007 <- read.table("LIZARD.txt", header = TRUE,na.strings='NA')

ainv <- ainverse(d007[, c(2:4)])

d007$indiv <- as.factor(d007$indiv)
d007$cohort <- as.factor(d007$cohort)
d007$sex <- as.factor(d007$sex)

asr011 <- asreml(
 fixed = p_yellow ~ cohort + sex,
 random = ~vm(indiv, ainv),
 residual = ~units,
 data = d007
)

plot(asr011)

(d007$p_yellow_log <- log((d007$p_yellow + 1)/(100 - d007$p_yellow + 1)))

asr011_transfo <- asreml(
  fixed = p_yellow_log ~ cohort + sex,
  random = ~vm(indiv, ainv),
  residual = ~idv(units),
  data=d007
)

plot(asr011_transfo)

wald(asr011_transfo, denDF = 'numeric')$Wald

summary(asr011_transfo)$varcomp

vpredict(asr011_transfo, h2 ~ V1/(V1+V2))

BLUP <- summary(asr011_transfo, coef = TRUE)$coef.random
head(BLUP)

BLUP<- as.data.frame(BLUP)

BLUP$Mean <- mean(d007$p_yellow_log)
BLUP$Preds <- BLUP$Mean + BLUP$solution
head(BLUP)

BLUP$BT_Preds <- ((100 + 1)*exp(BLUP$Preds) - 1)/(1 + exp(BLUP$Preds))
head(BLUP)
tail(BLUP)

BLUP$BT_Preds <- ((100 + 1)*exp(BLUP$Preds) - 1)/(1 + exp(BLUP$Preds))
head(BLUP)
tail(BLUP)
