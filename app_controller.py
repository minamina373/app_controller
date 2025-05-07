#! coding: UTF-8

import sys
import os
import glob
import app_base
import importlib
import inspect
import time
import re
#import copy

_path ="./"
#アプリの状態リスト
_app_state={}
_app_base=app_base.app_base()

#！！配下のクラス名は動作しだしたら絶対変更するな！！
#バージョンが上がることによってファイル内のクラス名が同じであれば値を共有できます
#バージョンを上げてクラス名を変更すると値が共有できませんし、何が起こるかわかりません、クラス名は絶対編集してはいけません

#クラス状態クラス 
#メンバはdictクラスで保存してね（後から結合してすべて渡すんで）
class class_state():
	public_values=None
	private_values=None

#モジュール状態クラス
class module_state():
	kind_name=""
	version=None
	file_name=""
	file_list=[]
	update_time=None
	old_update_time=None
	classes={}
	def __init__(self,_file_name=None,_update_time=None):
		self.file_name =_file_name
		_keys=self.file_name.split("_")
		self.kind_name=_keys[0]
		self.version=None
		self.file_list=[]
		self.old_update_time=None

		if len(_keys) >=3:
			self.version=_keys[2]
		self.update_time =_update_time
		self.classes={}

	#モジュールに紐づくクラスの設定
	def set_classes(self,_mod):
		try:
			
			#クラスのリストを作成
			for _row in map(lambda x:x[0],inspect.getmembers(_mod,inspect.isclass)):
				#辞書に値を足します
				if _row in self.classes:
					if self.classes[_row] is None:
						#値がなければ新規作成
						self.classes[_row]=class_state()
				else:
					self.classes[_row]=class_state()
				#print "+++--  " + _row

			#差分を削除
			for _row in get_diff_list(self.classes,map(lambda x:x[0],inspect.getmembers(_mod,inspect.isclass))):
				del self.classes[_row]

		except Exception as e:
			#エラー
			print str(e.args)
			_app_base.add_log("controller_error",str(e.args) +"\n" ,True)

#差分を比較し違いをリストにして返します
def get_diff_list(_alist,_blist):
	_ret_list=[]
	for _row in _alist:
		if not _row in _blist:
			_ret_list.append(_row)

	return _ret_list

#モジュール状態に値を足します
#_app_name 名前
#_name ファイルパス
def set_app_state(_app_name,_name):
	_file_path="{0}{1}.py".format(_path,_name)
	if _app_name in _app_state:
		#値あり
		_value = _app_state[_app_name]
		# 要素の追加(ファイルの更新日時)
		#更新時間を古いものと新しいものをとっておく
		_value.old_update_time=_value.update_time
		_value.update_time= os.path.getmtime(_file_path)
		_value.file_name=_name
	else:
		#値無し
		# 要素の追加(ファイルの更新日時)
		_app_state[_app_name] =  module_state(_name,os.path.getmtime(_file_path))


#モジュール内のクラスからメソッドを実行
def class_exec(_mod,_list,_public_values=None,_setting_values=None,_event_state=0):
	_klass = None
	#print _list
	for _row in _list:
		print "＋実行クラス名:" + _row
		#無ければ返す
		if  not hasattr(_mod,_row):
			return 

		#クラスがあれば実行
		_klass =  getattr(_mod,_row)

		#クラスがapp_baseを継承していなければ返す
		try:
			#print _row
			if not issubclass(_klass , app_base.app_base):
				print "継承なし"
				return 
		except Exception as e:
			#エラーなんで次
			print str(e.args)
			_app_base.add_log("controller_error","＋実行クラス名:" + _row +"\n" ,True)
			_app_base.add_log("controller_error",str(e.args) +"\n" ,True)
			continue


		#print "00 " + _row 
		#クラスのインスタンスの生成
		try:
			#コンストラクタに値を含める
			_module=_klass(_list[_row].private_values)
			#クラスの実行
			#_module.on_cert()
			#上から順番に実行されます
			_module.on_setting(_setting_values)
			if _event_state ==1:
				#_event_stateが1の場合のみ実行されます
				_module.on_setting_load(_app_state)

			#_event_stateが2の場合は実行しません
			if _event_state !=2:
				_module.on_exec(_public_values)
				#on_load
				#on_event
				#on_end

			if _event_state ==2:
				#_event_stateが2の場合のみ実行されます
				_module.on_setting_end(_app_state)

			#値の取得
			_list[_row].private_values=_module.get_private_values()
			_list[_row].public_values=_module.get_public_values()
			#print _list[_row].private_values
			#print _list[_row].public_values
			#print dir()
			#クラスの削除
			del _module

		except Exception as e:
			#エラーなんで次
			print str(e.args)
			#ログ
			_app_base.add_log("controller_error","＋実行クラス名:" + _row +"\n" ,True)
			_app_base.add_log("controller_error",str(e.args) +"\n" ,True)


			continue



