
[torabo-tsuki LP](https://github.com/sekigon-gonnoc/torabo-tsuki-lp)用のZMKファームウェア

* _centralがついているuf2をトラックボールがついている方に、_peripheralを反対側に書き込んでください
* キーマップはkeymap-editorおよびzmk-studioで編集できます
* [キーマッププレビュー](https://marcotech-jp.github.io/zmk-keyboard-torabo-tsuki-lp/)

## キーマッププレビューをローカルで表示

リポジトリのルートディレクトリで、PythonのHTTPサーバーを起動します。

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

ブラウザで <http://127.0.0.1:8000/> を開いてください。設定を変更した後は、ページを再読み込みすると反映されます。サーバーを終了するには、起動したターミナルで `Ctrl+C` を押します。

## キーマップの検証

```sh
python3 scripts/validate_keymap.py
```

各レイヤーのbinding数を検証します。この検証はGitHub Actionsでもファームウェアのビルド前に実行されます。

物理座標に設定されたbindingも確認できます。

```sh
python3 scripts/validate_keymap.py layer_1 r1 c11
```
