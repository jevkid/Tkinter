import os, sys
lib_path = os.path.abspath('../../classes/')
print lib_path
sys.path.append(lib_path)

# import mymodule

# import sys
# print sys.path
# directory = sys.path[0]
# index = directory.rfind('code')
# directory = directory[0:index]
# directory += "classes"
# sys.path.insert(0,directory)

from storage import Storage
from questionnaire import Questionnaire
from course import Course
from staff import Staff

q = Questionnaire()