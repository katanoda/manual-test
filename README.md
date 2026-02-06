# 製品取扱説明書生成のためのプロジェクト

Markdownで記述し、MkDocsを使用してWebサイトおよびPDFとして出力するためのドキュメントプロジェクトです。

## 概要

- **ツール**: MkDocs, mkdocs-material, mkdocs-with-pdf
- **エントリポイント**: `doc/manual.md`
- **出力**: GitHub Pages (Web), PDF

## 自動デプロイについて

このプロジェクトは GitHub Actions により、以下のトリガーで自動的にドキュメントのビルドとデプロイが行われます。

1. **`main` ブランチへのプッシュ**:
   - `main` ブランチに変更をプッシュすると、最新のドキュメントが GitHub Pages に反映されます。

2. **タグのプッシュ (`v*`)**:
   - `v1.0` などのタグをプッシュすることでもデプロイが実行されます。
   - コマンド例:

     ```bash
     git tag v1.0
     git push origin v1.0
     ```

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
   デフォルト設定 (`mkdocs.yml`) はPDF生成が無効化されているため、そのまま実行可能です。

   ```bash
   mkdocs serve
   ```

3. ビルド (PDF生成含む):

   **PDFを含めてビルドする場合 (Windows推奨)**:

   ```bash
   python build_pdf.py
   ```

   ※ `build_pdf.py` は、GTK3のパス設定を自動的に行い、エラーを回避します。

   Webのみビルドする場合:

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
