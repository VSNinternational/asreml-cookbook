
library(asreml)

d002 <- read.table("TWINLONG.txt", header = TRUE,na.strings='NA')

d002$pair <- as.factor(d002$pair)
d002$twin <- as.factor(d002$twin)

asr025_MC <- asreml(
  fixed = iq ~ twin,
  residual = ~id(pair):corv(twin),
  data = d002
)

asr025_MI <- asreml(
  fixed = iq ~ twin,
  residual = ~id(pair):idv(twin),
  data = d002
)

lrt(asr025_MI, asr025_MC, boundary = FALSE)

summary(asr025_MC)$varcomp
