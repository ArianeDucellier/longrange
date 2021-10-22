# Run this script to generate the FARIMA time series
# to test the different methods to compute d

library(fracdiff)
library(EnvStats)
library(CircStats)

set.seed(0)

N <- 10000
n <- 100

# 1) Gaussian FARIMA(1,d,0)

phi <- 0.5
d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, ar=c(phi), d=d[i], rand.gen=rnorm)
  filename <- paste("../data/FARIMA/series_1_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 2) Gaussian FARIMA(0,d,1)

theta <- 0.5
d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, ma=c(theta), d=d[i], rand.gen=rnorm)
  filename <- paste("../data/FARIMA/series_2_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 3) Gaussian FARIMA(1,d,1)

phi <- - 0.3
theta <- - 0.7
d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, ar=c(phi), ma=c(theta), d=d[i], rand.gen=rnorm)
  filename <- paste("../data/FARIMA/series_3_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 4) Gaussian FARIMA(1,d,1)

phi <- 0.3
theta <- 0.7
d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, ar=c(phi), ma=c(theta), d=d[i], rand.gen=rnorm)
  filename <- paste("../data/FARIMA/series_4_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 5) FARIMA(0,d,0) with exponential innovations

d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, d=d[i], rand.gen=rexp)
  filename <- paste("../data/FARIMA/series_5_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 6) FARIMA(0,d,0) with lognormal innovations

d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, d=d[i], rand.gen=rlnorm)
  filename <- paste("../data/FARIMA/series_6_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 7) Symmetric stable FARIMA(0,d,0)
# a) alpha <- 1.5

alpha <- 1.5
d <- c(0.0, 0.1, 0.2, 0.3)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, d=d[i], rand.gen=rstable, index=alpha)
  filename <- paste("../data/FARIMA/series_7a_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# a) alpha <- 1.2

alpha <- 1.2
d <- c(0.0, 0.1)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, d=d[i], rand.gen=rstable, index=alpha)
  filename <- paste("../data/FARIMA/series_7b_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 8) Symmetric stable FARIMA(1,d,1)
# a) alpha <- 1.5

alpha <- 1.5
phi <- 0.3
theta <- 0.7
d <- c(0.0, 0.1, 0.2, 0.3)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, ar=c(phi), ma=c(theta), d=d[i], rand.gen=rstable, index=alpha)
  filename <- paste("../data/FARIMA/series_8a_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# a) alpha <- 1.2

alpha <- 1.2
phi <- 0.3
theta <- 0.7
d <- c(0.0, 0.1)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, ar=c(phi), ma=c(theta), d=d[i], rand.gen=rstable, index=alpha)
  filename <- paste("../data/FARIMA/series_8b_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 9) FARIMA(0,d,0) with Pareto innovations

alpha <- 1.5
d <- c(0.0, 0.1, 0.2, 0.3)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, d=d[i], rand.gen=rpareto, location=1, shape=alpha, n.start=n)
  filename <- paste("../data/FARIMA/series_9_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}

# 10) FARIMA(0,d,0) with skewed stable innovations

alpha <- 1.5
d <- c(0.0, 0.1, 0.2, 0.3)

for (i in 1:length(d)){
  ts <- fracdiff.sim(N, d=d[i], rand.gen=rstable, index=alpha, skewness=1)
  filename <- paste("../data/FARIMA/series_10_", i, ".txt", sep="")
  write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE) 
}
