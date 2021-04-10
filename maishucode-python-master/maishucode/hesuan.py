import random

total_pop = 1400000000  #总人口
rate = 0.00001  #感染率
group_size = 100  #每组人数

check_num = 0
caiyang_num = 0

#计算采用数量：总人数 + 要重复采样的数量
caiyang_num = total_pop + (total_pop * rate) * group_size
#计算检测次数：人数除以10 + 重复检测数
check_num = total_pop / group_size + (total_pop * rate) * group_size

print(f'采用数：{caiyang_num:,}, 检测数量：{check_num:,}')

group_size = 100000  #10万人一组
group_num = 1400000000 / 100000 # 共1400组
from math import log
check_num = round(log(group_size, 2) * group_num)
print(f'检测数量：{check_num:,}')


pop = list(range(1, 10001))

# for x in pop:
#     print(x)

TOTAL_POPULATION = 1400000000
PERCENT = 0.0001
GROUP = 10
test_count = 0
