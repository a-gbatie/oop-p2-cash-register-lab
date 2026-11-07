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
      print("Not valid discount") # prints an error for invalid discount
    
  def add_item(self, name, price, quantity=1): # adds an item - quantity deault is 1
    for _ in range(quantity): # repeats for the quantity of items
      self.items.append(name) # stores the items
    
    transaction_total = price * quantity
    self.total += transaction_total # adds the full cost of the items to the total
    self.previous_transactions.append({"name": name, "price": price, "quantity": quantity}) # adds the item's price to the previous transactions
    
  def apply_discount(self):
    if self.discount == 0: # checks if there is no discount
      print("There is no discount to apply.") 
    else:
      self.total -= self.total * (self.discount / 100) # applies the discount to the total
      print(f"After the discount, the total comes to ${self.total:g}.") # success message with new total
  
  def void_last_transaction(self):
    if not self.previous_transactions:
      print("No transaction to void.")
    else:
      last_transaction = self.previous_transactions.pop()

      price = last_transaction["price"]
      quantity = last_transaction["quantity"]

      self.total -= price * quantity

      for _ in range(quantity):
        self.items.pop()