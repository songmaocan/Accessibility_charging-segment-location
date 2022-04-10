\ Model Relaxed master problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x_0_0 + x_0_1 + x_1_0 + x_1_1
Subject To
 flow_balance_for_OD-0: x_0_0 + x_0_1 = 1
 flow_balance_for_OD-1: x_1_0 + x_1_1 = 1
 flow_balance_for_construction: y_0 + y_1 = 1
 Coupling_0_0: - y_0 <= 0
 Coupling_1_0: - y_0 <= 0
 Coupling_2_0: <= 0
 Coupling_3_0: <= 0
 Coupling_0_1: - y_0 <= 0
 Coupling_1_1: - y_0 <= 0
 Coupling_2_1: <= 0
 Coupling_3_1: <= 0
Bounds
Binaries
 x_0_0 x_0_1 x_1_0 x_1_1 y_0 y_1
End
