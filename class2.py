def createdeck():
    
    deck=[]
    
    facevalues=["A","J","Q","K"]
    for i in range(4):
        for card in range(2,11):
            deck.append(card)
        
        for c in facevalues:
            deck.append(c)
    return deck
deck= createdeck()

print(deck)

class player():
    def __init__(self, hand=[], money=100):
        self.hand= hand
        self.money= money
        self.score= self.setscore()
    def __str__(self):
        currenthand= " "
        for card in self.hand:
            currenthand= str(card) + " "
            
        finalstatus= currenthand +"Score is "+str(self.score)
        return fiunalstatus
        
    def setscore(self):
        faceCardsDist= {"A":11,"J":10,"Q":10,"K":10,
                        "2":2,"3":3,"4":4,"5":5,"6":6,
                        "7":7,"8":8,"9":9,"10":10}
        acecounter= 0
        for card in self.hand:
            self.score += faceCardsDist[card]
            if card == "A":
                acecounter += 1
            elif self.score > 21 and acecounter != 0:
                self.score -= 10
                acecounter = 0
            return self.score
    
    def hit(self, card):
        self.hand.append(card)
        self.score =self.setScore()
        
    def pay(self,amount):
        self.money -= amount
        
    def win(self, amount):
       self.money += amount 