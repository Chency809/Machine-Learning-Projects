import warnings
warnings. filterwarnings("ignore")

import numpy as np
import sklearn.linear_model

# Initialize the output vectors of models
model1 = np.random.choice((1, 0), 100, replace = True, p = (0.9, 0.1)).reshape(-1, 1)
model2 = np.random.choice((1, 0), 100, replace = True, p = (0.5, 0.5)).reshape(-1, 1)
model3 = np.random.choice((1, 0), 100, replace = True, p = (0.1, 0.9)).reshape(-1, 1)

train_set = np.concatenate([model1, model2, model3], axis = 1)

# Initialize the labels
labels = np.random.choice((1,0), 100, replace = True, p = (0.9, 0.1))

regressor = sklearn.linear_model.LogisticRegression(max_iter = 10000, fit_intercept = False)
regressor.fit(train_set, labels)

print(regressor.coef_)
print(regressor.score(train_set, labels))


