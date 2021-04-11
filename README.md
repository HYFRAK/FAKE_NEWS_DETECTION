# Fake News Detection 
***
An automated fake news detection bot that can perform the following
tasks: <br />
● Check the news source's authenticity by providing fake news% <br />
● Check whether the title of the news is accurate. <br />
● Check whether the text/content of the news is accurate.
***
## Getting Started
***
Requirements :
requests==2.23.0
numpy==1.19.5
nltk==3.2.5
pandas==1.1.5
scikit_learn==0.24.1

Clone the repo using :
>%git clone https://github.com/HYFRAK/FAKE_NEWS_DETECTION.git

To install requirements, navigate to the folder and use (in terminal/command line) :
>%pip install -r requirements.txt

Download the Kaggle dataset https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset , and move the csv files to the FAKE_NEWS_DETECTION folder.
***
## Usage
***
#### Check the news source's authenticity:
>%!python3  detect.py -s --source_site-- 
#### Check whether the title of the news is accurate.
>%!python3  detect.py -t --title--
#### Check whether the text of the news is accurate.
>%!python3  detect.py -r --text (Upto 512 char.)--
#### Two or more arguments can also be passed simultaneously:
>%!python3  detect.py -t --title-- -r --text (Upto 512 char.)-- -s --source_site-- 
#### Display Help
>%!python3  detect.py -h
***

