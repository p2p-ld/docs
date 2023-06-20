```{index} pair: Protocol; BitTorrent
```
(BitTorrent)=
# BitTorrent

Bittorrent is unarguably the most successful p2p protocol to date, and needless to say we have much to learn walking in its footsteps. 

## Summary

There are a number of very complete explanations of BitTorrent as a protocol, so we don't attempt one here outside of giving an unfamiliar reader a general sense of how it works. 

### Torrents

Data is shared on BitTorrent in units described by `.torrent` files. They are [bencoded](https://en.wikipedia.org/wiki/Bencode) dictionaries that contain the following fields (in Bittorrent v1):

- `announce`: The URL of one or several trackers (described below)
- `info`: A dictionary which includes metadata that describes the included file(s) and their length. The files are concatenated and then split into fixed-size pieces, and the info dict contains the SHA-1 hash of each piece.

For example, a directory of three random files has a (decoded) `.torrent` file that looks like this:

```json
{
  "announce": "http://example.tracker.com:8080/announce",
  "info":{
    "files":[
        {
          "length": 204800,
          "path":["random-file3"]
        },
        {
          "length": 51200,
          "path": ["random-file2"]
        },
        {
          "length": 102400,
          "path":["random-file"]
        }
    ],
    "name": "random",
    "piece length": 16384,
    "pieces": "<long string of concatenated hashes>"
  }
}
```

The contents of a torrent file are then uniquely indexed by the `infohash`, which is the hash of the entire (bencoded) `info` dictionary. {key}`Magnet Links <BitTorrent; Magnet Links>` are an abbreviated form of the `.torrent` file that contain only the info-hash, which allows downloading peers to request and independently verify the rest of the info dictionary and start downloading without a complete `.torrent`.

A generic magnet link looks like:

`magnet:?xt=urn:btih:<INFOHASH>&dn=<TORRENT_NAME>&tr=<TRACKER_URL>`

BitTorrent v2 extends traditional `.torrent` files to include a {index}`Merkle Tree` which generalizes the traditional piece structure with some nice properties like being able to recognize unique files across multiple `.torrent`s, etc. 

### Trackers

To connect peers that might have or be interested in the contents of a given `.torrent` file, the `.torrent` (but not its contents) are uploaded to a {index}`Tracker <BitTorrent; Tracker>`. Peers interested in downloading a `.torrent` will connect to the trackers that it indicates in its `announce`[^announcelist] metadata, and the trackers will return a list of peer IP:Port combinations that the peer can download the file from. The downloading (leeching) peer doesn't need to trust the uploading (seeding) peers that the data they are sending is what is specified by the `.torrent`: the client checks the computed hash of each received piece against the hashes in the info dict, which is in turn checked against the info hash. 

Trackers solve the problem of {index}`Discovery` by giving a clear point where peers can find other peers from only the information contained within the `.torrent` itself. Trackers introduce a degree of brittleness, however, as they can become a single point of failure. Additional means of discovering peers have been added to BitTorrent over time, including [{index}`Distributed Hash Tables <DHT>`](http://www.bittorrent.org/beps/bep_0005.html), [Peer Exchange](http://www.bittorrent.org/beps/bep_0011.html)

Beyond their technical role, BitTorrent trackers also form a **social space** that is critical to understand its success as a protocol. While prior protocols like {index}`Gnutella <Protocol; Gnutella>` (of {index}`Limewire <Client; Limewire>`/{index}`Kazaa <Client; Kazaa>` fame) had integrated search and peer discovery into the client and protocol itself, separating trackers as a means of organizing the BitTorrent ecosystem has allowed them to flourish as a means of experimenting with the kinds of social organization that keeps p2p swarms healthy. Tracker communities range from huge and disconnected as in widely-known public trackers like ThePirateBay, to tiny and close-knit like some niche private trackers.

The bifurcated tracker/peer structure makes the overall system remarkably *resilient*. The trackers don't host any infringing content themselves, they just organize the metadata for finding it, so they are relatively long-lived and inexpensive to start compared to more resource- and risk-intensive piracy vectors. If they are shut down, the peers can continue to share amongst themselves through DHT, Peer Exchange, and any other trackers that are specified in the `.torrent` files. When a successor pops up, the members of the old tracker can then re-collect the `.torrent` files from the prior site, and without needing a massive re-upload of data to a centralized server repopulate the new site.

```{seealso}
See more detailed discussion re: lessons from BitTorrent Trackers for social infrastructure in "[Archives Need Communities](https://jon-e.net/infrastructure/#archives-need-communities)" in {cite}`saundersDecentralizedInfrastructureNeuro2022`
```

### Protocol

Peers that have been referred to one another from a tracker or other means start by attempting to make a connection with a 'handshake' that specifies the peer is connecting with BitTorrent and any other protocol extensions it supports. 

There are a number of subtleties in the transfer protocol, but it can be broadly summarized as a series of steps where peers tell each other which pieces they have, which they are interested in, and then sharing them amongst themselves. 

Though not explicitly in the protocol spec, two prominent design decisions are worth mentioning (See eg. {cite}`legoutRarestFirstChoke2006` for additional discussion).

- **Peer Selection:** Which peers should I spent finite bandwidth uploading to? BitTorrent uses a variety of **Choke** algorithms that reward peers that reciprocate bandwidth. Choke algorithms are typically some variant of a 'tit-for-tat' strategy, although rarely the strict bitwise tit-for-tat favored by later blockchain systems and others that require a peer to upload an equivalent amount to what they have downloaded before they are given any additional pieces. Contrast this with [{index}`BitSwap`](#BitSwap) from IPFS. It is by *not* perfectly optimizing peer selection that BitTorrent is better capable of using more of its available network resources. 
- **Piece Selection:** Which pieces should be uploaded/requested first? BitTorrent uses a **Rarest First** strategy, where a peer keeps track of the number of copies of each piece present in the swarm, and preferentially seeds the rarest pieces. This keeps the swarm healthy, rewarding keeping and sharing complete copies of files. This is in contrast to, eg. [SWARM](#SWARM) which explicitly rewards hosting and sharing the most in-demand pieces. 


## Lessons

(This section is mostly a scratchpad at the moment)

### Adopt

- Eventually had to add a generic 'extension extension' ([BEP 10](http://www.bittorrent.org/beps/bep_0010.html)), where on initial connection a peer informs another peer what extra features of the protocol it supports without needing to make constant adjustment to the underlying BitTorrent protocol. This pattern is adopted by most p2p protocols that follow, including [Nostr](#Nostr) which is almost *entirely* extensions.
	- These extensions are not self-describing, however, and they require some centralized registry of extensions, see also [IPFS](#IPFS) and its handling of codecs, which curiously build a lot of infrastructure for self-describing extensions but at the very last stage fall back to a single git repository as the registry.
- `.torrent` files make for a very **low barrier to entry** and are extremely **portable.** They also operate over the existing idioms of files and folders, rather than creating their own filesystem abstraction.
- Explicit peer and piece selection algorithms are left out of the protocol specification, allowing individual implementations to experiment with what works. This makes it possible to exploit the protocol by refusing to seed ever, but this rarely occurs in practice, as people are not the complete assholes imagined in worst-case scenarios of scarcity. Indeed even the most selfish peers have the intrinsic incentive to upload, as by aggressively seeding the pieces that a leeching peer already has, the other peers in the swarm are less likely to "waste" the bandwidth of the seeders and more bandwidth can be allocated to pieces that the leecher doesn't already have.


### Adapt

- **Metadata**. Currently all torrent metadata is contained within the tracker, so while it is possible to restore all the files that were indexed by a downed tracker, it is very difficult to restore all the metadata at a torrent level and above, eg. the organization of specific torrents into hierarchical categories that allow one to search for an artist, all the albums they have produced, all the versions of that album in different file formats, and so on. 
- Give more in-protocol tools to social systems. This is tricky because we don't necessarily need to go down the road of DAOs and make strictly enforceable contracts. Recall that it is precisely by relaxing conditions of "optimality" that BitTorrent makes use of all resources available. 
- **Cross-Swarm Indexing** - BitTorrent organizes all peer connections within swarms that are particular for a given `.torrent` file. We instead want to be able for a set of socially connected peers to be able to share many files. 
- **Anonymity** This is also a tricky balance - We want to do three things that are potentially in conflict:
	1. Make use of the social structure of our peer swarm to be able to allocate automatic rehosting/sharding of files uploaded by close friends, etc.
	2. Maintain the possibility for loose anonymity where peers can share files without needing a large and well-connected social system to share files to them
	3. Avoid significant performance penalties from guarantees of strong network-level anonymity like Tor. 
- **Trackers** are a good idea, even if they could use some updating. It is good to have an explicit entrypoint specified with a distributed, social mechanism rather than prespecified as a hardcoded entry point. It is a good idea to make a clear space for social curation of information, rather than something that is intrinsically bound to a torrent at the time of uploading. We update the notion of trackers with [Peer Federations](#Peer-Federations).

## References

- Bittorrent Protocol Specification (BEP 3): http://www.bittorrent.org/beps/bep_0003.html
- Bittorrent v2 (BEP 52): http://www.bittorrent.org/beps/bep_0052.html
- Magnet Links (BEP 9): http://www.bittorrent.org/beps/bep_0009.html
- More on BitTorrent and incentives - {cite}`cohenIncentivesBuildRobustness2003`


[^announcelist]: Or, properly, in the `announce-list` per ([BEP 12](http://www.bittorrent.org/beps/bep_0012.html))