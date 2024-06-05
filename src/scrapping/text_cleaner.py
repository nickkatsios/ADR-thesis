import os
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from markdown2 import markdown
from bs4 import BeautifulSoup
from collections import Counter
import random

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Path to the ADR directory
adr_directory = "../../data/ADRs-Updated"

def clean_text(markdown_content):
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

    # remove common terms
    common_terms = ["context", "decision", "status", "consequences",
                     "motivation", "options", "option", "alternatives", "alternative"]
    
    tokens = [word for word in tokens if word not in common_terms]

    return ' '.join(tokens), tokens


# # pick a random file to test the function
# file_name = random.choice(os.listdir(adr_directory))
# file_path = os.path.join(adr_directory, file_name)
# with open(file_path, 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.replace("\n", " "))
#     preprocessed_text, num_tokens = clean_text(text)
#     print("---------------------------------------------------------------------------------\n\n\n\n")
#     print(preprocessed_text)

all_words = []
for file_name in os.listdir(adr_directory):
    file_path = os.path.join(adr_directory, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        preprocessed_text, words = clean_text(text)
        all_words.extend(words)

word_freq = Counter(all_words)
print(word_freq.most_common(50))


            