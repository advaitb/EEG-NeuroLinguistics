import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

C = 1
kernel = 'rbf'
iterations = 1000
m_accuracysvm = []
m_accuracyrf = []
m_accuracyab = []
X = pd.read_csv('inputval_dec.txt',sep=',',header = None)



X[18]= 0
X.loc[0:66,18] = 1


#print X

y = X[18].copy()

#print y

X.drop(X.columns[[18]],axis = 1,inplace =True)

pca = PCA()
pca.fit(X)
X = pca.transform(X)

X = normalize(X)


#X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=7)

#rf = RandomForestClassifier(n_estimators = 100)
#ab = AdaBoostClassifier(n_estimators = 100)
#svm = SVC(C,kernel)
gbc = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
#gbc.fit(X_train, y_train)

#rf.predict(X_test)

#rf.score(X_test,y_test)
#print "RF accuracy: ",rf.score(X_test,y_test)
#print "AdaB accuracy: ",ab.score(X_test,y_test)

#for _ in range(iterations):
#svm.fit(X_train,y_train)
#rf.fit(X_train,y_train)
#ab.fit(X_train,y_train)
#score = svm.score(X_test,y_test)
scores = cross_val_score(gbc, X, y, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

'''
predictions = rf.predict(X)

# round predictions
rounded = [round(x) for x in predictions]
print rounded
'''
#	m_accuracyab.append(svm.score(X_test,y_test))
#	m_accuracyrf.append(rf.score(X_test,y_test))
#	m_accuracyab.append(ab.score(X_test,y_test))
	
#print "Accuracies:"	
#print "SVM:", np.mean(m_accuracysvm)
#print "RF: ", np.mean(m_accuracyrf)
#print "ADAB: ", np.mean(m_accuracyab)
