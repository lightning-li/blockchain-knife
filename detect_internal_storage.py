#!/usr/bin/env python
# coding=utf-8

import leveldb
from ethereum import utils
import rlp
import sys

db = leveldb.LevelDB("/Users/likang/private_ethereum/ss_ethereum/geth/chaindata")

accountHash2content = {}

def getAccountInfoByStateRoot(st, key) :
    #print "root : " + st.encode("hex")
    root_node = rlp.decode(db.Get(st))

    if len(root_node) == 2 :
        # the last bit of first hex represent whether adding 0x0
        # if the last bit is 1, represent not adding 0x0
        # the last second bit of first hex represent node_type
        # if it's 1, represent leaf. if not, represent extension_node

        if root_node[0][0].encode("hex")[0] == "2" :
            key += root_node[0].encode("hex")[2:]
            accountHash2content[key] = rlp.decode(root_node[1])
            #print key
            return
        elif root_node[0][0].encode("hex")[0] == "3" :
            key += root_node[0].encode("hex")[1:]
            #print key
            accountHash2content[key] = rlp.decode(root_node[1])
            return
        else :
            if root_node[0][0].encode("hex")[0] == "0" :
                key += root_node[0].encode("hex")[2:]
            else :
                key += root_node[0].encode("hex")[1:]

            getAccountInfoByStateRoot(root_node[1], key)
    else :
        for i in range(10) :
            if root_node[i] != "" :
                getAccountInfoByStateRoot(root_node[i], key + str(i))
        for i in range(6):
            if root_node[10 + i] != "" :
                getAccountInfoByStateRoot(root_node[10 + i], key + chr(97 + i))
        if root_node[16] != "" :
            getAccountInfoByStateRoot(root_node[16], key)
        
if __name__ == "__main__" :

    getAccountInfoByStateRoot(sys.argv[1].decode("hex"), "")
    for key in accountHash2content :
        print key + " : ",
        print accountHash2content[key]
        print
