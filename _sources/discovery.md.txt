# Discovery

How do we find people and know how to connect to them?

- Bootstrapping initial connections
- Gossiping

```{index} Hole Punching
```
## Hole Punching

- https://tailscale.com/blog/how-nat-traversal-works/
- {index}`Hypercore`
	- See: https://docs.holepunch.to/apps/keet.io
	- https://github.com/mafintosh/dht-rpc
	- https://docs.holepunch.to/building-blocks/hyperdht
- Socket Supply Co


## Scraps

https://xmpp.org/extensions/xep-0030.html

> There are three kinds of information that need to be discovered about an entity:
>
> - its basic identity (type and/or category)
> - the features it offers and protocols it supports
> - any additional items associated with the entity, whether or not they are addressable as JIDs
>
> All three MUST be supported, but the first two kinds of information relate to the entity itself whereas the third kind of information relates to items associated with the entity itself; therefore two different query types are needed.

- subscription to particular data types or query patterns - each peer keeps a list of things that we should tell it about when we make a new graph. So I might want to always see new posts and pre-emptively index those but I don't care about your datasets. This should probably exist at the level of a peer relationship rather than a peer outbox-like thing
