import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Set explicit NLTK data path to avoid issues in certain environments
nltk.data.path.append("/usr/share/nltk_data")

# Initialize PorterStemmer
ps = PorterStemmer()

# Function to transform input text
def transform_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Tokenize the text using nltk
    text = nltk.word_tokenize(text)

    # Remove non-alphanumeric characters
    y = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]

    # Apply stemming
    y = [ps.stem(i) for i in y]

    # Return the transformed text
    return " ".join(y)

# Load pre-trained TF-IDF vectorizer and spam classification model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("Email/SMS Spam Classifier")

# Input text area for user to enter SMS content
input_sms = st.text_area("Enter the message")

# Predict button that processes the input and shows the result
if st.button('Predict'):
    # 1. Preprocess the input message
    transformed_sms = transform_text(input_sms)
    
    # 2. Vectorize the transformed message
    vector_input = tfidf.transform([transformed_sms])
    
    # 3. Predict the spam or not
    result = model.predict(vector_input)[0]

    # 4. Display the result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
