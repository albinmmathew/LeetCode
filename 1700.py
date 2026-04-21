# Number of Students Unable to Eat Lunch

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0
        while count<len(students) and sandwiches:
            if students[0] == sandwiches[0]:
                count = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                count+=1
                students.append(students.pop(0))
        return len(sandwiches)