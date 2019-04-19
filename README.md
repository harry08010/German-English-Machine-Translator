# German-English-Machine-Translator

**Update 04/19/2019: trained models for this project were uploaded to Google Drive, you can access them from here:

[Baseline_Model](https://drive.google.com/open?id=1UHSbb6b9t2wUekWlv6yuz_Wau-VhPguB)

[Bidirectional_LSTM_Model](https://drive.google.com/open?id=1RSTd1J3Cd0w6dPIoTThQI0NvjRgsX4gT)

[Attention_Model](https://drive.google.com/open?id=1nZgFew911WI0B88cHk6dyr7QcqBaGICI)

## Intro
This repo is created for TAMU 2019 Spring CSCE 636 final project. During this project, a German to English machine translator is implemented. Machine translation belongs to sequence processing problem. Therefore, an encoder-decoder model is build with embeddings and LSTM layers. 

Dataset used in this project can be found here: [German – English deu-eng.zip](http://www.manythings.org/anki/deu-eng.zip). In the project, the first 90,000 phrase pairs were used. After shuffling, the first 75,000 were used as training set and the left 15,000 were used as validation set and test set, 7,500 for each. Three models were trianed during this project: baseline, bidirectionan LSTM, attention. Finally, the best model, <b>the bidirectional LSTM</b>, achieved a training accuracy of 86% and validation accuracy of 77%. 

## How to Run the Code
### Training
Program dealing with data-preprocessing and training is in the `WF_CSCE636_Project.ipynb` file. All the three models were included in it. (<i>Note: To run the attention model training, `attention_decoder.py` is required.</i>)

### GUI
You can run the following command to start the GUI (Python 3 required):
```
python3 mt_gui.py
```
Since the bidirectional LSTM model(`bi_model.h5`) performs the best, the GUI only loaded this model. In addition, `eng_tokenizer.pickle` and `ger_tokenizer.pickle` are required to provide tokens.

```
Note: If you want to run with the attention model (`attentnion_model.h5`), please uncomment line 60 in the `mt_gui.py`, and comment out line 59. 
```

## Sample Data
For testing purpose, some sample data is uploaded in the `sample_data.txt`. The first column includes English sentences and the second column is corresponding German sentence.

## Video Demo
A video demo of the machine translation model can be found here: [TAMU CSCE 636 GUI demo](https://youtu.be/0kFv9De3y0s).





