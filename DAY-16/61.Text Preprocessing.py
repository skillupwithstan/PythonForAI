import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Download required NLTK resources
#nltk.download('punkt_tab') 
#nltk.download('stopwords')
#nltk.download('wordnet')

text = "The running data scientists are solving complex NLP problems!"

# 1. Lowercasing
text_lower = text.lower()

# 2. Tokenization
tokens = word_tokenize(text_lower)
print(tokens)

# 3. Remove Punctuation and Stop Words
stop_words = set(stopwords.words('english'))
print(stop_words)

cleaned_tokens = [
    word for word in tokens 
    if word not in stop_words and word not in string.punctuation
]

'''
cleaned_tokens = []
for word in tokens:
    if(word not in stop_words):
        cleaned_tokens = cleaned_tokens + word
'''

print(cleaned_tokens)

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
preprocessed_text = [lemmatizer.lemmatize(word) for word in cleaned_tokens]

print("Original Text:", text)
print("Processed Tokens:", preprocessed_text)
# Output: ['running', 'data', 'scientist', 'solving', 'complex', 'nlp', 'problem']