#ソートツール(数字付け
def atoi(text):
    return int(text) if text.isdigit() else text
#ソートツール(リスト化
def natural_keys(text):
    return [ atoi(c) for c in text.split("_") ]

#フォルダ内のファイル名を取得するぞ
def get_file_list(_app_name):
	#ファイル名の規則は　種類_名前_バージョン(数字、大きいほうが最新)　だぞ
	_filelist = sorted([os.path.splitext(os.path.basename(path))[0] for path in glob.glob(_path+ '**')
		if re.search('^{0}{1}_(\w|\W)+_\d+\.py$|^{0}{1}_(?!.*_).+.py$'.format(_path,_app_name), path.lower())]
		, key=natural_keys,reverse=True)

	return _filelist

#アプリの種類とリストの取得
def get_app_list(_app_name):
	_tmp_list =[]
	_del_list=[]
	#フォルダ内のファイル名を取得する
	_filelist = get_file_list(_app_name)

	#print _filelist
	#リストの構造
	# {kind: name: version: path: classes: }
	# classes {name: public_values: private_values:}


	#app_state_listに値を足します
	for _name in _filelist:
		_keys=_name.split("_")
		_dict_key="{0}_{1}".format(_keys[0],_keys[1])
		#値がないのであれば最初でありリストに追加
		if not _dict_key in _tmp_list:
			_tmp_list.append(_dict_key)
			set_app_state(_dict_key,_name)

		#取得したファイル一覧も保存
		_app_state[_dict_key].file_list=[s for s in _filelist if s.startswith(_dict_key + "_") or s==_dict_key]

	#差分を削除
	for _row in get_diff_list((d for d in _app_state if _app_state[d].kind_name==_app_name),_tmp_list):
			del _app_state[_row]

	#print _app_state
	

#モジュールを実行します
def module_exec(_app_row,_public_values=None,_setting_values=None,_event_state=0):
	#print _app_row
	_public_dict={}

	#モジュールの読み込み
	_mod =None
	try:
		print "実行ファイル名:"+_app_state[_app_row].file_name
		_mod = importlib.import_module(_app_state[_app_row].file_name)

		#print _app_state[_app_row].file_name
		#print _app_state[_app_row].update_time
		#print _app_state[_app_row].old_update_time
		#更新時間を古いものと新しいものをとっておく
		if _app_state[_app_row] is not None:
			if _app_state[_app_row].update_time != _app_state[_app_row].old_update_time:
				print "reload"
				#del _mod
				reload(_mod)

		#配下クラスの読み込み
		_app_state[_app_row].set_classes(_mod)
	except Exception as e:
		#エラーなんで次
		print str(e.args)
		#ログ
		_app_base.add_log("controller_error","実行ファイル名:"+_app_state[_app_row].file_name + "\n" ,True)
		_app_base.add_log("controller_error",str(e.args) +"\n" ,True)

		return _public_dict

	#実行
	class_exec(_mod,_app_state[_app_row].classes,_public_values,_setting_values,_event_state)

	#pulblic_valuesの取得
	for _l in _app_state[_app_row].classes:
		if _app_state[_app_row].classes[_l].public_values is not None:
			_public_dict.update(_app_state[_app_row].classes[_l].public_values)


	#モジュールの削除
	del _mod

	return _public_dict

#一回実行
def exec_one():
	print "--START--"
	_setting_dict={}
	_public_dict={}

	#アプリの作成
	get_app_list("setting")
	get_app_list("process")
	get_app_list("module")


	#settingのみ(setting_load実行時)
	for _row in (d for d in _app_state if _app_state[d].kind_name=="setting"):
		#_event_stateが1の場合のみ on_setting_load が実行されます
		_setting_dict.update(module_exec(_row,_public_values=None,_setting_values=None,_event_state=1))

	#processのみ
	for _row in (d for d in _app_state if _app_state[d].kind_name=="process"):
		_public_dict.update(module_exec(_row,_public_values=None,_setting_values=_setting_dict,_event_state=0))

	#moduleのみ
	for _row in (d for d in _app_state if _app_state[d].kind_name=="module"):
		module_exec(_row,_public_values=_public_dict,_setting_values=_setting_dict,_event_state=0)

	#settingのみ(setting_end実行時)
	for _row in (d  for d in _app_state if _app_state[d].kind_name=="setting"):
		#_event_stateが2の場合のみ on_setting_end が実行されます
		module_exec(_row,_public_values=_public_dict,_setting_values=_setting_dict,_event_state=2)


#メイン処理
def main_loop():
	while True:
		#実行
		exec_one()
		#1秒スリープ
		time.sleep(1)


#メイン処理
if __name__ == "__main__" :
	main_loop()




	

