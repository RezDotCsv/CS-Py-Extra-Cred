#Write a series of Python classes to model students, professors, course, classes, and majors. 
# Implement as many of the magic methods as make sense for your model. Submit a git repo with 
# a readme describing how to use your classes.
#I will leave the specifics up to you but you should implement things like add/drop 
# class, get_advisor/advisee, course requirements, major requirements.
#Note that a class is a specific term offering of a course which is a more general description.
#Because it is so open ended, I am offering up to 20% extra credit (this is your
#  golden parachute for those of you who have been less than studious). The standard 
# for 10% extra credit would be a barebones model with a readme ~100-150 lines of code. 
# 20% would include a full demo and documentation ~500+ lines of code.
#Submission link on google classroom soon. Notify me ahead of time if you plan to do this assignment.

#Base class for both students and professors to deal with all the naming stuff
class Human:
    listOfHumans = []
    
    #The default for when a person has no prefered name
    def  __init__(self, legalName, id: int, prefName):
        
        if(id in self.listOfHumans):
            raise ValueError('ID already exists please try a diffrent ID')
        self.listOfHumans.append(id)
        self._legalName = legalName
        self._prefName = prefName
        self._Id = id
        
    
    
  
    @property
    def id(self):
        return self._Id
    
    @property
    def name(self):
        if(self._prefName == ""):
            return self._legalName
        elif(self._legalName == ""):
            return "Person does not exist at the moment"
        else:
            return self._prefName
    @property
    def legalName(self):
        return self._legalName
    @property
    def prefName(self):
        return self._prefName
    
    @prefName.setter
    def prefName(self, name):
        self._prefName = name




class Students:
    
    #Perfect case where all info is known
    def __init__(self, human : Human, major, advisor, classesTaken):
        self._human = human
        self._major = major
        self._advisor = advisor
        self._classesTaken = classesTaken
    
   
    
    @classmethod
    def hasTaken(self):
        return self._classesTaken
    def completedTerm(self):
        self._classesTaken.append(self._classes)
        self.classes = []
    
    @property
    def human(self):
        return self._human
    @property
    def advisor(self):
        return self._advisor
    @property
    def name(self):
        return self.human.name
    @property
    def major(self):
        return self._major
    @property
    def classes(self):
        return self._classes
    
    @classes.deleter
    def classes(self):
        classes = []

    @major.setter    
    def major(self, Major):
        self._major = Major

    @advisor.setter
    def advisor(self, advisor):
        self._advisor = advisor
        
    @classes.setter
    def classes(self, classes):
        if(classes.reiqurimentsMet):
            self._classes.append(classes)
        else:
            "Student does not met " % classes.requirments
    
            
  



        
                     
#Prof class
class Professors:


    def __init__(self, human : Human, teaches, advise):
        self._human = human
        self._teaches = teaches
        self._advise = advise
    @property
    def advise(self):
        if(Students.advisor != advise):
            self._advise = Students.advisor.getter 
    @property
    def name(self):
        return self._human.name








#Classes class 
class Classes:

    def __init__(self, requirments):
        self._requriments = requirments
        
        

    @classmethod
    def requirmentsMet(self):
        for c in self._requriments:
            if(not (c in Students.hasTaken)):
                return False
        return True

    @property
    def requirments(self):
        return self._requriments
    @property
    def professor(self):
        return self.professor
    @professor.setter
    def professor(self, name):
        return self.professor.append(name)
    
    @property
    def removeProfessor(self, name):
       return self.professor.remove(name)




#course class
class Course:
    def __init__(self, Classes):
        self._course.append(Classes)

        


#majors class
class Majors:
    def __init__(self) -> None:
        pass
        


