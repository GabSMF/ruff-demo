import os
import math
from typing import Dict, List, Optional


class Student:
    def __init__(
        self,name:str, grades:List[int], nickname:Optional[str]=None, notes:Optional[List[str]]=None
    ):
        self.name=name
        self.grades=grades
        self.nickname=nickname
        self.notes=notes or []
        self.profile={"has_nickname": self.nickname is not None, "notes_count":len(self.notes)}

    def average(self)->float:
        if len(self.grades) == 0:
            return 0
        return sum(self.grades)/len(self.grades)

    def best_grade(self)->int:
        return max(self.grades) if self.grades else 0

    def label(self)->str:
        alias = self.nickname if self.nickname is not None else self.name
        return "{} ({:.1f})".format(alias,self.average())

    def to_record(self)->Dict[str, object]:
        return {
        "name":self.name,
        "nickname":self.nickname,
        "average":self.average(),
        "best_grade":self.best_grade(),
        "notes":self.notes,
        }

    def summary(self)->str:
        label=self.label()
        average=self.average()
        return   "{} has {} grades and average {:.1f}".format(label,len(self.grades),average)
