import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud 
import pandas as pd
import textstat
from preprocessor import corpus_data
from analyzer import speech_stats
import nltk

nltk.download('inaugural', quiet=True)
nltk.download('vader_lexicon', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)  #

st.title("How Have American Presidential Inaugural Adresses Evolved from 1789?")

data = corpus_data()
df = pd.DataFrame(data)
stats_df = speech_stats(df)

tab1, tab2, tab3 = st.tabs(["Readability and Sentiment", "Words", "Metrics"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        user_word = st.text_input("Track a word frequency:").lower()
    with col2:
        decade_block = st.selectbox("Select Years for Word Cloud:", ["1789-1839", "1840-1889", "1890-1939", "1940-1989", "1990-2026"])

    if user_word:
        freq_data = []
        for _, row in df.iterrows():
            count = row["words"].count(user_word)
            freq_data.append({"year": row['year'], 'count': count})
        freq_df = pd.DataFrame(freq_data).set_index('year')
        st.subheader(f"Frequence of '{user_word}' over time")
        st.line_chart(freq_df)

        st.subheader(f"Word Cloud for {decade_block}")
        start_yr, end_yr = map(int, decade_block.split("-"))
        subset_text = " ".join(df[(df['year'] >= start_yr) & (df['year'] <= end_yr)]['text'])

        wc = WordCloud(width=800, height=400, background_color='white').generate(subset_text)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wc, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

with tab2:
    st.subheader("Flesch-Kincaid Grade Level")
    st.line_chart(stats_df.set_index('Year')["FK_Grade"])

    st.subheader("VADER Sentiment Compound Score")
    st.markdown("-1 indivates an extreme negative sentiment while +1 indicates an extreme positive sentiment")
    st.line_chart(stats_df.set_index("Year")["Sentiment_Compound"])
    
with tab3:
    st.subheader("Lexical Diversity or Type Token Ratio")
    st.line_chart(stats_df.set_index("Year")["Lexical_Diversity"])    
    st.subheader("Average Sentence Length")
    st.line_chart(stats_df.set_index('Year')["Average Sentence Length"])
