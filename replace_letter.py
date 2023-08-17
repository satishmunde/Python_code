letter='''Dear  <|Name|>
Your are Selected
 in Tcs at pune your package is 3.5 lpa.

Datte : <|Date|>
'''
name=input("Enter Your name")
date=input("Enter Date")
letter= letter.replace("<|Name|>",name)
letter= letter.replace("<|Date|>", date)
print(letter)