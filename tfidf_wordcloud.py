import sys
import argparse
from wordcloud import WordCloud
import re

num = re.compile(r'[0-9]+st')

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help='input file')
parser.add_argument('-o', '--output', dest='output', default='wordcloud.png',
                    help='')
args = parser.parse_args()

stopwords = {'after', 'and', 'at', 'as', 'by', 'for', 'from', 'in', 'of', 'on', 'over', 'per', 'since', 'through',
             'till', 'to', 'under', 'beside', 'with', 'down', 'off', 'around', 'among', 'between', 'above', 'across',
             'along', 'near', 'up', 'into', 'onto', 'until', 'upon', 'within', 'without', 'about', 'above', 'across',
             'annual', 'around', 'the', 'it', 'via', 'you'}


def main():
    tfidf = dict()
    for line in args.input:
        l_lst = line.strip().split()
        if len(l_lst) >= 2 and l_lst[0] not in stopwords and not num.search(l_lst[0]):
            tfidf.setdefault(l_lst[0], float(l_lst[1]))

    wordcloud = WordCloud(width=960, height=640, max_words=100, background_color="white")
    wordcloud.fit_words(tfidf)
    wordcloud.to_file(args.output)


if __name__ == '__main__':
    main()

