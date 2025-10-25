# #Avasthi is having some amount of money and he is having only some denominations of 100,50,20,10,5,2,1. He needs to know how many notes are required for the amount present with him. (Do it using Switch case)
# Input: The first line is the amount of money present. The second line is the denomination present with the Avasthi
def currency():
  amount = int(input("Enter Number :"))
  dominance=int(input("Enter Note :"))# should be 100,50,20,10,5,2,1
  dominant_notes = {100:0,50:0,20:0,10:0,5:0,2:0,1:0}
  bade_Notes = amount//dominance
  dominant_notes[dominance]=bade_Notes # it return maximum bote that can be come 
  amount=amount-bade_Notes*dominance
  currency = [100,50,20,10,5,2,1]
  currency.remove(dominance) # yeh not alredy store ho chuka he 
  #applying two pointer 
  left=0
 
  while amount!=0 and left< len(currency):
    if amount>=currency[left]:
      amount-=currency[left]
      dominant_notes[currency[left]]+=1
    else:
      left+=1
  print(dominant_notes)      
      

currency()