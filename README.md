# 製品取扱説明書生成プロジェクト

Markdownで記述されたドキュメントを、MkDocsを使用してWebサイトおよびPDFとして出力するためのプロジェクトです。

## 目次

1. [概要](#概要)
2. [前提条件](#前提条件)
3. [ローカルでの実行方法](#ローカルでの実行方法)
4. [自動デプロイとリリース](#自動デプロイとリリース)
5. [ディレクトリ構成](#ディレクトリ構成)

---

## 概要

- **使用ツール**:
  - [MkDocs](https://www.mkdocs.org/): 静的サイトジェネレーター
  - [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/): テーマ
  - [mkdocs-with-pdf](https://github.com/orzklv/mkdocs-with-pdf): PDF生成
  - [mike](https://github.com/jimporter/mike): バージョン管理

- **主な機能**:
  - Webドキュメントの生成（レスポンシブ、検索機能付き）
  - PDFドキュメントの自動生成
  - GitHub Actionsによる自動デプロイとバージョン管理

---

## 前提条件

### 共通

- **Python**: バージョン 3.12 以上推奨

### Windowsユーザー向けの注意 (PDF生成)

PDF生成機能を使用するには、**GTK+ (GTK3)** ライブラリが必要です。

1. **[GTK3 for Windows Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)** からインストーラーをダウンロードしてインストールしてください。
2. インストール後、PCを再起動してください。

> **Note**: Webプレビューのみであれば、GTK3は不要です。

---

## ローカルでの実行方法

### 1. セットアップ

必要な依存パッケージをインストールします。

```bash
pip install -r requirements.txt
```

### 2. プレビュー (Webサイト)

開発用サーバーを起動してブラウザで確認します。デフォルトではWeb版のみビルドされます（高速・安定）。

```bash
mkdocs serve
```

起動後、 <http://127.0.0.1:8000> にアクセスしてください。

### 3. PDFビルド

Windows環境でPDFを含めて完全なビルドを行う場合は、付属のスクリプトを使用します（GTK3パス問題の回避用）。

```bash
python build_pdf.py
```

成果物は `site/` ディレクトリ配下に出力されます。

- Web: `site/index.html` 等
- PDF: `site/pdf/document.pdf`

---

## 自動デプロイとリリース

GitHub Actionsにより、ドキュメントのビルド・公開・リリースが自動化されています。

### 開発版の更新 (`main` ブランチ)

`main` ブランチに変更をプッシュすると、**開発版 (dev)** としてWebサイトが更新されます。

- URL: `https://<user>.github.io/<repo>/dev/`

### リリース版の作成 (タグ `v*`)

`v1.0` などのバージョンタグをプッシュすると、正式な**リリース版**として保存されます。

1. **タグの作成とプッシュ**:

   ```bash
   git tag v1.0
   git push origin v1.0
   ```

2. **自動処理される内容**:
   - Webサイト: `/v1.0/` にドキュメントが生成され、`/latest` がこのバージョンを指すようになります。
   - PDF: 生成された `document.pdf` が、GitHubリポジトリの **[Releases]** ページにアセットとして追加されます。

---

## ディレクトリ構成

```text
.
├── doc/                        # ドキュメントのソース
│   ├── index.md                # トップページ
│   ├── chapters/               # 各章のMarkdownファイル
│   └── images/                 # 画像ファイル
├── mkdocs.yml                  # Webプレビュー用設定 (通常用)
├── mkdocs_pdf.yml              # PDF生成・本番ビルド用設定
├── build_pdf.py                # Windows用PDFビルドスクリプト
├── requirements.txt            # Python依存関係
└── .github/workflows/          # CI/CD設定
```
