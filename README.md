# acl_statistics

## 概要

[ACLアンソロジー](https://aclweb.org/anthology/)掲載のNLP系トップカンファレンスに対して、カンファレンス毎のtfidfを計算し、wordcloudで可視化する

トップカンファレンスは以下の4つとした

- ACL
- NAACL
- CoNLL
- EMNLP


## 使い方

```bash
# tfidfを作成
mkdir data; cd data
python ../crawl_all_title.py

# wordcloudでtfidfを可視化
cat XXXX.tfidf | python tfidf_wordcloud.py -o XXXX.png
```

tfidf はすでに計算してあるので、お使いの際は可視化だけどうぞ。