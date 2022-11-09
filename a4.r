library(ggplot2)

data1 <- read.csv("q1.csv", header = TRUE, sep = ",")

ggplot(data1) +
    geom_line(aes(x, actual), color = "lightblue", linetype = "dashed") +
    geom_point(aes(x, actual), color = "blue") +
    geom_line(aes(x, u), color = "black", linetype = "dotted") +
    geom_point(aes(x, u))
ggsave(file = "q1.pdf")
