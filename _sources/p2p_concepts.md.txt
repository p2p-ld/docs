# P2P Concepts

Overview of the various concepts that p2p systems have to handle or address with links to the sections where we address them!

- [Definitions](definitions) - Terms used within the protocol spec
- [Protocol](protocol) - The protocol spec itself, which encompasses the following sections and describes how they relate to one another.
- [Identity](identity) - How each peer in the swarm is identified (or not)
- [Discovery](discovery) - How peers are discovered and connected to in the swarm, or, how an identity is dereferenced into some network entity.
- [Data Structures](data_structures) - What and how data is represented within the protocol
- [Querying](querying) - How data, or pieces of data are requested from hosting peers
- [Evolvability](evolvability) - How the protocol is intended to accommodate changes, plugins, etc.

Additionally, p2p-ld considers these additional properties that are not universal to p2p protocols:

- [Vocabulary](vocabulary) - The linked data vocabulary that is used within the protocol
- [Encryption](encryption) - How individual messages can be encrypted and decrypted by peers
- [Federation](federation) - How peers can form supra-peer clusters for swarm robustness, social organization, and governance
- [Backwards Compatibility](backwards_compatibility) - How the protocol integrates with existing protocols and technologies.
