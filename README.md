# German-English-Machine-Translator

## Intro
This repo is created for TAMU 2019 Spring CSCE 636 final project. During this project, a German to English machine translator is implemented. Machine translation belongs to sequence processing problem. Therefore, an encoder-decoder model is build with embeddings and LSTM layers. 

Dataset used in this project can be found here: [German – English deu-eng.zip](http://www.manythings.org/anki/deu-eng.zip). In the project, the first 50,000 phrase pairs were used. After shuffling, the first 48,000 were used as training set and the left 2,000 were used as test set. Three models were trianed during this project: baseline, bidirectionan LSTM, attention. Finally, the best model, <b>the bidirectional LSTM</b>, achieved a training accuracy of 94% and validation accuracy of 76%. 

## How to Run the Code
### Training
Program dealing with data-preprocessing and training is in the `WF_CSCE636_Project.ipynb` file. All the three models were included in it. (<i>Note: To run the attention model training, `attention_decoder.py` is required.</i>)

### GUI
You can run the following command to start the GUI (Python 3 required):
```
python3 mt_gui.py
```
Since the bidirectional LSTM model(`bi_model.h5`) performs the best, the GUI only loaded this model. In addition, `eng_tokenizer.pickle` and `ger_tokenizer.pickle` are required to provide tokens.

## Sample Data
For testing purpose, some sample data is uploaded in the `sample_data.txt`. The first column includes German sentences and the second column is corresponding English translation.

## Video Demo
A video demo of the machine translation model can be found here: [TAMU CSCE 636 GUI demo](https://youtu.be/utwoyIkFqKs).





