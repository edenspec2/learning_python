
angle <- function(x,y){
  dot.prod <- x %*% y 
  norm.x <- norm(x, type = "2")
  norm.y <- norm(y, type = "2")
  theta <- acos(dot.prod / (norm.x * norm.y))
  as.numeric(theta)
}

x <- as.matrix(c(2,4))
y <- as.matrix(c(3,5))
angle(t(x),y)          # Use of transpose to make vectors (matrices) conformable.

xyz_file_generator_library()
