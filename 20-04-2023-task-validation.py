
'''
#+994505555555
1.Uzunluq 13 simvol
2.+ ilə başlayır
3.Operatorlar:50,55,70,77,99,10,51
4.Birinci simvolu çıxmaqla yalnız rəqəm
5*.Hər errora görə error message
'''
def validate(number):
  operators=[50,55,70,77,99,10,51]
  if(len(number)!=13):
    message="The length of the entered number does not match"
  elif(type(int(number[1:13])) is not int):
    message="The number must contain digits"
  elif(number[0]!="+"): 
    message="Country code must be entered"
  elif(int(number[4:6]) not in operators):
    message="The operator code was entered incorrectly"
  else:
    message="The number has been successfully validated"
  return message
  
print(validate("+994507777777"))
