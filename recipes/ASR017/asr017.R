
library(asreml)

d021 <- read.table("PINE_CLONES.txt", header=TRUE,na.strings='NA')

d021ped <- read.table("PINE_CLONES_PED.txt", header = TRUE,na.strings='NA')

d021$location <- as.factor(d021$location)

levels(d021$location)
d021_r <- d021[d021$location ==  'Rail', ]

d021_r$clone <- as.factor(d021_r$clone)
d021_r$block <- as.factor(d021_r$block)
d021_r$location <- as.factor(d021_r$location)

summary(d021_r)

head(table(d021_r$block, d021_r$clone))

hist(d021_r$height_8)

ainv<- ainverse(d021ped)

asr017 <- asreml(
  fixed = height_8 ~ 1,
  random = ~block + vm(clone, ainv),
  data = d021_r
)

plot(asr017)

res<-residuals(asr017)
which.max(res)
which.min(res)

d021_r$height_8[d021_r$height_8==187] <- NA
d021_r$height_8[d021_r$height_8==311] <- NA

