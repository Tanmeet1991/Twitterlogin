class Detail:
    def userlogin(self,email,password,number):
        self.__email = email
        self.__password = password
        self.__phone = number
        return self.__email, self.__password, self.__phone
    
    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def set_password(self, password):
        self.__password = password
        
    def get_pasword(self):
        return self.__password
    
    def set_phone(self, number):
        self.__phone = number
        
    def get_phone(self):
        return self.__phone
    
        
login_1 = Detail()

with open('D:\\Twitter login\\email.txt', 'r') as myfile:
    user = myfile.readline()
login_1.set_email(user)
with open('D:\\Twitter login\\password.txt', 'r') as myfile:
    password = myfile.readline()
login_1.set_password(password)

with open('D:\\Twitter login\\phone.txt', 'r') as myfile:
    number = myfile.readline()
login_1.set_phone(number)

if __name__ == "__main__":

    print(login_1.get_email())
    print(login_1.get_pasword())
    print(login_1.get_phone())
