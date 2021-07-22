print("Welcome to my Favorite Song Characteristics Chart\n")
Name= "Day Rave"
#The Name of the song
def artist():
    Artist= "Vybz Kartel"
    return Artist
#The Name of the artiste the sings the song
Featuring= "None"
#The name of the other artists that sing in the song
def genre():
    Genre= "Dancehall"
    return Genre
#The Style or Catergory of the Song
DurationSec= 199
def extracredit(number):
    result = number/60
    if result > 4 :
        return 1
    else:
        return 0
aim = extracredit(DurationSec)
#The Total Song time in Seconds
 
Album= "Day Rave"
# # The Name of the album that includes the song
Produced_by= "Drop Top Records- Johnny Wonder"
# #The Name of the Record Studio that produced the song
Country= "Jamaica"
#The Name of the Country the song was released in
Riddim= "Drop Dem Riddim"
# #The Name of the Riddim the song is played on
def year():
    Year= 2019
    return Year
#The Month and Year the song was released
print(Name)
print(artist())
print(Featuring)
print(genre())
print(DurationSec,"Seconds")
print("Is this Song 4 minutes long ? ",bool(aim))
print(Album)
print(Produced_by)
print(Country)
print(Riddim)
print(year())