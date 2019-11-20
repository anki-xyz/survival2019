# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from time import time
from tqdm import tqdm

def f(i):
    N = 0
    for q in range(10**7):
        N += q**2
        
    return i

if __name__ == '__main__':
    cpu_cores = multiprocessing.cpu_count()
    print("Cores available: ", cpu_cores)

    for cpu_cores_utilized in range(1,8+1):
        t0 = time()
        
        p = ProcessPoolExecutor(cpu_cores_utilized)
        
        results = []
        
        for i in tqdm(p.map(f, range(8)), total=8):
            results.append(i)
        
        elapsed_time = time()-t0
        
        print("Using {} cores, it took {:.2f} s".format(cpu_cores_utilized,
            elapsed_time))












