import pickle
class Students:
    
    def gets(self):
        self.name=input("Enter Name of student :")
        self.enroll=input("Enter Enrollment number :")
        self.sem=input("Enter Semester :")
        self.branch=input("Enter branch :")
        self.ph=input("Enter phone number :")
                   
    def display(self):
        print(f"Name:{self.name}\tEnrollment no.:{self.enroll}\tSemester:{self.sem}\tBranch:{self.branch}\tPhone no.:{self.ph}")
        
    def profile(self):
        bn=input("Enter your enrollment number to display your profile:")
        k=0
        with open("student.pkl",'rb') as f:
            while (1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.enroll==bn:
                            print("YOUR PROFILE:-")
                            print("**************************************")
                            i.display()
                            k=1
                except EOFError:
                    if k!=1:
                        print("No record found")
                    break
                    
    def View_issued_book(self):
        bn=input("Enter your enrollment number:")
        k=0
        with open("issue_book.pkl",'rb') as f:
            while (1):
                try:
                    obj=pickle.load(f)
                    if obj[2]==bn:
                        print(f"Book ISBN:{obj[0]}\tBook Title:{obj[1]}\tDue Date:{obj[4]}")
                except EOFError:
                    if k!=1:
                        print("No record found")
                    break
                    
    def check_fine(self):
        bn=input("Enter your enrollment number:")
        k=0
        with open("issue_book.pkl",'rb') as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    if(bn==obj[2]):
                        k=1
                        t=date.today()
                        l=t-obj[4]
                        if(l.days>0):
                            print(f"Book:{obj[1]}\tYour Fine is rupees:{l.days*0.50}")
                        else:
                            print(f"Book:{obj[1]}\tNo fine")
                except EOFError:
                    if k!=1:
                        print("Enrollment Number Not Found")
                    break
                    
    def display_book(self):
        with open("book.pkl",'rb') as f:
            print(f"\nBOOK RECORD:-")
            print("***************************************************************************************")
            while (1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        i.displayb()
                except EOFError:
                    print("Data read is completed")
                    break