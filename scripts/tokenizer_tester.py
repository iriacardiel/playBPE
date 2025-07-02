from tokenizers import BasicTokenizer, RegexTokenizer
from termcolor import colored

# If we dont train the tokenizer no compression occurs. Only unicode encode / decode.
vocab_size = 1500
with open("corpora/fantasy.txt", "r", encoding="utf-8") as f:
    corpus_train = f.read()
    
corpus_test = "not spoken aloud in centuries" #"not spoken aloud in centuries"

# BASIC TOKENIZER 
tokenizer = BasicTokenizer()
tokenizer.train(text=corpus_train, vocab_size=vocab_size, verbose=False)
for token in tokenizer.encode(corpus_test):
    print(colored(f"{str(token).ljust(3)} | {tokenizer.decode([token])}", "red"))

# REGEX TOKENIZER 
tokenizer = RegexTokenizer()
tokenizer.train(text=corpus_train, vocab_size=vocab_size, verbose=False)
for token in tokenizer.encode(corpus_test):
    print(colored(f"{str(token).ljust(3)} | {tokenizer.decode([token])}", "blue"))
