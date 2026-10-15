import nltk
from nltk.corpus import inaugural
import string

nltk.download('inaugural')

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def corpus_data():
    data = []
    for fileid in inaugural.fileids():
        year = int(fileid[:4])
        name = fileid[5:]
        raw_text = inaugural.raw(fileid)
        text = clean_text(raw_text)
        data.append({
            "year" : year, 
            "fileid" : name,
            "raw_text" : raw_text,
            "text" : text,
            "words" : text.split(),
        })

    return data
    
