import logging
from control_eng.libs.some_graphs import display_sin_graph, object_graph
from libs import *

#ロガーの設定
logger = logging.getLogger('mycontrollog')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('./logs/logfile.log')
fmt = logging.Formatter('%(asctime)s%(message)s')
handler.setFormatter(fmt)
logger.addHandler(handler)

def main():
    logger.debug('[START] My System Start')
    
    # display_sin_graph()
    object_graph()


    logger.debug('[END] My System Start')
    