# Final Project: Article Summarizer

Complete the tasks in the Python Notebook in this repository.
Make sure to add and push the pkl or text file of your scraped html (this is specified in the notebook)

## Rubric
* (Question 1) Article html stored in separate file that is committed and pushed: 1 pt
* (Question 2) Polarity score printed with an appropriate label: 1 pt
* (Question 2) Number of sentences printed: 1 pt
* (Question 3) Correct (or equivalent in the case of multiple tokens with same frequency) tokens printed: 1 pt
* (Question 4) Correct (or equivalent in the case of multiple lemmas with same frequency) lemmas printed: 1 pt
* (Question 5) Histogram shown with appropriate labelling: 1 pt
* (Question 6) Histogram shown with appropriate labelling: 1 pt
* (Question 7) Cutoff score seems appropriate given histograms: 2 pts (1/score)
* (Question 8) Summary contains a shortened version of the article (less than half the number of sentences): 1 pt
* (Question 8) Summary sentences are in the same order as they appeared in the original article: 1 pt
* (Question 9) Polarity score printed with an appropriate label: 1 pt
* (Question 9) Number of sentences printed: 1 pt
* (Question 10) Summary contains a shortened version of the article (less than half the number of sentences): 1 pt
* (Question 10) Summary sentences are in the same order as they appeared in the original article: 1 pt
* (Question 11) Polarity score printed with an appropriate label: 1 pt
* (Question 11) Number of sentences printed: 1 pt
* (Question 12) Thoughtful answer based on reported polarity scores: 1 pt
* (Question 13) Thoughtful answer based on summaries: 1 pt

## Setup Notes
1. Setup a virtual environment:  
`py -m venv .venv`  
2. Activate the virtual environment:  
`.venv\Scripts\activate`  
3. Update pip & install requirements
`py -m pip install --upgrade pip setuptools wheel`  
`py -m pip install -r requirements.txt`
4. Set correct interpreter & kernel
5. Install textblob requirements:  `python -m textblob.download_corpora`
6. `python -m spacy download en_core_web_sm` to install english language model

## Key Features

*   **Multi-Page Web Scraping**: Utilizes `requests` and `BeautifulSoup` to navigate a paginated product collection and gather data.
*   **Sentiment Analysis**: Employs `TextBlob` to calculate polarity scores for text content.
*   **Linguistic Analysis**: Uses `spaCy` for advanced text processing, including tokenization, lemmatization, and stop-word removal.
*   **Frequency Distribution**: Determines the most common tokens and lemmas to identify key themes.
*   **Data Visualization**: Generates histograms with `matplotlib` to visualize the distribution of sentiment scores.
*   **Rule-Based Summarization**: Creates extractive summaries by filtering content based on a sentiment polarity threshold.

---

## Project Components

### 1. Web Scraper (`nick-kuchar-scraper-multipage.py`)

This script is responsible for acquiring the raw data for analysis.

*   **Functionality**: It systematically scrapes all product titles and descriptions from the "Oahu" collection on nickkuchar.com.
*   **Process**:
    1.  It iterates through all 8 pages of the product collection.
    2.  On each page, it extracts the URL for every product.
    3.  It then visits each product URL to scrape the full product title and description.
    4.  All scraped titles and descriptions are compiled and saved into a single, clean HTML file: `nick-kuchar_titles_and_descriptions.html`. This file serves as the static data source for the NLP notebook.

### 2. NLP Analysis & Summarization (`article-summarizer.ipynb`)

This Jupyter Notebook contains the core text analysis and summarization logic.

*   **Objective**: To analyze the sentiment of the scraped product descriptions and generate a concise summary of the most positive content.
*   **Workflow**:
    1.  **Data Loading**: Reads and parses the text from `nick-kuchar_titles_and_descriptions.html`.
    2.  **Initial Analysis**: Performs an initial sentiment analysis on the entire text corpus to get a baseline polarity score and sentence count.
    3.  **Token & Lemma Frequency**: Identifies the 5 most frequent tokens and lemmas (excluding stop words and punctuation) to understand the key terms.
    4.  **Sentiment Distribution**: Calculates the sentiment score for each individual product description and plots a histogram to visualize the distribution. This step is crucial for determining an appropriate sentiment "cutoff" score for the summary.
    5.  **Summary Generation**: Creates two distinct summaries by iterating through each description:
        *   **Token-Based Summary**: Adds a description to the summary if its raw token-based sentiment score is above the defined cutoff.
        *   **Lemma-Based Summary**: Adds a description if the sentiment score of its *lemmatized* text is above the cutoff.
    6.  **Final Evaluation**: Calculates and prints the final polarity score and sentence count for each generated summary, allowing for a comparison of the two methods.

---

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # For Windows
    python -m venv .venv
    .venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    python -m textblob.download_corpora
    python -m spacy download en_core_web_sm
    ```

## How to Run

1.  Ensure all dependencies are installed by following the setup instructions.
2.  Run the web scraper to generate the data file:
    ```bash
    python nick-kuchar-scraper-multipage.py
    ```
3.  Launch Jupyter Notebook or JupyterLab:
    ```bash
    jupyter notebook
    ```
4.  Open `article-summarizer.ipynb` and run the cells in order to see the full analysis and summary generation.
   

## Licenses
Code and instructions in this repository are provided for educational purposes only. 
Users are responsible for verifying and complying with all third-party licenses before using any code, data, or resources referenced herein.