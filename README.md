NLP Study across Inaugural Speeches

An **Interactive NLP (Natural Language Processing) web application** that anayzes over two centuries of American presidential inaugural adresses (from 1789-2026) using Python, NLTK and Streamlit.

**Tech Stack:** Python | NLTK | Streamlit | Pandas | Textstat | WordCloud | Matplotlib

# Features
   - **Lexical Diversity** : Ratio of Unique Words/Total Words to evaluation vocabulary richness across different historical eras.
   - **Readability Index** : Measures the U.S. school grade level required to comprehend each of the texts using the Flesch Kincaid Metric
   - **VADER Sentiment Compound** : Uses NLTK's Vader sentiment Analyzer to judge the overall tone (with -1 being extremely negative and +1 being extremely positive)
   - **Keyword Frequency** : User can input a search term and find it's frequency across every presidential election year in a line chart.
   - **Word Cloud**: User can select a 50-year time period from the `wordcloud` library to generate a Word Cloud with colours and most commonly used words in the half-century.

Modules:
1. `preprocessor.py`
   Uses the NLTK Inaugural Corpus to extract every presidential adress from 1789.
   Cleans raw text by converting all characters to lowerase and strips punctuation using string translation tables.

2. 'analyzer.py'
   Processes the corpus data to compute key metrics such as Lexical Diversity, Average Sentence Legnth, Flesch Kincaid Grade Level readability scores, and VADER sentiment compound polarities.
  
3. `app.py`
   Uses **Streamlit** to create an interactive web interface, organized into three tabs:
   - **Tab 1**: Words
       Allows users to input a search term (e.g. *freedom*, *constitution*) to observe it's usage frequency across every presidential election.
     **Example with "Freedom"**
     <img width="1408" height="700" alt="2026-10-16T14-20_chart" src="https://github.com/user-attachments/assets/c9d71050-60b9-448d-a570-9f1a53be0b27" />
     
       Allows users to create WordClouds for each half-century.
       **Example from 1950-1989**
      <img width="916" height="532" alt="image" src="https://github.com/user-attachments/assets/918cd416-9e75-457c-81b7-b9a97d3ab850" />


   - **Tab 2**: Readability and Sentiment
       Uses line charts to show how Flesch Kincaid Levels and the VADER Compound score has changed over the years.
     **Flesch Kincaid Levels:**
      <img width="1408" height="700" alt="2026-10-16T14-29_chart" src="https://github.com/user-attachments/assets/a0c16716-9eb8-460c-a3c4-6da4774b2b4a" />
  (It's fascinating to observe a decrease in the reading level of speeches over the years)

    **Sentiment VADER**
   <img width="1408" height="700" alt="2026-10-16T14-31_chart" src="https://github.com/user-attachments/assets/4381512c-7baa-422d-a2ad-4a9f4eb130b9" />
    (It's interesting to note that the speeches are extremely positive, except for the large drop in the Vader Compound in 1865, which is when Abrahan Lincoln delivered a sober speech on the Civil War)

  - **Tab 3** : Core Metrics
    Returns a line-chart on Lexical Diversity and Average Sentence Length over the years
  <img width="1408" height="700" alt="2026-10-16T14-36_chart" src="https://github.com/user-attachments/assets/46facb11-22e3-43bd-a124-dde5696ed793" />
  <img width="1408" height="700" alt="2026-10-16T14-36_chart (1)" src="https://github.com/user-attachments/assets/550b2411-1523-41c0-a6f4-93f8ef0563b8" />

  
