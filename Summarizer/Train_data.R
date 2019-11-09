data<- read.csv("Downloads/Summarizer/data_food.csv")
data_origi<- read.csv("Downloads/Summarizer/Reviews.csv")
#save(x = a , file = "data_100.csv")
a<- data[1:100,]

text1 <- paste(a[,'Text'],collapse = ' << ')

write.table(text1, file = "data_text.txt",
            row.names = FALSE)

summarize <- paste(a[,'Summary'],collapse = ' << ')
write.table(summarize, file = "data_sum.txt",
            row.names = FALSE)

#================

archivo <- "Downloads/Summarizer/text_trad_100.txt"
con <- file(archivo, open="r") # Abrimos la conexión
text_trad <- readLines(con)   

archivo <- "Downloads/Summarizer/sum_trad_100.txt"
con <- file(archivo, open="r") # Abrimos la conexión
sum_trad <- readLines(con)

#================
Text<- strsplit(text_trad, " << ")
Summary<- strsplit(sum_trad, " << ")

data_trad<- data.frame(Text, Summary)

save(file = data_trad.csv)



