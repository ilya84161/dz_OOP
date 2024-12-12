with open ('files/1.txt', 'r', encoding='UTF-8') as a:
    #print(a.read())
    count_a=0
    af=''
    for line in a:
        count_a+=1
        af+=line
    af='1.txt\n'+str(count_a)+'\n'+af

with open ('files/2.txt', 'r', encoding='UTF-8') as b:
    #print(b.read())
    count_b=0
    bf=''
    for line in b:
        count_b+=1
        bf+=line
    bf='2.txt\n'+str(count_b)+'\n'+bf

with open ('files/3.txt', 'r', encoding='UTF-8') as c:
    #print(c.read())
    count_c=0
    cf=''
    for line in c:
        count_c+=1
        cf+=line
    cf='3.txt\n'+str(count_c)+'\n'+cf

ln_files=[count_a, count_b, count_c] #список с длинами файлов
ln_files_sorted=sorted(ln_files) 

pre_all_files=[af, bf, cf] #список с содержимым для вставки в общий файл

all_files='' # собираем вместе сортированные файлы
for i in range(len(pre_all_files)):
    index=ln_files.index(ln_files_sorted[i])
    all_files+=pre_all_files[index]+'\n' # вставляем в общий файл по очереди из предварительного в соответствии с индексом отсортированного

with open ('files/all.txt', 'w+', encoding='UTF-8', newline="") as all:
    all.write(all_files)