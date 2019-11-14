import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc



import pandas as pd
import plotly.graph_objs as go


#************************************************* Extraer de URL *************************************

def extraer_link(URL):
  #Importar librerias
  import bs4 as bs # web scraping
  import urllib.request #extraer de la web
  # Extraemos texto de la url
  link = urllib.request.urlopen(URL)
  article = link.read() #para leer los datos
  parsed_article = bs.BeautifulSoup(article,'lxml')
  paragraphs = parsed_article.find_all('p')
  origin_text = ""
  for p in paragraphs:
      origin_text += p.text
  
  return(origin_text)

URL = "https://www.biografiasyvidas.com/biografia/d/dali.htm"
crudo= extraer_link(URL) #llamado de la funcion

#************************************** Limpiar texto *********************************************

def Cleaner_text_sin_tok(text1):
  #minusculas
  text1 = text1.lower()
  #quitar numeros
  import re 
  text1 = re.sub (r'\d+','', text1) 
  text1= re.sub(r'\r\n', '', text1)
  text1=text1.replace('y', '')
  #quitar puntuacion
  text1 = re.sub(r'[^\w\s]','',text1)
  # SpaCy
  import spacy
  from spacy.lang.es import Spanish
  from spacy.tokenizer import Tokenizer
  nlp2 = Spanish()

# nlp es usado para crear docuementos con anotaciones linguisticas 
  doc = nlp2(text1)

# Creamos una lista de tokens
  token_list = []
  for token in doc:
      token_list.append(token.text)
# stop words
  from spacy.lang.es.stop_words import STOP_WORDS
  spacy_stopwords = spacy.lang.es.stop_words.STOP_WORDS
  spacy_stopwords.add('y') #agregar y
  spacy_stopwords.add('a') #agregar a
  spacy_stopwords.add('e')

  filtered_sent=[]
# filtrando stop words
  for word in doc:
      if word.is_stop==False:
          filtered_sent.append(word)
          
  sentence = filtered_sent
  sent_str = ""
  
#Reunir nuevamente el texto
  for i in sentence:
      sent_str += str(i) + "  "
      sent_str = sent_str[:-1]

#Quitar espacios en blanco repetidos    
  text1 = " ".join(sent_str.split())

  return(text1)

text = Cleaner_text_sin_tok(crudo) #llamado de la funcion

## NGrams **************************************************************************************

def df_py(text,n,N):
  import nltk
  from nltk import ngrams
  import collections
  import pandas as pd

  Ngrams = ngrams(text.split(), n)
  Ngrams2 = list(Ngrams)

  #Conteo pares de palabras
  bigram_counts = collections.Counter(Ngrams2)
  bigram_df = pd.DataFrame(bigram_counts.most_common(N),
                           columns=['gram', 'count'])
  #Ordenar de mayor a menor
  bigram_df = bigram_df.sort_values('count')
  #Agregar comillas
  bigram_df['gram'] = bigram_df['gram'].apply(lambda x: "'" + str(x) + "'")
  return(bigram_df)

df = df_py(text,2,11)#llamado de la funcion


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Texto', value='tab-1-example'),
        dcc.Tab(label='Gráficos', value='tab-2-example'),
        dcc.Tab(label='Resumen', value='tab-3-example'),
    ]),
    html.Div(id='tabs-content-example')
])


@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return html.Div([
            html.H3('Tab content 1'),
            
        ])
        
    elif tab == 'tab-2-example':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-1-tabs',
                figure={
                    'data': [{
                        'x': df["count"],
                        'y': df["gram"],
                        'type': 'bar',
                        'orientation': 'h'
                    }]
                }
            )
        ])
    
    elif tab == 'tab-3-example':
        return html.Div([
            html.H3('Tab content 3'),
            dcc.Graph(
                id='graph-3-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])


if __name__ == '__main__':
    app.run_server(debug=True)