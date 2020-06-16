from keras.utils.data_utils import get_file
import io

path = get_file(
    'nietzsche.txt',
    origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt')
with io.open(path, encoding='utf-8') as f:
    text = f.read().lower()


f = open("text_sample.txt", "w+")
f.write(text)
f.close()

if __name__ == "__main__":
    pass
