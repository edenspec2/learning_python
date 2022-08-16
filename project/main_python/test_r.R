setwd("C:/Program Files/R/R-4.2.1/library")
library('tools')
library('plyr')

source("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python/comp.set.1.1.R")
npa_dipole("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python/new_directory/test_dir","2 3 4 5")

setwd("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python")
xyz <- data.frame(data.table::fread("xyz_csv_file_for_r_2.csv" ,
                                    sep = " ", header = F, fill = T
))
xyz <- apply(xyz, as.numeric)



xyz_file_generator("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python")

setwd("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python")
swapper('csv_file_for_r_1.xyz','2 5')
coor.trans('csv_file_for_r_2.xyz','2 3 4 5')
setwd("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python/new_directory/test_dir")
setwd("C:/Users/עדן/Documents/GitHub/learning_python/project/main_python/new_directory")