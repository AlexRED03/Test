# n = int(input())
# stars = "*"
# while len(stars) <= n:
#     print(stars)
#     stars += "*"

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# a = int(input())
# b = int(input())
# s = 0
# while a <= b:
#     s += a
#     a += 1
# print(s)

# a = int(input())
# s = 0
# while a != 0:
#     s += a
#     a = int(input())

# print(s)

# a = int(input())
# b = int(input())
# c = 1
# while c % a != 0 or c % b != 0:
#     c += 1
# print(c)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)    

# a = int(input())
# while a < 101:
#     if a < 10:
#         a = int(input())
#         continue
#     print(a)
#     a = int(input())
#     if a > 101:
#         break
# while True:
#     a = int(input())
#     if 10 < a < 100:
#         print(a)
#     if a > 100:
#         break

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())  
# for j in range (c, d+1):
#     print(' ', j, sep='\t', end='')
# print ()
# for i in range (a, b+1):
#     print(i, end='\t')    
#     for j in range (c, d+1):
#         print (i*j,  end='\t')
#     print ()

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# for i in range(c, d + 1):
#     print("\t" + str(i), end="")
# print()
# for i in range(a, b + 1):
#     print(i, end="\t")
#     for n in range(c, d + 1):
#         print(i * n, end="\t")
#     print()

# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# for i in range (a,b+1):
#     if i % 2 == 1:
#         s +=i
# print(s)

# a,b = (int(i) for i in input().split())

"""Способ ввода другой в одной строке через пробел"""

# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# if s%2 == 0:
#     a+=1
# for i in range(a,b+1,2):
#     s+=i9
# print(s)

# 
# a = int(input())
# b = int(input())
# s = 0
# p = 0
# for i in range(a,b+1):
#     if i % 3 == 0:
#         s += i
#         p += 1
# print(s/p)

# x = [x for x in range(int(input()),int(input()) + 1) if x % 3 == 0]
# print(sum(x)/len(x))

# class Person:
#     def __init__(self, id):
#         self.id = id
# some_person = Person(100)
# some_person.__dict__['age'] = 30
# print (some_person.age + len(some_person.__dict__))

# class Income:
#     def __init__(self, id_):
#         self.id_ = id_
#         id_ = 100
# income_1 = Income(1000)
# print(income_1.id_)    

# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
 
        
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.courses_in_progress += ['Python']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]
 
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)


# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
 
#     def add_courses(self, course_name):
#         self.finished_course.append(course_name)   
 
     
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
        
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)


print (dir (str))