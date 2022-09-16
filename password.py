#密碼重設程式
password = 'a123456'
user = input('請輸入你的密碼: ')
while True:
	if user == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!! 還有2次機會')
		user = input('請重新輸入你的密碼: ')
		if user == password:
			print('登入成功')
			break
		else:
			print('密碼錯誤!! 還有1次機會')
			user = input('請重新輸入你的密碼: ')
			if user == password:
				print('登入成功')
				break
			else:
				print('登入失敗 請重新嘗試')
				break