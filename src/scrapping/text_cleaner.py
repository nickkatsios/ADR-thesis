import os
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from markdown2 import markdown
from bs4 import BeautifulSoup

# Base cleaner for text
def clean_text(markdown_content):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    # these produce good results
    # if we exclude more words, the results are not as good
    unwanted_terms = ["context", "decision", "status", "consequences", "consequences", "michael"
                  "motivation", "options", "option", "alternatives", "need",
                  "alternative", "nygard", "nygards", "use", "using" , "used", "accepted", "date"]
    # Convert Markdown to HTML
    html_content = markdown(markdown_content)
    # Parse HTML to text
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    # Remove non-alphabetic characters and lower the case
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    # Tokenize, remove stop words, and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]
    # remove words with less than 3 characters
    tokens = [word for word in tokens if len(word) > 2]
    # remove common terms and words that are are present in every document and do not provide any information
    tokens = [word for word in tokens if word not in unwanted_terms]
    return ' '.join(tokens)

# Less strict cleaning for experimentation
def clean_text2(markdown_content):
    pass
    # TODO: modify this function to clean the text in a less strict way


def read_and_clean_adrs(adr_directory, save):
    cleaned_texts = []
    # Read, preprocess, and encode each ADR file
    total_files = len(os.listdir(adr_directory))
    for file_name in os.listdir(adr_directory):
        if file_name.endswith('.md'):
            file_path = os.path.join(adr_directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                preprocessed_text = clean_text(text)
                cleaned_texts.append(preprocessed_text)
                if save:
                    # save the preprocessed text to a file with the same filename in another directory
                    with open(f"../../data/ADRs-Cleaned/{file_name}", 'w') as preprocessed_file:
                        preprocessed_file.write(preprocessed_text)
    return cleaned_texts


            