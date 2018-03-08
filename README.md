# tiny_coin
  简易比特币 --tiny coin with Python

  区块链的底层技术原理：
      把上个区块哈希值和当前记录的哈希值一块加入到新的区块，并将区块按创建的时间顺序依次串联成链。
  
  运行机制：
  
  1、产生新区块所包含的内容：
      key（区块键值）、timestamp（时间戳）、data（数据）、pervious_hash（上一个区块的哈希值）、hash（当前的哈希值）。
  
  2、判断区块的有效性：
      当前区块的pervious_hash 等于上一个区块的hash，即为有效的区块。
