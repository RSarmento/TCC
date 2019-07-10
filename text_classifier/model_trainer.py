# training word2vec on 3 sentences
import gensim
from gensim.corpora import dictionary


def trainer(corpus):
    word_count = word_counter(corpus)
    model = gensim.models.Word2Vec(corpus, min_count=1, size=word_count, workers=4)
    return model


def word_counter(corpus):
    # creates a set with every words from the corpus
    unique = set()
    for i in corpus:
        for j in i:
            unique.add(j)

    return len(unique)


def lda_model(corpus):
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]
    lda = gensim.models.ldamodel.LdaModel
    return lda(doc_term_matrix, num_topics=3, id2word=dictionary, passes=50)

