from tqdm import tqdm
import time

for i in tqdm(range(10)):
    time.sleep(0.5)

bar = tqdm(total=100)
for i in range(10):
    bar.update(10)
    time.sleep(0.5)
