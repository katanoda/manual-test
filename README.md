# 製品取扱説明書ドキュメント

Markdownで記述し、MkDocsを使用してWebサイトおよびPDFとして出力するためのドキュメントプロジェクトです。

## 概要

- **ツール**: MkDocs, mkdocs-material, mkdocs-with-pdf
- **エントリポイント**: `doc/manual.md`
- **出力**: GitHub Pages (Web), PDF

## ローカルでの実行方法

1. 依存関係のインストール:

   ```bash
   pip install -r requirements.txt
   ```

2. プレビューサーバー起動:

   ```bash
   mkdocs serve
   ```

   <http://127.0.0.1:8000> にアクセスしてください。

3. ビルド (PDF生成含む):

   ```bash
   mkdocs build
   ```

   `site/` ディレクトリ配下に出力されます。

## ディレクトリ構成

- `doc/`: ドキュメントのソースファイル
  - `manual.md`: トップページ
  - `chapters/`: 各チャプターのMarkdownファイル
- `mkdocs.yml`: MkDocsの設定ファイル
- `.github/workflows/`: GitHub Actionsの設定ファイル

詳細な検証方法や使い方は [walkthrough.md] を参照してください（※BrainArtifacts内に生成されています）。
