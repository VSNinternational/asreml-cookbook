
library(asreml)

d013 <- read.table("ARCHBOLD_APPLE.txt", header = TRUE,na.strings='NA')

d013 <- transform(d013, rep = factor(rep), spacing = factor(spacing), stock = factor(stock), gen = factor(gen),
                 wplot = factor(paste(row, spacing, sep = "_")),
                 subplot = factor(paste(row, spacing, stock, sep="_")))

asr016 <- asreml(
  fixed = yield ~ spacing*stock*gen, 
  random = ~rep + rep:wplot + rep:wplot:subplot, 
  residual = ~units,
  data = d013
)

plot(asr016)

wald(asr016, denDF = 'numeric', ssType = 'incremental')$Wald

predict(asr016, classify = 'spacing')$pvals
predict(asr016, classify = 'stock:gen')$pvals

summary(asr016)$varcomp
