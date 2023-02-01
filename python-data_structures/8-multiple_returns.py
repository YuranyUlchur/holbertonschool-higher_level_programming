#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    if len_sentence:
        return(len_sentence, sentence[0])
    else:
        return(0, None)
