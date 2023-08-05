import os
import re
import nltk
import pandas as pd
from tqdm import tqdm
from nltk.corpus import stopwords
from gensim import corpora, models
import pyLDAvis.gensim_models

def get_directory_path():
    print("📂 Welcome to the LDA Analysis Tool!")
    print("This tool analyzes file names in a directory and categorizes them into topics.")
    print("It then saves a CSV file containing the file's path, name, dominant topic, and the top words for that topic.")
    print("Lastly, a visualization (lda.html) of the topics is generated.")
    print("\nLet's begin...\n")

    while True:
        dir_path = input("🔍 Please enter the full path to your directory: ").strip()
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            return dir_path
        else:
            print("❌ Directory not found. Please enter a valid directory path.")

def get_num_topics():
    while True:
        try:
            num_topics = int(input("\n🤔 How many topics would you like to extract from the file names? "))
            if num_topics > 0:
                return num_topics
            else:
                print("❌ Please enter a positive integer value for the number of topics.")
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value for the number of topics.")


def train_lda_model(doc_term_matrix, num_topics, dictionary):
    try:
        # Attempting LdaMulticore
        Lda = models.LdaMulticore
        ldamodel = Lda(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=50)
        print("✅ Using multicore LDA...")
    except Exception as e:
        print(f"❌ Multicore LDA failed due to: {str(e)}")
        print("⏳ Falling back to single core LDA...")
        Lda = models.LdaModel
        ldamodel = Lda(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=50)
    return ldamodel



def main():
    dir_path = get_directory_path()
    num_topics = get_num_topics()

    print("\n⏳ Setting up necessary libraries and data...")
    nltk.download('punkt', quiet=True)
    nltk.download("stopwords", quiet=True)
    stop_words = stopwords.words('english')

    print("⏳ Reading and processing file names...")
    file_names = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

    # Processing file names...
    file_names_cleaned = [re.sub(r'\.[^.]*$', '', name) for name in file_names]
    file_names_cleaned = [re.sub(r'[_-]+', ' ', name) for name in file_names_cleaned]
    file_names_cleaned = [re.sub(r'\W+', ' ', name) for name in file_names_cleaned]

    file_names_words = [nltk.word_tokenize(name) for name in file_names_cleaned]
    file_names_words = [[word for word in name if word not in stop_words] for name in file_names_words]

    dictionary = corpora.Dictionary(file_names_words)
    doc_term_matrix = [dictionary.doc2bow(name) for name in file_names_words]
    
    
    
    #training
    print("\n⏳ Running LDA analysis... (this may take some time)")
    ldamodel = train_lda_model(doc_term_matrix, num_topics, dictionary)


    
    
    
    dominant_topics = [max(ldamodel[doc], key=lambda x: x[1])[0] for doc in doc_term_matrix]
    topic_words = {i: [word_prob[0] for word_prob in ldamodel.show_topic(i, topn=10)] for i in range(num_topics)}

    df = pd.DataFrame({
        'file_path': dir_path,
        'file_name': file_names,
        'dominant_topic': dominant_topics,
        'top_words': [topic_words[topic] for topic in dominant_topics]
    })

    df.to_csv('file_topics.csv', index=False)
    vis = pyLDAvis.gensim_models.prepare(ldamodel, doc_term_matrix, dictionary, n_jobs=1)
    pyLDAvis.save_html(vis, 'lda.html')

    for idx, topic in ldamodel.print_topics(-1):
        print('Topic: {} \nWords: {}'.format(idx, topic))

    print("\n🎉 Analysis complete! Check the generated lda.html for a visualization of the topics.")
    print("📄 A CSV file (file_topics.csv) has also been created with the analysis results.")

if __name__ == "__main__":
    main()
