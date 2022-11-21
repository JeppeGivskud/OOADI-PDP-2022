from User import*

class ListOfUsers():
    def __init__(self):

        self.customers= []

    def add_customer(self,customer):
        self.customers.append(customer)

    def delete_customer(self,customer):
        index = self.customers.index(customer)
        print(self.customers[index].name)
        del self.customers[index]

    def Example(self):
        User1 = CostumerWithProfile("JørgenFisen", "12345678", "70707070", "Jørgen", "hansen@gmail.com")
        User2 = CostumerWithProfile("BennyManden", "098765431", "80808080", "Benny", "hansen@gmail.com")
        User3 = CostumerWithProfile("HanseDrengen", "13243546", "90909090", "Hans", "hansen@gmail.com")
        User4 = CostumerWithProfile("YvonnePigen", "4444444", "60606060", "Yvonne", "hansen@gmail.com")
        self.add_customer(User1)
        self.add_customer(User2)
        self.add_customer(User3)
        self.add_customer(User4)

if __name__=="__main__":
    All_Users =ListOfUsers()
    All_Users.Example()
    print(All_Users.customers[0].name)
