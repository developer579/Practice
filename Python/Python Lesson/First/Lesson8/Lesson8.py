class Car:
	
	def __init__(self,nm,lt):
		self.num = nm
		self.lit = lt
	
	def getNum(self):
		return self.num
	
	def getLit(self):
		return self.lit
		
cr1 = Car(1234,25.5)
nm1 = cr1.getNum()
lt1 = cr1.getLit()

cr2 = Car(2345,30.5)
nm2 = cr2.getNum()
lt2 = cr2.getLit()

print("ナンバーは",nm1,"ガソリン量は",lt1,"です。")
print("ナンバーは",nm2,"ガソリン量は",lt2,"です。")