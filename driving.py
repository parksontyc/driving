country = input('請輸入您的國籍:')
age = input('請輸入您的年齡:')
age = int(age)
if country == '台灣' :
	if age < 18 :
		print('你不能考駕照哦')
	elif age >= 18 and age < 65 :
		print('你可以考駕照哦')
	elif age > 70 :
		print('你太老，坐車吧')

elif country == '美國' :
	if age < 16 :
		print('你不能考駕照哦')
	elif age >= 16 and age < 70 :
		print('你可以考駕照哦')
	elif age > 70 :
		print('你太老，坐車吧')		
else :
	print('國籍只能輸入台灣或美國哦')		