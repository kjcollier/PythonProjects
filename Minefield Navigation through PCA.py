# A previous homework assigment that really helped me understand how machine
# learning can be used to solve problems by probability.The goal is to use PCA
# to safely navigate through a minefield, and then use some analysis tools to
# analyze the results.

# Importing files
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score as acsc
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split as tts
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
from warnings import filterwarnings
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Suppressing warnings
filterwarnings('ignore')

# Using pandas to read sonar_all_data_2.csv
df_mines = pd.read_csv('sonar_all_data_2.csv',header=None)

# Using the last column as y-values, and the rest as x-values
x = df_mines.iloc[:,:(-2)]
y = df_mines.iloc[:,-1]

# Splitting train and test
x_train_non_std, x_test_non_std, y_train, y_test = tts(x,y,test_size=0.3,random_state=0)

# Standardizing
stdsc = StandardScaler()
x_train = stdsc.fit_transform(x_train_non_std)
x_test = stdsc.transform(x_test_non_std)

# Applying PCA, learning method, checking accuracy, and combining; but using a 
# for loop to test numbers 1-60 for n_components.
k = 1 # The counter
y_pred_max_acc = 0 # A variable to save the predicted values that provide the 
                   # max accuracy
acc_max = 0 # A variable to save the max accuracy value
y_comb_max_acc = 0 # A variable to save max y_comb value at max accuracy
best_n = 0 # A variable to save n-component that works best
acc_list = [] # A list to save each accuracy value
for k in range(1,61):
    # Applying PCA
    pca = PCA(n_components=k)
    x_train_pca = pca.fit_transform(x_train)
    x_test_pca = pca.transform(x_test)
    
    # MLPClassifier for learning method
    mlpc = MLPClassifier(hidden_layer_sizes=(100),activation='logistic',max_iter=2000,alpha=0.00001,solver='adam',tol=0.0001)
    mlpc.fit(x_train_pca,y_train)
    
    # Predicting y_values
    y_pred = mlpc.predict(x_test_pca)
    
    # Checking accuracy
    print("\nRun #" + str(k))
    print("Misclassified samples: %d" % (y_test != y_pred).sum())
    acc = acsc(y_test, y_pred)
    print("Accuracy: %.2f" % acc)
    
    # Combining train and test
    x_comb_pca = np.vstack((x_train_pca, x_test_pca))
    y_comb = np.hstack((y_train, y_test))
    
    # Predicting combined y-values
    y_comb_pred = mlpc.predict(x_comb_pca)
    
    # Checking combined accuracy
    print("Misclassified combined samples: %d" % (y_comb != y_comb_pred).sum())
    print("Combined Accuracy: %.2f" % acsc(y_comb, y_comb_pred))
    
    # Adding accuracy values to accuracy list
    acc_list.append(acc)
    
    # Setting max accuracy and max y_pred values
    if acc > acc_max:
        acc_max = acc
        y_pred_max_acc = y_pred
        y_comb_max_acc = y_comb
        best_n = k
    
# Printing maximum accuracy value
print("\nMaxumum Accuracy Achieved: %.2f" % acc_max)
print("Best n-component:", best_n)

# Plotting
x_vals = range(1,61)
plt.plot(x_vals,acc_list)
plt.xlabel("N-values in PCA")
plt.ylabel("Accuracy")
plt.show()

# Creating a confusion matrix and printing
cmat = confusion_matrix(y_test,y_pred_max_acc)
print("Printing a heatmap of the confusion matrix: ")
plt.figure(figsize=(2,2))
sns.heatmap(cmat, annot=True)