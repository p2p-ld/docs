```{index} IPFS
```
# IPFS

If IPFS is {index}`BitTorrent` + {index}`git`, and {key}`ActivityPub` is {key}`Distributed Messaging` + {key}`Linked Data`, then p2p-ld is IPFS + ActivityPub. We build on IPFS and are heavily inspired by its design and shortcomings revealed by practical use.


## Problems 

- Slow access!
- No identity misses the social nature of infrastructure. Where bittorrent had trackers, there is no similar concept in IPFS to organize archives. 
	- Hence the need for filecoin, an exogenous incentive to store, but then it becomes transactional which generates its own problems.
	- Trust! eg. its use in phishing attacks is because there is no way to know who the hell a given CID is owned by. It needs to be possible to do social curation, or at leats know when something is riskier or not.
- Lack of metadata means having to build a lot of shit post-hoc, like IPLD and multihashes and codecs and whatnot.

## IPLD

## Overlap

- {index}`Merkle DAG`s

## Differences

- Not permanent storage! Identities retain custody and control over objects in the network.
