# se390_mandarin_tokenizer
SE390 Internal Project Tokenizer

## Setup
Download the zip file from https://www.dropbox.com/s/4ntmofahfb4d19p/resources.zip?dl=0 and extract it into a directory called "resources" in the root of this project

Ensure that you have python 2.7.x installed. Do the following in a shell:
```
pip install -r requirements.txt
source setup.sh
```

## Run
Do the following in a shell:
```
cd src
python segmenter.py
```

Enter lines of chinese characters that you wish to have segmented. To finish inputting text, enter a blank line.
