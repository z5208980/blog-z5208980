---
title: "Near Smart Contract"
date: "2022-01-17"
tags: ["Web", "Developer"]
image: ""
gradients: ["#fdfcfb", "#e2d1c3"]
---

### Motivation
There is a hackathon, that I'm attending and I found a group. So this is basically, my learning progress and note for understanding how
to create an application and smart contracting on the NEAR ecosystem. From what I know so far, is that NEAR's `web3` is given by `near-api-js` api
and the smart contract is coded in `AssemblyScript` or `Rust`, but for my purposes I think I want that extra learning curve in learning a new language (since AS is similar to JS or TS).

### Creating an NEAR App
`npx create-near-app app-name`
Essentially, this command allows the boilerplate of a simple application in different frameworks, either a combination of 
- Frontend: `Vanilla JS` or `React.js`
- Backend: `AS` or `Rust`

I'm going to go for *Vanilla JS* and *Rust* as I haven't coded in Vanilla JS in awhile and Rust is a new language I want to learn.

### Compiling and using NEAR contract (Rust)
To compile and implement a NEAR contract on Rust, the framework or library to use is `near-sdk-rs`

Inspecting the default (simple) smart contract on the `create-near-app`, [here](https://github.com/near/create-near-app/blob/master/common/contracts/rust/src/lib.rs),

Before starting, we should look at the structure of a smart contract. It typically begins with the folder titled that *Contract Name*
- SmartContract
    - src
        - lib.rs    (Where the smart contract implementation is)
    - Cargo.toml    (Used as metadata about the smart contract including dependencies, version, compile configs, etc)

Taking a look into lib.rs
```rust
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
```

Usually, there should be a import of the near sdk **borsh** which is super helper for **conversing gas** in both **storage and gas cost**. Any other import and libraries what may be needed for the contract should also be loaded at the beginning of the `.rs` file. Examples include.
```rust
use near_sdk::{env, near_bindgen, setup_alloc, AccountId, Balance, EpochHeight};
```
where we see this is anothe import of the `near_sdk` but importing the `env` and `near_bindgen` and account information as well as the blockchain information.

And finally, mostly likely, smart contract will be using a key value storage system. Hence in Rust we'll need to include the library,
```rust
use std::collections::HashMap;
```
**Note:** The other method relies on **singleton** storage more like a list of a custom *struct*.

### Memory allocation and improve efficiency
This is a must include in almost all the smart contract used. It simply as memory allocation to make memory management as efficient as possible when compile with **WASM**.
```rust
setup_alloc!();
```
### Near Wrapper in Rust
Moving on to the implementation of the contract in Rust, inorder for Near to interact with the Rust contract, it'll require the **Macro** `#[near_bindgen]`. This is particularly important since creating `structs` or the contract itself via `impl` then we need to wrap the `#[near_bindgen]` by prepending in the header. For example, the contract will be called, *ExampleContract*.

In the case of a contract, we need to define a struct datatype. This is followed by, a `impl Default` which is a error handler for the initialisation of the contract. In most cases this can be the constructor of the smart contract, but there can be case where we want more control of the contract so, we have to do something there and add the initalisation in the `impl ExampleContract` instead. This is lastly finished with the logic of the smart contract. Again we'll need to use the *macro* `[near_bindgen]`,

```rust
#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize)]
pub struct ExampleContract { 
    // attributes that the contract will have 
    balances: HashMap<AccountId, Balance>, // Example of Hashmap, I think it translates to mapping(address => uint256) balances
    result: Option<Balance>,    // Example of optional variable
    n_balance: U128,

}

// This can most likely be the constructor for the smart contract
impl Default for ExampleContract {
    fn default() -> Self {
        env::panic(b"contract should be initialized before usage")
        // Self { balances: HashMap::new(), }
    }
}

// This is where all the methods and implementation belongs
#[near_bindgen]
impl ExampleContract {
    #[init] // Using [#init] macro to tell NEAr that this is a initialisation function. This is like the initialiser
    pub fn new() -> Self {
        assert!(!env::state_exists(), "The contract is already initialized");
        ExampleContract {
            balance: HashMap::new(),
            n_balance: 0,
            result: None,
        }
    }

    // See Borrowing &self
    pub fn get_votes(&self) -> HashMap<AccountId, U128> {
        self.balance
            .iter()
            .map(|(account_id, stake)| (account_id.clone(), (*stake).into()))
            .collect()
    }
}
```

### `&self`
This allows the methods to get a view of the states of the smart contract without changing the state itself. This is commonly used in **getter methods** to safely get attributes and states in the smart contract.


```rust
pub fn getter(&self) -> AccountId { ... }
```

### `&mut self`
This will allows for change the state, and hence better for setter methods or a function that requires updating the state.

```rust
pub fn setter(&mut self, new_value: String) { ... }
```

### `#[payable]`
Very similar to `payable` macro in *Solidity* just include on top of function 

```rust
#[payable]
pub fn payable_function() {
    let tokens = env::attached_deposit()
}
```

### Private 
To create a private methods, just remove the `pub` in the `fn` declaration

```rust
#[private]
fn private_method() { ... }
```

### Internal
From solidity, `internal` macro in NEAR is using `#[private]`. This hence can only be called by the contract itself.

```rust
#[private]
pub fn contract_method() { ... }
```

### Using solidity to NEAR via Aurora

Requirements
- Metamask on Ropsten Testnet

Connect to ropsten testnet on metamask, then goto the link: [https://testnet.rainbowbridge.app/transfer](https://testnet.rainbowbridge.app/transfer).

