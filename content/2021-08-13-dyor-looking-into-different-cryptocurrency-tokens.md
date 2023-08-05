---
title: "DYOR - Looking into different Crypto Tokens"
date: "2021-08-13"
tags: ["Cryptocurrency"]
image: ""
gradients: ["#8EC5FC", "#E0C3FC"]
---

*This post was collated from 2021-08-13 to 2021-10-08*

## Polygon
Previously known as **Matic Network**, **Polygon** is a *layer 2* scaling solution (first launched in 2017) that utilises the **Polygon SDK**, a toolkit that developers can use to achieve secure and easy-to-scale applications. It is used to scale applications on the Ethereum Network. Its architectural design is built with the *Plasma Framework* and the Proof of Stake (PoS) mechanism as a **sidechain**. Technically, this means that Ethereum can be a **multi-chain** system with the incorporation of the Polygon ecosystem as a connector.

### Layer 2 Solution
In general, Layer 2 solutions are like wrapper solutions for Layer 1 blockchains, sending the computations off-chain (similar to oracles) but also known as a *sidechain*. Sidechains are smaller blockchains that connect to the mainchain. In this case, **Ethereum** is the mainchain (Layer 1) and the **Matic chain** is the sidechain (Layer 2). Tokens are deposited on the main Smart Contract (on the Ethereum network).

The benefits of Layer 2 solutions like Polygon are:
- Increase throughput on the mainchain by minimizing on-chain computations.
- Spread transaction efficiency across the network.
- Reduce computation and gas fees.

However, it can also add more complexity to the system and may have settlement finality issues.

Developers can use the Polygon SDK to easily connect their blockchain to the Ethereum mainchain via the scalable Polygon ecosystem. The connection between the two is facilitated by **Plasma**, a framework that allows for the creation of sidechains to Ethereum's blockchain as a trust security layer. These sidechains, as mentioned earlier, collectively off-chain compute transactions before finalizing them on the Ethereum mainchain. However, Plasma uses one transfer per transaction.

#### Rollup
A **Rollup** is a term used in blockchain to define the aggregation of transactions off-chain inside a smart contract to reduce fees and congestion. There are different types of rollups, including:

**ZK Rollups**: This method is similar to Plasma, where one transaction per transfer is used. Rollup bundles hundreds of transfers, and **Zero Knowledge proofs** are used as proof for the batched transactions on Ethereum to validate their validity. It contains a validity proof.

**Optimistic Rollups**: This type of rollup includes **fraud proofs** used to provide an optimistic view of the world and provide evidence of incorrect state transitions. This serves as a security feature, as **block producers** are also involved. It provides scalability for Layer 2 while retaining Layer 1 (Ethereum) security.

### MATIC
**MATIC** is the token for Polygon and is mainly used for governance, security, and gas fees on Polygon services. Since the ecosystem uses PoS, MATIC is also used for staking. The maximum supply of MATIC tokens is **10,000,000,000**.

---

## Nano
Nano is a lightweight cryptocurrency that is known for its very low latency and zero transaction fees. It was first launched in 2015 and is a simple protocol used for easy peer-to-peer transactions without a centralized entity. One of its key features is that Nano uses a **block lattice** structure, which is a **DAG** (Directed Acyclic Graph) data structure from graph theory. Nano focuses on providing speed, making it one of the fastest cryptocurrency networks for transaction processing.

### Directed Acyclic Graph (DAG)
A **DAG** is a directed graph that consists of directional edges and vertices. The term **Acyclic** means that there are no cycles in the graph. In the context of blockchain technology, transactions are stored on a graph-like structure without any loops back to previous transactions, thus maintaining immutability. DAG can be seen as a tree-like structure that expands to the linked list structure commonly used in blockchains. DAG offers advantages such as achieving consensus on validating transactions coming from network users rather than miners, which leads to lower energy consumption. However, DAGs may require central coordinators to handle certain tasks.

---

