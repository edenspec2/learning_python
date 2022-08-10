setwd("C:/Program Files/R/R-4.2.1/library")
library('tools')
library('plyr')

source("C:/Users/עדן/Documents/GitHub/learning_python/project/moleculaR-main/R_scripts/code/comp.set.1.1.R")
xyz_file_generator("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python")
folder <- "mortalkombat"

setwd("../")
dir.create(paste("../", folder, sep = ''), showWarnings = F)





