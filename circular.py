import numpy as np
import matplotlib.pyplot as plt

# Definições do grid polar
R = 1.0  # Raio máximo
Nr = 100  # Número de pontos em rho
Nphi = 100  # Número de pontos em phi
rho = np.linspace(0, R, Nr)
phi = np.linspace(0, 2 * np.pi, Nphi)
dr = rho[1] - rho[0]
dphi = phi[1] - phi[0]

# Inicializar f com condições de contorno
f = np.zeros((Nr, Nphi))

# Condições de contorno na borda externa
f[-1, 0:int(Nphi / 2) + 1] = 3  # Metade da borda externa fixa em 3
f[-1, int(Nphi / 2):Nphi] = -3  # Outra metade da borda fixa em -3

# Método iterativo para resolver a equação de Laplace
tol = 1e-6  # Critério de convergência
max_iter = 10000000  # Máximo de iterações permitidas
w = 0.80  # Fator de relaxação para melhorar a convergência (testado empiricamente)
erro_max=10
while erro_max > tol:
    f_old = f.copy()  # Cópia do estado antigo para verificar a convergência
    for i in range(1, Nr - 1):  # Percorre as posições em rho (ignorando as bordas)
        for j in range(Nphi):  # Percorre as posições em phi
            jm = (j - 1) % Nphi  # Índice anterior em phi (com condições periódicas)
            jp = (j + 1) % Nphi  # Índice posterior em phi (com condições periódicas)

            # Termos da equação de diferenças finitas no Laplaciano
            term_rho = (f[i + 1, j] + f[i - 1, j]) / dr**2
            term_phi = (f[i, jp] + f[i, jm]) / (dphi**2 * rho[i]**2)
            term_rho2 = (f[i + 1, j] - f[i - 1, j]) / (2 * dr * rho[i])
            f_new = (term_rho + term_phi + term_rho2) / (2 / dr**2 + 2 / (dphi**2 * rho[i]**2))

            # Atualização com relaxação
            f[i, j] = f[i, j] + (1+w) * (f_new - f[i, j])

    # Verifica a convergência
    erro_max = np.max(np.abs(f - f_old))

# Visualização
RHO, PHI = np.meshgrid(rho, phi, indexing='ij')
X, Y = RHO * np.cos(PHI), RHO * np.sin(PHI)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, f, levels=100, cmap="plasma")
plt.colorbar(label="Potencial")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solução da Equação de Laplace em Coordenadas Polares")
plt.axis("equal")
plt.show()
