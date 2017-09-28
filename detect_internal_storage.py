#!/usr/bin/env python
# coding=utf-8

import leveldb
from ethereum import utils
import rlp
import sys

db = leveldb.LevelDB("/Users/likang/private_ethereum/ss_ethereum/geth/chaindata")

accountHash2content = {}

def getAccountInfoByAddress(st, addr) :
    if len(addr) == 42 :
        addr = addr[2:]
    elif len(addr) != 40 :
        return
    
    getAccountInfoByStateRoot(st.decode("hex"), "")
    if accountHash2content.has_key(utils.sha3(addr.decode("hex")).encode("hex")) :
        return accountHash2content[utils.sha3(addr.decode("hex")).encode("hex")]
    else :
        return

def getAccountInfoByStateRoot(st, key) :
    #print "root : " + st.encode("hex")
    root_node = rlp.decode(db.Get(st))

    if len(root_node) == 2 :
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
    
    if len(sys.argv) != 3 and len(sys.argv) != 4 :
        sys.exit("arguments number is not 3 and  4")

    if len(sys.argv) == 3 :
        assert sys.argv[1] == "all"
        if len(sys.argv[2])  == 66 :
            st = sys.argv[2][2:]
        elif len(sys.argv[2]) == 64 :
            st = sys.argv[2]
        else :
            sys.exit()

        getAccountInfoByStateRoot(st.decode("hex"), "")
        for key in accountHash2content :
            print key + " : ",
            print repr(accountHash2content[key])
            print

    else :
        assert sys.argv[1] == "one"
        if len(sys.argv[2]) == 66 :
            st = sys.argv[2][2:]
        elif len(sys.argv[2]) == 64 :
            st = sys.argv[2]
        else :
            sys.exit()
        if len(sys.argv[3]) == 42 :
            account = sys.argv[3][2:]
        elif len(sys.argv[3]) == 40 :
            account = sys.argv[3]
        else :
            sys.exit()
        print repr(getAccountInfoByAddress(st, account))
