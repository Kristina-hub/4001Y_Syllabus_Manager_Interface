# 4001Y_Syllabus_Manager_Interface

### Table of Contents
- [About](#About)
- [Examples of Use Cases](#Examples-of-Use-Cases)
- [Installation](#Installation)
- [Kristina](#Kristina)
- [Twitter Sadaf](#Twitter-Sadaf)
- [Facebook Yifei](#Facebook-Yifei)
- [Reddit Yifei](#Reddit-Yifei)
- [Integration](#Integration)


## About
Build a product that focuses on predicting market-moving events before they become widely available on news sites (such as Thomson Reuters, Associate Press) that can be utilized by Citi market traders.

## Examples of Use Cases

1. Considers social media (e.g. Twitter, Facebook) and other types (e.g. Global News, Stock News)
2. Uses fast and slow media types to detect macro-trends so that we can assess the impact on various portfolios
3. Groups events in a trend based on how this will affect the markets and individual asset classes
4. Builds a product that could help us evaluate potential “macro trends” and their impact on stocks

## Installation

```shell script
$ pip install newsapi-python
$ pip install tweepy
$ pip install praw
$ pip install facebook_scraper

```

```shell script
$ pip install flask
$ pip install textblob
$ pip install -U scikit-learn

```

```shell script
$ pip install nltk
$ python
$ import nltk
$ nltk.download('punkt')
$ nltk.download('wordnet')
$ nltk.download('averaged_perceptron_tagger')
$ nltk.download('twitter_samples')
$ nltk.download('stopwords')

```
## Notice
The repository contains large files, please use following command to pull
```
git-lfs pull
```
## Kristina
  - User is prompted to input the name and category of the stock they want to purchase
  - An API gets the most recent news articles related to this stock
  - A classifier was trained with positive tweets and negative tweets to identify positive and negative words
  - The news articles are parsed into tokens and scanned for positive or negative connotations
  - If the majority of words relating to the stock are positive, the output recommends to buy the stock
  - If the majority of words relating to the stock are negative, the output recommends to not buy the stock

## Miranda
  - User is prompted to input the name of the stock they want to purchase
  - An API gets the most recent 1000 tweets related to this stock
  - Used VADER (Valence Aware Dictionary and Sentiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media
  - Cleaned tokens, trained model and performed semantic analysis
  - VADER provides a compound score, it is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1(most extreme negative) and +1 (most extreme positive).
    positive sentiment : (compound score >= 0.05)
    neutral sentiment : (compound score > -0.05) and (compound score < 0.05)
    negative sentiment : (compound score <= -0.05)
  - The tweets are parsed into tokens and scanned for positive or negative connotations
  - If the majority of words relating to the stock are positive, the output recommends to buy the stock
  - If the majority of words relating to the stock are negative, the output recommends to not buy the stock
  
## Winston
  - Used a facebook scraper to collect posts data from public stock related groups
  - Combining Sklearn and NLTK classifieres to imporve the accuracy
  - Classifieres were trained with short movie reviews to identify positive and negative words
  - The trained classifiers are saved as ['\*.pickle'] files under [yifei_facebook/algo_pickle] folder
  - The data collected from facebook are parsed into cleaned tokens and performed senmantic analysis

### Demo
  ![](kristina_global_news/demos/global_news_demo.gif)

### Tools
  - Used NewsAPI https://newsapi.org/ because the free version allows 100 requests per day
