library(shiny)
library(rvest)



shinyServer(function(input, output) {

    output$distPlot <- renderPlot({

        # generate bins based on input$bins from ui.R
        x    <- faithful[, 2]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)

        # draw the histogram with the specified number of bins
        hist(x, breaks = bins, col = 'darkgray', border = 'white')

    })
    

##*********************** Scraping
    extraccion <- reactive({
      URl_li1 <- input$URL1
      contenido_texto <- read_html(URl_li1)
      texto_crudo <-paste(contenido_texto %>% html_nodes("p") %>%  html_text(), collapse = " ")
      
      URl_li2 <- input$URL2
      contenido_texto <- read_html(URl_li2)
      texto_crudo2 <-paste(contenido_texto %>% html_nodes("p") %>%  html_text(), collapse = " ")
      
      
      tabla_texto <- data.frame(texto=rbind(texto_crudo,texto_crudo2))
        
    })
    
    
    
    
    # Renderizar tabal para mostrar
    output$table <- renderDataTable(extraccion())
    
#****************************    

    


})
