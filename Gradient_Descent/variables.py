from function import cost_function3
from scipy.optimize import minimize

initial_guess = [100, 100, 100] # Số lượng ban đầu sản xuất của mỗi loại giày
bounds = ((10, None), (10, None), (10, None)) # Giới hạn dương số lượng sản xuất
result = minimize(cost_function3, initial_guess, bounds=bounds)

x1_opt, x2_opt, x3_opt = result.x[0], result.x[1], result.x[2]
profit_opt = -(cost_function3(result.x))

print(f"Số lượng sản xuất tối ưu của loại 1: {x1_opt}")
print(f"Số lượng sản xuất tối ưu của loại 2: {x2_opt}")
print(f"Số lượng sản xuất tối ưu của loại 3: {x3_opt}")
print(f"Lợi nhuận tối đa: {profit_opt}")