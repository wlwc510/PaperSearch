#coding utf-8
import numpy as np
import os
import re
import nltk
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

sent_tokenizer = nltk.data.load(r'tokenizers/punkt/english.pickle')

def all_embedding():
    embeddings_index = {}
    with open(r'D:\分类器构造\numberbatch-en-17.06.txt\numberbatch-en.txt', encoding='utf-8') as f:
        for line in f:
            values = line.split(' ')
            word = values[0]
            embedding = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = embedding
    return embeddings_index
embeddings_index = all_embedding()
# sentence = 'he is dog'
#
# words = sentence.split(' ')
# print(words)

def read_file(path):
    if not os.path.exists(path):
        print('text not exist')
    else:
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.readlines()
        return content

# 处理每一个句子，把句子变成向量
def sentence_embedding_matrix(input_sentence):
    word_embedding_matrix = np.zeros((len(input_sentence), 300), dtype=np.float32)
    for i, word in enumerate(input_sentence):
        if word in embeddings_index:
            word_embedding_matrix[i] = embeddings_index[word]
        else:
            new_embedding = np.array(np.random.uniform(-1.0, 1.0, 300))
            word_embedding_matrix[i] = new_embedding
    sentence_embedding = np.sum(word_embedding_matrix, axis=0)
    return sentence_embedding

# 获取所有的文档内容
def get_text(file_dir, start, end):
    text_content_list = []
    text_name_list = os.listdir(file_dir)
    text_name_list = sorted(text_name_list, key=lambda i: int(re.match(r'(\d+)', i).group()))
    for text in text_name_list[start - 1: end]:
        text_list = []
        text_path = os.path.join(file_dir, text)
        content = read_file(text_path)
        content_to_sentence = sent_tokenizer.tokenize(content[0])
        for sentence in content_to_sentence:
            sentence_embedding = list(sentence_embedding_matrix(sentence))
            text_list.append(sentence_embedding)


        text_content_list.extend(text_list)
        # text_content = ''.join(text_content_list)
    return text_content_list

# 创建label列表
def creat_labellist(label_dir, label_start, label_end):
    text_name_list = os.listdir(label_dir)
    text_name_list = sorted(text_name_list, key=lambda i: int(re.match(r'(\d+)', i).group()))
    label_list = []
    for text in text_name_list[label_start - 1: label_end]:
        label_path = os.path.join(label_dir, text)
        label = read_file(label_path)[0].split(' ')
        label_list.extend(label)

    return label_list

def build_machine(train_data, train_label, test_data, test_label):
    # '''逻辑回归'''
    clf = LogisticRegression()
    clf.fit(train_data, train_label)
    pred = clf.predict(test_data)
    accuracy = accuracy_score(test_label, pred)
    report = classification_report(test_label, pred)
    return pred, accuracy, report



# file_path = r"E:\PycharmProjects\remote sensing preprogress\2.txt"
file_dir = r"D:\study\大四\毕设\xl2\Disscusion"
label_dir = r"D:\study\大四\毕设\xl2\Discussion lable"



vec = get_text(file_dir, 1, 51)
print('vec ok')
label = creat_labellist(label_dir, 1, 51)
print('label ok')

train_data, train_label = vec[ : int(0.8 * len(label))], label[ : int(0.8 * len(label))]
text_data, text_label = vec[int(0.8 * len(label)): ], label[int(0.8 * len(label)): ]
print('training')

pred, accuracy, report = build_machine(train_data, train_label, text_data, text_label)

print(pred)
print(accuracy)
print(report)




# print(word_embedding_matrix)
# sentence_embedding = np.sum(word_embedding_matrix, axis=0)
# print(sentence_embedding)
# print(sentence_embedding.shape)


