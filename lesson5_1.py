'''
Пользователь вводит данные о количестве предприятий, 
их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) 
для каждого предприятия.. Программа должна определить среднюю прибыль 
(за год для всех предприятий) и вывести наименования предприятий, 
чья прибыль выше среднего и отдельно вывести наименования предприятий, 
чья прибыль ниже среднего.
'''

def print_cmp_avg(cmpns):
    for comp, avg_income in cmpns.items():
        print(f"Компания {comp} с доходом {avg_income}")

comp_cnt = int(input("Введите кол-во предприятий: "))
comp_income = {}
for i in range(comp_cnt):
    comp_name = input(f"Введите название {i}-ой компании: ")
    income = input(f"Введите прибыль {i}-ой компании за 4 квартала: через ',' ")
    vals = list(map(float, income.split(',')))
    comp_income[comp_name] = sum(vals)/len(vals)

avg_all = sum(comp_income.values())/len(comp_income.values())
print(f"Cредняя прибыль за год для всех предприятий: {avg_all}")
cmpns_above = dict((k, v) for k, v in comp_income.items() if v >= avg_all)
cmpns_below = dict((k, v) for k, v in comp_income.items() if v < avg_all)
print(f"Наименования предприятий, чья прибыль выше среднего:")
print_cmp_avg(cmpns_above)
print(f"Наименования предприятий, чья прибыль ниже среднего:")
print_cmp_avg(cmpns_below)

