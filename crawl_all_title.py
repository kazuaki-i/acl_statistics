# ACLアンソロジーのタイトルをクロールしつつTF-IDFを計算する

import sys
import requests
import re
import math
import argparse
import snowballstemmer

from collections import defaultdict
from operator import itemgetter
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', dest='dir', default='data/',
                    help='output directory')
args = parser.parse_args()

# クロール対象の会議
urls = ['https://aclweb.org/anthology/events/acl-{}/',
        'https://aclweb.org/anthology/events/conll-{}/',
        'https://aclweb.org/anthology/events/naacl-{}/',
        'https://aclweb.org/anthology/events/emnlp-{}/']

# 保存先のディレクトリ
DIR = args.dir.rstrip('/')

stemmer = snowballstemmer.stemmer('english')

head_rm = re.compile(r'^[?.!\'\"\-,:;()]+')
tail_rm = re.compile(r'[?.!\'\"\-,:;()]+$')


def main():
    tf, df = defaultdict(lambda: defaultdict(int)), defaultdict(int)
    for i in range(2000, 2020):
        for url in urls:
            url_key = url.format(i)
            soup = BeautifulSoup(requests.get(url_key).content, 'lxml')
            p = 0

            if not soup:
                continue

            v = dict()
            for a in soup.find_all('a', {'class': 'align-middle', 'href': True, 'data-placement': False}):
                # 本会議のみのタイトルを取得するための条件その１
                if len(a.get('class')) > 1 and not a.get('href').startswith('/anthology/papers/'):
                    continue

                # 本会議のみのタイトルを取得するための条件その２
                title = a.text
                if title.startswith('Proceedings of'):
                    if '/anthology/papers/' in a.get('href'):
                        p += 1
                    if p > 1:
                        break
                    continue

                for w in title.strip().split():
                    word = tail_rm.sub('', head_rm.sub('', w))
                    word = stemmer.stemWord(word.lower())
                    if word and not word.isdigit() and len(word) > 1:
                        v.setdefault(word)
                        tf[url_key][word] += 1

            for k, _ in v.items():
                df[k] += 1

            print('{} fin.'.format(url.format(i)), file=sys.stderr, flush=True)

    # クロールしたデータの保存
    with open('{}/df.tsv'.format(DIR), 'w', encoding='utf-8') as f:
        for k, v in sorted(df.items(), key=itemgetter(1), reverse=True):
            print('{}\t{}'.format(k, v), file=f)

    for u, d in tf.items():
        u = u.strip('/').split('/')[-1]
        with open('{}/{}_tf.tcv'.format(DIR, u), 'w', encoding='utf-8') as f:
            for k, v in sorted(d.items(), key=itemgetter(1), reverse=True):
                print('{}\t{}'.format(k, v), file=f)

    for u, d in tf.items():
        u = u.strip('/').split('/')[-1]
        tfidf = dict()
        for k, v in d.items():
            tfidf.setdefault(k, math.log(v) / (df.get(k, 0) + 1))

        with open('{}/{}_tfidf.tcv'.format(DIR, u), 'w', encoding='utf-8') as f:
            for k, v in sorted(tfidf.items(), key=itemgetter(1), reverse=True):
                print(k, v, d.get(k), df.get(k), file=f)


if __name__ == '__main__':
    main()

