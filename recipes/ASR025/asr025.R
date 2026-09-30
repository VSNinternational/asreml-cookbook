
library(asreml)

d002 <- read.table("TWINLONG.txt", header = TRUE,na.strings='NA')

d002$pair <- as.factor(d002$pair)
d002$twin <- as.factor(d002$twin)

asr025_full <- asreml(
  fixed = iq ~ twin,
  residual = ~id(pair):corv(twin),
  data = d002
)

asr025_nested <- asreml(
  fixed = iq ~ twin,
  residual = ~id(pair):idv(twin),
  data = d002
)

lrt(asr025_nested, asr025_full, boundary=FALSE)

summary(asr025_full)$varcomp
