# Dat/Hypercore

Hypercore, originally known as the Dat protocol {cite}`ogdenDatDistributedDataset2017`, and apparently now known as HolePunch, is a p2p protocol designed for versioned transfer of large files.

## Summary

- **Merkle Trees** - The underlying data model is a tree!
	- Specifically an ordered tree 
- **Version Controlled** - including incremental versioning
- **Sparse Replication** - Like bittorrent, it is possible to only download part of a given dataset.
- **Encrypted** transfer
- **Discovery** - Multiple mechanisms
	- DNS name servers
	- Multicast DNS
	- Kademlia DHT

### SLEEP

Data structure that supports traversing dat graphs

### Protocol

Message container format:

```
<varint - length of rest of message>
  <varint - header>
  <message>
```

Header consists of 
- **type** - 
	- 0 - `feed`
	- 1 - `handshake`
	- 2 - `info` - state changes, like changing from uploading to downloading
	- 3 - `have` - telling other peers what chunks we have
	- 4 - `unhave` - you deleted something you used to have
	- 5 - `want` - tell me when you `have` these chunks
	- 6 - `unwant` - I no longer want these!
	- 7 - `request` - Get a single chunk of specifically indexed data.
	- 8 - `cancel` - nevermind
	- 9 - `data` - actually send/receive a chunk!
- **channel** - 0 for metadata, 1 for content

## Lessons

### Adopt

- Using hashes of public keys during discovery rather than the public keys themselves. Avoids needing a bunch of key rotations.
- Use per-file hashing (as per BitTorrent v2 as well)

### Adapt

- Identities as cryptographic keys is great, but need some means of giving them petnames/shortnames.
- Tree-only data structures make everything append-only!
- The Random Access properties are really neat! (being able to read a specific 100MB chunk within a CSV) but they come with some tradeoffs! 

### Ignore


```{index} Hypercore; Holepunch
```
## Holepunch

https://docs.holepunch.to/
