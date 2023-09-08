#function 2 : Have Parameter/No Return 
#parameter คือ ตัวแปรประเภทหนึ่ง
# จะใช้ได้เฉพาะในฟังก์ชันนั้นๆเท่านั้น

def funcA( x , y ) :
        print('Hi...')
        z = x + y
        print(f'{x} + {y} = {z}')
        #ไม่มีคำสั่ง return

def funcB( x ) : 
        print(f"x is {x} 555...")

funcA(10,50)
funcA(50,50)
funcB('sau iot')