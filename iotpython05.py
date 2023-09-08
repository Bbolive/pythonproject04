# หาพื้นที่สี่เหลี่ยมและสามเหลี่ยม โดยรับกว้าง ยาว/ฐาน สูง ทางแป้นพิมพ์ และแสดงผลทางหน้าจอ
# feature การทำงานอะไรบ้าง
# 1. รับค่า กว้าง ยาว 2. รับค่า ฐาน สูง 
# 3. คำนวณพื้นที่สี่เหลี่ยม และแสดงผลพื้นที่สีเหลี่ยม 4. คำนวณพื้นที่สามเหลี่ยม และแสดงพื้นที่สามเหลี่ยม
def inputwithLong( ) :
    wi = float( input('ป้อนความว้าง') )
    lo = float( input('ป้อนความยาว') )
    return wi, lo

def inputBaseHigh( ) :
    ba = float( input('ป้อนฐาน'))
    hi = float( input('ป้อนความสูง'))
    return ba, hi

def calAndShowAreaSquare( wi, lo ) :
    area = wi * lo
    print(f'สี่เหลี่ยมกว้าง {wi} ยาว {lo} มีพื้นที่ {area}')

def calAndShowAreaTrianbla(ba, hi ) :
    area = ba * hi / 2
    print(f'สามเหลี่ยมฐาน {ba} สูง {hi} มีพื้นที่ {area}')

wi, lo = inputwithLong( )
calAndShowAreaSquare( wi, lo )
print('---------------------------------------------')
ba, hi = inputBaseHigh( )
calAndShowAreaTrianbla(ba, hi)

