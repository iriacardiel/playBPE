import streamlit as st
from tokenizers import BasicTokenizer, RegexTokenizer
import os
import random

# --- Helper functions ---

def color_token(token, color):
    return f'<span style="background-color:{color}; padding:2px 4px; border-radius:4px; margin:1px;">{token}</span>'

def generate_colors(n):
    random.seed(42)
    return [f"hsl({random.randint(0, 360)}, 70%, 75%)" for _ in range(n)]

# --- App layout ---
st.set_page_config(page_title="Tokenizer Visualizer", layout="wide")
st.title("🧪 Tokenizer Visualizer")

# --- Catalog of corpus files ---
CORPUS_DIR = "corpora"
corpus_files = [f for f in os.listdir(CORPUS_DIR) if f.endswith(".txt")]


    


text_to_tokenize = {
                "fantasy.txt":" The wind rose suddenly, as if exhaling a secret.",
                "science-fiction.txt":" Even the androids moved slower"
                }

col1, col2 = st.columns(2)
with col1:
    # Select training corpus text
    selected_corpus = st.selectbox("📚 Select training corpus file:", corpus_files)
    
    # Load corpus
    with open(os.path.join(CORPUS_DIR, selected_corpus), "r", encoding="utf-8") as f:
        corpus_train = f.read()
    
    # Show corpus
    with st.expander("📄 Show training corpus text"):
        st.text_area("Training Text", value=corpus_train, height=300)
        
with col2:
    
    # Enter text to tokenize
    corpus_test = st.text_input("✏️ Enter text to tokenize:", text_to_tokenize.get(selected_corpus))

# Choose vocabulary size
vocab_size = st.slider("📏 Select vocabulary size:", min_value=256, max_value=5000, value=1500, step=30)


# --- Train tokenizers ---
btok = BasicTokenizer()
btok.train(text=corpus_train, vocab_size=vocab_size, verbose=False)
b_ids = btok.encode(corpus_test)
b_tokens = [btok.decode([i]) for i in b_ids]

rtok = RegexTokenizer()
rtok.train(text=corpus_train, vocab_size=vocab_size, verbose=False)
r_ids = rtok.encode(corpus_test)
r_tokens = [rtok.decode([i]) for i in r_ids]

# --- Generate colors ---
b_colors = generate_colors(len(b_tokens))
r_colors = generate_colors(len(r_tokens))

# --- Display side-by-side ---
col3, col4 = st.columns(2)

with col3:
    st.header("🔴 BasicTokenizer")
    colored_btokens = " ".join([color_token(tok, col) for tok, col in zip(b_tokens, b_colors)])
    st.markdown(colored_btokens, unsafe_allow_html=True)
    st.text_area("Token IDs", value=str(b_ids), height=100, key="basic_ids", disabled=True)

with col4:
    st.header("🔵 RegexTokenizer")
    colored_rtokens = " ".join([color_token(tok, col) for tok, col in zip(r_tokens, r_colors)])
    st.markdown(colored_rtokens, unsafe_allow_html=True)
    st.text_area("Token IDs", value=str(r_ids), height=100, key="regex_ids", disabled=True)
