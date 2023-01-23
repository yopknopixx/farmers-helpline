# Autonomous Voice-Based Helpline for Farmers' Queries

This repository contains the code for an autonomous voice-based helpline for farmers to address their queries utilizing the Twilio to handle voice calls and implementing natural language processing (NLP) models such as BERT-large, BART-QA, and DPR to understand and respond to farmers' queries. We have built a question answering engine using Haystack and Elasticsearch to retrieve relevant information and answers to farmers' questions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Elasticsearch v8.6.0
- Haystack v1.12.2
- PyTorch v1.7.1
- Transformers v4.6.1
- Django v4.1.5
- Twilio v7.16.0

### Installing

A step by step series of examples that tell you how to get a development env running

1. Clone the repository

```
git clone https://github.com/yopknopixx/farmers-helpline.git
```

2. Install the requirements

```
pip install -r requirements.txt
```

3. Run the Elasticsearch server in a Docker container

```
docker run --name es01 --net elastic -p 9200:9200 -it docker.elastic.co/elasticsearch/elasticsearch:8.6.0
```

4. Run the Django server

```
python manage.py runserver
```

5. Run web scraper to crawl websites and collect relevant data
    
    ```
    document_store = ElasticsearchDocumentStore(host="localhost", username="", password="")
    crawler = Crawler(
        urls=["https://en.wikipedia.org/wiki/Agriculture"],   # Websites to crawl
        crawler_depth=1,    # How many links to follow
        output_dir="crawled_files",
    )
    ```

6.Add the call handler to Twilio

```
twilio phone-numbers:update "+91XXXXXXXXXX" --voice-url="https://your_public_url/callTo/0/en-IN/"
```

## Usage

There are two ways to use the application:

### 1. Using the web interface

1. Go to the web interface at https://your_public_url/
2. Enter your query in the search bar
3. Click on the search button
4. The answer to your query will be displayed

### 2. Using the voice interface

1. Call the number +91XXXXXXXXXX
2. You will be asked to select your language. Speak the language you want to use.
3. You will be asked to state your query. Speak your query in the selected language.
4. The answer to your query will be played back to you.
