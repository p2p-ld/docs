# Spritely/Goblin

The Spritely Institute is likely the closest in spirit and design to what we are considering with p2p-ld, and have significant experience having previously worked on [ActivityPub](activitypub). The primary point of departure is their focus on building applications and running code, rather than structuring and sharing data --- so their work is largely complementary.

Overlapping design choices include
- Emphasis on making a social, rather than a technological system! 
- Capability security vs ACLs - Containers of other identities might be a useful way of coordinating who gets capabilities, but implementing them as capabilities rather than access checks makes for a much richer space of interaction and mutation.
- `Goblins` as "addressable entities with encapsulated behavior" are similar to {index}`Container`s
- Distributed objects: we imagine containers as being instantiated in multiple places at once and being acted on by multiple actors. Spritely's use of the "Unum Pattern" focused on distributed behavior rather than distributed data is something we plan on following up on and re-evaluating some of our designs. One place we may diverge is in our emphasis of 'forking' and activity that doesn't need to be explicitly approved: actors need not necessarily operate on the same shared object, but might make their own assertions, links, and so forth that don't directly change the object as owned by the original actor.

Stuff we can learn from
- A lot
- Promise Pipelining to reduce roundtrips
- Implementation of protocol agnosticisim in OCapN
- Discussion of safety of computing base and evaluation environment

Their description of *portable encrypted storage* ({index}`Storage; Portability`) is also extremely useful:

> 1. Documents must be **{index}`Content Addressed <Content Addressing>`** and **location agnostic.** In other words, the name of the particular resource is based on information stemming from the content itself rather than a particular network location. Generally this name is the hash of the corresponding document in the case of immutable documents and a public key (or hash thereof) in the case of mutable documents. 
> 2. Both **{index}`immutable and mutable documents <Mutability>`** must be supported, with the latter generally being built upon the former. 
> 3. Documents must be **{index}`encrypted <Encryption>`** such that the documents can be stored in locations that are oblivious to their actual contents. Only those possessing read capabilities should be able to access the documents' contents. 
> 4. Documents should be **chunked** so that they are not vulnerable to sizeof-file attacks. 
> 5. Reading (and, in the case of mutable documents, writing) documents must be accessed through abstract **capabilities.** 
> 6. Files must be network agnostic, meaning that they are not only location agnostic but agnostic even to a specific network structure. peer-to-peer, client-to-server, and sneakernet networks all should be supported with the same object URIs between them.

## References

- {cite}`lemmer-webberHeartSpritelyDistributed`
- OCapN - https://github.com/ocapn/ocapn
- Golem - https://gitlab.com/spritely/golem/blob/master/README.org