import streamlit as st
import pickle
import string
import nltk

# Download necessary NLTK resources only if they haven't been downloaded yet
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# Function to preprocess the text
def transform_text(text):
    text = text.lower()  # Convert to lowercase
    text = nltk.word_tokenize(text)  # Tokenize the text

    y = []
    for word in text:
        if word.isalnum():  # Keep only alphanumeric words
            y.append(word)

    text = y[:]
    y.clear()

    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(word)

    text = y[:]
    y.clear()

    for word in text:
        y.append(ps.stem(word))  # Apply stemming

    return " ".join(y)

# Load pre-trained model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit app UI
st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocess the input text
    transformed_sms = transform_text(input_sms)
    
    # 2. Vectorize the preprocessed text
    vector_input = tfidf.transform([transformed_sms])
    
    # 3. Make prediction using the trained model
    result = model.predict(vector_input)[0]
    
    # 4. Display the result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
