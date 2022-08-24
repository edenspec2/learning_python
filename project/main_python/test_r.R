setwd("C:/Program Files/R/R-4.2.1/library")
library('tools')
library('plyr')

source("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/comp.set.1.1.R")
setwd("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole/molecule1")
nbos.info =list.files(pattern = "nbo_")

x=nbo.info("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole/molecule1","2 3 4")
df=nbo.df("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole")



