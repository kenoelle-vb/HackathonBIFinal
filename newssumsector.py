from bs4 import BeautifulSoup
import streamlit as st
import requests
import tk as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import nltk
from langchain_groq import ChatGroq
import os
from groq import Groq
nltk.download('punkt')
#from google.colab import userdata

query = st.selectbox(
    "Pilih sektor untuk berita",
    ("Manufaktur", "Agrikultur", "Pertambangan", "Keuangan", "E-commerce"))

news1 = 1
news2 = 2
news3 = 3
news4 = 4
news5 = 5

# SCRAPING NEWS NUMBER 1 -------------------------------------------------------------
url = f"https://www.emitennews.com/search/{query}/{news1}"
webcontent = requests.get(url).text
soup = BeautifulSoup(webcontent, "lxml")
#title1 = soup.find("p", class_ = "fs-16").text.replace('</p>','')
link = soup.find("a", class_ = 'news-card-2 search-result-item') #.text.replace('href=','').split(',') #["href"]
#title1 = str(title1)
link = str(link)
substr1 = "href="
substr2 = '<div'
idxs1 = link.index(substr1)
idxs2 = link.index(substr2)
resx = ""
for idxs in range(idxs1 + len(substr1) + 1, idxs2):
  resx = resx + link[idxs]
  resx1 = resx[:-2]

# SCRAPING NEWS NUMBER 2 -------------------------------------------------------------
url = f"https://www.emitennews.com/search/{query}/{news2}"
webcontent = requests.get(url).text
soup = BeautifulSoup(webcontent, "lxml")
#title2 = soup.find("p", class_ = "fs-16").text.replace('</p>','')
link = soup.find("a", class_ = 'news-card-2 search-result-item') #.text.replace('href=','').split(',') #["href"]
#title2 = str(title2)
link = str(link)
substr1 = "href="
substr2 = '<div'
idxs1 = link.index(substr1)
idxs2 = link.index(substr2)
resx = ""
for idxs in range(idxs1 + len(substr1) + 1, idxs2):
  resx = resx + link[idxs]
  resx2 = resx[:-2]

# SCRAPING NEWS NUMBER 3 -------------------------------------------------------------
url = f"https://www.emitennews.com/search/{query}/{news3}"
webcontent = requests.get(url).text
soup = BeautifulSoup(webcontent, "lxml")
#title3 = soup.find("p", class_ = "fs-16").text.replace('</p>','')
link = soup.find("a", class_ = 'news-card-2 search-result-item') #.text.replace('href=','').split(',') #["href"]
#title3 = str(title3)
link = str(link)
substr1 = "href="
substr2 = '<div'
idxs1 = link.index(substr1)
idxs2 = link.index(substr2)
resx = ""
for idxs in range(idxs1 + len(substr1) + 1, idxs2):
  resx = resx + link[idxs]
  resx3 = resx[:-2]

# SCRAPING NEWS NUMBER 4 -------------------------------------------------------------
url = f"https://www.emitennews.com/search/{query}/{news4}"
webcontent = requests.get(url).text
soup = BeautifulSoup(webcontent, "lxml")
#title4 = soup.find("p", class_ = "fs-16").text.replace('</p>','')
link = soup.find("a", class_ = 'news-card-2 search-result-item') #.text.replace('href=','').split(',') #["href"]
#title4 = str(title4)
link = str(link)
substr1 = "href="
substr2 = '<div'
idxs1 = link.index(substr1)
idxs2 = link.index(substr2)
resx = ""
for idxs in range(idxs1 + len(substr1) + 1, idxs2):
  resx = resx + link[idxs]
  resx4 = resx[:-2]

# SCRAPING NEWS NUMBER 5 -------------------------------------------------------------
url = f"https://www.emitennews.com/search/{query}/{news5}"
webcontent = requests.get(url).text
soup = BeautifulSoup(webcontent, "lxml")
#title5 = soup.find("p", class_ = "fs-16").text.replace('</p>','')
link = soup.find("a", class_ = 'news-card-2 search-result-item') #.text.replace('href=','').split(',') #["href"]
#title5 = str(title5)
link = str(link)
substr1 = "href="
substr2 = '<div'
idxs1 = link.index(substr1)
idxs2 = link.index(substr2)
resx = ""
for idxs in range(idxs1 + len(substr1) + 1, idxs2):
  resx = resx + link[idxs]
  resx5 = resx[:-2]

