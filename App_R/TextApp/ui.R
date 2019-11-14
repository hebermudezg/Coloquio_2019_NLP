library(shiny)
library(shinydashboard)
library(LDAvis)
library(tidyverse)


shinyUI(
  dashboardPage(
    dashboardHeader(title = "Unalytics"),
    dashboardSidebar(
      sidebarMenu(
        menuItem("Text explorer", tabName = "tab_explorer", icon = icon("dashboard")),
        menuItem("Word analysis", tabName = 'tab_word_analysis', icon = icon('bar-chart')),
        menuItem("Sentiment analysis",tabName = 'tab_sentiment', icon = icon('smile-o')),
        menuItem("Word relationships", tabName = 'tab_word_relationships', icon = icon('arrows-alt')),
        menuItem("Topics", tabName = "tab_topics", icon = icon("th")),
        menuItem("Find similar items", tabName = "tab_similar", icon = icon("flask"))
        
      )
    ),
    
    dashboardBody(
      fluidRow(
        tabItems(
          # First tab content
          tabItem(tabName = "tab_explorer",
                  column( width = 12, offset = 0.5, 
                          h2("Table Filter"), 
                          # Nadeem is doing
                          fluidRow(
                            wellPanel( h4("Filter the table by the categories in each column")))
                        )
                )
            )
        )
    ),


     tabItem(tabName = "tab_word_analysis",
                  tabBox(width = 12,
                         tabPanel("Word Counts",
                                  wellPanel(
                                    selectInput("input_word_counts_facet_by", "Split by",
                                                choices = options_columns),
                                    numericInput("input_word_counts_n", "Number of words",
                                                 value = 12, min = 3)),
                                  plotOutput("plot_word_counts", height = "500px")),
                         tabPanel("Word Cloud",
                                  wellPanel(
                                    selectInput("input_word_cloud_filter_by", "Filter by") #,
                                                #choices = options_columns),
                                    uiOutput("controls_word_cloud") ,
                                    numericInput("input_word_cloud_n", "Maximum number of words to show")#,
                                                # value = 50, min = 10),
                                    plotOutput("plot_word_cloud")
                                  )),
                         tabPanel("Split Word Cloud",
                                  wellPanel(
                                    "The dimension you choose must only have a few categories for the plot to show",
                                    selectInput("input_split_word_cloud_split_by", "Split by",
                                                #choices = options_columns_without_none),
                                    numericInput("input_split_word_cloud_n", "Maximum nunber of words to show")#,
                                                # value = 50, min = 10)),
                                  plotOutput("plot_split_word_cloud")
                            )
                        )
        )



  )
)