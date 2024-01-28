import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
import time
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, matthews_corrcoef, roc_auc_score
import joblib


# will probably need to change this path...
df = pd.read_csv("../archive/KAGGLE/DATASET-balanced.csv")
# /Users/eamon/Desktop/archive/KAGGLE

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

#print(X.head(10))
#print(y.head(10))

lb = preprocessing.LabelBinarizer()
lb.fit(y)
y = lb.transform(y)
y = y.ravel()
#print(y)

model = RandomForestClassifier(n_estimators=50, random_state=1)

kf = KFold(n_splits=5,  shuffle=True, random_state=1)

print(model)
#print("KFold splits: " + str(kf.get_n_splits(X)))



acc_score = []
prec_score = []
rec_score = []
f1s = []
MCCs = []
ROCareas = []

#print(type(X), X.iloc[0], type(X.iloc[0]))
start = time.time()
for train_index , test_index in kf.split(X):
    X_train , X_test = X.iloc[train_index,:],X.iloc[test_index,:]
    y_train , y_test = y[train_index] , y[test_index]
    
    
    model.fit(X_train,y_train)
    pred_values = model.predict(X_test)
    print(type(X_test))
     
    acc = accuracy_score(pred_values , y_test)
    acc_score.append(acc)

    prec = precision_score(y_test , pred_values, average="binary", pos_label=1)
    prec_score.append(prec)
    
    rec = recall_score(y_test , pred_values, average="binary", pos_label=1)
    rec_score.append(rec)
    
    f1 = f1_score(y_test , pred_values, average="binary", pos_label=1)
    f1s.append(f1)
    
    mcc = matthews_corrcoef(y_test , pred_values)
    MCCs.append(mcc)   
    
    roc = roc_auc_score(y_test , pred_values)
    ROCareas.append(roc)
    
end = time.time()
timeTaken = (end - start)
print("Model trained in: " + str( round(timeTaken, 2) ) + " seconds.")

print("Mean results and (std.):\n")
print("Accuracy: " + str( round(np.mean(acc_score)*100, 3) ) + "% (" + str( round(np.std(acc_score)*100, 3) ) + ")\n")
print("Precision: " + str( round(np.mean(prec_score), 3) ) + " (" + str( round(np.std(prec_score), 3) ) + ")")
print("Recall: " + str( round(np.mean(rec_score), 3) ) + " (" + str( round(np.std(rec_score), 3) ) + ")")
print("F1-Score: " + str( round(np.mean(f1s), 3) ) + " (" + str( round(np.std(f1s), 3) ) + ")")
print("MCC: " + str( round(np.mean(MCCs), 3) ) + " (" + str( round(np.std(MCCs), 3) ) + ")")
print("ROC AUC: " + str( round(np.mean(ROCareas), 3) ) + " (" + str( round(np.std(ROCareas), 3) ) + ")")

joblib.dump(model, 'audio_deepfake_model.joblib')

print(type(X.iloc[0:2]))
model.predict(X.iloc[0:2])
