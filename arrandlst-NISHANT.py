from array import *
import numpy as np


arr1=array("i")
# print(arr1)
arr2=array("i",[1,2,3,4])
# print(arr2)


arr3=np.array([],dtype=int)
# print(arr3)
arr4=np.array([2,3,4,5])
# print(arr4)

arr5=array("i",[1,2,3,4])
arr5.insert(0,0)
# print(arr5) #the time complexity of insertation of an elem in array is O(n) because it depends on the number of elem needs to be shifted so we will go for the worst case that is we will insert the elem at the begning of the array.and the space complexity is O(1)



# my_array=array("i",[1,2,3,4,5,6])
# my_array.append(10)
# print(my_array)
# my_array.insert(0,10)
# print(my_array)
# # print(my_array[-1])
# # print(my_array.index(10))
# print(my_array.count(10))
# my_array.pop()
# my_array.remove(3)

# print(my_array.buffer_info())
# newarr=array("i",[1,2,3,4])
# my_array.extend(newarr)
# print(my_array.tolist())
# print(my_array[:-1])



twodarray=np.array([[1,2,3,4],[5,6,7,8],[2,2,2,2],[9,1,1,3]])
# print(twodarray)

# newtwodarray1=np.insert(twodarray,0,[[3,4,5,6]],axis=1)
# print(newtwodarray1)
# axis=0 for row
# axis=1 for column
# newtwodarray2=np.append(twodarray,[[1,2,2,1]],axis=0)
# print(newtwodarray2)

# the time complexity of insertation of an array in two dimensional array is O(mn)


def access_element(array,rowidx,colidx):
     if rowidx>=len(array) and colidx>=len(array[0]):#-------O(1)
          print("incorrect index")#--------------------------O(1)
     else:
          print(array[rowidx][colidx])#----------------------O(1)

# access_element(twodarray,2,2)#---------------O(1)

def traverse(array):
     for i in range(len(array)):
          for j in range(len(array[i])):
               print(array[i][j])


# traverse(twodarray)

def linearsearch(array,el):
     get=False
     for i in range(len(array)):
          for j in range(len(array[i])):
               if array[i][j]==el:
                    print("row:",i,"col:",j)
                    get=True
     if not get:
          print("element not found")

# linearsearch(twodarray,1)


new2darray=np.delete(twodarray,2,axis=1)
# print(new2darray)

my_list=[1,2,5,6,3,4,5]
# my_list[0:2]=["a","b"]
# print(my_list[0:2])


# print("nishant"[::-1])#how can  you reverse a string in python

# deleting element of a list
new_list=["a","b","c","d","e"]
# print(new_list.pop())#this method also return the value which is deleted
# del new_list[0:3]
# new_list.remove("d")
# print(new_list)


# linear search

def linear_search(p_list,p_target):
     for idx ,value in enumerate(p_list):#-------------O(n)
          print(idx,value)#----------------------O(1)
          if value==p_target:#----------------------O(1)
               return idx#----------------------O(1)
     return -1

# print(linear_search(new_list,"a"))#----------------------O(n) and space complexity O(1) because no extra memory is reqired 

#list operations and funcions
l1=[1,3,5]
l2=[4,2,8]
l3=l1+l2# + operator is used to concat two or more list 
# print(l3)
l4=l1*5# * operator is used to repeat element in list 
# print(l4)



# convert a string to list
# st="string"
# ls=list(st)
st="s-t-r-i-n-g"
ls=st.split("-")
# print(ls)
backtostr="".join(ls)
# print(backtostr)


# list comprehension
lst=[1,2,3,4,5]
new_lst=[i*2 for i in lst]
# print(new_lst)

my_list2=[1,4,-6,4,-2,0,-7,-5,3,5,-6,4,-2]
newmy_list2=[i for i in my_list2 if i>=0]
# print(my_list2)
# print(newmy_list2)

sentence='my name is Nishant Sharma'
def const(letter):
     vowel='aeiou'
     return letter.isalpha() and letter.lower() not in vowel
   
constlist=[letter if const(letter) else "-" for letter in sentence ]
# print(constlist)



# print(" ".isalpha()) this is false

# def number(number):
#      return number if number>0 else "negative number"  # see how logics can we written 
# print(number(-2))


# project 1

# noof_day=int(input("How many day's Temperature? "))
# data=[]
# for i in range(1,noof_day+1):
#      ask=float(input(f"Day {i}'s high Temp: "))
#      data.append(ask)
# avg=sum(data)/len(data)
# print(f"Average={avg}")
# count=0
# for i in data:
#      if i>avg:
#           count+=1
# print(f"{count} day(s) above average")

# def missing_number(arr,leng):
#     missing=[]
#     el=1
#     for i in range(1,leng+1):
#         if i not in arr:
#             missing.append(i)
#     return missing

# print(missing_number([1,4,6],6))





