setwd("C:/Program Files/R/R-4.2.1/library")
library('tools')
library('plyr')

source("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/comp.set.1.1.R")
setwd("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole")
x=nbo.info("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole/molecule1","2 3 4 5")
y=mol.info("info_A1_o.csv","vib_1_A1_o.csv")
info=dot.prod.info("info_A1_o.csv")
f=steRimol.df("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole")




y=paton.df("C:/Users/edens/Documents/GitHub/learning_python/project/main_python/test_dipole")
