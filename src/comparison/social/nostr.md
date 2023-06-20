(Nostr)=
# Nostr

Again, though we have a general distrust of the anarcho-capitalists, it's worth a comparison.

Nostr is an extremely minimal protocol: https://nostr.com/the-protocol . There just isn't a lot there worth speaking of.

## DNS identity

Like [AT Protocol](at_protocol), there is a NIP (noster implementation possibility) for using {index}`DNS` to map keys: https://github.com/nostr-protocol/nips/blob/master/05.md 

It seems to be Webfinger-like, using a .json file under a `.well-known` path on a domain. An identity issues an event indicating a `nip05` type:

```json
{
  "pubkey": "b0635d6a9851d3aed0cd6c495b282167acf761729078d975fc341b22650b07b9",
  "kind": 0,
  "content": "{\"name\": \"bob\", \"nip05\": \"bob@example.com\"}"
}
```

and then does a GET to `https://example.com/.well-known/nostr.json?name=bob`. If the response looks like this:

```json
{
  "names": {
    "bob": "b0635d6a9851d3aed0cd6c495b282167acf761729078d975fc341b22650b07b9"
  }
}
```

then the identity is considered verified.

## Petnames

And a notion of {index}`Petnames`: https://github.com/nostr-protocol/nips/blob/master/02.md

## Not so good

- Just a client-server architecture: clients must talk to relays, relays do not talk to one another.
- Very very little in the way of a formalized spec for relays
- Made by a bunch of bitcoin guys