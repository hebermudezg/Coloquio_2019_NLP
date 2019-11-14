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
    
    # Extraccion va en un evento reactivo dado que la URL cambia cada vez que se use
    extraccion <- reactive({
      lego_movie <- html(input$URL)
      lego_movie %>%
        html_nodes("p") %>%
        html_text()
      
      })
  
    # renderizar para luego mostrar en la ui. 
    output$text_scrapiado <- renderText({
      extraccion()
    
    })
    
    
    


})
