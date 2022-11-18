from main import Human
from main import Students
from main import Classes
from main import Professors
from main import Course
from main import Majors

class Test:
    
    #Testing if human works

    
    def testCaseHuman1():
        person1= Human("Josh Fambler", 1245678, '')
        assert person1.legalName == "Josh Fambler", "Basic name testing"
        assert person1.name == "Josh Fambler"
        
        person2= Human("Josh Faler", 124578, '')
        person2.prefName = "Nax"
        assert person2.name == "Nax", "Testing Name change"
        assert person2.legalName == "Josh Faler", "Pref Name Diff from name"
        assert person2._Id == 124578
        print("Test Human 1 passed")


    #Test attempting to input someone with an ID already exists    
    def testCaseHuman2():
        Human.listOfHumans =[]
        
        person1= Human("Josh Fambler", 1245678, '')
        try:
            person2= Human("Josh Faler", 1245678, '')
            print("Test Failed")    
        except: 
            ValueError('ID already exists please try a diffrent ID')
            print("Test Human 2 passed")
            Human.listOfHumans =[]
    def testCaseProfessor():
        cS = Classes("Cs 220", "")
        p1 = Human("Jemmy Raz", 12435, '')
        
        prof1 =Professors(p1, cS, "" )
        assert (prof1.name) == "Jemmy Raz", "Naming is passedown"
        print("testCaseProfessor passed") 
    def testCaseStudent1():
        p1 = Human("Jemmy Raz", 12435, '')
        s1 = Students(p1, "Clowning", "Rocko Le Rock", '')
        assert (s1.name) == "Jemmy Raz", "Naming is passedown"

    

        
    if __name__ == "__main__":
        testCaseHuman1()
        testCaseProfessor()
        testCaseHuman2()
        testCaseStudent1()

        
        
