'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

matrix_ = [ [1,2,7],
            [3,4,4],
            [5,3,6]]

t_matrix_ = list(map(list, zip(*matrix_)))
min_vals = []
for row in t_matrix_:
    min_vals.append(min(row))
print(f"Максимальный элемент - {max(min_vals)}")