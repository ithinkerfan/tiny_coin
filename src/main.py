#encoding=utf-8

import datetime as date

from block.block import Block
from chain.chain import Chain

def create_genesis_block():
    #创建创世块的信息
    block = Block(0, date.datetime.now(), 'This is Genesis block', '0')
    return block

def main():
    #创建创世块
    genesis_block  = create_genesis_block()
    #初始化链
    my_simple_chain = Chain()
    #获得上一个添加的区块信息
    last_block = my_simple_chain.add_genesis_block(genesis_block)

    #使用for循环添加9个区块
    for i in range(1,10):
        last_block = my_simple_chain.add_block(last_block, 'This is block # '+str(i))
    #打印所有区块的信息
    my_simple_chain.print_chain_data()
    #判断区块链的有效性
    if(my_simple_chain.validate() == 0):
        print('Hurray chain is valid...')
    else:
        print('Chain has been compromised!!!!')

if __name__ == '__main__':
    main()
