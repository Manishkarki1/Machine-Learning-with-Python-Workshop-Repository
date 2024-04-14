# we must have to pass Exception in customException
# class CustomError(Exception):
#     def __init__(self,message,code=None):
#         super().__init__(self,message,code)
#         self.code=code
#         self.message=message
#     def __str__(self):
#         return f"Error with code {self.code}" if self.code else "Error occur"

# num=2
# try:
#     if num==2:
#         raise CustomError('Error')
#     else:
#         print('you are good')
# except CustomError as e:
#     print(e)

# lru cache
# from functools import lru_cache 
# import time
# @lru_cache(maxsize=None)
# def calculate_sq(n):
#     time.sleep(5)
#     return n * n

# print(calculate_sq(25))

# print(calculate_sq(28))
# print(calculate_sq(2))

# GIL(global interpreter lock)
#  Threading and multiprocessing
import threading
import time

def waste_time(n):
    time.sleep(n)
    print(f'successfully wasting our life by {n} sec')

# Corrected thread creation
t1 = threading.Thread(target=waste_time, args=(2,))
t2 = threading.Thread(target=waste_time, args=(3,))
t3 = threading.Thread(target=waste_time, args=(10,))
t1.start()


t2.start()
t3.join(t2)


