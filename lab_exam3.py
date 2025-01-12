import numpy as np

def reconstruct_matrix(U, S, V):
    if S.ndim == 1:
        S = np.diag(S)

    original_matrix = np.dot(U, np.dot(S, V))
    return original_matrix


A = np.array([[1, 2, 3], [4, 5, 6]])


U, S, V = np.linalg.svd(A, full_matrices=False)

reconstructed_A = reconstruct_matrix(U, S, V)
print("Reconstructed Matrix:")
print(reconstructed_A)

print("Is the reconstruction accurate?", np.allclose(A, reconstructed_A))
