# 🎤 カラオケ曲メモアプリ

## 概要
カラオケで歌いたい曲の配信状況を管理できるWebアプリです。  
曲名・アーティスト名で検索でき、JOYSOUND / DAM / お気に入りで絞り込みできます。

## 公開URL
https://aiziro.pythonanywhere.com

## 使用技術
- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2
- Git / GitHub
- PythonAnywhere

## 主な機能
- 曲の追加
- 曲の削除
- 曲名・アーティスト名検索
- JOYSOUND / DAM の登録
- お気に入り登録・解除
- フィルター表示
  - すべて
  - JOYSOUND
  - DAM
  - お気に入り

## 工夫した点
- SQLiteを使ってデータを保存できるようにした
- POST処理を追加・削除・お気に入り切り替えで分岐した
- Jinja2でDBの値に応じてタグや星の表示を切り替えた
- ゆるかわだけど可愛すぎないUIを意識した

## 今後追加したい機能
- 編集機能
- スマホ表示の調整
- 曲の並び替え
- 登録日表示