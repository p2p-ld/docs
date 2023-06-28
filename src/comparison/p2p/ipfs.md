```{index} IPFS
```
(IPFS)=
# IPFS

If IPFS is {index}`BitTorrent` + {index}`git`, and {index}`ActivityPub` is {index}`Distributed Messaging` + {index}`Linked Data`, then p2p-ld is IPFS + ActivityPub. We build on IPFS and are heavily inspired by its design and shortcomings revealed by practical use.

## Summary

```{index} IPFS; BitSwap
```
(BitSwap)=
### BitSwap

```{index} IPFS; IPLD
```
(IPLD)=
### IPLD

```{index} IPFS; Multiformats
```
### Multiformats

- https://ipfs.io/ipns/multiformats.io/
- {index}`IPFS; Multihash` - https://ipfs.io/ipns/multiformats.io/multihash/
- {index}`IPFS; Multicodec` - https://github.com/multiformats/multicodec

```{index} IPFS; libp2p
```
(libp2p)=
### libp2p

## Problems 

- Slow access!
- No identity misses the social nature of infrastructure. Where bittorrent had trackers, there is no similar concept in IPFS to organize archives. 
	- Hence the need for filecoin, an exogenous incentive to store, but then it becomes transactional which generates its own problems.
	- Trust! eg. its use in phishing attacks is because there is no way to know who the hell a given CID is owned by. It needs to be possible to do social curation, or at leats know when something is riskier or not.
- Lack of metadata means having to build a lot of shit post-hoc, like IPLD and multihashes and codecs and whatnot.

## Overlap

- {index}`Merkle DAG`s

## Differences

- Not permanent storage! Identities retain custody and control over objects in the network.