url1 = resx1
url2 = resx2
url3 = resx3
url4 = resx4
url5 = resx5

article1 = Article(url1)
article2 = Article(url2)
article3 = Article(url3)
article4 = Article(url4)
article5 = Article(url5)

article1.download()
article2.download()
article3.download()
article4.download()
article5.download()

article1.parse()
article2.parse()
article3.parse()
article4.parse()
article5.parse()

article1.nlp()
article2.nlp()
article3.nlp()
article4.nlp()
article5.nlp()

summary1 = article1.text
summary2 = article2.text
summary3 = article3.text
summary4 = article4.text
summary5 = article5.text

all_summary = summary1 + "\n" + "\n" + summary2 + "\n" + "\n" + summary3 + "\n" + "\n" + summary4 + "\n" + "\n" + summary5

client = Groq(api_key="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")

# What the article is about
summary_bullet_point_whatarticleabout = f"Explain what the news in {all_summary} is about, using 5 bullet points of each news, and only answer in Indonesian, do not mention the news source"
bulletpointsummary_whatarticleabout = client.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_point_whatarticleabout,}],model="llama3-8b-8192")

bulletpointsummary_whatarticleabout = bulletpointsummary_whatarticleabout.choices[0].message.content
st.header(f'Rangkuman berita untuk {query}', divider='rainbow')
st.code(bulletpointsummary_whatarticleabout)

# How the condition affects business owners
summary_bullet_point_affecttosector = f"Explain how the conditions in {all_summary} affects business in the {query} sector, make 10 bullet points with it's own description, only answer in Indonesian, do not mention the news source"
bulletpointsummary_affecttosector = client.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_point_affecttosector,}],model="llama3-8b-8192")

bulletpointsummary_affecttosector = bulletpointsummary_affecttosector.choices[0].message.content
st.header(f'Bagaimana efeknya pada bisnis di sektor {query}?', divider='rainbow')
st.code(bulletpointsummary_affecttosector)

summary_bullet_point_whatshouldbusinessdo = f"Explain how owners of business in the {query} sector, should do in the condition of {all_summary} to not lose profit and keep growing, make 10 bullet points with detailed description, only answer based on the content of {all_summary}, and only answer in Indonesian, do not mention the news source"
bulletpointsummary_whatshouldbusinessdo = client.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_point_whatshouldbusinessdo,}],model="llama3-8b-8192")

bulletpointsummary_whatshouldbusinessdo = bulletpointsummary_whatshouldbusinessdo.choices[0].message.content
st.header(f'Apa yang sebaiknya bisnis di sektor {query} lakukan?', divider='rainbow')
st.code(bulletpointsummary_whatshouldbusinessdo)

import plotly.express as px
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, timedelta
from datetime import datetime
import streamlit as st

st.header(f'Performa perusahaan-perusahaan dalam sektor {spesquery} selama 3 bulan terakhir', divider='rainbow')

specific_query = st.selectbox(
    "Sektor mana bisnis anda?",
    ("Manufaktur", "Agrikultur", "Pertambangan", "Keuangan", "E-commerce"))

today = date.today()

d1 = date.today() - timedelta(days=90) # timespan of last 5 years
start_date = d1.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Manufaktur
if specific_query == "Manufaktur" :
  company1 = "ASII.jk"
  company2 = "UNTR.jk"
  company3 = "ISAT.jk"
  company4 = "INDF.jk"
  company5 = "GGRM.jk"

# Agrikultur
if specific_query == "Agrikultur" :
  company1 = "AALI.jk"
  company2 = "INDF.jk"
  company3 = "SMAR.jk"
  company4 = "BSDE.jk"
  company5 = "CTRA.jk"

# Pertambangan
if specific_query == "Pertambangan" :
  company1 = "ANTM.jk"
  company2 = "BSDE.jk"
  company3 = "INDF.jk"
  company4 = "SMAR.jk"
  company5 = "TINS.jk"

