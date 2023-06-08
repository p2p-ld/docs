# AT Protocol/Bluesky

```{index} Identity
```
```{index} Bluesky
```
```{index} Identity; DID
```

We aren't too concerned with billionaires cosplaying as altruists and the technologies they produce, but the AT Protocol has a few ideas, particularly related to [identity](https://atproto.com/guides/identity), that are interesting.

Specifically, AT protocol differentiates between *handles* and *identities*, where DNS entries are used as short handles that resolve to a [DID](https://www.w3.org/TR/did-core/).

That's about it, the rest of the handling of DID's is extremely centralized (see [did:plc](https://atproto.com/specs/did-plc) which requires resolution against a single domain), and the requirement of all posts to be funneled through [Big Graph Services](https://blueskyweb.xyz/blog/5-5-2023-federation-architecture) rather than directly peer to peer is transparently designed to ensure a marketing and advertising layer in between actors in the network.

