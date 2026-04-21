

# myproject CRUD

![Python](https://img.shields.io/badge/Python-3.13.13-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-6.0.4-green?style=flat-square&logo=django)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Database](https://img.shields.io/badge/Database-SQLite3-lightgrey?style=flat-square&logo=sqlite)

Django を使用した CRUD アプリケーションです。

## プロジェクト構成

```
myproject/
├── manage.py           # Django管理コマンド
├── db.sqlite3          # SQLiteデータベース
├── myproject/          # プロジェクト設定
│   ├── settings.py     # Django設定
│   ├── urls.py         # ルーティング設定
│   ├── wsgi.py         # WSGI設定
│   └── asgi.py         # ASGI設定
└── crud/               # CRUDアプリケーション
    ├── models.py       # データモデル定義
    ├── views.py        # ビュー定義
    ├── admin.py        # 管理画面設定
    ├── urls.py         # アプリケーションのルーティング
    ├── migrations/     # データベースマイグレーション
    └── templates/      # HTMLテンプレート
        ├── top.html
        └── crud/
            ├── base.html           # ベーステンプレート
            └── product_list.html   # 製品一覧ページ
```

## 使用技術

- **Python**: 3.13.13
- **Django**: 6.0.4
- **Database**: SQLite3

## セットアップ

### 1. 仮想環境の有効化

```bash
.\myvenv\Scripts\Activate.ps1
```

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 3. マイグレーションの実行

```bash
python manage.py migrate
```

### 4. 開発サーバーの起動

```bash
python manage.py runserver
```

ブラウザで `http://127.0.0.1:8000/` にアクセスしてください。

## 機能

- **トップページ**: `http://127.0.0.1:8000/`
- **製品一覧**: CRUD 操作でデータベースのレコード管理

## 言語・タイムゾーン設定

- 言語: 日本語 (ja)
- タイムゾーン: Asia/Tokyo

## ライセンス

MIT
