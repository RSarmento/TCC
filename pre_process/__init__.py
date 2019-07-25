import pre_process.exec as pp
import sentiment_analysis.sentimental as s
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


ementas_acordaos = pp.load()
acordao_pp = pp.clean(ementas_acordaos[0])
ementa_pp = pp.clean(ementas_acordaos[1])
dataset = {'resultado': s.sentiment_analysis(acordao_pp), 'ementa': ementa_pp}
pp.save(dataset)

print('done.')

X_train, X_test, y_train, y_test = train_test_split(ementa_pp, acordao_pp, test_size=0.2, random_state=0)
model = SklearnClassifier(SVC(kernel='linear'))
