# acl_statistics

## 概要

[ACLアンソロジー](https://aclweb.org/anthology/)掲載のNLP系トップカンファレンスを定量的に分析する。

できること

- カンファレンス毎のtfidfを計算し、wordcloudで可視化する

暇があれば増やす予定

## 使い方

```bash
# tfidfを作成
mkdir data; cd data
python ../crawl_all_title.py

# wordcloudでtfidfを可視化
cat XXXX.tfidf | python tfidf_wordcloud.py -o XXXX.png
```

tfidf はすでに計算してあるので、お使いの際は可視化だけどうぞ。