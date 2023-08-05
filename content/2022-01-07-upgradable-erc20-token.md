---
title: "Upgradable ERC20 Token"
date: "2022-01-07"
tags: ["Cryptocurrency", "Blockchain"]
image: ""
gradients: ["#48c6ef", "#6f86d6"]
---

## Creating an Upgradable ERC20 Token
This is just my understanding and notes for creating a upgradable ERC20 token using the proxy pattern.

repo: https://github.com/z5208980/Upgradable-ERC20

### Initialisable

When implementing our ERC20 token, traditionally they are initialised with the `constructor()`, however in Solidity, the constructor can be called once. Hence to ensure that initialisation is called once, we can an `Initialisable` contract that handles that a given function is called **once**. In this case, our constructor is called `initialise()`. Now fills it in the role of a constructor for a smart contract. 

The mostly section of the contract is the, 
```sol
function isConstructor() {
	// ...
	assembly { cs := extcodesize(self) }
	return cs == 0;
}
```
where the function is checking if the contract *itself* is a function. `extcodesize` is basically an **OPCODE** that determines if an address is a contract address. More technical it checks for. **Note** That this will return 0 as the contract has not been deployed yet and hence, the contract that contains a function with the `modifier` will act as the constructor, as `isConstructor` is `true`.

### ERC20

The main implementation of the ERC20 token can be found via Openzeppelin. As a method the ERC20 contract in Openzep uses the `constructor()` method, and since we only want the ERC20 to be initialised once, the ERC20 need to inherit,

```sol
contract ERC20 is Initialisable {
```

and the constructor is replaced with a function that **need to be manually called** with the `initialiser` modifier from Initialisable to enforce its single-use.

```sol
// ERC20 with compatible upgrade
function initialise(string memory _name, string memory _symbol, uint8 _decimals, uint256 _supply) initialiser

// typical ERC20
constructor(string memory name_, string memory symbol_)
```

### Proxy contract

First I will have a proxy contract. This will include features such as **owner of proxy**  and the **memory location of the ERC20 contract address**. We can effectively do so in the assembly code of the `Proxy contract`.

The purpose of a proxy is to store an address of the latest deployed contract and redirect calls to that logic. Hence we *"The proxy owner"* has the flexibility to fix or implementation new logic via functions to the ERC20 tokens.

In order for the Proxy to be in charge of calling the ERC20 methods, it needs to know the functions of the ERC20 contract. The most common design of doing this via `delegetecall` in the assembly

```sol
fallback() external payable {
	address impl = getImplementation();
	assembly {
		let ptr := mload(0x40)
		calldatacopy(ptr, 0, calldatasize)
		let result := delegatecall(gas, impl, ptr, calldatasize, 0, 0)
		let size := returndatasize
		returndatacopy(ptr, 0, size)
		switch result
		case  0  {  revert(ptr, size)  }
		default  {  return(ptr, size)  }
	}
}
```

Here we are can obtain the implementation of the ERC20 token by using our getter function. Then using assembly code, use `calldatacopy` to obtain `msg.data` which will contain the **ERC20 function** method that was called and store it in the `ptr` memory address. With this we can do a lower end call, `delegatecall` passing the `gas, implementation, msg.data, calldatasize` 

Wrapping around the delegatecall implementation is the `fallback()` function. The `fallback()` is simply where functions that are not in the contract are executed. Hence when a function from the ERC20 implementation is called like `mint()`, `transfer()` the proxy doesn't contain these and hence the `fallback()` is executed which in turn will exec and the assembly that will `delegatecall`. 

### Usage
This is a very simplified and short description detailing how I implemented the ERC20 token that has upgradable features. In ord
er to use this the method is as follows,
1. Deploy `ERC20.sol` address as **logic**. This address is like a dummy contract for the proxy, hence **no interactions** will be made using this contract. 
2. Deploy `Proxy.sol`
3. Then set the logic (implementation of the ERC20) with the Proxy using the `upgradeTo(ERC20Address)`
4. Reconnect the Proxy contract using the **Proxy address** using the **ERC20 ABI**. This will ensure that the ERC20 functions can be used within the Proxy contract.
5. `initalise()` which is originally an ERC20 method can be called using the Proxy contract and it will work since the contract will trigger the `fallback()` trigger the assembly to execute the low-end call of `initalise()`. This should initialise the ERC20 as the Proxy contract.
6. In case of a bug or the tokens required upgrade, then implement the ERC20 token and deploy it (Just like **Step 1**).
7. Using the newly deployed ERC20 address. Load in the Proxy contract as its original Proxy ABI and this should have the `upgradeTo(address)` where the new ERC20 implementation with the upgrade is set.
8. Change back the Proxy to the ERC20 ABI and it should be used as normal but now with the new methods and features. (Just like in **Step 4**)