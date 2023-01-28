import random



class AppleTree:
    id = type(int)
    all_obj = {}
    all_text :str= ''
    def __init__(self, Name,id,all_obj,plod, weight,all_text):
        self.ne = Name
        self.id = id
        self.plod = plod
        self.weight = weight
        self.all_obj.update({self.ne:[plod, weight]})
        self.dobavka_AppleTree()

    def printer(self):
        items = self.all_obj.items()
        most_plod :int = 0
        most_weight :int = 0
        name_plod :str = ''
        name_weight :str = ''
        for item in items:
            if most_plod < item[1][0]:
                most_plod = item[1][0]
                name_plod = item[0]
            if most_weight < item[1][1]:
                most_weight = item[1][1]
                name_weight = item[0]
        text = (f'\nСамое плодоносное растение - {name_plod} ({most_plod} шт.), \n'
              f'Самые тяжелые плоды - {name_weight} ({most_weight} гр.) ')
        AppleTree.all_text += text
        return AppleTree.all_text


    def dobavka_AppleTree(self):
        text = '\n' + "Название плодоносного растения: " + self.ne + '\n'
        text += "Количество плодов: "+  str(self.plod) + '\n'
        text += "Примерный вес каждого плода (в граммах): "+ str(self.weight) + '\n'
        AppleTree.all_text += text
        return AppleTree.all_text


all_trees = ['Яблоня','Груша','Вишня','Бананы']

for _ in range(len(all_trees)):
    tree = AppleTree(all_trees[_],_,all_obj={},plod= random.randint(1, 125), weight= random.randint(150, 225),all_text='')

AppleTree.printer(AppleTree)
print(AppleTree.all_text)

with open("out.txt","w") as file:
    file.write(AppleTree.all_text)

