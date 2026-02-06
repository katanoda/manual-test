# 製品取扱説明書ドキュメント

Markdownで記述し、MkDocsを使用してWebサイトおよびPDFとして出力するためのドキュメントプロジェクトです。

## 概要

- **ツール**: MkDocs, mkdocs-material, mkdocs-with-pdf
- **エントリポイント**: `doc/manual.md`
- **出力**: GitHub Pages (Web), PDF

## 前提条件 (Windowsユーザー向けの注意)

PDF生成機能 (`mkdocs-with-pdf`) を使用するためには、**GTK+ (GTK3)** ライブラリが必要です。
これがない場合、`OSError: cannot load library ...` というエラーが発生してビルドに失敗します。

1. **[GTK3 for Windows Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)** からインストーラーをダウンロードしてインストールしてください。
2. インストール後、PCを再起動してください。

> **Note**: PDF生成が不要であれば、後述の「Webプレビューのみ」の手順で回避可能です。

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

   **※PDF生成エラーが出る場合（Webのみ確認したい場合）:**

   ```bash
   mkdocs serve -f mkdocs_web.yml
   ```

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
