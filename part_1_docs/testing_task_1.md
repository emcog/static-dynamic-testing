### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
  #---> card.value should have == to test value rather than = which assigns a value 
    if card.value = 1:
      return True
      #---> else needs a colon
    else
      return False
   

  #---> line below: typo, dif should be def, comma should separate card1 & card2; 
  dif highest_card(self, card1 card2): 
  if card1.value > card2.value:
  #---> line below should return card1
    return card
  else:
    return card2
  


def cards_total(self, cards):
  #---> line below: total should be initialised with a numeric value, i.e. total = 0
  total
  for card in cards:
    total += card.value
    #---> line below: should be an fString. i.e. f"You have a total of + {total}
    return "You have a total of" + total