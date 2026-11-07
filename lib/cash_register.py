#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0): # runs when new cash register is created
    self.total = 0 # starts total at 0
    self.discount = discount # stores the discount percentage
    self.items = [] # creates an empty list to hold items
    self.previous_transactions = [] # creates an empty list to hold previous transactions

  @property # getter for discount
  def discount(self): # returns the discount percentage
    return self._discount
  
  @discount.setter # setter for discount
  def discount(self, value): # sets the discount percentage
    if isinstance(value, int) and 0 <= value <= 100: # checks the allowed range
      self._discount = value # stores the valid discount percentage
    else:
      raise ValueError("Discount must be an integer between 0 and 100") # raises an error for invalid discount
    
  def add_item(self, name, price, quantity=1): # adds an item - quantity deault is 1
    for _ in range(quantity): # repeats for the quantity of items
      self.items.append(name) # stores the items
      self.previous_transactions.append(price) # adds the item's price to the previous transactions
    
    self.total += price * quantity # adds the full cost of the items to the total
    
  def apply_discount(self):
    self.total -= self.total * (self.discount / 100) # applies the discount to the total