# Identity

How is an individual peer identified?

- Cryptographic identity
- Web of trust/shared identity
- External verification/discovery via DNS and other out of band means.

## {index}`Instances`

A given identity can have 0 or many instances - a manifestation of the peer within a particular server and runtime. 

Each instance indicates a collection of peers 

When connecting to a peer, the peer MUST tell the connecting peer of the instances that are within its permission scope.

## Aliases

A given identity can have 0 or many bidirectional links indicating that the identity is `sameAs` another
- eg. a fediverse account can indicate a cryptographic identity and then be used equivalently.
- Verification aliases MUST have a backlink from the original identity
- Subscribers to a given identity MUST store and represent the known aliases and treat them as equivalent
- Other accounts can give an alias to an identity that MAY be accepted (by issuing a backlink) or denied (by ignoring it).

### Succession

An identity has a specific field indicating whether it is "active" or "retired," and can issue a special top-level link with given permission scope indicating the identity that succeeds it.
	- eg in the case of harrassment, one can hop identities and only tell close friends.

## Beacons

Any peer can operate as a "Pub" (in the parlance of SSB) or a bootstrapping node, where a dereferenceable network location (eg. DNS) can be resolved to a

A given identity can have 0 or many static inbound references that can resolve a network

