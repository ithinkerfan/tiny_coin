#encoding=utf-8

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
#加入系统路径   （路径合并    （获取文件路径（文件的真实路径），上一级目录））
from hashlib import sha256


'''
定义区块类：
初始化属性：
        index：区块key
        timestamp：时间戳
        data：数据
        pervious_hash：上一个区块的哈希值
        hash：当前的哈希值
'''
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._hash_block()

    def _hash_block(self):
        sha = sha256()
        #将index、timestamp、data、previous_hash一块进行哈希计算
        sha.update( str(self.index).encode('ascii') +
                    str(self.timestamp).encode('ascii') +
                    self.data.encode('ascii') +
                    self.previous_hash.encode('ascii'))

        return sha.hexdigest() #返回哈希值的16进制显示

        #sha.digest() 是二进制显示

