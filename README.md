# プロジェクト名

Pythonでプログラムを順番に定期的に実行するスクリプト


---

## 目次

- [概要](#概要)
- [機能](#機能)
- [注意](#注意)


---

## 概要

app_controller.py　ファイルを実行することにより配下のプログラムを動的に読み込み実行し続ける、軽量のサービスコントローラです：

- 言語/フレームワーク:  Python


---

## 機能

- app_controller.py　は全てのサービスをコントロールするファイルです
- app_base.py を継承した配下のプログラムを作成します、このファイルが動的にインポートされファイルを置くだけで勝手に実行されます

- ファイル名規則は
- 種類_名前_バージョン(数字、整数、大きいほうが最新、バージョンは無しでも行けます)
- 種類は　setting ,process, module 
- 実行順はsetting →process→ module →setting 
-  setting:　ループの最初にon_setting_load が実行されます　public_valuesに入れた値がsetting_valueとしてprocess,moduleに引き継がれます、共通設定取得やログの開始に使います通常は1個しか作りません
-  process: settingの次に実行されます、メインのデータ取得処理です、public_valueに入れた値がmoduleに引き継がれます
-  module: processの次に実行されます、processで作成した値をもとに処理を行います
-  setting: ループの最後にon_setting_endを発火させるため実行されます
- イベントは			
- on_setting_load (event_stateが1の場合のみ実行されます
- on_load
- on_process_event（moduleの場合にprocessから受け取ったpublic_valuesの数だけ実行します）
- on_end
- on_setting_end (event_stateが2の場合のみ実行されます
- の順番でイベントとが実行されます
- on_setting load end はsettingモジュールでしか発火しません
- 配下のクラスは　app_base.py　が継承されたクラスしか動作しません、なので親クラス用のこのファイルが必要です


---

## 注意

- ！！配下のクラス名は動作しだしたら絶対変更するな！！
- バージョンが上がることによってファイル内のクラス名が同じであれば値を共有できます
- バージョンを上げてクラス名を変更すると値が共有できませんし、何が起こるかわかりません、クラス名は絶対編集してはいけません

