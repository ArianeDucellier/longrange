# Run this script to generate multiple FARIMA time series
# of different lenths to test the different methods to compute d

library(fracdiff)
library(EnvStats)
library(CircStats)

set.seed(0)

# Lenths of the time series
Ns <- c(100, 1000, 10000, 100000)

# Number of time series
M <- 50

# Burn-out
n <- 100

# Create output directory
output_dir <- "../data/FARIMA"
if (!dir.exists(output_dir)){
  dir.create(output_dir)
}

for (i in (1:length(Ns))){
  
  output_dir <- paste("../data/FARIMA/length_", Ns[i], sep="")
  if (!dir.exists(output_dir)){
    dir.create(output_dir)
  }

  # 1) Gaussian FARIMA(1,d,0)
  
  phi <- 0.5
  d <- c(0.0, 0.1, 0.2, 0.3, 0.4)
  
  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_1_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], ar=c(phi), d=d[j], rand.gen=rnorm)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_1_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 2) Gaussian FARIMA(0,d,1)
  
  theta <- 0.5
  d <- c(0.0, 0.1, 0.2, 0.3, 0.4)
  
  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_2_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], ma=c(theta), d=d[j], rand.gen=rnorm)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_2_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 3) Gaussian FARIMA(1,d,1)
  
  phi <- - 0.3
  theta <- - 0.7
  d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_3_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], ar=c(phi), ma=c(theta), d=d[j], rand.gen=rnorm)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_3_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 4) Gaussian FARIMA(1,d,1)
  
  phi <- 0.3
  theta <- 0.7
  d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_4_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], ar=c(phi), ma=c(theta), d=d[j], rand.gen=rnorm)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_4_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 5) FARIMA(0,d,0) with exponential innovations
  
  d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_5_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], d=d[j], rand.gen=rexp)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_5_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 6) FARIMA(0,d,0) with lognormal innovations
  
  d <- c(0.0, 0.1, 0.2, 0.3, 0.4)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_6_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], d=d[j], rand.gen=rlnorm)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_6_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 7) Symmetric stable FARIMA(0,d,0)
  # a) alpha <- 1.5
  
  alpha <- 1.5
  d <- c(0.0, 0.1, 0.2, 0.3)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_7a_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], d=d[j], rand.gen=rstable, index=alpha)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_7a_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # b) alpha <- 1.2
  
  alpha <- 1.2
  d <- c(0.0, 0.1)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_7b_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], d=d[j], rand.gen=rstable, index=alpha)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_7b_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 8) Symmetric stable FARIMA(1,d,1)
  # a) alpha <- 1.5
  
  alpha <- 1.5
  phi <- 0.3
  theta <- 0.7
  d <- c(0.0, 0.1, 0.2, 0.3)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_8a_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], ar=c(phi), ma=c(theta), d=d[j], rand.gen=rstable, index=alpha)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_8a_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # b) alpha <- 1.2
  
  alpha <- 1.2
  phi <- 0.3
  theta <- 0.7
  d <- c(0.0, 0.1)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_8b_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], ar=c(phi), ma=c(theta), d=d[j], rand.gen=rstable, index=alpha)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_8b_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 9) FARIMA(0,d,0) with Pareto innovations
  
  alpha <- 1.5
  d <- c(0.0, 0.1, 0.2, 0.3)
  
  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_9_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], d=d[j], rand.gen=rpareto, location=1, shape=alpha, n.start=n)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_9_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }

  # 10) FARIMA(0,d,0) with skewed stable innovations
  
  alpha <- 1.5
  d <- c(0.0, 0.1, 0.2, 0.3)

  for (j in 1:length(d)){
    
    output_dir <- paste("../data/FARIMA/length_", Ns[i], "/series_10_", j, sep="")
    if (!dir.exists(output_dir)){
      dir.create(output_dir)
    }
    
    for (k in 1:M){ 
      ts <- fracdiff.sim(Ns[i], d=d[j], rand.gen=rstable, index=alpha, skewness=1)
      filename <- paste("../data/FARIMA/length_", Ns[i], "/series_10_", j, "/sample_", k, ".txt", sep="")
      write.table(ts$series, filename, sep="\t", row.names=FALSE, col.names=FALSE)
    }
  }
}
