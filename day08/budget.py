class Category:

  def __init__(self, category_name):
    self.ledger = []
    self.category_name = category_name
    self.money_spent = 0

  def deposit(self, amount, description=''):
    self.ledger.append({
      'amount': round(float(amount),2),
      'description': description
    })

  def withdraw(self, amount, description= ''):
    if self.check_funds(amount):
      self.ledger.append({
        'amount': -abs(round(float(amount), 2)),
        'description': description
      })
      self.money_spent += amount
      return True
    else:
      return False

  def get_balance(self):
    balance = sum([entry['amount'] for entry in self.ledger])
    return balance

  def transfer(self, amount, to_category):
    
    if self.check_funds(amount):
      description_to = f"Transfer to {to_category.category_name}"
      description_from = f"Transfer from {self.category_name}"

      self.ledger.append({
        'amount': -abs(round(float(amount), 2)),
        'description': description_to
      })

      to_category.ledger.append({
        'amount': round(float(amount), 2),
        'description': description_from
      })
      return True
      
    else:
      return False

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    else:
      return False

  def __str__(self):
    h1 = f"{self.category_name:*^30}\n"
    middle = ''
    total = 0
    for entry in self.ledger:
      amount = f"{entry['amount']:.2f}"
      middle += f"{entry['description'][:23]:<23}{amount:>7}\n"
      total += entry['amount']
    last = f"Total: {round(total,2)}"
    
    return h1+middle+last


def create_spend_chart(categories):
  h1 = "Percentage spent by category\n"
  graph = ''
  data = []
  total_spent = sum([c.money_spent for c in categories])
  for c in categories:
    c_n = c.category_name
    perc = c.money_spent/total_spent
    data.append({
      'name': c_n,
      'perc': perc
    })

  for i in range(10,-1,-1):
    graph += f"{i*10}|"
    
    