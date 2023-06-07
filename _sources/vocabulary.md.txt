# Vocabulary

## Imports

- `skos:sameAs` - for declaring that a given triplet is equivalent to another.

## Container

- `ordering` - how the children are to be ordered
	- `declaration` - makes numerical references stronger, but less predictable.
	- `alphabetic` - makes numerical references weaker, but more predictable

## Social

- Containers of other accounts
- proxy identites: a given identity can specify a collection of alts that can only be resolved with the correct permission scope - so eg. a public account that is stable can be linked to by an abusive user, but they won't be able to resolve a more private alt.
- Peer Relationship Types
	- Other peers can be given special roles that allow them to operate on behalf of the peer in mutually independent ways:
	- Keybearer - also share a given private key, 
- Visibility
	- A peer can indicate that it is visible to a given scope as defined by a collection of peers and associated rules. 
	- eg. a "close friends" collection could be given the visibility rule to make a peer visible to n-deep friends of friends.
	- A 
