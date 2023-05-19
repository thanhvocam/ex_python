import numpy as np
from scipy.optimize import minimize_scalar

# Hàm chi phí để đo lượng ảnh hưởng của số lần quảng cáo lên trải nghiệm người dùng
def cost_function(ad_count):
    # Thông số có thể được điều chỉnh cho vấn đề cụ thể
    max_ad_count = 10
    user_experience_threshold = 0.7

    # Tính toán ảnh hưởng của số lần quảng cáo đến trải nghiệm người dùng
    user_experience = 1 - (1 - user_experience_threshold) * (ad_count / max_ad_count)

    # Trả về giá trị hàm chi phí
    return -user_experience

# Tìm giá trị lớn nhất của hàm chi phí và trả về số lần quảng cáo tối ưu
def optimize_ad_count():
    # Tìm kiếm giá trị lớn nhất của hàm chi phí trong khoảng từ 1 đến 10
    optimization_result = minimize_scalar(cost_function, bounds=(1, 10), method='bounded')

    # Trả về số lần quảng cáo tối ưu
    return optimization_result.x

import numpy as np
from scipy.optimize import minimize_scalar

# Hàm chi phí của chiến dịch marketing
def cost_function2(marketing_budget):
    # Thông số bắt buộc trong bài toán này
    conversion_rate = 0.02
    sale_price = 100
    fixed_costs = 50000

    # Tính doanh thu từ chiến dịch marketing
    revenues = marketing_budget * conversion_rate * sale_price

    # Tính lợi nhuận từ chiến dịch marketing
    profit = revenues - fixed_costs - marketing_budget

    # Trả về giá trị hàm chi phí
    return -profit

# Tìm giá trị nhỏ nhất của hàm chi phí và trả về ngân sách marketing tối ưu
def optimize_marketing_budget():
    # Tìm kiếm giá trị nhỏ nhất của hàm chi phí với phương pháp 'bounded' (được giới hạn trên khoảng [0, 100000])
    optimization_result = minimize_scalar(cost_function, bounds=(0, 100000), method='bounded')

    # Trả về số tiền ngân sách marketing tối ưu
    return optimization_result.x
