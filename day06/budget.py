class Category:

  def __init__(self, category_name):
    self.ledger = []
    self.category_name = category_name
    self.total_withdrawed = 0

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
      self.total_withdrawed += amount
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

  def total_amount_withdrawed(self):
    return self.total_withdrawed
    

def create_spend_chart(categories):
  categories_list = [x.category_name for x in categories]
  h2 = f"Percentage spent by category\n"

  withdraws = []
  for _ in categories:
    withdraws.append((
      _.category_name,
      _.total_amount_withdrawed()
    ))
  total = sum([x[1] for x in withdraws])
  percentage = [int(str(x[1]/total)[2]) for x in withdraws]
  
  middle = ""
  y_axis = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|' , ' 30|', ' 20|', ' 10|', '  0|']
  dataframe = {
    0: y_axis
  }
  for i,c in enumerate(categories):
    cat_bar = [' o '] * (percentage[i]+1)
    while len(cat_bar) < 11:
      cat_bar.insert(0, '   ')
    dataframe[i+1] = cat_bar

  for i in zip(*dataframe.values()):
    middle += ''.join(i) + ' \n'
  
  last = "    " + "---"*len(categories_list) + "-\n"
  max_len = len(max(categories_list, key=len))
  c = [ x.ljust(max_len) for x in categories_list ]
  for name in zip(*c):
    last += '     ' + '  '.join(name) + '  \n'

  return (f"{h2}{middle}{last.rstrip()}  ")
  
  