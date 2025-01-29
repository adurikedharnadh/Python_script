class example:
    def __init__(self, str1, str2):
        self.name1= str1
        self.name2= str2
        self.name3="Devops is key to success"


    def print_value(self):
        print(self.name1,self.name2, self.name3)

    def display_value(self,var1):
        print(self.name1, self.name2, var1)




var = example("Hello", "Welcome")
var.print_value()
var.display_value("Training")


var1 = example("Kedhar is ", "Devops Engineer")
var1.print_value()
var1.display_value("All the best for the job")


var2 = example("Devops Engineer", "Have a great day")
var2.print_value()
var2.display_value("Aws is core")
