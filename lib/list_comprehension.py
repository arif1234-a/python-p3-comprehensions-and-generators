#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]  # List comprehension to extract evens

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]  # Appends "!" to each sentence