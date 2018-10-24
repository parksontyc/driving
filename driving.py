country = input('請輸入您的國籍:')
age = input('請輸入您的年齡:')
age = int(age)
if country == '台灣' :
	if age < 18 :
		print('你不能考駕照哦')
	elif age >= 18 and age < 65 :
		print('你可以考駕照哦')
	else :
		print('你太老，坐車吧')

