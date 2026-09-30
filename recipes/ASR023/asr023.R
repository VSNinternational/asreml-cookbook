
library(asreml)

d019 <- read.table("LUNG.txt", header = TRUE,na.strings='NA')

d019$rat <- as.factor(d019$rat)
d019$time <- as.factor(d019$time)

asr023_before <- asreml(
  fixed = resp ~ 1, 
  subset = time == 'Before', 
  data = d019
)

summary(asr023_before)$varcomp

asr023_after <- asreml(
  fixed = resp ~ 1, 
  subset = time == 'After', 
  data = d019
)

summary(asr023_after)$varcomp

initR <- c(0.5, 0.266, 0.975)

d019 <- d019[order(d019$time),]

asr023 <- asreml(
  fixed = resp ~ time, 
  residual = ~corgh(time, init = initR):id(rat),
  data = d019
)

summary(asr023)$varcomp

wald(asr023, denDF = 'numeric')$Wald

predict(asr023, classify = 'time')$pvals

