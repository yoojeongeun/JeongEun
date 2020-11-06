
Poly_code = input("생성 다항식을 입력하시오 : ")
Poly_code = Poly_code.split('+')
In_Zero = 0



for i in Poly_code:
    if(i[0] == 'x'):
        In_Zero += 1 << int(i[1])
    else :
        In_Zero += 1

Poly_code = bin(In_Zero)


TF_Data = input("전송 데이터를 입력하시오 :")
TF_Data = TF_Data[::-1] 
temp = 0
TM = 0


for i in TF_Data:
    if i == "1":
        TM += 2**temp
    temp += 1

Orign_TF_Data = TF_Data
TF_Data = TM

        
TF_Data = TF_Data << int(len(Poly_code)-3)
TF_Data = bin(TF_Data)


Poly_arr = list(Poly_code)
del Poly_arr[0:2]

TF_arr = list(TF_Data)
del TF_arr[0:2]


flag = True
Div_arr = TF_arr[0:len(Poly_arr)]

def ctr():
    del Div_arr[0]
    del TF_arr[0]
    if len(Poly_arr) > len(TF_arr):
        return 
    Div_arr.append(TF_arr[len(Poly_arr)-1])

    

while flag:
    if Div_arr[0] =='0':
        print(Div_arr)
        ctr()
        if len(TF_arr) == len(Poly_arr) -1:
            break
        continue

    for i in range(0, len(Poly_arr)):
                   if Div_arr[i] ==  Poly_arr[i] :
                       Div_arr[i] = '0'
            
                   else:
                       Div_arr[i] = '1'
    ctr() 

            

print("체크섬 : " + ''.join(Div_arr))
print("송신데이터 : " + Orign_TF_Data + ''.join(Div_arr) )
                
                   
                       

        
       