## The Graph
The Graph is an indexing protocol used for querying data on distributed networks. It aims to allow applications to create public APIs that can organize and manage public data on blockchains or databases such as Ethereum, Binance, Cosmos, and IPFS. Developers building DApps can use and build on this data without the need for a server, leveraging the public infrastructure provided by The Graph.

The decentralization of The Graph comes from having nodes on the Graph network that can process the requests.

### Nodes
There are several nodes on the Graph network, but two important ones are:

**Indexers**
Indexers are responsible for staking GRT (Graph Tokens) provided by users on the network. They execute query requests and earn GRT for their services. Indexers also ensure the availability, trustworthiness, and decentralized properties of the open APIs.

**Curators**
Curators are nodes that organize the data for the public APIs created. These APIs have a special name called **subgraph**. Curators analyze these subgraphs, and potential subgraphs are signaled to the indexers (curation). Developers can then use these subgraphs to easily access more accurate data.

**Delegators**
Delegators earn a portion of GRT from Indexers by delegating their stake to them.

### Subgraphs
From the official documentation, a subgraph is defined as "which data The Graph will index from Ethereum and how it will store it. Once deployed, it will form a part of a global graph of blockchain data." Essentially, a subgraph is an API that uses GraphQL to query a section of the blockchain specified by the API. The data is stored in JSON format and can be easily managed using Web3.

Using The Graph as a framework in a DApp eliminates the need for custom push and pull oracles to store and manage on-chain storage. This simplifies the development process and abstracts away the complexity and time required. However, it's important to note that using The Graph means the data is accessible to everyone, and there may be limitations on authentication such as requiring an API key to access certain data.

To build and deploy a subgraph, you would typically use The Graph's CLI. A subgraph consists of:

- `subgraph.yaml`: A manifest file that describes the subgraph.
- `schema.graphql`: A schema that defines how the data is structured and queried.
- `AssemblyScript Mappings`: Mappings that define how the data is indexed and processed.

### GRT
GRT is the native ERC-20 cryptocurrency that powers The Graph's blockchain. It is primarily used for staking, where Indexers can earn GRT for processing queries. GRT tokens can also be used for payments, governance, and other purposes. The maximum supply of GRT is 10,057,044,431 tokens.

---

## Harmony
Harmony is an open blockchain platform designed for deploying DApps. It utilizes sharding to address the scalability issues faced by Ethereum. Harmony's block creation time is around 2 seconds, significantly faster than Ethereum's ~14 seconds. The mainnet consists of four shards, each containing 1000 nodes.

Sharding has proven to be an effective approach for scalability in blockchains. Harmony's sharding process is random and utilizes Verifiable Delay Function (VDF) to achieve this randomness.

### Verifiable Delay Function (VDF)
VDF is a function that takes a sequence of numbers as input and requires a certain amount of time to verify and evaluate. VDF is desirable in decentralized systems as it generates randomness in a trustless environment. The motivation for VDF is the difficulty of achieving true randomness in blockchain networks, as traditional sources of randomness may be susceptible to manipulation or bias.

### Crosslinks
Crosslinks in Harmony are checkpoints that provide a way to reference shard blocks in the beacon chain. They allow the shards to communicate and maintain consensus across the network. Crosslinks are crucial for the security and integrity of the Harmony blockchain, as they ensure that all shards are in sync.

### Consensus Mechanism
Harmony utilizes a consensus mechanism called Effective Proof-of-Stake (EPoS). EPoS combines both Proof-of-Stake (PoS) and Practical Byzantine Fault Tolerance (PBFT) to achieve consensus. Validators are chosen through a random selection process, and they take turns proposing and validating blocks. The PBFT consensus algorithm ensures fast finality and security.

### Staking
Staking is an integral part of Harmony's ecosystem. Validators and delegators can stake their tokens to participate in block validation and earn rewards. Validators are responsible for block creation and consensus, while delegators support validators by staking their tokens and receiving a portion of the rewards.

