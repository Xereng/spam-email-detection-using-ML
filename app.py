import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Read the data
DATA_JSON_FILE = 'email-text-data.json'

try:
    data = pd.read_json(DATA_JSON_FILE)
except FileNotFoundError:
    st.error(f"File {DATA_JSON_FILE} not found.")
    st.stop()

# Check for column names
if 'MESSAGE' not in data.columns or 'CATEGORY' not in data.columns:
    st.error("The dataset must contain 'MESSAGE' and 'CATEGORY' columns.")
    st.stop()

# Initialize the vectorizer and classifier
vectorizer = CountVectorizer(stop_words='english')
all_features = vectorizer.fit_transform(data['MESSAGE'])

X_train, X_test, y_train, y_test = train_test_split(all_features, data['CATEGORY'], 
                                                   test_size=0.3, random_state=88)

classifier = MultinomialNB()
classifier.fit(X_train, y_train)

def email_prediction(msg):
    matrix = vectorizer.transform([msg])
    prediction = classifier.predict(matrix)[0]
    prob = classifier.predict_proba(matrix).max()  # Get highest probability
    return prediction, prob

def main():
    st.title("SPAM e-MAIL CLASSIFICATION")
    st.subheader('Built with Python and Streamlit')

    msg = st.text_input("Enter Your Message Below... eg. Let's catch up tonight, You have a meeting scheduled for tomorrow, To join our premium membership please enter code ALLYSON30 etc.")
    
    if st.button('Predict'):
        if msg.strip() == "":
            st.warning("Please enter a message before predicting.")
        else:
            result, prob = email_prediction(msg)
            if result:
                st.error(f"SPAM (Probability: {prob*100:.2f}%)")
            else:
                st.success(f"HAM (Probability: {prob*100:.2f}%)")

if __name__ == '__main__':
    main()
