
library(asreml)
library(ASRgenomics)

d009ped <- read.table("AINVERSE_PED.txt", header = TRUE)

ainv <- ainverse(d009ped)

head(ainv)

attributes(ainv)$rowNames

ainv.f <- ASRgenomics::sparse2full(K = ainv)
A <- G.inverse(G = ainv.f)$Ginv

A<-matrix(A, nrow = 16, ncol =16)
rownames(A) <- c( "*","ID15","ID1" ,  "ID2",  "ID3",  "ID4" , "ID5" , "ID6" , "ID7" , "ID8" , "ID9","ID10" ,"ID11" ,"ID12","ID13","ID14")
colnames(A) <- c( "*", "ID15","ID1" ,  "ID2",  "ID3",  "ID4" , "ID5" , "ID6" , "ID7" , "ID8" , "ID9","ID10" ,"ID11","ID12","ID13","ID14")
round(A,2)


ainv <- ainverse(d009ped, mv = c("ID15", "*"))

attributes(ainv)$rowNames


ainv <- ainverse(d009ped, mv = c( "*"), fgen = list("f_gen", 0.5)) 

ainv.f <- ASRgenomics::sparse2full(K=ainv)
a<- G.inverse(G=ainv.f)$Ginv
A<-matrix(a, nrow = 15, ncol =15)
rownames(A) <- c( "ID15","ID1" ,  "ID2",  "ID3",  "ID4" , "ID5" , "ID6" , "ID7" , "ID8" , "ID9","ID10" ,"ID11" ,"ID12","ID13","ID14")
colnames(A) <- c(  "ID15","ID1" ,  "ID2",  "ID3",  "ID4" , "ID5" , "ID6" , "ID7" , "ID8" , "ID9","ID10" ,"ID11","ID12","ID13","ID14")
round(A,2)


d009ped_selfing <- d009ped[, c(1, 3, 2, 4, 5, 6)]

ainv<- ainverse(d009ped_selfing, mv = c("*"), selfing = 0.3)


ainv.f <- ASRgenomics::sparse2full(K=ainv)
a<- G.inverse(G=ainv.f)$Ginv
A<-matrix(a, nrow = 15, ncol =15)
rownames(A) <- c("ID15","ID1" ,  "ID2",  "ID3",  "ID4" , "ID5" , "ID6" , "ID7" , "ID8" , "ID9","ID10" ,"ID11" ,"ID12","ID13","ID14")
colnames(A) <- c( "ID15","ID1" ,  "ID2",  "ID3",  "ID4" , "ID5" , "ID6" , "ID7" , "ID8" , "ID9","ID10" ,"ID11","ID12","ID13","ID14")
round(A,2)


d009ped_mgs <- d009ped[, c(1, 2, 5, 3, 4, 6)]

ainv <- ainverse(d009ped_mgs, mv = "*", mgs = TRUE)

ainv.f <- ASRgenomics::sparse2full(K=ainv)
a<- G.inverse(G=ainv.f)$Ginv
A<-matrix(a, nrow = 15, ncol =15)
rownames(A) <- c("ID15","ID1" ,  "ID2",  "ID3",  "ID4" , "ID5" , "ID6" , "ID7" , "ID8" , "ID9","ID10" ,"ID11" ,"ID12","ID13","ID14")
colnames(A) <- c( "ID15","ID1" ,  "ID2",  "ID3",  "ID4" , "ID5" , "ID6" , "ID7" , "ID8" , "ID9","ID10" ,"ID11","ID12","ID13","ID14")
round(A,2)


d009ped_psort <- d009ped[c(1, 8, 2, 3, 12, 5, 6, 14, 7, 9, 10, 11, 13),]

ainv_ped <- ainverse(d009ped_psort, mv = "*", psort = TRUE)
ainv_ped
