import pandas as pd 
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import textstat
nltk.download('vader_lexicon', quiet=True)

def lexical_diversity(words):
    return len(set(words))/len(words)


def speech_stats(df):
    sia = SentimentIntensityAnalyzer()
    stats = []
    
    for _, row in df.iterrows():
        raw_text = row["raw_text"]
        words = row["words"]
        sentences = sent_tokenize(raw_text)

        avg_sent_len = len(words) / len(sentences)
        ttr = lexical_diversity(words)
        fk_grade = textstat.flesch_kincaid_grade(raw_text)
        sentiment = sia.polarity_scores(raw_text)["compound"]

        stats.append({
            'Year': row["year"],
            'Lexical_Diversity' : ttr,
            'FK_Grade' : fk_grade,
            'Average Sentence Length' : avg_sent_len,
            'Sentiment_Compound' : sentiment
        })

    return pd.DataFrame(stats)

