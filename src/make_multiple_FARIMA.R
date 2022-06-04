# Run this script to generate multiple FARIMA time series
# to test the different methods to compute d

library(fracdiff)
library(EnvStats)

set.seed(0)

# Like Taqqu
N <- 10000
# Same length as Chestler catalog with magnitudes
#N <- 852

M <- 50
n <- 100

# Create output directory
output_dir <- "../data/FARIMA_multiple"
if (!dir.exists(output_dir)){
  dir.create(output_dir)
}

# 9) FARIMA(0,d,0) with Pareto innovations

alpha <- 1.5
d <- c(0.0, 0.1, 0.2, 0.3)

for (i in 1:length(d)){

  output_dir <- paste("../data/FARIMA_multiple/series_9_", i, sep="")
  if (!dir.exists(output_dir)){
    dir.create(output_dir)
  }

  for (j in 1:M){ 
     ts <- fracdiff.sim(N, d=d[i], rand.gen=rpareto, location=1, shape=alpha, n.start=n)
     filename <- paste("../data/FARIMA_multiple/series_9_", i, "/sample_", j, ".txt", sep="")
     write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
  }
}
