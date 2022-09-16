#密碼重設程式
password = 'a123456'
i = 3
user = input('請輸入你的密碼: ')
while i > 0:
	i = i - 1
	if user == password:
		print('登入成功')
		break
	else:
		if i > 0:
			print('密碼錯誤!! 還有', i, '次機會')
			user = input('請重新輸入你的密碼: ')
		else:
			print('登入失敗 請重新嘗試')
	