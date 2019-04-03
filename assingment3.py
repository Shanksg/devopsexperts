#class3

#a = 1 / 0

if __name__ == '__main__':
    try:
        a = 1 / 0
    except:
        print("no exception :)")

#7
my_file = open("words.txt", 'a+')
my_file.close()

#8
my_file = open("words.txt", 'a+')
name =  input("your name is :")
my_file.write(name + "\n")
my_file.close()

#9
my_file = open("words.txt", 'r')
show = my_file.read()
print(show)
my_file.close()

#10
#word = "שלום"
#'\xd7\xa9\xd7\x9c\xd7\x95\xd7\x9d'
#print(word)
my_newfile = open("words2.txt", 'w',encoding='utf-8')
my_newfile.write("בדיקה")
my_newfile.close()

my_newfile = open("words2.txt", 'r',encoding='utf-8')
hebtxt = my_newfile.read()
print(hebtxt)
my_newfile.close()

###EXTRA???###
###EXTRA###
from PIL import Image
img = Image.new('RGB', (800,1280), (255, 255, 255))
img.save("image.png", "PNG")
