library(tidyverse)

students <- read_csv("students.csv")

head(students)

unique(students["school_name"])

