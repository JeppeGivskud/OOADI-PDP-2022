from Orders import*

class User():
    def __init__(self,user_id,name,e_mail):
        self.user_id=user_id
        self.name=name
        self.e_mail=e_mail

class SupportStaff(User):
    def __init__(self, user_name, user_password, user_id, name, e_mail):
        super().__init__(user_id, name, e_mail)
        self.user_password = user_password
        self.user_name = user_name

    def change_user_info(self,User):
        print(User)
        User.user_password=333

class CostumerWithProfile(User):
    def __init__(self, user_name, user_password,phone_number, user_id, name, e_mail):
        super().__init__(user_id,name,e_mail)
        self.user_password = user_password
        self.user_name = user_name
        self.phone_number=phone_number
        self.Orderlist=[]

    def retrieve_orderlist(self,Orderlist):
        self.Orderlist.append(Orderlist)

class CustomerWithoutProfile(User):
    def __init__(self, phone_number, user_id, name, e_mail):
        super().__init__(user_id, name, e_mail)
        self.phone_number = phone_number
        self.Order=Order

    def retrieve_orderlist(self,Order):
        self.Order = Order

class TivoliManagement(User):
    def __init__(self, user_name, user_password, user_id, name, e_mail):
        super().__init__(user_id,name,e_mail)
        self.user_password = user_password
        self.user_name = user_name

    def create_event(self):
        pass

    def change_event(self):
        pass

    def delete_event(self):
        pass

    def release_tickets(self):
        pass

    def view_tickets(self):
        pass

