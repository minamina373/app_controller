#! coding: UTF-8

import sys
import os
import datetime



#基底クラス
class app_base():

	private_values={}
	public_values={}
	setting_values={}
	_log_dir= os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), './log_data/'))



	#########コンストラクタ
	def __init__(self,_private_values=None):
		#初期設定
		self.private_values=_private_values
	
	#クラスの値を取得します(dictで返すこと)
	def get_private_values(self):
		return self.private_values

	#クラスで生成した値を取得します(dictで返すこと)
	def get_public_values(self):
		return self.public_values


	#########取得系
	#説明
	def get_description(self):
		return "説明なし"

	#########設定系
	def set_description(self,_description):
		pass

	#########イベント
	#実行
	def on_exec(self,_public_values=None):

		#on_setting
		#on_setting_load(すべてのプロセスの始まりにのみ呼び出される)(このイベントは特殊でコントローラーのapp_stateを取得できる)
		#on_load
		#on_event
		#on_end
		#on_setting_end(すべてのプロセスの終わりのみ呼び出される)(このイベントは特殊でコントローラーのapp_stateを取得できる)

		self.on_load()
		self.on_event(_public_values)
		self.on_end()

	#プロセスから受け取った値を処理します
	def on_process_event(self,_public_values):
		pass

	#初期設定
	def on_setting(self,_setting_values=None):
		self.setting_values=_setting_values

	#認証イベント
	def on_load(self):
		pass
	def on_end(self):
		pass

	#セッティングイベント
	def on_setting_load(self,_app_state=None):
		pass
	def on_setting_end(self,_app_state=None):
		pass


	#イベント発生装置
	def on_event(self,_public_values=None):
		self.public_values=_public_values
		if self.public_values is None:
			return 
		for _row in self.public_values:
			self.on_public_event({_row:self.public_values[_row]})

	#on_eventで取得された情報分発生
	def on_public_event(self,_values):
		pass


	################ログ関連
	#ログあるかどうか
	def is_log_exists(self,_logname):
		_day= datetime.datetime.now()
		_log_name="{2}/{0}_{1}.txt".format(_day.strftime('%Y-%m-%d'),_logname,self._log_dir)
		return self.is_file_exists(_log_name)

	#ファイルあるかどうか
	def is_file_exists(self,_path):
		if os.path.isfile(_path):
			return True
		return False

	#ファイル削除
	def file_remove(self,_path):
		os.remove(_path)

	#古いログを消します
	def delete_old_log(self,_int_day=1):
		_day= datetime.datetime.now()
		_day_1ago= _day + datetime.timedelta(days=(-1 * _int_day))
		for _file in os.listdir('{0}/'.format(self._log_dir)):
			if _file.startswith(_day_1ago.strftime('%Y-%m-%d')):
				print "古いファイルを削除 {0}".format(_file)
				self.file_remove('{0}/'.format(self._log_dir) + _file)

	#ログに書きこみます
	#_is_op_date True＝ログの頭に日時をつけます
	#_is_mail_send True = 文面をメールを送ります
	def add_log(self,_logname,_text,_is_op_date = False,_is_mail_send=False):
		_day= datetime.datetime.now()
		_log_name="{2}/{0}_{1}.txt".format(_day.strftime('%Y-%m-%d'),_logname,self._log_dir)
		_log_tx = open(_log_name, 'a')
		if _is_op_date:
			_log_tx.write(_day.strftime('%Y-%m-%d %H:%M:%S :'))
		_log_tx.write(_text)
		_log_tx.close()
		
		#メールを送る
		if _is_mail_send:
			self.mail_send(_text)
	
	#メール送る
	def mail_send(self,_text):
		pass


if __name__ == "__main__" :
	pass