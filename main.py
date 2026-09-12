"""
输入半径，计算圆的周长和面积
Version:    1.2
Author:     fgr
"""

import math

radius = float(input('请输入圆的半径'))
perimete = 2 * math.pi * radius
area = math.pi * radius * radius
print(f'{perimete = : .2f}')
print(f'{area = : .2f}')


