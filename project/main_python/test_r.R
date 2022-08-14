setwd("C:/Program Files/R/R-4.2.1/library")
library('tools')
library('plyr')

source("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python/comp.set.1.1.R")
xyz_file_generator("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python")

setwd("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python")
swapper('csv_file_for_r_1.xyz','2 5')
coor.trans('csv_file_for_r_2.xyz','2 3 4 5')

steRimol("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python","3 4 5")


Center.Of.Mass <- function (coor.atoms, mol.dir) {
  setwd('..')
  xyz_file_generator(list.files(pattern = "basic"))
  setwd(list.files(pattern = "basic"))
  coor.trans(list.files(pattern = ".xyz"),coor.atoms)
  xyz <- data.table::fread(list.files(pattern = "tc.xyz"), header = F, colClasses = c("character", "numeric", "numeric", "numeric"),
                           stringsAsFactors = F)
  suppressMessages(xyz$V1 <- plyr::mapvalues(xyz$V1,
                                             from = c(
                                               "H", "B", "C", "N", "O", "F", "Si", "P",
                                               "S", "Cl", "Br", "I","Co", 'Ni'
                                             ),
                                             to = c("1", "5", "6", "7", "8", "9", "14", "15", "16", "17", "35", "53","27", "28")
  ))
  xyz <- data.frame(transform(xyz, V1 = as.numeric(V1)))
  for (i in 1:dim(xyz)[1]) ifelse(xyz[i,1] > 1, xyz[i,1] <- xyz[i,1] * 2, 1)
  M <- sum(xyz[,1])
  for (i in 1:dim(xyz)[1]) xyz[i,2:4] <- xyz[i,1] * xyz[i,2:4]
  com <- c(sum(xyz[,2]), sum(xyz[,3]), sum(xyz[,4]))
  com <- (1/M)*com
  unlink(list.files(pattern = ".xyz"))
  setwd('..')
  setwd(mol.dir)
  return(com)
}

Center.Of.Mass.Substructure <- function (coor.atoms, mol.dir, sub.atoms) {
  setwd('..')
  atoms <- strsplit(sub.atoms, " ")
  unlisted.atoms <- unlist(atoms)
  numeric.atoms <- as.numeric(unlisted.atoms)
  xyz_file_generator(list.files(pattern = 'basic'))
  setwd(list.files(pattern = "basic"))
  coor.trans(list.files(pattern = ".xyz"),coor.atoms)
  xyz <- data.table::fread(list.files(pattern = "tc.xyz"), header = F, colClasses = c("character", "numeric", "numeric", "numeric"),
                           stringsAsFactors = F)
  suppressMessages(xyz$V1 <- plyr::mapvalues(xyz$V1,
                                             from = c(
                                               "H", "B", "C", "N", "O", "F", "Si", "P",
                                               "S", "Cl", "Br", "I","Co", "Ni"
                                             ),
                                             to = c("1", "5", "6", "7", "8", "9", "14", "15", "16", "17", "35", "53","27", "28")
  ))
  xyz <- data.frame(transform(xyz, V1 = as.numeric(V1)))
  xyz <- xyz[numeric.atoms,]
  for (i in 1:dim(xyz)[1]) ifelse(xyz[i,1] > 1, xyz[i,1] <- xyz[i,1] * 2, 1)
  M <- sum(xyz[,1])
  for (i in 1:dim(xyz)[1]) xyz[i,2:4] <- xyz[i,1] * xyz[i,2:4]
  com <- c(sum(xyz[,2]), sum(xyz[,3]), sum(xyz[,4]))
  com <- (1/M)*com
  unlink(list.files(pattern = '*.xyz'))
  setwd('..')
  setwd(mol.dir)
  return(com)
}