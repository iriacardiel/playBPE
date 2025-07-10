from tokenizers import BasicBPETokenizer, RegexBPETokenizer
from termcolor import colored

# If we dont train the tokenizer no compression occurs. Only unicode encode / decode.
vocab_size = 1500
selected_corpus = "tinyshakespeare.txt"
with open(f"corpora/{selected_corpus}", "r", encoding="utf-8") as f:
    corpus_train = f.read()
    
# THE LONGER THE TEXT THE BETTER THE TOKENIZER BUT LONGER THE TRAINING TIME
text_to_tokenize = {
                "fantasy.txt":" The wind rose suddenly, as if exhaling a secret.", # SHORT
                "science-fiction.txt":" Even the androids moved slower", # SHORT
                "tinyshakespeare.txt" : " It is a truth universally acknowledged" # LONG
                }
    
corpus_test = text_to_tokenize.get(selected_corpus)

# BASIC TOKENIZER 
tokenizer = BasicBPETokenizer()
tokenizer.train(text=corpus_train, vocab_size=vocab_size, verbose=False)
tokenizer.save("basic")
for token in tokenizer.encode(corpus_test):
    print(colored(f"{str(token).ljust(3)} | {tokenizer.decode([token])}", "red"))

# REGEX TOKENIZER 
tokenizer = RegexBPETokenizer()
tokenizer.train(text=corpus_train, vocab_size=vocab_size, verbose=False)
tokenizer.save("regex")
for token in tokenizer.encode(corpus_test):
    print(colored(f"{str(token).ljust(3)} | {tokenizer.decode([token])}", "blue"))
