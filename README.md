---

# 📧 Spam Email Classifier

This is a simple **Spam Email Classifier Web App** built using **Python**, **Streamlit**, and **Scikit-learn**.

It predicts whether a message is **SPAM** or **HAM** (not spam) using a **Naive Bayes machine learning model**.

---

## 🚀 Features

* Simple and interactive web interface
* Real-time prediction of spam or ham messages
* Built with machine learning using a real email dataset

---

## 🛠️ Built With

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) - for building the web app
* [Scikit-learn](https://scikit-learn.org/) - for machine learning
* [Pandas](https://pandas.pydata.org/) - for data handling

---

## 📂 Dataset

The app uses a JSON file `email-text-data.json` that contains:

* `MESSAGE`: the email or message text
* `CATEGORY`: the label (`spam` or `ham`)

Example:

```json
[
  {
    "MESSAGE": "Congratulations! You've won a $1000 gift card. Click here.",
    "CATEGORY": "spam"
  },
  {
    "MESSAGE": "Let's have a meeting at 10 am tomorrow.",
    "CATEGORY": "ham"
  }
]
```

---

## ⚙️ How It Works

1. The dataset is loaded and the text is converted into numbers using `CountVectorizer`.
2. A **Naive Bayes classifier** is trained to recognize spam patterns.
3. The user enters a message into the app.
4. The model predicts whether the message is spam or not and shows the result.

---

## ▶️ How to Run the App

1. **Clone this repo:**

   ```bash
   git clone https://github.com/your-username/spam-email-classifier.git
   cd spam-email-classifier
   ```

2. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   streamlit run app.py
   ```

4. **Open in your browser** (usually opens automatically):
   `http://localhost:8501`

---

## 📦 File Structure

```
spam-email-classifier/
├── app.py                  # Main application file
├── email-text-data.json    # Dataset containing email messages and labels
├── requirements.txt        # Python package dependencies
└── README.md               # Project overview

```

---

## 📌 Example Prediction

You enter:

```
Congratulations! Claim your free prize now.
```

The app predicts:

```
SPAM ❌
```

---

## 🧠 About the Algorithm and Model

This app uses the **Multinomial Naive Bayes** algorithm — a simple yet powerful text classification algorithm — to predict whether an email message is **SPAM** or **HAM**.

### 🔍 Algorithm: Multinomial Naive Bayes

* **Naive Bayes** is a family of probabilistic algorithms based on applying **Bayes' theorem** with strong (naive) independence assumptions between the features.
* **Multinomial Naive Bayes** is specifically designed for text classification tasks where features are word counts or frequencies.
* The algorithm works well for spam detection because it can easily handle the types of patterns (e.g., frequent words) that are typical in spam emails.

### 🛠️ How the Model is Trained

1. The app uses a dataset (`email-text-data.json`) containing email `MESSAGE`s (text) and their corresponding `CATEGORY` labels (either `spam` or `ham`).
2. **Text Preprocessing:**

   * The `CountVectorizer` from `scikit-learn` is used to convert the raw text into numerical features (word counts).
   * Common English stop words (like "the", "is", "in") are removed to reduce noise.
3. The dataset is split into:

   * **70%** training data
   * **30%** testing data
4. The **Multinomial Naive Bayes algorithm** is trained on the training data to build the model. This trained model is then used to predict whether new email messages are spam or not.

### 📊 Libraries Used

* **`scikit-learn`**:

  * `CountVectorizer`: Converts text to numerical features.
  * `MultinomialNB`: The Naive Bayes algorithm used to build the model.
  * `train_test_split`: Splits the dataset into training and testing sets.


---
