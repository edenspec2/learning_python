##'meow meow meow'.split()
import numpy as np

class Person():
    def __init__(self, sex='male', give_random_location=True):
        self.sex=sex
        if give_random_location:
            self.current_loaction=self.give_location()
        else:
            self.current_location=np.array([0, 0, 0])
        
    def speak(self, sentence='yes'):
        print(sentence)

    def move(self,coordiantes):
        self.current_location=self.current_location+coordiantes
        
    def give_location(self):
        self.current_location=np.array([0, 0, 0])

class MailMan(Person):
    def deliver_mail(self):
        self.speak('You got mail')
        
if __name__=='__main__':
    my_buddy=Person('female') # sex='male'
    my_mailman=MailMan(give_random_location=False)
    my_mailman.deliver_mail()
    my_mailman.move([1, 1, 2])
    print(my_mailman.current_location)
