# blockchain-knife
some useful tools/scripts about blockchain or something else.

1. ethereum-learn-share.py

    script used by https://ethereum.iethpay.com/application/how-to-implete-a-decentralized-file-storage.html

2. zksnark

  - fork from https://github.com/ethereum/research.git , including finite field, curve and pairing

  - adding some explanation in the source file.

  - Greate Website : http://www.dragonwins.com/domains/getteched/crypto/index.htm . There is a good explanation about GF(p^n) : http://www.dragonwins.com/domains/getteched/crypto/polynomial_arithmetic_in_gf(p%5En).htm

3. detect_internal_storage.py

    this script can fetch data from ethereum leveldb. there are two functions : (1). getAccountInfoByaddress to get one account info, you should pass two arguments to this function, one is stateRoot, another is account address. (2). getAccountInfoByStateRoot to get all accounts info, you should pass two arguments to this, one is stateRoot, another is "".
    
    usage : 1). python detect_internal_storage.py all stateRoot. 
            2). python detect_internal_storage.py one stateRoot account
            
    **note:** this script can also fetch contarct stoarge data from ethereum leveldb. and you should replace stateRoot to storageRoot
