## Создание, чтение и редактирование текстовых файлов
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close

# exit()
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close

exit()