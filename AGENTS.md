# AGENTS.md

## このリポジトリについて

torabo-tsuki LP の右トラックボール仕様向け ZMK ファームウェア。

- 右側: central + トラックボール
- 左側: peripheral
- ビルド構成は `build.yaml` を参照し、左右の役割を入れ替えない。

## 編集時の注意

- キーマップの正本は `config/keymap.keymap`。
- 各レイヤーの概要は `README.md` の「レイヤー構成」を参照し、キーマップ変更時はREADMEの説明も同期する。
- M Layout の各レイヤーは `12 / 12 / 14 / 12` bindings。物理位置と binding の順序を維持する。
- トラックボールは `snippets/input-trackball/`、右側固有の入力変換は `boards/shields/torabo_tsuki_lp/torabo_tsuki_lp_right.overlay` にある。

特に指定がなければ日本語で回答する。
