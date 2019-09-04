# COSC189:Data Mining

This is the final project of COSC189 - Text Analysis on Game Reviews

Author: Mengdan Zhu, Weiyi Wu, Boran Lu, Huaibin Ge

## Data
### Data Scraping

The data was mainly scraped from [Steam Community](https://steamcommunity.com/app) and [Steam Database](https://steamdb.info/graph/).

### Data Normalization and Data Tokenization
* Conducted text normalization such as adding stop words, porter stemmer and removing punctuations and digits using regular expressions
* Tokenized and vectorized those words to sparse matrix

## Methods
### Sentiment Classification(1-gram, 2-gram and 3-gram language models)
* Logistic Regression
* Random Forest 
* Support Vector Machine(SVM)
* Naive Bayes

### Predicting Game Scores(Metacritic Scores)
* Linear Model
* Support Vector Regression(SVR)
* Random Forest Regression

### Topic Modelling
* Latent Dirichlet Allocation(LDA)



More info in the [Report](https://github.com/mengdanzhu/COSC189_Data_Mining/blob/master/Final%20Report.pdf).
