class Chips:



        def __init__(self, twentyCount, tenCount, fiveCount, oneCount):
                self.fiveCount = fiveCount
                self.tenCount = tenCount
                self.twentyCount = twentyCount
                self.oneCount = oneCount

        def upperlimit(self):
                total = (self.fiveCount * 5) + (self.tenCount * 10) + (self.twentyCount * 20) + (self.oneCount * 1) # type: ignore
                if(total > 50000):
                        print("You are way too wealthy sonny boy")
        
        def add(self, number):
                twenties = int(number/20)
                self.twentyCount = self.twentyCount + twenties
                number = number - (twenties * 20) # subtract the value of twenties from number
                tens = int(number/10)
                self.tenCount = self.tenCount + tens
                number = number - (tens * 10)
                fives = int(number/5) 
                self.fiveCount = self.fiveCount + fives
                number = number - (fives * 5)
                ones = int(number)
                self.oneCount = self.oneCount + ones
 
        def playChips(self, number):
                twenties = int(number/20)
                if(twenties <= self.twentyCount):
                        self.twentyCount = self.twentyCount - twenties
                        number = number - (twenties * 20)
                else:
                        number = number - (self.twentyCount * 20)
                        self.twentyCount = 0
                tens = int(number/10)
                if(tens <= self.tenCount):
                        self.tenCount = self.tenCount - tens
                        number = number - (tens * 10)
                else:
                        number = number - (self.tenCount * 10)
                        self.tenCount = 0
                fives = int(number/5) 
                if(fives <= self.fiveCount):
                        self.fiveCount = self.fiveCount - fives
                        number = number - (fives * 5)
                else:
                        number = number - (self.fiveCount * 5)
                        self.fiveCount = 0
                ones = int(number)
                if(ones <= self.oneCount):
                        self.oneCount = self.oneCount - ones
                        number = number - (ones * 1)
                else:
                        number = number - (self.oneCount * 1)
                        self.oneCount = self.oneCount - ones
                if(self.oneCount < 0):
                        print("You are broke go beg your significant other for forgiveness before the divorce.")
                        print("They're gonna take the kids")
        def allIn(self):
                total = self.twentyCount * 20 + self.tenCount * 10 + self.fiveCount * 5 + self.oneCount
                self.twentyCount = 0
                self.tenCount = 0
                self.fiveCount = 0
                self.oneCount = 0
                return total
        def printChips(self):
                print(self.twentyCount, "twenties", self.tenCount, "tens", self.fiveCount, "fives", self.oneCount, "ones")    
        def printTotal(self):
                total = (self.fiveCount * 5) + (self.tenCount * 10) + (self.twentyCount * 20) + (self.oneCount * 1)
                print("Total Chips: ", total)
                if(total <= 0):
                        print("You lose")
                        self.fiveCount = 0
                        self.tenCount = 0
                        self.twentyCount = 0
                        self.oneCount = 0
                return total
        
if __name__ == "__main__":
                          
        Player1 = Chips(1000, 20000, 22398, 9423)
        Player1.upperlimit()
        Player1.printChips()
        Player2 = Chips
        Player1.add(53)
        Player1.printChips()
        Player1.playChips(10)
        total = Player1.printTotal()
        print(total)
        Player1.printChips()
        Player1.add(5392)
        Player1.printChips()
        Player1.allIn()
        Player1.printChips()


        