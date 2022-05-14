from prettytable import PrettyTable


class Crop:
    def __init__(self, args):
        (self.name, self.price, self.usage, self.farming_cost, self.storage_cost, self.output, self.income,
         self.humidity, self.temperature, self.humidity_response, self.temperature_response) = args
        self.income_calculated = 0
        self.plan_income = 0
        self.farm_cost = 0

    def productivity_decrease(self, humidity, temperature):
        h_decrease = abs(self.humidity - humidity) * self.humidity_response
        t_decrease = abs(self.temperature - temperature) * self.temperature_response
        return h_decrease + t_decrease

    def productivity(self, area, humidity, temperature):
        d = self.productivity_decrease(humidity, temperature)
        koeff = (100 - d) / 100
        return koeff * area * self.output

    def income_field(self, area, humidity, temperature):
        estimation = self.productivity(area, humidity, temperature)
        self.plan_income = estimation * self.income / 10
        self.farm_cost = area * (self.farming_cost + self.price * self.usage / 1000)
        self.storage_cost = estimation * self.storage_cost
        self.income_calculated = self.plan_income - self.farm_cost - self.storage_cost


def calculate_field(crops):
    area = int(input('Введите площадь:'))
    humidity = int(input('Введите влажность:'))
    temperature = int(input('Введите температуру:'))
    for crop in crops:
        crop.income_field(area, humidity, temperature)


def calc(x):
    return x.income_calculated

def print_sorted(crops, key):
    result = sorted(crops, key=calc, reverse=True)
    mytable = PrettyTable()
    top_table = ["Прибыль, р", "Доход от продажи, р", "Затраты на посевы и выращивание, р", "Затраты на хранение, р"]
    mytable.field_names = ['№', "Название культуры", top_table[int(key[0])-1], top_table[int(key[1])-1], top_table[int(key[2])-1], top_table[int(key[3])-1]]
    i = 0
    for s in result:
        i += 1
        list_table = [int(s.income_calculated), int(s.plan_income), int(s.farm_cost), int(s.storage_cost)]
        mytable.add_row([i, s.name, list_table[int(key[0])-1], list_table[int(key[1])-1], list_table[int(key[2])-1], list_table[int(key[3])-1]])
    print(mytable)

def generate_output(crops):
    output = []
    for crop in crops:
        crop_dict = {
            'name': crop.name,
            'income_calculated': crop.income_calculated,
            'plan_income': crop.plan_income,
            'farm_cost': crop.farm_cost,
            'storage_cost': crop.storage_cost
        }
        output.append(crop_dict)
    return output
