#(9)ตัวดำเนินการทางตรรกศาสตร์

#AND = และ  ต้องจริงทั้งสองจะได้จริง
#OR = หรือ   จริงอย่างใดอย่างนึงจะได้จริง
#NOT = ไม่   ตรงกันข้าม

#คำตอบ => จริง/เท็จ

x = (5>10)
y = (10==5)

a = (10==10)
b = (4!=5)

z = x and y #ทำการเปรียบเทียบ
print("เปรียบเทียบ x และ y = ",z)

d = a or b #ทำการเปรียบเทียบ
print("เปรียบเทียบ a และ b = ",d)

d = a or b #ทำการเปรียบเทียบ
print("เปรียบเทียบ a และ b(ใช้ not) = ",not d)