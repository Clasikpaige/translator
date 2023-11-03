# preprocess.py
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def preprocess_text(text):
    tokens = word_tokenize(text)
    # Additional preprocessing steps can be added here
    return " ".join(tokens)

urhobo_sentences = []
english_sentences = []

# Load sentences from urhobo.txt and english.txt, preprocess, and store in urhobo_sentences and english_sentences

with open('data/urhobo.txt', 'r', encoding='utf-8') as urhobo_file:
    urhobo_sentences = [preprocess_text(line) for line in urhobo_file.readlines()]

with open('data/english.txt', 'r', encoding='utf-8') as english_file:
    english_sentences = [preprocess_text(line) for line in english_file.readlines()]

# Save preprocessed data
with open('data/preprocessed_urhobo.txt', 'w', encoding='utf-8') as urhobo_output_file:
    urhobo_output_file.write("\n".join(urhobo_sentences))

with open('data/preprocessed_english.txt', 'w', encoding='utf-8') as english_output_file:
    english_output_file.write("\n".join(english_sentences))
