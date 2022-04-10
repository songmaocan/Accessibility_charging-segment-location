\ Model Relaxed master problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x_0_0 + x_0_2 + x_0_3 + x_0_4 + x_0_5 + x_1_0 + x_1_2 + x_1_3 + x_1_4
   + x_1_5
Subject To
 flow_balance_for_OD-0: x_0_0 + x_0_1 + x_0_2 + x_0_3 + x_0_4 + x_0_5 = 1
 flow_balance_for_OD-1: x_1_0 + x_1_1 + x_1_2 + x_1_3 + x_1_4 + x_1_5 = 1
 flow_balance_for_construction: y_0 + y_1 + y_2 + y_3 + y_4 + y_5 = 1
 Coupling_0_0: x_0_1 - y_0 - y_5 <= 0
 Coupling_1_0: - y_2 <= 0
 Coupling_2_0: - y_3 <= 0
 Coupling_3_0: x_0_1 - y_4 <= 0
 Coupling_0_1: - y_0 - y_5 <= 0
 Coupling_1_1: x_1_1 - y_2 <= 0
 Coupling_2_1: x_1_1 - y_3 <= 0
 Coupling_3_1: - y_4 <= 0
Bounds
Binaries
 x_0_0 x_0_1 x_0_2 x_0_3 x_0_4 x_0_5 x_1_0 x_1_1 x_1_2 x_1_3 x_1_4 x_1_5
 y_0 y_1 y_2 y_3 y_4 y_5
End
