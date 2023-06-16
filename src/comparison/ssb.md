```{index} Protocol; Secure Scuttlebutt
```
# Secure Scuttlebutt



## Feeds & Metafeeds

- Peers maintain a list of feeds they subscribe to
- When peers connect, they ask for updates to subscribed feeds
- Metafeeds can provide metadata about other feeds, and can form a tree structure with other Metafeeds as subfeeds.
	- {index}`Bencoded <single: Encoding; Bencoding>` rather than JSON.

```{mermaid}
flowchart LR
  subgraph Main [Main Feed]
  	mf["`Main Feed Posts
  	*metafeed/announce*
  	message`"]
  end
  subgraph Meta [Meta feed]
  	direction TB
  	mf1["`Metafeed posts
  	*metafeed/add/existing
  	message`"]
  	mf2["`Metafeed posts
  	*metafeed/add/existing
  	message`"]
  	mf3["`Metafeed posts
  	*metafeed/add/derived
  	message`"]
	mf4["`Metafeed posts
  	*metafeed/add/existing
  	message`"]
  	mf1 --> mf2
  	mf2 --> mf3
  	mf3 --> mf4
  end

  subgraph SubfeedA [Subfeed A]
  	direction LR
  	sfa1["`Application specific 
  	message in subfeed`"]
  	sfa2["`Application specific 
  	message in subfeed`"]
  	sfa1 --> sfa2
  end 
  subgraph SubfeedB [Subfeed B]
  	direction LR
  	sfb1["`Application specific 
  	message in subfeed`"]
  	sfb2["`Application specific 
  	message in subfeed`"]
  	sfb1 --> sfb2
  end 
  subgraph SubfeedC [Subfeed C]
  	direction LR
  	sfc1["`Application specific 
  	message in subfeed`"]
  	sfc2["`Application specific 
  	message in subfeed`"]
  	sfc1 --> sfc2
  end 
  subgraph SubfeedD [Subfeed D]
  	direction LR
  	sfd1["`Application specific 
  	message in subfeed`"]
  	sfd2["`Application specific 
  	message in subfeed`"]
  	sfd1 --> sfd2
  end 

  Main --> Meta
  Meta --> SubfeedA
  Meta --> SubfeedB
  Meta --> SubfeedC
  Meta --> SubfeedD
```

Uses for metafeeds

- Storing multiple network identities with a special feed off the user's root metafeed. (contents of metafeed entries can be encrypted)
- Allow for multiple devices to use the same identity - https://github.com/ssbc/fusion-identity-spec
	- Device A `invite`s Device B to identity
	- Device B `consent`s
	- Device A `entrust`s phone with private key
	- Device B posts a `proof-of-key` message
	- If device B lost, `tombstone` the fusion identity message 

## References

- https://ssbc.github.io/scuttlebutt-protocol-guide/