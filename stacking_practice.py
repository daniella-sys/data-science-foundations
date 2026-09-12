#Об'єднання баз даних клієнтів банківських відділень
import numpy as np
branch_a = np.array([[101, 5000], 
                     [102, 7500], 
                     [103, 3200]])

branch_b = np.array([[104, 9100], 
                     [105, 4800]])
#Об'єднати по вертикалі
all_clients_v = np.vstack((branch_a, branch_b))
print("Розмірність матриці:", all_clients_v)
all_clients_concat0 = np.concatenate((branch_a, branch_b), axis=0)
print("Розмірність матриці:", all_clients_concat0.shape)

extra_features = np.array([[750, 28], 
                           [680, 35], 
                           [810, 42]])
full_branch_a_h = np.hstack((branch_a, extra_features))
full_branch_a_concat1 = np.concatenate((branch_a, extra_features), axis=1)
print("Розмірність матриці:", full_branch_a_h.shape)
print("Розмірність матриці:", full_branch_a_concat1)

        

