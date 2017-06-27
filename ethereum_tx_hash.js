// 需运行 geth 客户端，rpcport 设置为 20000，并且在客户端解锁账户
// 交易哈希值与 chainId 有关，在 Genesis 文件中设置，主网是 1.
// 运行结果
/*
➜  /Users/likang/Documents/git/blockchain-knife git:(master) ✗ >>node ethereum_tx_hash.js
true
0xA3Ac96fbe4b0DcE5F6f89a715CA00934d68f6C37
true
coinbase : 0xa3ac96fbe4b0dce5f6f89a715ca00934d68f6c37
balance : 1.38600021e+22
0:0xf64844b1497a775c3f5ac7be316227c925009e90c5955476869c29b21006c9bf
1:0x5d80a2e08a7cf16ab4b2b0e38b9046b0f85be771158e7a278155ca8d2d8993fd
2:0x9723ac630a21f4616ef019052538eca9959240fd7aa53582d1664dc6b25e2ac0
3:0x3e96dbbd2f4be5e3a64dda36a451bc52346b7c1a7d62340e3f83730b675c2938
4:0x76095dbd00781c92528f833f0bb331266cef96b8624461557f637409a78d99f3
5:0x4457ef8e7fc13373112ddbdc65b0c5c0e9c9c54fd01ac69a1bd96e1a36f711b9
6:0x9e394315efbc2f4e5856e4dfd41e261eb98f7058eefa039821e6b593d45284ff
7:0xa939516e74689441e8fd09a21065e7e157eefadefd6d8b8945cec99ea1a25d08
8:0xf8bae0f74e1af141e31883092cbeb74cd000dcfd27004c8adb855f0163206ea4
9:0xf5febfc97444bad5153266cdd7c1c56c0648ac4f3612318b6d2a0ba1e9f5e8d8
*/

var Web3 = require("web3");
var web3 = new Web3();

web3.setProvider(new web3.providers.HttpProvider("http://localhost:20000"));

console.log(web3.isConnected());
var add = "a3ac96fbe4b0dce5f6f89a715ca00934d68f6c37"
//将地址转换为有校验和的大小写混合地址
var checksum_Addr = web3.toChecksumAddress(add)
console.log(checksum_Addr);
// 检查校验和账户是否有效
console.log(web3.isAddress("0x49DC59feE91E751aa92e7728269BF1a88B75Fc53"));

var coinbase = web3.eth.coinbase;
var balance = web3.eth.getBalance(coinbase);

console.log("coinbase : " + coinbase);
console.log("balance : " + balance);

for (var i = 0; i < 10; i++) {

    var res = web3.eth.sendTransaction({from : "0xa3ac96fbe4b0dce5f6f89a715ca00934d68f6c37", to : "0x55d34b686aa8C04921397c5807DB9ECEdba00a4c", value : 10 + i, nonce : 17, gas : 200000, gasPrice : 50000000000});
    console.log(i + ":" + res);
}