### EVM Compatibility
Harmony is fully EVM-compatible, which means that developers can use existing Ethereum tools and languages, such as Solidity, to build and deploy smart contracts on the Harmony blockchain. This compatibility allows for easy migration of existing Ethereum DApps to Harmony, providing developers with more options and flexibility.

---

## Enjin
Enjin is a blockchain-based gaming platform that was launched on the Ethereum network in 2018. It enables users to create clans, chat, obtain, and sell virtual items within games. One of its major features is the ability for developers to create and manage in-game items as virtual tokens on the Ethereum blockchain. These virtual tokens, known as non-fungible tokens (NFTs), represent unique and rare items and are minted and backed by Enjin Coin (ENJ), which assigns them a value relative to ENJ. The minted tokens are stored on-chain in the form of ERC-1155 tokens.

So Enjin isn’t a blockchain, rather it a gaming platform. In term of technical, there isn’t really much I can found so I’m really not sure, but from I can found, it just uses Etheruems goverance and concensus methods. There are various SDK to enable functionality such as

- buying ENJ
- minting in game items
- playing game and acquiring virutal items 
- trading 
- selling Basically a marketplace for game items. These SDK makes sure that developers minimimse cost and complexity when trying to build and create on ENJ platform.

### Enjin Coin (ENJ)
Enjin Coin (ENJ) is the native ERC-20 token of the Enjin platform. As mentioned earlier, ENJ is used to assign value to virtual items within games. It has a maximum supply of 1,000,000,000 (1 billion) tokens.

---

## 0x
0x is a protocol that was launched on the Ethereum network in 2017. Its purpose is to facilitate peer-to-peer exchanges of ERC-20 tokens and ERC-721 non-fungible tokens (NFTs) on the Ethereum platform. Essentially, 0x acts as a decentralized exchange (DEX) protocol that allows users to trade tokens directly with each other. What sets 0x apart is its ability to enable developers to build exchange functionalities on top of its infrastructure.

### Makers and Takers
In the 0x network, there are two main actors: makers and takers.

- Makers: Makers are users who create buy or sell orders on the 0x network.
- Takers: Takers are users who fulfill the buy or sell orders created by makers.

### 0x Architecture
0x utilizes a state channel approach to take computation off-chain, reducing transaction costs on the Ethereum blockchain. The state channel technology enables the storage of transaction orders off-chain, leading to less congestion on the network and lower gas fees. Since 0x is built on the Ethereum blockchain, it utilizes Ethereum's proof-of-stake consensus mechanism and other associated protocols.

### ZRX
ZRX is the native token of the 0x protocol. It is primarily used for governance on the 0x platform, allowing ZRX holders to influence voting proposals for the protocol. Additionally, ZRX is used for paying trading fees and staking in pools to earn ETH rewards. The maximum supply of ZRX tokens is 1,000,000,000.

---

## Avalanche
Avalanche is a smart contract platform launched in 2020, designed for building decentralized finance (DeFi), trading, and economic applications. It boasts the fastest standard transaction finality of 1 second and one of the largest validator sets, providing low-cost and eco-friendly transactions. Avalanche utilizes a proof-of-stake consensus mechanism and is compatible with the Ethereum Virtual Machine (EVM), making it compatible with the Solidity programming language.

### Primary Network
The Avalanche primary network serves as the global hub for Avalanche's blockchain and consists of three main chains:

- Exchange Chain (X-Chain): The X-Chain is used for trading assets on the Avalanche platform.
- Platform Chain (P-Chain): The P-Chain manages subnets and coordinates validators. It contains metadata about the Avalanche network.
- Contract Chain (C-Chain): The C-Chain is where smart contracts are created and executed.

In the Avalanche network, validators are members of one or more subnets, and subnets achieve consensus on multiple blockchains. Validators provide their location, undergo KYC, and hold a valid license, sacrificing some privacy to participate and secure the network.

