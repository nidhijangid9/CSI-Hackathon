import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def WeightGain(e1, e3, e4):
    print(" Age: %s\n Weight%s\n Height%s\n" % (e1.get(), e3.get(), e4.get()))

    # Read data from CSV file
    data = pd.read_csv('input.csv')

    # Extract relevant columns from the data
    Breakfastdata = data['Breakfast'].to_numpy()
    Lunchdata = data['Lunch'].to_numpy()
    Dinnerdata = data['Dinner'].to_numpy()
    Food_itemsdata = data['Food_items']

    # Initialize lists to store food items for each meal
    breakfastfoodseparated = []
    Lunchfoodseparated = []
    Dinnerfoodseparated = []

    # Initialize lists to store indexes of food items for each meal
    breakfastfoodseparatedID = []
    LunchfoodseparatedID = []
    DinnerfoodseparatedID = []

    # Loop through the data to separate food items for each meal
    for i in range(len(Breakfastdata)):
        if Breakfastdata[i] == 1:
            breakfastfoodseparated.append(Food_itemsdata[i])
            breakfastfoodseparatedID.append(i)
        if Lunchdata[i] == 1:
            Lunchfoodseparated.append(Food_itemsdata[i])
            LunchfoodseparatedID.append(i)
        if Dinnerdata[i] == 1:
            Dinnerfoodseparated.append(Food_itemsdata[i])
            DinnerfoodseparatedID.append(i)

    # Convert DataFrame to NumPy array for further processing
    LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID].T.to_numpy()
    breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID].T.to_numpy()
    DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID].T.to_numpy()

    # Extract age from input
    age = int(e1.get())

    # Extract weight and height from input
    weight = float(e3.get())
    height = float(e4.get())

    # Determine age category based on age
    agecl = int(age / 20)

    # K-Means clustering for lunch food items
    Datacalorie = LunchfoodseparatedIDdata[1:, 1:]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    lnchlbl = kmeans.labels_

    # K-Means clustering for breakfast food items
    Datacalorie = breakfastfoodseparatedIDdata[1:, 1:]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    brklbl = kmeans.labels_

    # K-Means clustering for dinner food items
    Datacalorie = DinnerfoodseparatedIDdata[1:, 1:]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    dnrlbl = kmeans.labels_

    # Read data from another CSV file
    datafin = pd.read_csv('inputfin.csv').T

    # Extract relevant categories from the data
    agecls = [0, 1, 2, 3, 4]
    healthycat = datafin.iloc[[1, 2, 3, 4, 6, 7, 9]].T.to_numpy()

    # Initialize arrays to store food items and labels
    healthycatfin = np.zeros((len(healthycat) * 5, 9), dtype=np.float32)
    yt = []

    # Populate arrays with data for classification
    for zz in range(5):
        for jj in range(len(healthycat)):
            valloc = list(healthycat[jj])
            valloc.append(agecls[zz])
            healthycatfin[t] = np.array(valloc)
            yt.append(brklbl[jj])
            t += 1

    # Prepare test data for classification
    X_test = np.zeros((len(healthycat) * 5, 9), dtype=np.float32)
    for jj in range(len(healthycat)):
        valloc = list(healthycat[jj])
        valloc.append(agecl)
        X_test[jj] = np.array(valloc)

    # Perform classification using Random Forest classifier
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(healthycatfin, yt)
    y_pred = clf.predict(X_test)

    # Print suggested food items
    print('SUGGESTED FOOD ITEMS ::')
    for ii in range(len(y_pred)):
        if y_pred[ii] == 1:
            print(Food_itemsdata[ii])