# Keuangan
if specific_query == "Keuangan" :
  company1 = "BMTR.jk"
  company2 = "BBCA.jk"
  company3 = "BNII.jk"
  company4 = "BAPA.jk"
  company5 = "BNLI.jk"

# e-commerce
if specific_query == "E-commerce" :
  company1 = "BUKA.jk"
  company2 = "TLKM.jk"
  company3 = "ISAT.jk"
  company4 = "SMDL.jk"
  company5 = "EXCL.jk"

# Downloading Data
if specific_query != "" :
  comp1_download = yf.download(tickers = company1,
                    start = start_date,
                    end = end_date)

  comp2_download = yf.download(tickers = company2,
                    start = start_date,
                    end = end_date)

  comp3_download = yf.download(tickers = company3,
                    start = start_date,
                    end = end_date)

  comp4_download = yf.download(tickers = company4,
                    start = start_date,
                    end = end_date)

  comp5_download = yf.download(tickers = company5,
                    start = start_date,
                    end = end_date)

company1str = str(company1)
company2str = str(company2)
company3str = str(company3)
company4str = str(company4)
company5str = str(company5)

# Retrieving Close Price
df1 = pd.DataFrame(comp1_download["Close"])
df2 = pd.DataFrame(comp2_download["Close"])
df3 = pd.DataFrame(comp3_download["Close"])
df4 = pd.DataFrame(comp4_download["Close"])
df5 = pd.DataFrame(comp5_download["Close"])

# Joining Dataframe Into 1 Dataframe

if specific_query == "Manufaktur" :
  df1 = pd.DataFrame({"ASII" : comp1_download["Close"]})
  df2 = pd.DataFrame({"UNTR" : comp2_download["Close"]})
  df3 = pd.DataFrame({"ISAT" : comp3_download["Close"]})
  df4 = pd.DataFrame({"INDF" : comp4_download["Close"]})
  df5 = pd.DataFrame({"GGRM" : comp5_download["Close"]})

if specific_query == "Agrikultur" :
  df1 = pd.DataFrame({"AALI" : comp1_download["Close"]})
  df2 = pd.DataFrame({"INDF" : comp2_download["Close"]})
  df3 = pd.DataFrame({"SMAR" : comp3_download["Close"]})
  df4 = pd.DataFrame({"BSDE" : comp4_download["Close"]})
  df5 = pd.DataFrame({"CTRA" : comp4_download["Close"]})

if specific_query == "Pertambangan" :
  df1 = pd.DataFrame({"ANTM" : comp1_download["Close"]})
  df2 = pd.DataFrame({"BSDE" : comp2_download["Close"]})
  df3 = pd.DataFrame({"INDF" : comp3_download["Close"]})
  df4 = pd.DataFrame({"SMAR" : comp4_download["Close"]})
  df5 = pd.DataFrame({"TINS" : comp5_download["Close"]})

if specific_query == "Keuangan" :
  df1 = pd.DataFrame({"BMTR" : comp1_download["Close"]})
  df2 = pd.DataFrame({"BBCA" : comp2_download["Close"]})
  df3 = pd.DataFrame({"BNII" : comp3_download["Close"]})
  df4 = pd.DataFrame({"BAPA" : comp4_download["Close"]})
  df5 = pd.DataFrame({"BNLI" : comp5_download["Close"]})

if specific_query == "E-commerce" :
  df1 = pd.DataFrame({"BUKA" : comp1_download["Close"]})
  df2 = pd.DataFrame({"TLKM" : comp2_download["Close"]})
  df3 = pd.DataFrame({"ISAT" : comp3_download["Close"]})
  df4 = pd.DataFrame({"SMDL" : comp4_download["Close"]})
  df5 = pd.DataFrame({"EXCL" : comp5_download["Close"]})

frames = [df1, df2, df3, df4, df5]
result = pd.concat(frames, axis=1, join='inner')

chart_data = pd.DataFrame(result, columns=["Company 1", "Company 2", "Company 3", "Company 4", "Company 5"])
st.line_chart(chart_data)
