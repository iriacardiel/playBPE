from tokenizers import BasicTokenizer

# If we dont train the tokenizer no compression occurs. Only unicode encode / decode.
tokenizer = BasicTokenizer()
corpus_train = "Hello this a long text to train on my data. Hello what do you think about it."
tokenizer.train(text = corpus_train, vocab_size=300, verbose = True)
print(tokenizer.encode("Hello how are you"))
print(tokenizer.decode([72, 101, 108, 108, 111, 32, 104, 111, 119, 32, 97, 114, 101, 32, 121, 111, 117]))
