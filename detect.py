import pickle
import spam

with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)

stat = True
while stat:
    user_input = input('input \n')
    if user_input == 'exit':
        stat = False
    else:
        features = spam.create_features(user_input)
        #print(features)
        print(clf.classify(features))