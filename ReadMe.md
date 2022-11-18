
All cless are made in the main file.
Test.py functions as a testing ground to experiment with the functionality of 
the classes as well
Classes will all for the creation of Students, Professors, Majors, Classess, and Courses.

Both students and Professors will use the helper class Human to transfer over some basic
functionality as to not repeat lines of code

Below is a demo a short demo of some of the class and how this can look like in practice as to how this would look like
thanks to the @property I am able to pass up information from the 
subclasses and retain the same naming convention to help with readability on the user end


| Class         | Methods       | Output         | Raw                |
| ------------- |:-------------:| --------------:|-------------------:|
| Human         |.name          |"Name"          |_human.nam          |
| Students      |.name          | "Name"         |student._human.name |
| Professors    |.name          | "Name"         |student._human.name |
| Classes       |.name          | "Name"         |classes._name       |

Note the last one is not human and is not using the human subclass, however it is still using the same conventions for simplicity


