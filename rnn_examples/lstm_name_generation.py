import numpy as np
import tensorflow as tf

f = open("name_sample.txt", "r")
text = f.read().lower()
print("Corpus Length:", len(text))

chars = sorted(list(set(text.lower())))
print('total chars:', len(chars))

EOS = chars[0]

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

def sample(y, indices_char, seed):
    np.random.seed(seed)
    y_index = np.random.choice(np.arange(len(chars)), 1, True, y)[0]

    return indices_char[y_index]

train_set = []
label = []

def get_train_test(text, train_set, label, EOS, char_indices):

    x = []
    y = []
    for i in range(len(text)):
        char = text[i]

        if char != EOS:
            print("works")
            x.append(char)
        else:
            print("EOS: ", char)
            y = x[1:] + [EOS]

            x = np.asarray([char_indices[i] for i in x])
            y = np.asarray([char_indices[i] for i in y])

            train_set.append(x)
            label.append(y)

            x,y = [],[]

def one_hot_encoding(data, dimensions):

    return tf.one_hot(data, depth = dimensions)



def build_model():
    pass

if __name__ == "__main__":
    get_train_test(text[:100], train_set, label, EOS, char_indices)

    print(train_set)
    print(label)
