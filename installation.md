# ワンフレーズで捕まえて_installtion

## 概要
宴会で活躍するゲーム`ワンフレーズで捕まえて` ゲームの、インストール手順です。
PyQtを使用していますので、クロスプラットフォームで使用できます。(Linuxは要XWindow)
ルールは[こちら](README.md)


## install python(Windows向け手順)

### python3xのインストール

[該当リンク](https://www.python.org/downloads)より、Windows向けPythonインストーラをダウンロードし、実行します。
すべて既定値でインストールします。

`C:\Users\<ユーザ名>\AppData\Local\Programs\Python\PythonXX-XX`にPythonがインストールされているはずです。
**ユーザ名は環境に合わせて変更してください!!!!!** / **PythonXX-XX**もバージョンに合わせて変更してください
この`C:\ ...\PythonXX-XX`までのパスをコピーします。
![imgs/img6](img6.png)


### 環境変数設定を開く

スタートメニューに`環境変数`と打ち込み、検索します。そして`環境変数を編集`を選択します。
![imgs/img1](img1.png)


### Pathの設定

環境変数`Path`を編集します。pythonとpython/scriptsの2種類を設定します。(後述)
![imgs/img2](img2.png)

### pythonの設定

先程コピーした`C:\Users\<ユーザ名>\AppData\Local\Programs\Python\PythonXX-XX`をペーストします。
![imgs/img3](img3.png)

### python/scriptsの設定

`Pythonのインストール先\Scripts`フォルダがあるはずです。ここを開いてコピーします。
![imgs/img4](img4.png)
![imgs/img5](img5.png)


以下2つを`Path`に設定していればOKです。
* `C:\Users\EC08A\AppData\Local\Programs\Python\Python37-32`
* `C:\Users\EC08A\AppData\Local\Programs\Python\Python37-32\Scripts`

![imgs/img7](img7.png)

## 今までの手順があってるか試す

### cmdを開く

Win + rを押して`cmd`と打ち込みます。
![imgs/img8](img8.png)

### python -Vを試す

pythonがインストールされている かつ、Pathが適切に設定されていると何かしらのメッセージが出ます。(正しい挙動)
～～～認識されていません。系のメッセージが出たときはなにか間違えています。 上記ステップを見直してください。
![imgs/img9](img9.png)

同様に`pip`も試します。長いメッセージがずらーっと出たら正解です。 同じく認識されてないときはなにか間違えてます。

![imgs/img10](img10.png)
