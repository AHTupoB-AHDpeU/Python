import os
from datetime import datetime

name = str(datetime.today().date())
os.mkdir(name)
print(name)

file = open("TEST.txt", "a+",
            encoding="utf-8")
file.close()
os.rename("C:\\Users\\antip\\PycharmProjects\\pythonProject8\\TEST.txt", "C:\\Users\\antip\\PycharmProjects"
                                                                         "\\pythonProject8\\{}\\TEST.txt".format(name))

os.mkdir("C:\\Users\\antip\\PycharmProjects\\pythonProject8\\{}\\New_directory".format(name))
os.rename("C:\\Users\\antip\\PycharmProjects\\pythonProject8\\{}\\TEST.txt".format(name),
          "C:\\Users\\antip\\PycharmProjects"
          "\\pythonProject8\\{}\\New_directory\\TEST.txt".format(name))
