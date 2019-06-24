import nltk
import os

sent_tokenizer = nltk.data.load(r'tokenizers/punkt/english.pickle')

def read_file(path):
    if not os.path.exists(path):
        print('text not exist')
    else:
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.readlines()
        return content

file_dir = r"D:\study\大四\毕设\xl2\Disscusion"


def token(number):
    file_path = os.path.join(file_dir, str(number) + '.txt')
    sentence = sent_tokenizer.tokenize(read_file(file_path)[0])
    return sentence

number=51
content_to_sentence = token(number)
for i, sentence in enumerate(content_to_sentence):
    print(i + 1, sentence)
    print('')
