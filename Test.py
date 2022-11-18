from main import Human
from main import Students
from main import Classes
from main import Professors
from main import Course
from main import Majors

class Test:
    
    #Testing if human works
    def testCaseHuman():
        person1= Human("Josh Fambler", 1245678, '')
        assert person1.legalName == "Josh Fambler", "Basic name testing"
        assert person1.name == "Josh Fambler"
        person1.prefName = "Nax"
        assert person1.name == "Nax"

    if __name__ == "__main__":
        testCaseHuman()
        print("Test Human passed")
