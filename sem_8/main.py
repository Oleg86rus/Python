# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text)
#

# with open('example.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line[:-1])

# with open('example.txt', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     while line:
#         print(line[:-1])
#         line = file.readline()


# with open('example.txt', 'r', encoding='utf-8') as file:
#      text = file.read()
#      print(text.splitlines())

# with open('example.txt', 'r', encoding='utf-8') as file:
#      text = file.readlines()
#      print(text)


# with open('example.txt', 'a', encoding='utf-8') as file:
#      some_list = ['hello', 'world', 'how', 'are', 'you']
#      for el in some_list:
#          file.write(el + '\n')

# import json
# some_dict = {1: 2, 2: 3}
# with open('example.txt', 'w', encoding='utf-8') as file:
#     json.dump(some_dict, file)

with open('example.txt', 'w', encoding='utf-8') as file:
    some_dict = {1: 2, 2: 3}
    file.write(str(some_dict)[1:-1])
