
list_file = ['1.txt', '2.txt', '3.txt']
dict_file = dict()

for file_name in list_file:
    num = 0
    with open(file_name, encoding='utf-8') as file:
        while True:
            str_ = file.readline()
            if not str_:
                break
            num += 1
        # print(num)
    #  if file.closed:
    #  print('\nOK\n')
    dict_file[file_name] = num

# print(dict_file)

sorted_list_file = sorted(dict_file.items(), key=lambda x: x[1])
# print(sorted_list_file)
# print(len(sorted_list_file))

fout = open('output.txt', 'w', encoding='utf8')

for file_name in sorted_list_file:
    fin = open(file_name[0], 'r', encoding='utf8')
    print(file_name[0], file=fout)
    print(file_name[1], file=fout)
    for str_ in range(file_name[1]):
        print(fin.readline().rstrip(), file=fout)
    fin.close()

fout.close()
