# acl_statistics

## 概要

[ACLアンソロジー](https://aclweb.org/anthology/)掲載のNLP系トップカンファレンスを定量的に分析するためのツール。


できること

- カンファレンス毎のtfidfを計算する。
- 上記の計算結果をwordcloudで可視化する

暇があれば増やす予定

## 使い方

```bash
# tfidfを作成
mkdir data
python ../crawl_all_title.py -d data

# wordcloudでtfidfを可視化(XXXXには可視化したいデータを選択)
cat data/XXXX.tfidf | python tfidf_wordcloud.py -o XXXX.png
```

※ tfidf はすでに計算してあるので、お使いの際は可視化だけどうぞ。