# import ohno
# import sys

# print(sys.path)

# print(ohno.stats_range([1,4,5,2,6]))
# print(random)
# i = 0

# def change(i):
#     i = 9

# change(i)
# print(i)

my_file = open("hello.txt", "w")
my_file.write('hello world\tme')
my_file.close()

my_file = open('hello.txt', 'r')
data = my_file.read().split('\t')
print(data)
my_file.close()