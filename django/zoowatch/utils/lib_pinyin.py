# -*- coding=utf-8 -*-
# Created Time: 2015年12月20日 星期日 14时50分00秒
# File Name: lib_pinyin.py

'''
汉语转拼音测试

pip install pypinyin
'''

from __future__ import unicode_literals
from pypinyin import pinyin, lazy_pinyin
import pypinyin, logging

logger = logging.getLogger('printinfo')


def get_word_pinyin_py(word):
    ''' 将输入的中文处理成拼音和拼音首字母 '''

    word_pinyin = ''
    word_py     = ''

    try:
        word_pinyin_list = lazy_pinyin(word, errors='ignore')
        for w in word_pinyin_list: word_pinyin += str(w)
        #print 'word_pinyin: ', word_pinyin

        word_py_list_out = pinyin(word, style=pypinyin.FIRST_LETTER)
        for i in word_py_list_out: word_py += str(i[0])
        #print 'word_py: ', word_py
    except Exception, ex:
        logger.exception(ex)

    return word_pinyin, word_py


def main():

    name = '老虎'
    get_word_pinyin_py(name)


if __name__ == '__main__':
    main()

