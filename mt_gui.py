# Please run this script on Linux environment with Python 3
# python3 mt_gui.py

import tkinter
from tkinter import *
from numpy import argmax
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from googletrans import Translator
import pickle
import numpy
import keras
from attention_decoder import AttentionDecoder


# encode and pad sequence
def encode_sequence(tokenizer, length, line):
    sequence = list()
    sequence.append(line)
    # integer encode sequences
    X = tokenizer.texts_to_sequences(sequence)
    # pad sequence with 0 values
    result = pad_sequences(X, maxlen=length, padding='post')
    print(result[0])
    return result[0]

# map an integer to a word
def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None

# generate target given source sequence
def predict_sequence(model, tokenizer, source):
	prediction = model.predict(source, verbose=0)[0]
	integers = [argmax(vector) for vector in prediction]
	target = list()
	for i in integers:
		word = word_for_id(i, tokenizer)
		if word is None:
			break
		target.append(word)
	return ' '.join(target)

def translate_ger_eng(model, tokenizer, source):
    # translate encoded source text
    source = source.reshape((1, source.shape[0]))
    translation = predict_sequence(model, tokenizer, source)
    return translation

def output():
    model_output_widget.delete('1.0', END)
    google_output_widget.delete('1.0', END)
    source_sentence = input_widget.get().lower()
    # gather the translation result from google translation
    translator = Translator()
    google_translation_result = translator.translate(source_sentence, src='de', dest='en')
    model = load_model('bi_model.h5') # load model
    with open('eng_tokenizer.pickle', 'rb') as handle: # load tokenizer
        eng_tokenizer = pickle.load(handle)

    with open('ger_tokenizer.pickle', 'rb') as handle:  # load tokenizer
        ger_tokenizer = pickle.load(handle)

    encoded_sentence = encode_sequence(ger_tokenizer, 17, source_sentence)
    eng_sentence = translate_ger_eng(model, eng_tokenizer, encoded_sentence)

    model_output_widget.insert(END, eng_sentence)
    google_output_widget.insert(END, google_translation_result.text)
    print(source_sentence)

root = Tk()
root.title = 'German to English Machine Translator Bot'
root.geometry('1000x350')

Label(root, text="Machine Translator Bot", fg="red", font = "Verdana 20 bold").grid(row=0, column=2)
logo = PhotoImage(file="label-pic_160x120.gif")
Label(root, image=logo).grid(row=1, column=2)

# Add an instruction
explanation = """Please input the German sentence you want to translate\n (sentence length less than 10)"""
Label(root, text=explanation, font = "Verdana 12").grid(row=2, column=2)

# Add an input for input German sentences
Label(root, text="German", fg="blue").grid(row=3, column=1)
input_widget = Entry(root, width=30, highlightcolor="dark blue")
input_widget.grid(row=4, column=1)

# Add the model translate result
Label(root, text="English", fg="blue").grid(row=3, column=3)
model_output_widget = Text(root, height=1, width=30)
model_output_widget.grid(row=4, column=3)

# Add the google translate result
Label(root, text="Translation Result from Google", fg="blue").grid(row=5, column=3)
google_output_widget = Text(root, height=1, width=30)
google_output_widget.grid(row=6, column=3)

# Add the translate button
Button(root,
       text="Translate",
       fg="green",
       command=output).grid(row=4, column=2)

# Add some examples
Label(root, text="Test Examples:", fg="blue").grid(row=5, column=1)
listbox=Listbox(root, height=4, width=50)
listbox.grid(row=6, column=1)
listbox.insert(1, "Ich habe einen Camion -> I have a truck")
listbox.insert(2, "Mit wem sprichst du -> who are you talking to")
listbox.insert(3, "Ich kann Montage nicht ausstehen -> I hate Mondays")
listbox.insert(4, "Es reut uns das getan zu haben -> we regret doing that")
root.mainloop()


