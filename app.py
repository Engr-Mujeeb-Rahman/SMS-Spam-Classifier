import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Only download if resources are not already downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


ps = PorterStemmer()

def transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load models
tfidf = pickle.load(open('D:\Jupyter Notebook\SMS Spam classifier\vectorizer_2.pkl', 'rb'))
model = pickle.load(open('D:\Jupyter Notebook\SMS Spam classifier\model_2.pkl', 'rb'))

# Custom professional and attractive CSS styling
st.markdown("""
    <style>
        body, .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #e0e0e0;
            font-family: 'Poppins', sans-serif;
        }

        h1 {
            color: #00f2fe;
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 2px 2px 5px #000000;
        }

        textarea {
            background-color: #1c1e26;
            color: #ffffff;
            border: 2px solid #00f2fe;
            border-radius: 15px;
            padding: 15px;
            font-size: 16px;
        }

        button[kind="primary"] {
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 10px 20px;
            font-weight: bold;
            font-size: 18px;
            transition: background 0.5s;
        }
        button[kind="primary"]:hover {
            background: linear-gradient(to right, #0072ff, #00c6ff);
            color: white;
        }

        .stHeader {
            font-size: 30px;
            font-weight: 800;
            color: #00f2fe;
            text-align: center;
            margin-top: 20px;
            text-shadow: 1px 1px 2px #000000;
        }

        .css-6qob1r {
            background: linear-gradient(180deg, #1c1e26 0%, #121212 100%);
            padding: 20px;
            border-radius: 15px;
        }

        .button {
            display: inline-block;
            padding: 10px 20px;
            background: linear-gradient(to right, #ffc107, #ff8c00);
            color: black;
            text-decoration: none;
            border-radius: 30px;
            text-align: center;
            font-weight: bold;
            transition: background 0.5s;
        }
        .button:hover {
            background: linear-gradient(to right, #ff8c00, #ffc107);
            color: white;
        }

        footer {
            visibility: hidden;
        }

        p.custom-text {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            color: #ffc107;
        }

        p.custom-text span {
            color: #04ECF0;
        }

        div[data-testid="stSidebar"] img {
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar configuration
# Sidebar configuration
with st.sidebar:
    st.markdown("""
        <style>
            div[data-testid="stSidebar"] {
                background: linear-gradient(135deg, #1c1e26, #2c5364);
                padding: 20px;
                border-radius: 15px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.image("logo.jpg", use_container_width=True)

    st.markdown('<p class="custom-text"><span>SMS</span> Spam <span>Classifier</span></p>', unsafe_allow_html=True)

    github_button_html = """
    <div style="text-align: center; margin-top: 50px;">
        <a class="button" href="https://github.com/Engr-Mujeeb-Rahman" target="_blank" rel="noopener noreferrer">Visit my GitHub</a>
    </div>
    """
    st.markdown(github_button_html, unsafe_allow_html=True)

    footer_html = """
    <div style="padding:10px; text-align:center;margin-top: 10px;">
        <p style="font-size:18px; color:#ffffff;">Made with ❤️ by Engr. Mujeeb Ur Rahman</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


# Streamlit UI
st.title("📩 SMS SPAM CLASSIFIER | App 🚀")
input_sms = st.text_area("Enter the message!")
        
        
if st.button('Predict'):
    
    # preprocess
    transform_sms = transform(input_sms)

    # vectorize
    vector_input = tfidf.transform([transform_sms])

    # predict
    result = model.predict(vector_input)[0]

    # Display
    if result == 1:
        st.header("🚫 SPAM — Warning! This could be harmful.")
    else:
        st.header("🟢 NOT SPAM — You're good to go!")
