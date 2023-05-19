from itertools import product
import subprocess

for opt_name, lr in product(('Adam',), (1e-4, 1e-3)):
    subprocess.call(f'python dm.py \
                    --opt_name {opt_name} \
                    --lr {lr}', \
                    shell=True
                )