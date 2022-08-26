setwd("C:/Program Files/R/R-4.2.1/library")
library('tools')
library('plyr')

source("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/comp.set.1.1.R")
setwd("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole")

z=steRimol("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole/molecule1","3 7 ")


bonds <- unique(data.table::fread(list.files(pattern = "bonds")))
setwd("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole/molecule1")
coor<-function(coordinates){
  origin <- as.numeric(unlist(strsplit(coordinates, " "))[[1]])
  direction <- as.numeric(unlist(strsplit(coordinates, " "))[[2]])
  bonds <- unique(data.table::fread(list.files(pattern = "bonds")))
  if (is.na(bonds[bonds$V1 == direction, ][1, 2])) { #check v1 for direction if not found
    coordinates <- paste(coordinates, as.character(bonds[bonds$V2 == direction, ][1, 1]), sep = " ") #check v2 and take pair from v1
  } else {
    coordinates <- paste(coordinates, as.character(bonds[bonds$V1 == direction, ][1, 2]), sep = " ")#if found take pair from v2
  }
  if (as.numeric(unlist(strsplit(coordinates, " "))[[3]]) == origin) { #if 3 coordinates
    coordinates <- as.numeric(unlist(strsplit(coordinates, " "))[1:2])
    coordinates <- paste(as.character(coordinates[1]), as.character(coordinates[2]), sep = ' ')
    if (is.na(bonds[bonds$V1 == direction, ][1, 2])) {
      coordinates <- paste(coordinates, as.character(bonds[bonds$V2 == direction, ][2, 1]), sep = " ")
    } else {
      coordinates <- paste(coordinates, as.character(bonds[bonds$V1 == direction, ][2, 2]), sep = " ")
    }
  }
  return (coordinates)
}

y=coor('2 7 4')

