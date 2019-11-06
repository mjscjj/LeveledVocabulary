#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>

def get_single_word_origin(word):
    from nltk import word_tokenize, pos_tag
    from nltk.corpus import wordnet
    from nltk.stem import WordNetLemmatizer
    # 获取单词的词性
    def get_wordnet_pos(tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    sentence = 'football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.'
    # tokens = word_tokenize(sentence)  # 分词
    tokens = [word, ]  # 分词
    tagged_sent = pos_tag(tokens)  # 获取单词词性

    wnl = WordNetLemmatizer()
    lemmas_sent = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # 词形还原
    # print(lemmas_sent[0])
    return lemmas_sent[0]


def get_word_origin(sentence):
    from nltk import word_tokenize, pos_tag
    from nltk.corpus import wordnet
    from nltk.stem import WordNetLemmatizer

    # 获取单词的词性
    def get_wordnet_pos(tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    tokens = word_tokenize(sentence)  # 分词
    tagged_sent = pos_tag(tokens)  # 获取单词词性

    wnl = WordNetLemmatizer()
    lemmas_sent = {}
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent[tag[0]] = wnl.lemmatize(tag[0], pos=wordnet_pos)  # 词形还原
    # print(lemmas_sent)
    return lemmas_sent


if __name__ == '__main__':
    print(get_word_origin("saw"))
