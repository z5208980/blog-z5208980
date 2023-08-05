---
title: "Introduction Notes to Blockchain"
date: "2021-04-23"
tags: ["Cryptocurrency", "Blockchain"]
image: ""
gradients: ["#ff9966", "#ff5e62"]
---

## Blockchain
To understand blockchain, it is simply a growing list of `blocks` that are linked. A block usually contains:
- Cryptographic hash of the previous block
- Timestamp
- Transaction data (in the form of a Merkle Tree)

The first ever block on the Bitcoin blockchain was known as the **Genesis Block**. It gave rise to the entire blockchain of the Bitcoin trading system.

The word *chain* in `blockchain` works like this: Say there was an initialized block with the data `Hello` that is given a hash, say `AA`. The hash `AA` is then used as a hash key for the next block `World`, given a hash `BB`, and it continues. The blockchain would look like this:

```
Hello AA
WorldAA BB
ByeBB CC
```


This sort of chaining effect ensures that if one block is altered, it will affect the entire database, known as the **avalanche effect**. This ensures that blockchains are **decentralized**.

### Merkle Tree
The Merkle Tree, named after Ralph Merkle, is a cryptography technique that uses Hash Trees.

### Decentralization
One of the main reasons why cryptocurrencies use blockchain technology is not just for data security and fault tolerance, but also for decentralization. Decentralization is the process of distributing power away from a central unit, allowing power to exist outside the control of the government and into the hands of the people.

### Ledger
In cryptocurrency, a **ledger** is a record or a book that stores all transactions made. In most cryptocurrencies, the ledger is usually public to allow for public verification and proof of work. A *blockchain* is a type of ledger where blocks are recorded and stored.

### Hashing
Hashing is a process that takes any string as input and produces a fixed-size string of characters. In the case of Bitcoin, it takes an input of 256 bits and uses a SHA-256 hashing algorithm. Hashing has several advantages, including collision resistance and being a one-way function.

### Bitcoin Miners
Bitcoin miners enjoy anonymity and privacy, which can be problematic when it comes to activities like money laundering. To maintain anonymity, privacy, and security, it is recommended to use multiple and refreshed addresses. Failing to do so can make a user's main address vulnerable to attackers, who can link other addresses to the main one and trace transactions to reveal the user's real-world identity. Additionally, de-anonymization can occur at the network layer, where an attacker can determine an IP address on a network. Using Tor can help counter these issues.

### Online Wallet
An online wallet for cryptocurrencies typically requires identification through Know Your Customer (KYC) procedures. This identification requirement eliminates anonymity, as records are kept for compliance purposes.

---

## Smart Contracts
Smart contracts are user-defined code on a blockchain that contain **instructions** to manage a digitized asset. They are triggered by a user node. Smart contracts have the following properties:
- **Immutable**: The code and instructions cannot be edited or changed.
- **Deterministic**: The output or the system involved has no randomness in its state.
- **Trustworthy**: The smart contract is reliable, secure, and validated.

Smart contracts on Ethereum are executed as **bytecode** and run on the **Ethereum Virtual Machine (EVM)** on each blockchain node. The bytecode used in Ethereum is commonly known as **Solidity**.

### Life Cycle of Smart Contracts
The life cycle of smart contracts typically involves the following stages:
1. **Requirement Analysis and Modeling**: This involves modeling the requirements of the smart contract.
2. **Development**: The code for the smart contract is produced.
3. **Testing**: Testing is performed locally and on a testnet to ensure the contract is complete and functions as intended.
4. **Deployment**: The smart contract is deployed onto the production stage of the blockchain, and a unique address is generated for interactions with the contract. Smart contracts remain active until they are disabled by the host or reach a terminating state where they cannot be executed.

During the life cycle, the gas fee for executing smart contracts needs to be considered. Gas is a payment required when a transaction triggers a smart contract. Factors such as computation, bandwidth requirement, memory, and volume of data should be optimized to keep the gas fee as low as possible.

### Encounters Experienced
When deploying a contract, it is important to record the **contract address**. This address can typically be found with the `to` parameter. Other Ethereum accounts must connect to the contract address to use the contract, and any restrictions enforced by the contract will apply. Making a function call or using the contract will result in a **transaction**. Occasionally, an error may occur during contract execution, such as an "Out of Gas" warning.

### Terminology
- **Gas**: The fee required when a transaction triggers a smart contract.
- **Etherscan**: A tool used to explore and search the Ethereum blockchain for contract addresses and other information.
- **Solidity**: The bytecode used in Ethereum.
- **Ethereum Virtual Machine (EVM)**: The virtual machine that runs the bytecode on each blockchain node.
- **Transaction**: A transaction occurs when a function call or contract is used.
- **Contract Address**: The address of the contract, which can be found with the `to` parameter.
- **Out of Gas**: An error that occurs when the gas limit is reached.

