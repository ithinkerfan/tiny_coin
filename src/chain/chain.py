#encoding=utf-8

import datetime as date
from block.block import Block

'''
定义区块链：
    链的属性选为列表，是因为有相同特征的元素，且可多次添加
'''
class Chain:

    def __init__(self):
        self.chain = []

    def add_genesis_block(self, genesis_block):
    #创建创世区块
        self.chain.append(genesis_block)

        last_block = self.chain[-1]
        return last_block #返回添加区块的值

    def add_block(self, last_block, data):
    #新增区块
        block = Block(last_block.index+1, date.datetime.now(), data, last_block.hash)

        self.chain.append(block)

        last_block = self.chain[-1]
        return last_block

    def print_chain_data(self):
    #打印区块链上的所有信息
        for block in self.chain:
            print('index={}, timestamp={}, data={}, prev_hash={}, hash={}'.format(
                            block.index,
                            block.timestamp,
                            block.data,
                            block.previous_hash,
                            block.hash))

    def validate(self):
    #判断区块链上的记录是否有效
        if len(self.chain) == 0:
            return 0

        if len(self.chain) == 1:
            return 0

        chain_len = len(self.chain)
        for i in range(0, chain_len-1):
            if self.chain[i].hash != self.chain[i+1].previous_hash:
                print('Invalid chain')
                return -1
        return 0
