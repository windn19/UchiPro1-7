class Check:
    def __init__(self):
        self.goods = {}

    def end_of_check(self):
        total = 0
        for name, data in self.goods.items():
            print(f'{name}, {data[0]}, {data[1]}')
            total += data[0] * data[1]
        print('-----')
        print(f'Стоимость покупок: {total}')

    def new_check(self):
        while True:
            s = input()
            if s == 'КОНЕЦ':
                self.end_of_check()
                break
            name, count, cost = s.split(', ')
            if name not in self.goods:
                self.goods[name] = [int(count), int(cost)]
            else:
                self.goods[name][0] += int(count)


check = Check()
check.new_check()
