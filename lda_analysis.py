import os
import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from gensim import corpora, models
import pyLDAvis.gensim_models

# Load NLTK's English stop-words list
nltk.download('punkt')
nltk.download("stopwords")
stop_words = stopwords.words('english')

# Specify the path to your directory
dir_path = "/content/sample_data/"
file_names = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# Remove file extensions, punctuation, and special characters from file names
file_names_cleaned = [re.sub(r'\.[^.]*$', '', name) for name in file_names]  # Remove file extensions
file_names_cleaned = [re.sub(r'[_-]+', ' ', name) for name in file_names_cleaned]  # Replace underscores and dashes with spaces
file_names_cleaned = [re.sub(r'\W+', ' ', name) for name in file_names_cleaned]  # Remove non-word characters

# Tokenize the cleaned file names and remove stop words
file_names_words = [nltk.word_tokenize(name) for name in file_names_cleaned]
file_names_words = [[word for word in name if word not in stop_words] for name in file_names_words]

# Create a dictionary representation of the documents
dictionary = corpora.Dictionary(file_names_words)

# Convert the list of documents (corpus) into Document-Term Matrix using dictionary prepared above
doc_term_matrix = [dictionary.doc2bow(name) for name in file_names_words]

# Define the number of topics you want
num_topics = 5

# Create the object for LDA model using gensim library
Lda = models.LdaMulticore

# Run and train LDA model on the document term matrix
ldamodel = Lda(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=50)

# Get the dominant topic for each document
dominant_topics = [max(ldamodel[doc], key=lambda x: x[1])[0] for doc in doc_term_matrix]

# Create a dictionary of topics and their top words
topic_words = {i: [word_prob[0] for word_prob in ldamodel.show_topic(i, topn=10)] for i in range(num_topics)}

# Create a DataFrame with the file paths, file names, their dominant topic, and the top words for the dominant topic
df = pd.DataFrame({
    'file_path': dir_path,
    'file_name': file_names,
    'dominant_topic': dominant_topics,
    'top_words': [topic_words[topic] for topic in dominant_topics]
})

# Save the DataFrame to a CSV file
df.to_csv('file_topics.csv', index=False)

# Visualization of topics
vis = pyLDAvis.gensim_models.prepare(ldamodel, doc_term_matrix, dictionary, n_jobs=1)
pyLDAvis.save_html(vis, 'lda.html')


# print words for each topic
for idx, topic in ldamodel.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))
