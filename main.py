from pubg.core import PUBG 
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


p = PUBG()
p.start()

# with ThreadPoolExecutor(max_workers=3) as executor:
#    executor.submit(p.moving)
