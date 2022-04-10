\ Model Relaxed master problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x_0_0 + x_0_2 + x_0_3 + x_0_5
Subject To
 flow_balance_for_OD-0: x_0_0 + x_0_1 + x_0_2 + x_0_3 + x_0_4 + x_0_5
   + x_0_6 = 1
 flow_balance_for_construction: y_0 + y_1 + y_2 + y_3 + y_4 + y_5 + y_6
   = 1
 Coupling_0_0: x_0_1 + x_0_4 + x_0_6 - y_0 - y_3 - y_5 <= 0
 Coupling_1_0: - y_0 <= 0
 Coupling_2_0: <= 0
 Coupling_3_0: x_0_1 + x_0_4 + x_0_6 - y_2 - y_3 - y_5 <= 0
Bounds
Binaries
 x_0_0 x_0_1 x_0_2 x_0_3 x_0_4 x_0_5 x_0_6 y_0 y_1 y_2 y_3 y_4 y_5 y_6
End
