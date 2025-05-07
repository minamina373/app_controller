#! coding: UTF-8
import sys
import os
import app_base
import datetime

#継承テストモジュール
class setting_load(app_base.app_base):

	#########取得系
	#オーバーライド
	#説明
	def get_description(self):
		return "メイン用のプロセス"

	def get_version(self):
		return "1.0.0"

	#########イベント
	#セッティングイベント
	def on_setting_load(self,_app_state):
		print "setting_load"
		#print _app_state


	def on_load(self):
		#ログに追加
		#self.add_log("testlog","プロセス開始\n",True)
		#プライベート用の値がなければ足します
		print "プロセス開始"
		#print self.private_values
		#カウンター設定
		if self.private_values is None:
			self.private_values={}

		if "count" in self.private_values:
			self.private_values["count"]=self.private_values["count"]+1
		else:
			#カウントがなければ足します
			self.private_values["count"]=0

		if not "time" in self.private_values:
			#時間がなければ足します
			self.private_values["time"]=datetime.datetime.now()




	#最後に実行される
	def on_end(self):
		pass


	#1時間に一回ぐらいログを削除
	def delete_log_process(self):
		#時差を使って設定 
		_td =  datetime.datetime.now() -self.private_values["time"]
		#print _td
		#secondは日をまたぐと0になる
		#print _td.seconds
		#print _td.total_seconds()
		if _td.total_seconds() >=3600:
			#時間をリセット(1時間ぐらいに1回)
			self.private_values["time"]=datetime.datetime.now()


		#1日前のログを削除(1時間ぐらいに1回)
		if self.private_values["count"] >=3600:
			#ログ削除
			self.delete_old_log()
			#カウンターをリセット
			self.private_values["count"]=0


	def on_setting_end(self,_app_state):
		print "setting_end"
		#ログ削除
		self.delete_log_process()

		#実行しているファイルとクラスの一覧
		for _row in _app_state:
			#検索したファイル一覧（逆順）
			print _app_state[_row].file_list[::-1]
			#実行されているファイル
			print " +" + _app_state[_row].file_name
			pass
		#print _app_state


	#値の取得
	#クラスの値を取得します
	#def get_public_values(self):
	#	return {"gege":"111"}

