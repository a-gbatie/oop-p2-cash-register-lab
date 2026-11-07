#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0): # runs when new cash register is created
    self.total = 0 # starts total at 0
    self.discount = discount # stores the discount percentage
    self.items = [] # creates an empty list to hold items
    self.previous_transactions = [] # creates an empty list to hold previous transactions
