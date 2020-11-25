class Category:
    ledger = []
    
    def __init__(self, title):
        self.title = title
        
    def __str__(self):
        string = f'{self.title:*^30}\n'
        for transaction in self.ledger:
            string+=f"{transaction['description'][:23]:<23}{transaction['amount']:>7.2f}\n"
            
        string += f"Total: {self.get_balance()}"
        return string
        
    def deposit(self,amount, description = ""):
        self.ledger = []
        transaction = {"amount":amount, "description": description}
        self.ledger.append(transaction)

    def withdraw(self,amount, description = ""):
        if self.check_funds(amount):
            EXISTING = False
            for transaction in self.ledger:
                if description in transaction:
                    transaction = {"amount":transaction["amount"]+(-amount), "description": description}
                    EXISTING = True 
            if not EXISTING:
                transaction = {"amount":-amount, "description": description}
                self.ledger.append(transaction)
            return True
        else:
            return False
        
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance
        
    def transfer(self,amount,category):
        if self.check_funds(amount):
            transaction = {"amount": -amount, "description": f"Transfer to {category.title}"}
            category.deposit(amount,f"Transfer from {self.title}")
            self.ledger.append(transaction)
            return True
        return False
    
    def check_funds(self,amount = 0):
       
        return amount <= self.get_balance()
    
def create_spend_chart(categories):
    string = "Percentage spent by category\n"
    spent_by_category = []
    percentage = []
    total_spent = 0
    titles = []
    
    for category in categories:
        initial = category.ledger[0]['amount']
        balance = category.get_balance()
        spent = initial-balance
        total_spent += spent
        spent_by_category.append(spent)
        titles.append(category.title)

    max_length = len(max(titles, key = len))
    v_title = [[' ' for y in range(len(categories))] for x in range(max_length)]
    
    for spend in spent_by_category:
        spent_perc = int((spend/total_spent) * 100)
        percentage.append(spent_perc)    
    
    for row in range(max_length):
        for col in range(len(categories)):
            try:
                v_title[row][col] = titles[col][row]
            except Exception:
                pass
    
    for i in range(10,-1,-1):
        string+=f'{i*10:>3}| '
        for x in range(len(categories)):
            if percentage[x] >= i * 10:
                string+="o  "
            else:
                string+="   "
        string+="\n" 
    
    string+="    " + "--"*(len(categories)+2) + "\n"
    for title in v_title:
        string+="     "
        for t in title:
            string+=f"{t}  "
        
        if title != v_title[-1]:
            string+="\n" 
        
    return string