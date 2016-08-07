

#1.corpusを構築
from gensim import corpora, models, similarities
from sklearn.datasets import fetch_20newsgroups
from collections import defaultdict
import nltk
import re


def create_dictionary_and_corpus(documents):
    texts = [tokens(document) for document in documents]

    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    # 全ドキュメントを横断して出現回数が1のtokenを捨てる 
    texts = [[token for token in text if frequency[token] > 1] for text in texts]

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    return dictionary, corpus

def tokens(document):
    symbols = ["'", '"', '`', '.', ',', '-', '!', '?', ':', ';', '(', ')', '*', '--', '\\']
    stopwords = nltk.corpus.stopwords.words('english')

    # ストップワードと記号を捨てる
    tokens = [re.sub(r'[,\.]$', '', word) for word in document.lower().split() if word not in stopwords + symbols]

    return tokens

def create_model_and_index(corpus):
    tfidf = models.TfidfModel(corpus)
    index = similarities.MatrixSimilarity(tfidf[corpus])
    return tfidf, index


# 20 newsgroups のデータをダウンロード
newsgroups_train = fetch_20newsgroups(subset='train',remove=('headers', 'footers', 'quotes'))

# 最初の100件を使って、辞書とcorpusを作成する
dictionary, corpus = create_dictionary_and_corpus(newsgroups_train.data[0:100])

#tfidfモデルとインデックス作成
model, index = create_model_and_index(corpus)

# System Evaluation
bow = dictionary.doc2bow(tokens(newsgroups_train.data[0]))
vec_tfidf = model[bow]
sims = index[vec_tfidf] 

sims = sorted(enumerate(sims), key=lambda item: item[1], reverse=True)

for i in range(3):
    doc_id     = sims[i][0]
    simirarity = round(sims[i][1] * 100, 0)
    print(doc_id, simirarity)
