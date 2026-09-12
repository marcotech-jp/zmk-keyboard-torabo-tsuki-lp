# AGENTS.md

## このリポジトリについて

torabo-tsuki LP の右トラックボール仕様向け ZMK ファームウェア。

- 右側: central + トラックボール
- 左側: peripheral
- ビルド構成は `build.yaml` を参照し、左右の役割を入れ替えない。

## 編集時の注意

- キーマップの正本は `config/keymap.keymap`。
- Mac側でCmdとCtrlをソフトウェアで入れ替えている。マクロ・コンボ・長押しなどのショートカットは、MacでCtrlとして動作させる場合はGUI（`LG`）、Cmdとして動作させる場合はCtrl（`LC`）を送信する。
- `README.md` は使い方、各レイヤーの簡潔な説明、プレビューへの案内など、必要最低限の内容にする。レイヤーの説明は残し、役割が変わった場合は更新する。
- 個々のキー配置やコンボの詳細はHTMLプレビューを参照し、READMEに重複して記載しない。レイヤーの役割が変わらない配置変更ではREADMEの更新は不要。
- M Layout の各レイヤーは `12 / 12 / 14 / 12` bindings。物理位置と binding の順序を維持する。
- トラックボールは `snippets/input-trackball/`、右側固有の入力変換は `boards/shields/torabo_tsuki_lp/torabo_tsuki_lp_right.overlay` にある。

特に指定がなければ日本語で回答する。
