class Solution:
    def countStudents(self, students, sandwiches) -> int:
        student_count = [0, 0]
        for student in students:
            student_count[student] += 1

        for sandwiche in sandwiches:
            if student_count[sandwiche] > 0:
                student_count[sandwiche] -= 1
            else:
                break

        return sum(student_count)


s = Solution()
print(s.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
print(s.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
