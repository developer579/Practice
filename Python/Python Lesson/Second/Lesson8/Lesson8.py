class Car:
	def __init__(self,nm,lt):
		self.num = nm
		self.lit = lt
	
	def getNum(self):
		return self.num
	
	def getLit(self):
		return self.lit
	
def P(self):
    for i in self:
	    print("ナンバーは",i.getNum(),"ガソリン量は",i.getLit(),"です。")

pr1 = Car(1234,25.5)
pr2 = Car(2345,30.5)
prs = [pr1,pr2]

P(prs)

add1 = str(input("データを追加しますか(yes,no)"))
if add1 is "yes" or "Yes" or "YES":
    nnum = int(input("ナンバーを入力してください。")) 
    nlit = float(input("ガソリン量を入力してください。"))
    pr3 = Car(nnum,nlit)
    prs.append(pr3)
    print(nnum,",",nlit,"を追加しました。")
else:
    print("処理を継続します。")

P(prs)