### Snowman
Avalanche uses a Directed Acyclic Graph (DAG) structure rather than a linear blockchain. The Snowman consensus protocol is specifically used for the linear chain within Avalanche. Snowman's high throughput makes it optimized for smart contracts, which are executed on the C-Chain. The protocol involves broadcasting a transaction to a set of validators, reaching a quorum, and adding the result to a counter. After a certain threshold, the transaction is considered valid. This approach enhances transaction validation speed and scalability.

## AVAX
AVAX is the native token of the Avalanche network, with a total supply of only 720,000,000 tokens. AVAX is used to pay for fees on the network, reward stakers who secure the network through proof of stake, and provide utility services within the ecosystem. Notably, transaction fees paid to the network are burned, contributing to the scarcity of the token.

---

## IOTA Foundation
The IOTA Foundation is a distributed ledger technology (DLT) solution based on a direct acyclic graph (DAG). It was founded in 2015 with a focus on the Internet of Things (IoT) and aims to enable feeless and secure transactions between IoT devices.

### Tangle
IOTA's distributed ledger is known as the Tangle. It utilizes a DAG structure to enable feeless microtransactions for IoT devices. In the Tangle, transactions join the graph as vertices and confirmations connect them with edges to two previous transactions. This approach eliminates the need for traditional miners and validators found in blockchain systems. The Tangle achieves fast confirmation times and broadcasts confirmations to all nodes, ensuring an unbiased view of the network state. Additionally, a simple proof-of-work (PoW) is used to verify transactions.

Benefits of Tangle and DAG technology include:
- Environmentally friendly with low energy consumption
- Fast transactions with minimal computation
- Feeless transactions without the need for miners
- Increased efficiency and security with more nodes
- Infinite scalability and higher throughput

### Central Coordinator (Coordicide)
Previously, the IOTA network relied on a Central Coordinator, which was a central node that governed the confirmation of valid transactions. However, this introduced centralization. The Coordicide initiative was launched to eliminate the Central Coordinator, leading to the development of IOTA 2.0. It's important to note that the exact mechanism of how the Central Coordinator is being replaced or removed entirely requires further research.

### Fast Probabilistic Consensus (FPC)
FPC is used in the IOTA network to quickly resolve conflicts, such as double-spending issues. When conflicts arise, neighboring nodes engage in consensus to reach a quick agreement on whether the conflicting transactions should be accepted.

## MIOTA
MIOTA represents Mega IOTA and is equivalent to 1,000,000 IOTA. It is commonly used for trading purposes, where buying and selling IOTAs are denoted in units of MIOTA. The maximum supply of MIOTA tokens is 2,779,530,283.

---

## Zilliqa
Zilliqa is a blockchain platform developed in 2017 that utilizes sharding as a Layer 2 scaling solution. It is a public permissionless blockchain that enables decentralized applications (DApps) to run on its network with high throughput and speed. Zilliqa has its own programming language called Scilla, which is used for writing smart contracts.

### Sharding
Zilliqa's sharding approach involves splitting the blockchain into smaller and unique shards. Each shard is responsible for validating a section of the blockchain and processing a subset of transactions. This parallel processing enables linear scalability, reducing latency and increasing performance. Nodes in Zilliqa perform proof-of-work (PoW) within the shards.

### Practical Byzantine Fault Tolerance (pBFT)
Practical Byzantine Fault Tolerance (pBFT) is the consensus mechanism used in Zilliqa. Each shard elects a leader, with the remaining nodes serving as backup nodes. The leader broadcasts blocks to the backup nodes, and consensus is reached when at least two-thirds of the nodes agree on the validity of the block. Zilliqa's pBFT consensus ensures deterministic finality, eliminating the need for multiple confirmation blocks to establish the state of the blockchain. The latest state block is always considered trusted.

## ZIL
ZIL is the native token of the Zilliqa blockchain, created in 2017. It has a maximum supply of 21,000,000,000 tokens. ZIL serves as a utility token used to pay for transaction fees and Scilla smart contracts on the Zilliqa network. Additionally, it provides incentives for miners.

