# Deep Bidirectional LSTM Network for Textual Sentiment Analysis

## Project Overview

This project focuses on developing a Deep Bidirectional Long Short-Term Memory (BiLSTM) network for Textual Sentiment Analysis in the context of cryptocurrency-related news and tweets. The goal is to create a model that can accurately analyze sentiment in textual data, particularly in the domain of cryptocurrency, to assist traders and investors in making informed decisions.

![Image](https://kc-v2-config.s3.ap-northeast-1.amazonaws.com/reaper-image/648c2e1df0fbfa000198fa1f_Sentiment%20Analysis%20in%20Crypto%20Trading%201600%20900%20%281%29.png)

## Features

1. **Deep BiLSTM Model:** The core of the project involves the implementation of a deep BiLSTM model using TensorFlow. Bidirectional LSTMs are well-suited for capturing contextual information in sequential data, making them effective for sentiment analysis tasks.

2. **Training Data:** The model is trained using a dataset comprising human-annotated cryptocurrency-related news and tweets. This ensures that the model learns to recognize sentiment nuances specific to the cryptocurrency domain.

3. **Crypto News Scraper:** A custom-built cryptocurrency news scraper is incorporated into the project. This tool fetches the latest news articles related to cryptocurrencies from various sources, providing a continuous stream of relevant data for analysis.

4. **Twitter Scraper:** Additionally, a Twitter scraper is implemented to gather real-time tweets related to various cryptocurrencies. This dynamic data source enables the model to adapt to changing market sentiments.

## Potential Impact

This project has the potential to significantly benefit crypto traders and investors by providing them with a tool to gauge market sentiment accurately. The sentiment analysis model, trained on a diverse dataset, can offer insights into public perceptions and reactions to cryptocurrency-related events. By integrating the news and Twitter scrapers, the system remains up-to-date with the latest information, allowing users to make more informed decisions in their investment journey.

## Usage

1. **Model Training:** The code for training the deep BiLSTM model is provided in the `train_model.py` script. Adjust hyperparameters and paths as needed.

2. **Cryptocurrency News Scraper:** The `google_news_scrap.py` script fetches the latest news articles. Configure sources and other parameters in the script.

3. **Twitter Scraper:** The `tweets_scrap.py` script collects real-time tweets related to cryptocurrencies. Ensure that API keys and access tokens are set up correctly.

4. **Inference:** Use the trained model for sentiment analysis on new data using the `predict_sentiment.py` script.

## Future Enhancements

- Implement a user interface for easy interaction and visualization of sentiment analysis results.
- Explore the use of pre-trained language models for improved performance.
- Expand the dataset to include a broader range of cryptocurrency-related text.

Feel free to contribute, report issues, or suggest improvements to make this tool more robust and beneficial for the cryptocurrency community.

*Note: Always exercise caution and conduct thorough research before making any financial decisions based on the results of sentiment analysis.*



## Installation Steps:

create env

```bash
conda create -n Smart_Finanncial_Assisstant python=3.10 -y
```

activate env
```bash
conda activate Smart_Finanncial_Assisstant
```

create requirements.txt

install requirements.txt
```bash
pip install -r requirements.txt
```
Collect raw data using the .ipynb and .py files inside data_collection folder .
