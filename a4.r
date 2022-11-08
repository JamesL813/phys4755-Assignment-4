library(ggplot2)

data1 <- read.csv("q1.csv", header = T, sep = ",")

ggplot(data1) +
    geom_line(aes(x, u), color = "grey") +
    geom_point(aes(x, u))
ggsave(file = "q1.pdf")
