# 動作確認方法

## 1. Pythonがローカル環境にインストールされているか確認

ターミナルまたはコマンドプロンプトにて
`python -V`
または
`python3 -V`
で確認

バージョン番号が表示されればインストール成功です。

バージョンが確認できない場合は、下記「Pythonがダウンロードされていない場合」を参照してダウンロードする。

## 2. 仮想環境を立ち上げる

### 1. 仮想環境を作成する

1. ターミナルでteamPythonLocalディレクトリに移動する

2. 以下のコマンドをターミナルで叩く
`python -m venv env`

3. envという名前のフォルダがteamPythonLocalディレクトリ配下に作成されたことを確認する

ここにライブラリなどをインストールしていきます。

### 2. 仮想環境を立ち上げる

macの場合

`source env/bin/activate`

windowsの場合

`.\env\Scripts\activate`

ターミナルを閉じた場合は毎回仮想環境の立ち上げを行う必要があります。

## 3. パッケージインストール

`pip install -r requirements.txt`

envディレクトリ配下にパッケージがダウンロードされます。

## 4. DBの作成

### 1. マイグレーションファイルの作成

`python manage.py makemigrations`

### 2. マイグレーション

`python manage.py migrate`

## 5. サーバーを立ち上げる

`python manage.py runserver`

## 動作確認
ブラウザで画面を表示する
http://127.0.0.1:8000/
をブラウザに打ち込みロード

## Pythonがダウンロードされていない場合

### Windows

### 1.	公式サイトからインストーラーをダウンロード

•	Pythonの公式サイトにアクセスし、「Downloads」セクションからWindows向けの最新バージョンのインストーラーをダウンロードします。
	
Python公式サイト: https://www.python.org/

### 2.	インストーラーの実行

•	ダウンロードしたインストーラーをダブルクリックして実行します。

### 3.	インストールオプションの設定

•	「Add Python to PATH」にチェックを入れます。

•	「Install Now」をクリックして、デフォルト設定でインストールします。または、「Customize installation」をクリックして、カスタム設定を行います。

### 4.	インストールの確認

•	インストールが完了したら、コマンドプロンプトを開き、以下のコマンドを実行してインストールが成功したか確認します。

`python --version`

### macOS

### 1.	公式サイトからインストーラーをダウンロード
•	Pythonの公式サイトにアクセスし、「Downloads」セクションからmacOS向けの最新バージョンのインストーラーをダウンロードします。

Python公式サイト: https://www.python.org/

### 2.	インストーラーの実行
•	ダウンロードしたインストーラーをダブルクリックして実行します。

### 3.	インストールの確認
•	ターミナルを開き、以下のコマンドを実行してインストールが成功したか確認します。

`python3 --version`

バージョン番号が表示されればインストール成功です。


# Djangoの使い方

## 新規のページを追加したいとき
1. 01_pages配下にhogehoge.htmlをつくる
2. appsディレクトリ配下のurls.pyにパスを追加する
3. appsディレクトリ配下のviews.pyに関数を作成し、POST, GET時の処理を書く

## 独自のTemplate構文

1. 変数
   テンプレートで変数を表示するには、`{{ variable_name }}`を使用します。
   例: `<p>{{ user_name }}</p>`

2. タグ
   テンプレートでロジックを実行するには、`{% tag %}`を使用します。
   例: `{% if user.is_authenticated %} <p>Welcome, {{ user_name }}!</p> {% endif %}`

3. フィルタ
   変数の表示を変更するには、`{{ variable|filter }}`を使用します。
   例: `<p>{{ text|upper }}</p>`で変数textが全て大文字に変換される

4. forループ
   リストの各アイテムに対してループ処理を行うには、`{% for item in list %}`を使用します。
   例: `{% for item in item_list %} <li>{{ item }}</li> {% endfor %}`

5. if文
   条件に基づいて処理を分岐するには、`{% if condition %}`を使用します。
   例: `{% if user.is_active %} <p>Active User</p> {% else %} <p>Inactive User</p> {% endif %}`

6. コメント
   テンプレート内でコメントを記述するには、`{# comment #}`を使用します。
   例: `{# これはコメントです #}`


7. extendsタグ
   ベーステンプレートを継承するには、`{% extends 'base.html' %}`を使用します。
   例: `{% extends 'layout.html' %}`

8. blockタグ
   継承したテンプレートのブロックをオーバーライドするには、`{% block block_name %}`を使用します。
   例: `{% block content %} <p>This is the content.</p> {% endblock %}`

9. csrf_tokenタグ
    POSTフォームでCSRF（シーサーフ）保護を行うには、`{% csrf_token %}`をフォーム内に含めます。
    例: `<form method="post">{% csrf_token %} ... </form>`


## 新規のテーブルをDBに追加する

1. models.pyにmodelを追加
2. migrationを行う
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

3. postgresでテーブルが確認できればOK
ただし、テーブル名は`Djangoに設定したアプリ名_テーブル名`になっています。

## DBに接続する方法

方法①

コマンドラインからDockerコンテナ内のPostgreSQLに接続
`docker-compose exec db psql -U user -d dbs`

もしくは DockerDesktopのコンテナのexecから接続
`psql -U user -d dbs`

全テーブルの確認
`\dt`

特定のテーブルの詳細を見る
`\d table_name`

方法②
pdAdminから確認

## Django admin用アカウントの作成
docker-compose exec web python manage.py createsuperuser
