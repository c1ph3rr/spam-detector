import os, random
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify
import pickle

spam_path = 'spam/'
ham_path = 'ham/'

def create_list(path):
    file_list = os.listdir(path)
    lst = []
    for i in file_list:
        f = open(path + i, 'r', encoding="utf8", errors='ignore')
        lst.append(f.read())
    f.close()
    return lst

spam = create_list(spam_path)
ham = create_list(ham_path)

spam_tuple = []
for email in spam:
    s = tuple((email, 'spam'))
    spam_tuple.append(s)

ham_tuple = []
for email in ham:
    s = tuple((email, 'ham'))
    ham_tuple.append(s)

all_emails = spam_tuple + ham_tuple
random.shuffle(all_emails)

def process_email(sentence):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(sentence)
    processed_email = []
    for word in tokens:
        word = word.lower()
        lemma = lemmatizer.lemmatize(word)
        processed_email.append(lemma)
    return processed_email

stoplist = stopwords.words('english')

def create_features(text):
    return {word: True for word in process_email(text) if not word in stoplist}

# all_features_labels = []
# for email, label in all_emails:
#     all_features_labels.append((create_features(email), label))
# print('length of dataset = ', len(all_features_labels))

# train_size = int(len(all_features_labels) * 0.8)
# train_set = all_features_labels[:train_size]
# test_set = all_features_labels[train_size:]
 
# clf = NaiveBayesClassifier.train(train_set)
# print('accuracy on train set = ' + str(classify.accuracy(clf, train_set)))
# print('accuracy on test set = ' + str(classify.accuracy(clf, test_set)))
# clf.show_most_informative_features(20)
 
# filename = 'model.pkl'
# with open(filename, 'wb') as f:
#     pickle.dump(clf, f)