#! coding: UTF-8
import sys
import os
import app_base


#継承テストモジュール
class process_main(app_base.app_base):

	#########取得系
	#オーバーライド
	#説明
	def get_description(self):
		return "メイン用のプロセス"

	def get_version(self):
		return "1.0.0"

	#########イベント
	#オーバーライド
	#認証イベント
	def on_load(self):

		if self.private_values is None:
			self.private_values=1
		else:
			self.private_values=self.private_values+1
		print self.private_values
		pass

	#イベント発生
	def on_public_event(self,_values):
		pass

	def on_end(self):
		print "base_644"
		pass

	#値の取得
	#クラスの値を取得します
	def get_public_values(self):
		return {"test":33}

