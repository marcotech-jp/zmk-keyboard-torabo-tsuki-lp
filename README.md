# このリポジトリは[sekigon-gonnoc/zmk-keyboard-torabo-tsuki-lp](https://github.com/sekigon-gonnoc/zmk-keyboard-torabo-tsuki-lp)のフォークです。

[torabo-tsuki LP](https://github.com/sekigon-gonnoc/torabo-tsuki-lp)用のZMKファームウェア
* [キーマッププレビュー](https://marcotech-jp.github.io/zmk-keyboard-torabo-tsuki-lp/)

## 使い方

* _centralがついているuf2をトラックボールがついている方に、_peripheralを反対側に書き込んでください
* キーマップはkeymap-editorおよびzmk-studioで編集できます
  * <https://nickcoutsos.github.io/keymap-editor/>

Mac側でCmdとCtrlをソフトウェアで入れ替える設定が前提です。マクロ・コンボ・長押しのショートカットは、入れ替え後に意図した操作になるよう設定しています。

## レイヤー構成

- `layer_0`（`default`）: 基本入力。
- `layer_1`（`Pointer`）: クリックや戻る・進むを操作する一時マウスレイヤー。トラックボールの最終操作から10秒後、またはマウス操作キー以外の入力で解除。
- `layer_2`（`Scroll`）: トラックボールをスクロール動作に切り替えるレイヤー。
- `layer_3`（`Extra`）: ファンクションキー、数字、Delete、Alt+Tabをまとめた追加入力。
- `layer_4`（`Function`）: 記号入力。
- `layer_5`（`Bluetooth`）: Bluetooth接続先の選択とペアリング情報のクリア。

## プレビューをローカルで表示

リポジトリのルートで実行し、<http://127.0.0.1:8000/> を開きます。

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

設定変更後はページを再読み込みしてください。終了は `Ctrl+C`。
