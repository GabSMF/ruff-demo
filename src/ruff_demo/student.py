import os
import math


class Student:
    def __init__( self,name:str, grades:list[int] ):
        self.name=name
        self.grades=grades

    def average(self)->float:
        return(sum(self.grades))/len(self.grades)

    def summary(self)->str:
        return   f"{self.name} has average {self.average():.1f}"
