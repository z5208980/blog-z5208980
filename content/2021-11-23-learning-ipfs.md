---
title: "IPFS and Filecoin"
date: "2021-11-23"
tags: ["Developer", "Web3", "Blockchain"]
image: ""
gradients: ["#43CBFF", "#9708CC"]
---

## Abstraction
Just note and information I've learnt while learning about IPFS and Filecoin.

### IPFS
-   Distributed storage **(P2P)**
-   Users (who are nodes) connect to each other to access and storage that has been pinned.
-   **Merkle DAG** (Merkle Direct Acyclic Graphs)
-   IPFS will contain a (content Identifier) cid, that is a hash that points to content. Usually in format starting with **Qm (v0), bafy (v1)**
-   You can host server (one node)
-   Pinning your content in hopes others can store it.
-   Run your network of nodes    
-   Use services (Pinata, Infura)

### Filecoin
-   Benefit to be host yourself without the need for paid service and dependant on other nodes.
-   P2P permissionless
-   Built with web3 and IPFS.
-   Has cryptographical proof to ensure decentralisation.

### How Filecoin works.
-   Users want to store content on the Filecoin network, so they make it publicly available for the storage market.
-   This availability allows miners to compete (bid) for that content. Users will then select the winning miners.
-   Filecoin transforms the data (request to be stored) in DAG format. Also has resulting cid which is compatible with IPFS.   
-   *Proof of verification* to publish on Filecoin blockchain is done via **Proof of Replication (ProRep)** and the miner stores data.  
-   **Proof-of-Spacetime (PoSt)** is a procedure during which miners are given cryptographic challenges that can only be correctly answered if the miner is actually storing a copy of the sealed data.
-   **Validate proofs** are added to the blockchain, and miners **earn rewards**.
-   Whenever users want the file, they select a miner fast, affordable miner to retrieve content.
    
### Welcome to Web 3.0
-   Tradition web uses location address to point to a single location, and if the server fails then we can’t access content. And even with the webpage being loaded on another device, we still can’t access it.
-   IPFS is a protocol for the web. Instead of using location addressing, IPFS uses content addressing. That is a hash of the content.
    
Web 3 is a combination of,
-   Distributed web **(offline access, etc)**
-   Blockchain **(allow permission, incentive)**
-   Semantic web **(interpolarity)**
-   Web 3 enables open service. **(trust)**

### Content Addressing
-   Is derived from the content and not location of where it is stored.   
-   Bitswap used to *gossip*.
-   Message protocol in IPFS used to exchange content.
-   **DHT (Distributed Hash Table)**: a distributed system for mapping key, val. It maps what the user is looking for to the peer that is storing the matching content.
-   When founding content we used
-   Root cid of the *DAG structure* by requesting node of each level

### Scenario of how IPFS discovery
-   Peer A sends a want-have cid I to network.
-   Peer B sees the message and sends a HAVE cid to Peer A.
-   Peer A then can request for the cid block by using want-block cid
-   `HAVE` message. (Not necessarily the content block), rather just want to know. `HAVE` is usually sent back to the want-have peer.    
-   Broadcast a `WANT` to connect to peers.
 -   `want -have`    
 -   `want-block`
-   `DONT_HAVE` message
    
### Filecoin Concept
- decentralised is not the same as distributed.
- better access content
- makes it peer to peer

### Process IPFS
- generate acid by uploading the content. (represents your content not by location [DNS])
- stored DHT on who has certain acids.
