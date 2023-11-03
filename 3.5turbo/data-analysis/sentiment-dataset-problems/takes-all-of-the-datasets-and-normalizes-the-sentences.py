import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def normalize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    normalized_sentence = []
    
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)
    
    for word, pos in nltk.pos_tag(words):
        # Lemmatize the word
        lemma = lemmatizer.lemmatize(word, get_wordnet_pos(pos))
        normalized_sentence.append(lemma.lower())
    
    return ' '.join(normalized_sentence)


def get_wordnet_pos(tag):
    """
    Map POS tag to first character lemmatize() accepts.
    """
    tag = tag[0].upper() + tag[1:].lower()
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV
    }

    return tag_dict.get(tag, wordnet.NOUN)


def normalize_datasets():
    datasets = [
        # list of datasets
        "This is an example sentence.",
        "The quick brown fox jumps over the lazy dog.",
        "Normalize all these sentences."
    ]

    normalized_datasets = []
    for dataset in datasets:
        normalized_sentence = normalize_sentence(dataset)
        normalized_datasets.append(normalized_sentence)

    return normalized_datasets


if __name__ == "__main__":
    normalized_data = normalize_datasets()
    for sentence in normalized_data:
        print(sentence)
