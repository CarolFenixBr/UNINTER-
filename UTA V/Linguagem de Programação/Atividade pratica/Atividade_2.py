from matplotlib import pyplot as plt

# o menu irá resultar nos valores de y1, y2, y3 por meio da equação ax + bx - c
def menu(x, a, b, c):
  y = a*x + b*x - c
  return y

# definição dos valores para x
x1 = 5
x2 = 7
x3 = 9

#definição dos valores para a, b, c
a = 3
b = 5
c = 9

# colocando titulo e folha quadriculada no gráfico
plt.title('Equação a*x +b*x - c')

plt.grid()

#plotando os resultados obtidos por x e y
plt.plot(x1,menu(x1, a, b, c), marker="o", markersize=15, markerfacecolor='red')
plt.plot(x2,menu(x2, a, b, c), marker="o",markersize=15, markerfacecolor='blue')
plt.plot(x3,menu(x3, a, b, c), marker="o",markersize=15, markerfacecolor='green')

#colocando legenda no gráfico
plt.legend([f'x={x1} y={menu(x1, a, b, c)}', f'x={x2} y={menu(x2, a, b, c)}', f'x={x3} y={menu(x3, a, b, c)}'])

plt.show
