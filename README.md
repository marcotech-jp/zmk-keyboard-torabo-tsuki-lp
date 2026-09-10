# このリポジトリは[sekigon-gonnoc/zmk-keyboard-torabo-tsuki-lp](https://github.com/sekigon-gonnoc/zmk-keyboard-torabo-tsuki-lp)のフォークです。

[torabo-tsuki LP](https://github.com/sekigon-gonnoc/torabo-tsuki-lp)用のZMKファームウェア
* [キーマッププレビュー](https://marcotech-jp.github.io/zmk-keyboard-torabo-tsuki-lp/)

## 使い方

* _centralがついているuf2をトラックボールがついている方に、_peripheralを反対側に書き込んでください
* キーマップはkeymap-editorおよびzmk-studioで編集できます
  * <https://nickcoutsos.github.io/keymap-editor/>

## レイヤー構成

- `layer_0`（`Windows`）: Windows用の基本入力レイヤー
- `layer_1`（`macOS`）: macOS用の差分レイヤー。`r1 c0` が左Command、`r3 c0` が左Ctrl。`r2 c6` で左のデスクトップ（Spaces）、`r2 c7` は短押しで右のデスクトップへ移動、長押しでMission Control
- `layer_2`（`Pointer`）: クリックや戻る・進むを操作する一時マウスレイヤー。トラックボールの最終操作から10秒後、またはマウス操作キー以外のキー入力時に解除
- `layer_3`（`Scroll`）: トラックボールをスクロール動作へ切り替える専用レイヤー。キー設定はすべて透過
- `layer_4`（`Extra`）: F1-F12、JISの1（Shiftで!）、Deleteを配置した追加キーレイヤー。`r2 c6` はAlt+Tab
- `layer_5`（`Function`）: ファンクションキー、ナビゲーション、出力切替をまとめたレイヤー。左端列の `r0 c0` はWindows用BLEプロファイル0とWindowsレイヤー、`r1 c0` はmacOS用BLEプロファイル1とmacOSレイヤーを同時に選択。`r2 c0`、`r3 c0` はBLEプロファイル2、3のみを選択
- `layer_6`（`Numbers`）: 数字と記号を入力するレイヤー

## キーマッププレビューをローカルで表示

左右とも実機に合わせた列の段差と親指キーの傾きで表示し、右端の追加1列も表示します。各キーには従来の `row`・`col` 座標を併記しています。

レイヤー選択タブと見出しには、「Layer 0 · Windows」の形式でレイヤー番号と名前を表示します。

リポジトリのルートディレクトリで、PythonのHTTPサーバーを起動します。

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

ブラウザで <http://127.0.0.1:8000/> を開いてください。設定を変更した後は、ページを再読み込みすると反映されます。サーバーを終了するには、起動したターミナルで `Ctrl+C` を押します。
