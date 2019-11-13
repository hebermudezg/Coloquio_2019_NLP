data<- read.csv("data_1000.csv")
View(data)
subdata <- data[1:400,]
#save(x = subdata , file = "data_300.csv")

text1 <- paste(subdata[,'Text'], collapse = ' Jijueputa ')
write.table(text1, file = "text_400.txt", row.names = FALSE)


summarize <- paste(subdata[,'Summary'],collapse = ' Jijueputa ')
write.table(summarize, file = "sum_400.txt",row.names = FALSE)

#================

archivo <- "text_400_trad.txt"
con <- file(archivo, open="r") # Abrimos la conexión
text_trad <- readLines(con)   

archivo2 <- "catre.txt"
con <- file(archivo2, open="r") # Abrimos la conexión
sum_trad <- readLines(con)

#================
Text<- as.data.frame(strsplit(text_trad, " Jijueputa "),col.names = F)
View(Text)

summ<- as.data.frame(strsplit(sum_trad, " Catretriplejijueputa "),col.names = F)
View(summ)

data_trad_400<- data.frame(summ, Text)
colnames(data_trad_400) <- c("Summary","Text")
View(data_trad_400)

write.csv(x = data_trad_400, file = "data_trad_400.csv")



