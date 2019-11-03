item <- read.csv("C:/Users/Niraj/Downloads/pca_gsp.csv")
x <- item[2:10]
x
summary(x)
cor(x)
fun <- princomp(x, scores = TRUE, cor = TRUE)
summary(fun)
loadings(fun)
plot(fun)
screeplot(fun, type = "lines", main = "Screen Plot")
biplot(fun)
fun$scores[1:10,]
