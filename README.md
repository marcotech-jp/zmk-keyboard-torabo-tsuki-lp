# このリポジトリは[sekigon-gonnoc/zmk-keyboard-torabo-tsuki-lp](https://github.com/sekigon-gonnoc/zmk-keyboard-torabo-tsuki-lp)のフォークです。

[torabo-tsuki LP](https://github.com/sekigon-gonnoc/torabo-tsuki-lp)用のZMKファームウェア
* [キーマッププレビュー](https://marcotech-jp.github.io/zmk-keyboard-torabo-tsuki-lp/)

## 使い方

* _centralがついているuf2をトラックボールがついている方に、_peripheralを反対側に書き込んでください
* キーマップはkeymap-editorおよびzmk-studioで編集できます
  * <https://nickcoutsos.github.io/keymap-editor/>

## レイヤー構成

- `layer_0`: 通常使用するQWERTYの基本入力レイヤー
- `layer_1`: クリックや戻る・進むを操作する一時マウスレイヤー
- `layer_2`: F1-F12、JISの1（Shiftで!）、Deleteを配置したトラックボールのスクロールレイヤー
- `layer_3`: ファンクションキー、ナビゲーション、出力切替をまとめたレイヤー
- `layer_4`: 数字と記号を入力するレイヤー

## キーマッププレビューをローカルで表示

左右とも実機に合わせた列の段差と親指キーの傾きで表示し、右端の追加1列も表示します。各キーには従来の `row`・`col` 座標を併記しています。

リポジトリのルートディレクトリで、PythonのHTTPサーバーを起動します。

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

ブラウザで <http://127.0.0.1:8000/> を開いてください。設定を変更した後は、ページを再読み込みすると反映されます。サーバーを終了するには、起動したターミナルで `Ctrl+C` を押します。
