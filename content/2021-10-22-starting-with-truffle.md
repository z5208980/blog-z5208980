---
title: "Starting With Truffle"
date: "2021-10-22"
tags: ["Blockchain"]
image: ""
gradients: ["#fdcbf1", "#e6dee9"]
---

## Truffle

### Setup Testing production

```bash
npm install truffle -g	# installs truffle
# download Ganache, either via CLI or software

npm install @openzeppelin/contracts	# contract implementation fo ERC 721 NFT
```

**Just a heads up**: To compile, you'll probably want to config your compiler versions. See [here](https://www.trufflesuite.com/docs/truffle/reference/configuration#compiler-configuration)

### Init truffle
```bash
truffle unbox
```
The main folder will be the `contracts` folder where all the implementation will be in `.sol`.

### Compile
```bash
truffle compile
```

### Migrate to Ganache 
```bash
truffle migrate
```
Ensure that the file name in `contracts` is the the contract class. That way the build is succeed, or else you'll need to change it manually in `build/contracts`

At this point you should have you named token which `is` of `ERC-721` deployed on Ganache with truffle!

For me the way I interacted with this was with `web3` with `express` as the backend and `vue` for the client side.

First in the frontend, connect to the ganache server with `Web3` and connect your `Contract`. 
```js
const web3 = new Web3('ganache_rpc_server');
const contract_instance = new web3.eth.Contract(contract_abi, contract_addr_on_ganache, {});
```

Then you'll need to connect to one of the ganache accounts,

```js
web3.eth.accounts.wallet.add('0x' + account_private_key);
```

Then I used vue for simple `send` and `call` given by the `contract_instance`. I'm not going to the details of web3 since, I've learnt it was a self learnt process. But if you want to see if you if you setup everything correctly, just call the `name()` and render it in vue's app or console log.
```js
this.nft_description.name = await contract_instance.methods.name().call();
this.nft_description.symbol = await contract_instance.methods.symbol().call();

## Luquidity Pool
Pair of tokens like BAT-ETH, SUSHI-ETH etc. These pairs funded in a pool for trading on the swap. 

A more finanically term (not my strong suit) is that the funds are in ratio, say 50:50. In our example BAT-ETH pair, a pool of $500 would habe $250 BAT and $250 ETH. Now that the pool has been funded, trades made on BAT (buying BAT) will decrease supply making the value of BAT increase and hence ETH decrease. This is so that there is balance in within the two pairs.

## Luiqudity Providers
Simply users that fund the pool. The purpose of funding a pool, is when trades are from the pool, then the fees they are paid will be given to the providers as reward for giving the tokens for the liquidity pool.

### Understanding Liquidity Pool in Smart contracts
(From my understanding)
The swaps had create token pairs say BAT- ETH** Luquid Pool (LP) which itself is a smart contract (Since LP are essentially locked up funds of the two pairs). They will thus have an address `lpAddresses` with the corresponding `tokenAddresses`. In this case it BAT. The naming scheme can be anything like *BAT-ETH Swap-Name LP*. This LP smart contract can be given to the frontend for users to *locked up funds*. Now my problem is how to create one.
```