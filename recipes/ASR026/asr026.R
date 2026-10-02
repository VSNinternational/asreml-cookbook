
library(asreml)
library(ASRgenomics)
library(dplyr)

d022genomic <- read.table("SPRING_BARLEY_SNP.txt", header = TRUE,na.strings='NA')

d022genomic_matrix <- data.matrix(d022genomic[,c(2:3490)])

row.names(d022genomic_matrix) <- d022genomic$lines 

d022genomic_matrix[1:6,1:6]

d022genomic_matrix <- qc.filtering(M=d022genomic_matrix, maf = 0.05, marker.callrate = 0.2, 
                       ind.callrate = 0.20, impute = FALSE, plots = FALSE)

d022_Gmatrix <- G.matrix(M=d022genomic_matrix$M.clean, method = "VanRaden")$G

d022_Gmatrix[1:6,1:6]

Ginv <- G.inverse(G=d022_Gmatrix, sparseform = TRUE)

d022_Gmatrix_bl <- G.tuneup(G=d022_Gmatrix, blend = TRUE, pblend=0.02)$Gb

Ginv_bl <- G.inverse(G=d022_Gmatrix_bl, sparseform = TRUE)$Ginv

