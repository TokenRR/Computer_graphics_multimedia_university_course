from PIL import Image
import os


cls = lambda: os.system('cls')


def algoritm (txtname, imagename, size = (540,960)):
    img = Image.new('RGB', size, 'white')
    f = open(txtname,'r')
    data = f.read().split('\n')
    for i in range(len(data)-1):
        data[i] = data[i].split(' ')
        img.putpixel((int(data[i][0]), int(data[i][1])), (0, 0, 0))
    img.save(f'{imagename}.png')
    return size


if __name__ == '__main__':
    cls()
    loop = True
    while loop:
        try:
            file_name = input('\nВведіть назву файлу с датасетом. Приклад: File_name (без розширення)\n')
            file_name = file_name + '.txt'
            image = input('Як назвати файл із зображенням?    ')
            size = algoritm(file_name, image)
            restart = input('Бажаєте відобразити ще один датасет?\n'
            '(Введіть "так" або "да" або "yes", щоб почати знову або натисніть "Enter", щоб завершити роботу)\n')
            cls()
            if restart.lower() == 'так' or restart.lower() == 'yes' or restart.lower() == 'да': continue
            else: loop = False
        except FileNotFoundError:
            continue