def first_second(my_list):
    first=max(my_list)
    my_list.remove(first)
    second=max(my_list)
    while first==second:
         my_list.remove(first)
         second=max(my_list)
         
    return first,second

# print(first_second([2,3,4,5,6,7,8,9,9,9,9,9,9,9,9]))



def remove_duplicates(arr):
    result=[]
    copy=[i for i in arr]
    for i in range(len(arr)):
        el=arr.pop()
        if el not in arr:
            result.append(el)
    if not result:
        return copy
    else:
        result.reverse()
        return result


# p=remove_duplicates([3,5,7,2,5])
# print(p)


# def rotate(twod):
#     result=[]
#     twod.reverse()
#     for i in range(len(twod)):
#         row=[]
#         for j in range(len(twod[0])):
#             row.append(twod[j][i])
#         result.append(row)
#     return result

# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))


# def longestPalindrome(s):
#         res=""
#         for i in range(len(s)):
#             substr=s[i]
#             for j in range(i+1,len(s)):
#                 substr+=s[j]
#                 if substr==substr[::-1]:
#                      if len(substr)>len(res):
#                           res=substr
#         if len(s)==1:
#              return s
#         else:
#              return res 
                     
# print(longestPalindrome("babad"))




# def rotate(nums, k):
#      arr=[]
#      if k>len(nums):
#           k=k%len(nums)
#      for i in range(len(nums)-1,len(nums)-k-1,-1):
#           el=nums.pop(i)
#           arr.append(el)
#      nums.reverse()
#      for i in arr:
#           nums.append(i)
#      nums.reverse()
#      print(nums)

# rotate([1,2,3,4,5,6,7],3)

d=dict([('name', 'nishant'), ('age', 21), ('course', 'cs'), (1, 123)])
my_dict={"name":"nishant","age":21,"course":"cs"}

# for i in my_dict:
#      print(i,my_dict[i])

# del my_dict["name"]

# el=my_dict.pop()#you can't use like this you have to specifa a key 

# el=my_dict.pop("name","if you not give this parameter this is rais an error so give a value here which will retrn when this method cant find the key")# this return the value of deleted key value pair
# print(el)

# el=my_dict.popitem()# this delete the last k v pair and return it in the form of tuple

# my_dict.clear()

# my_dict2=my_dict.copy()
# del my_dict2["name"]
# print(my_dict)
# print(my_dict2)

# new_dict={}.fromkeys([1,2,3,4],0)
# print(new_dict)

# el = my_dict.get("name","given key does't exist")
# print(el)

# meo=my_dict.items()
# print(meo)

# key=my_dict.keys()
# print(key)

val=my_dict.setdefault("name","added")
print(val)
print(my_dict)



# new_dic={1:"a",2:"b",3:"c","age":22}
# my_dict.update(new_dic)
# print(my_dict)


# dict_1=dict(name="nishant",age=21)
# dict_1["age"]=20
# print(dict_1)



import random
city_names=["paris","london","rome","berlin","madrid"]

city_temp={city:random.randint(20,30) for city in city_names}

high_temp_city={key:value for (key,value) in city_temp.items() if value>25}




# print(city_temp)
# print(type(city_temp.items()))
# print(high_temp_city)


def count_word_frequency(words):
     dic=dict()
     for i in range(len(words)):
          w=words[i]
          c=1
          for j in range(i+1,len(words)):
               if w==words[j]:
                    c+=1
          if w not in dic.keys():
               dic[w]=c
        
     return dic
# res=count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] )
# print(res)

# l= ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']



def max_value_key(my_dict):
     res=0
     for key in my_dict:
          if my_dict[key]>res:
               res=my_dict[key]
     for key in my_dict:
          if my_dict[key]==res:
               return key
# print(max_value_key({'a': 5, 'b': 9, 'c': 2}))


# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------

# tuples
# tuples are immutable and can have duplicate elements of any data type
my_tuple1=tuple()
my_tuple2=()
my_tuple3=(1,)
my_tuple4=tuple("123345")
my_tuple5=("a","b","c")


# print(type(my_tuple1))
# print(type(my_tuple2))
# print(my_tuple3)
# print(my_tuple4)
# print(my_tuple5)

# print(my_tuple5.index("a"))
# s=max(my_tuple4)
# s=min(my_tuple4)
# print(s)

# l=[1,2,3,4]
# tup=tuple(l)
# print(tup.__len__())
# print(len(tup))


def tuple_elementwise_sum(tuple1,tuple2):
    return tuple([tuple1[i]+tuple2[i] for i in range(len(tuple1))])
# print(tuple_elementwise_sum((1, 2, 3),(4, 5, 6)))



def concatenate_strings(input_tuple):
     s=""
     for i in input_tuple:
          s=s+i+" "
     return s[:-1]


print(concatenate_strings(('Hello', 'World', 'from', 'Python')))
