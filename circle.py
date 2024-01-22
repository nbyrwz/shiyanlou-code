import math
# 计算圆的面积
r = 2
area = r * r * math.pi
# 格式化输出圆的面积，保留10位小数
print("{:2d} {:.10f}".format(r,area))