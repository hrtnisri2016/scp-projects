class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def __repr__(self):
    """
    When the budget object is printed it will display:
    - A title line of 30 characters where the name of the category is centered in a line of * characters.
    - A list of the items in the ledger. Each line will show the description and amount. 
    - A line displaying the category total.
    """
    # title line
    category_char = len(self.category)
    star_on_left = int((30 - category_char) / 2)
    star_on_right = star_on_left if category_char % 2 == 0 else star_on_left + 1
    message = star_on_left * "*" + self.category + star_on_right * "*"
    
    # list of the items in the ledger
    for item in self.ledger:
      # about the description
      description = item["description"]
      description_shown = description[:23] if len(description) > 23 else description + " " * (23 - len(description))
      # about the amount
      amount = str(item["amount"])
      if "." not in amount:
        amount += ".00"
      else: # "." in amount:
        real, decimal = amount.split(".")
        if len(decimal) < 2:
          amount += "0"
        else: # len(decimal) >= 2:
          amount = f"{real}.{decimal[:2]}"
      amount_shown = " " * (7 - len(amount)) + amount
      # overall line for every items in the ledger
      message += "\n" + description_shown + amount_shown
    
    # a line displaying the category total
    message += f"\nTotal: {self.get_balance()}"
    # print the message
    return message

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
    
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -1 * amount, "description": description})
      return True
    else: 
      return False
      
  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item.get("amount", 0)
    return balance
  
  def transfer(self, amount, destination):
    if self.check_funds(amount):
      self.ledger.append({"amount": -1 * amount, "description": f"Transfer to {destination.category}"})
      destination.ledger.append({"amount": amount, "description": f"Transfer from {self.category}"})
      return True
    else: 
      return False
    
  def check_funds(self, amount):
    return False if amount > self.get_balance() else True


def create_spend_chart(category_list):
  """
  In the form of a bar chart, this function will display the percentage spent in each category passed in to the function.
  """
  chart = "Percentage spent by category"
  spending_by_category = []

  for category in category_list:
    spending = 0
    for item in category.ledger:
      spending += -1 * item["amount"] if item["amount"] < 0 else 0
    spending_by_category.append(spending)

  total_spending = sum(spending_by_category)
  spending_percentage = [int(str(spend * 10 / total_spending).split('.')[0]) * 10 for spend in spending_by_category]

  value_bar = {
      "\n100| " : "",
      "\n 90| " : "",
      "\n 80| " : "",
      "\n 70| " : "",
      "\n 60| " : "",
      "\n 50| " : "",
      "\n 40| " : "",
      "\n 30| " : "",
      "\n 20| " : "",
      "\n 10| " : "",
      "\n  0| " : "",
  }

  for value in spending_percentage:
    for number in range(0, 110, 10):
      value = int(value)
      str_number = f"\n{number}| " if number == 100 else (f"\n  {number}| " if number == 0 else f"\n {number}| ")
      if value < number:
        value_bar[str_number] += "   "
      else: # value percentage <= number
        value_bar[str_number] += "o  "

  for number in range(100, -10, -10):
    str_number = f"\n{number}| " if number == 100 else (f"\n  {number}| " if number == 0 else f"\n {number}| ")
    chart += f"{str_number}{value_bar[str_number]}"

  many_strip = "---" * len(category_list)
  chart += f"\n    -{many_strip}"

  category_name = [name.category for name in category_list]
  max_character = max([len(name) for name in category_name])
  name_char = [list(name) for name in category_name]

  for index in range(0, max_character):
    chart += "\n" + " " * 5
    for char in name_char:
      if index > len(char)-1:
        chart += " " * 3
      else : # index <= len(char)
        chart += f"{char[index]}  "
  
  return chart