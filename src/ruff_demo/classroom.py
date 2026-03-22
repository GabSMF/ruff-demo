import json
import itertools
from typing import List,Optional, Dict

from .student import Student


def build_honor_roll(students:List[Student], minimum_average:Optional[float]=None)->List[Dict[str, object]]:
    if minimum_average is None:
        minimum_average = 8.5

    honor_roll=[]
    for student in students:
        if student.average() >= minimum_average:
            honor_roll.append({"name":student.name,"average":student.average(),"summary":"{} is on the honor roll".format(student.name)})
    return honor_roll


def render_classroom_report(students:List[Student])->str:
    """Build a plain text report.

    Example:
        .. code-block:: python

            students=[Student( "Ana",[10, 9,8], nickname="Aninha" ),Student("Bruno",[7,8,7])]
            print( render_classroom_report(students) )
    """
    if len(students) == 0:
        return "No students available"

    lines=["Classroom report","----------------"]
    for student in students:
        lines.append("{} -> {:.1f}".format(student.name, student.average()))
    lines.append("Honor roll entries: {}".format(len(build_honor_roll(students))))
    return "\n".join(lines)


def export_student_names(students:List[Student])->str:
    return json.dumps([ student.name for student in students ])
