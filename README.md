# playBPE
A playground to understand BPE (Byte-Pair Encoding) Tokenization 

- https://en.wikipedia.org/wiki/Byte-pair_encoding
- https://huggingface.co/learn/llm-course/chapter6/5
- Tokenizers are based on Andrej Karpathy - Let's build the GPT Tokenizer https://www.youtube.com/watch?v=zduSFxRajkE&t=350s

![alt text](images/image0.png)

# Set up the environment

1. Create virtual environment: ```python -m venv venv```

2. Activate virtual environment: ```source venv/bin/activate```

3. Install python dependencies: ```pip install -r requirements.txt```

# Tokenizer Tester (Python Script)

Run [tokenizer_tester.py](scripts/tokenizer_tester.py)

```python scripts/tokenizer_tester.py```

![alt text](images/image1.png)

# Tokenizer Visualizer (Streamlit App)

Run [tokenizer_viewer.py](scripts/tokenizer_viewer.py)

```streamlit run scripts/tokenizer_viewer.py```

![alt text](images/image2.png)

Go to http://localhost:8501 in your browser.

![alt text](images/image0.png)