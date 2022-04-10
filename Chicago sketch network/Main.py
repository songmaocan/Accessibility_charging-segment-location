"""
Algorithm: Solve the accessibility-oriented wireless charging lanes location problem
 by the column generation
Copyright: Maocan Song, 1097133316@qq.com
Date: 2022-1-19
"""
import time
from Method import Solve

def main():
    start_time = time.time()
    mod=Solve()
    mod.g_solving_the_wireless_charging_lanes_location_problem()
    end_time = time.time()
    spend_time = end_time - start_time
    mod.output_results(spend_time)
    print("CPU running time {} min".format(round(spend_time / 60), 3))

if __name__ == '__main__':
    main()