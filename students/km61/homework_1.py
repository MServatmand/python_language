#task1------------------------------------------------------------
""" �����:��������� ��������, ��� ������ ��� ����� � ����� �� ����. ����� ����� ���������� ������� � �������� �����.
������ ����:�3 ������ �����. ������ ����� ���������� ������� � �������� �����.
������� ����:�������� ���� ����� ����� �� �����.
"""



#write your answer here...
print('������� ��� ����� �����')
number_one=(input()) #��������� ��������� ������ �����
number_two=(input())#��������� ��������� ������ �����
number_three=(input())#��������� ��������� ������ �����
print(������ ����� �����:�+a+b+c+, '!') #����� �� ����� ����� ������ �����





#task2------------------------------------------------------------
�����:��������� ��������, ��� ������ ������� ���� ������ ������������ ���������� �� �������� ���� �����. ���������� ������� ������� ������ � ������� ������.
������ ����:�2 ������ �����. ������ ����� ���������� ������� � �������� �����.
������� ����:�������� ����� ���������� �� �����.
"""



#write your answer here...
      print('������� �������� ������� �������������� ������������')
cathetus_one=int(input())
      cathetus_two=int(input())
square=(1/2* cathetus_one * cathetus_two)\print('������� ����������� �����:', square)



#task3------------------------------------------------------------
"""
�����:�N �������� �������� K ����� � ���������� �� �� ����� ������. ��������� ������ ���������� � ������. ������ ����� ������ ����� �������? ������ ����� ���������� � ������?
�������� ������ ����� N � K. ���� ������� ������� ��� �����: ������ �� ���������� ���� �������.
������ ����:�2 ����� �����. ������ ����� ���������� ������� � �������� �����.
������� ����:�������� ��� �����. ����� - ������� ����� � ��������, ����� - ������� �����, �� �������� � ������.


#write your answer here...

print('������� ���������� ���������')
student_amount=int(input()) #��������� ��������� ���������� ���������
print('������� ���������� �����') 
apple_amount=int(input()) #��������� ��������� ���������� �����
everyone=(apple_amount//student_amount) #������������� ��������  ������ ����� �� �������
apple_rest=apple_amount%student_amount #������������� �������� ������� �����
print('���������� �����, ������� ������� ������ �������:', everyone )
print('���������� �����, ������� ��������� � �������:', apple_rest)



#task4------------------------------------------------------------
"""
�����:������ ����� N - ������� ������, ����������� ���� ������. ������ ����� � ������ ���� ���������� �������� ��������, ���� �� ���� ����� 00:00?
�������� ������� �������� ��� �����: ������� ����� (�� 0 �� 23) � ������� ������ (�� 0 �� 59). ³����� �� �����, �� ��������� � ������ ���� ������ ������� ����, ���� ����� N ���� ���� ��������� �������.
������ ����:�1 ���� �����, �� ������� ����������
������� ����:�������� ��� �����. ����� - ������, ����� - �������.


#write your answer here...

print('������� ���������� ����� ����� ��������')
minute_amount=int(input()) #��������� ����������� �������� ���������� �����
hour=minute_amount//60 #������ ������ ���������� �����
min=minute_amount%60 #������ ������ ���������� �����
print(hour,'���� �', min, '������')



#task5------------------------------------------------------------
"""
�����:��������� ��������, ��� ��� �����������, �������� ����� "Hello", ��'� ����������� � ���� ������ ���� �����. ��������� �Hello, Mike!�
������ ����:���'� �����������
������� ����:�������� ����� ���������

"""



#write your answer here...
print('������� ���')
name=input() #���������� ������������� ��������
print('Hello, ' + name+ '!')


#task6------------------------------------------------------------
"""
�����:��������� ��������, ��� ����� ���� ����� � ����� ���� ��������� � �������� �������� �� ��������:
�The next number for the number 179 is 180.
The previous number for the number 179 is 178.������ ����:����� �����
������� ����:���� ����� �� ��������� � �������� ��������.
"""



#write your answer here...

print('������� ����� �����')
number_one=int(input()) # ������������� �������� ������� �����
previous=number_one-1 #���������� ��� ������� ����������� ����� �������
next=number_one+1 #���������� ��� ������� ���������� ����� �������
print('���������� �����:', previous)
print('��������� �����:', next)

#task7------------------------------------------------------------
"""
�����:������ ������� ���������� ��� ��� ����� ����� �� ������ �� ����� �����. � ������� ���� ��������� ���������� ����� ��� �����, � ����������, �� �� ����� ������ ���� ����� �� ����� ���� �����. ��� ��������� ������� ����� ��������� ��������?
������ ����:�3 ����� ����� - ������� ����� � ������ ����. ������ ����� ���������� ������� � �������� �����.
������� ����:������ - ������� �����
 """
#write your answer here...
print('������� ���������� �������� ������ ������')
amount_first_group=int(input())
print('������� ���������� �������� ������ ������')
amount_second_group=int(input())
print('������� ���������� �������� �����e� ������')
amount_third_group =int(input())
amount_tables=int((amount_first_group//2 + amount_first_group%2)+(amount_second_group//2+ amount_second_group%2) + (amount_third_group//2+ amount_third_group%2))
print('����������� ���������� ����:', amount_tables)
