class team():
    
    def __init__(self, Name ="Name", Origin= "Origin"):
        self.teamName= Name
        self.TeamOrigin = Origin
        
    def defineTeamName(self, Name):
        self.teamName =Name

    def defineTeamOrigin(self, Origin):
        self.TeamOrigin= Origin

'''class InheritanceClassName (parentclass):
    def __init__(self, Input1, Input2):
        parentclass.__init__(self)
        self.attribute1= Input1
        self.attribute2= Input2
        self.attribute3= 0'''

class player(team):
    def __init__(self,playername, playerpoints, TeamName, TeamOrigin):
       team.__init__(self,TeamName,TeamOrigin)
       self.playername= playername
       self.playerpoints= playerpoints
    
    def scoredpoint(self):
        self.playerpoints += 1
       
    def setname(self, Name):
        self.playername =Name
    
    def __str__(self):
        return self.playername+" has Scored "+str(self.playerpoints)+" points"
        
        
Team1= team("Love","Austrilia")
Team2= team("Get","USA")
Team3= team()
player1= player("sid", 0, "Originals","Jamaica")
player1.scoredpoint()
print(player1.playerpoints)
player1.setname("Delano")
print(player1.playername)
print(player1)



print(player1.playername)
print(player1.playerpoints)
print(player1.teamName)
print(player1.TeamOrigin)
player1.defineTeamName("Gully")


print(Team1.teamName)
print(Team2.teamName)
print(Team3.teamName)
Team1.defineTeamName("Delano")
print(Team1.teamName)
print(Team1.TeamOrigin)
print(Team2.TeamOrigin)
print(Team3.TeamOrigin)
Team1.defineTeamOrigin("England")
print(Team1.TeamOrigin)