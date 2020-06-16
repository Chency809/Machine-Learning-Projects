# Ignore the furture warnings
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Import the necessary packages
from sklearn.decomposition import PCA
import numpy as np

# Initialize the dataset, and create a PCA
np.random.seed(0)

train = np.random.rand(10000).reshape(100, 100)
test = np.random.rand(1000).reshape(10, 100)
pca = PCA(100)

# Fit PCA on x (train set) and transform train set
train_reduced = pca.fit_transform(train)

# Apply PCA on test set.
test_reduced = pca.transform(test)

'''
    Check the shape of the reduced dataset and retained variance
    The v[i] represents the i+1-D retained variance
'''

print(train_reduced.shape)
vectore_of_retained_variance = pca.explained_variance_ratio_.cumsum()
print(vectore_of_retained_variance)