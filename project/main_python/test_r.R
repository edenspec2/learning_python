setwd("C:/Program Files/R/R-4.2.1/library")
library('tools')
library('plyr')

source("C:/Users/עדן/Documents/GitHub/learning_python/project/moleculaR-main/R_scripts/code/comp.set.1.1.R")
xyz_file_generator("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python")

setwd("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python")
swapper('csv_file_for_r_1.xyz','2 5')
coor.trans('csv_file_for_r_2.xyz','2 3 4')




