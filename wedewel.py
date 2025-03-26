from numpy import zeros, arange, pi, cos, sin
from pylab import show, imshow, colorbar

# Configuração inicial
V = 1.0  # Potencial
N = 101  # Dimensão da matriz
phi = zeros([N, N], float)  # Matriz inicial
tol = 1e-6
erromax = 10
w=0.94

# Parâmetros do círculo
cx, cy = 50, 50  # Centro do círculo
r1 = 50  # Raio do círculo
n_points = 360  # Número de pontos para desenhar o círculo (maior = mais preciso)

# Desenhando o perímetro do círculo com precisão
theta = arange(0, 2 * pi, 2 * pi / n_points)  # Ângulos igualmente espaçados
for angle in theta:
    x = int(cx + r1 * cos(angle))  # Coordenada x
    y = int(cy + r1 * sin(angle))  # Coordenada y
    if 0 <= x < N and 0 <= y < N:  # Verifica se está dentro dos limites da matriz
        phi[x, y] = V
            
imshow(phi)
colorbar()
show()
'''
while (erromax>tol):
    erromax = 0
    for i in range(1,N-1):
        for j in range(1,N-1):
            aux = 0.25*( phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1] )
            delta = aux - phi[i,j]
            phi[i,j] = phi[i,j]+(1+w)*delta
            erro = abs(aux-phi[i,j])
            if erro>erromax:
                erromax = erro

imshow(phi)
colorbar()
show()
    '''
 




