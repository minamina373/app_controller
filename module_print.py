#! coding: UTF-8
import sys
import os
import app_base


#継承テストモジュール
class module_print(app_base.app_base):

	#########取得系
	#オーバーライド
	#説明
	def get_description(self):
		return "プリント用のモジュール"

	def get_version(self):
		return "1.0.0"

	#########イベント
	#オーバーライド
	#認証イベント
	def on_load(self):
		#print "setting_valuse"
		#print self.setting_values

		if self.private_values is None:
			self.private_values=1
		else:
			self.private_values=self.private_values+1
		#print self.private_values


		#self.add_log("print","{0}\n".format(self.private_values),True)
		pass


	def on_public_event(self,_values):
		#print "public_values"
		#print _values

		pass

	def on_end(self):
		pass
		#print self.public_values;