# Design Decisions

A scratchpad for keeping track of the specific choices that we are making so that we know they are choices lol.

## Cultivate Abundance

Much of the focus and energy in p2p and decentralized systems has been vaccuumed up by cryptocurrency and other blockchain scams. These technologies intrinsically generate artificial scarcity rather than the abundance of p2p systems like bittorrent. Much of the thinking in these systems is oriented around self-sovereignty, but p2p-ld is intended to cultivate mutualism and the radical mutual responsibility to each other that any truly autonomous social system outside of libertarian fantasies requires. We don't design the *system* to be maximally efficient and make *system-level* guarantees about reliability or persistence, but design systems for people to organize these things among themselves, voluntarily. We are *not* interested in making a self-sustaining system that is "out there" and needs to be maintained by some blockchain economy. We are interested in making tools *for us* to make our own digital life online

## Permanence is Impossible

{attribution="Octavia Butler, Parable of the Sower"}
> Every one knows that change is inevitable. From the second law of thermodynamics to Darwinian evolution, from Buddhism's insistence that nothing is permanent and all suffering results from our delusions of permanence to the third chapter of Ecclesiastes ("To everything there is a season"), change is part of life, of existence, of the common wisdom. But I don't believe we're dealing with all that that means. We haven't even begun to deal with it.

There is no such thing as a [Cool URI that doesn't change](https://www.w3.org/Provider/Style/URI), and there is no such thing as a persistent identifier that lasts forever {cite}`kunzePersistenceStatementsDescribing2017`. All things change. Change can be because of practical reasons like running out of funding and shutting down the server, cultural reasons like shifting meanings of words, or larger shifts that render the entire domain that a thing is fixed in irrelevant. No matter how many layers of abstraction and redirection we want to create, there is no system that will for all time be able to unambiguously identify something on the web or elsewhere. 

The appearance of persistence is a *social* phenomenon rather than a *technological* one. `Archive.org` continues to exist because many people actively keep it existing, not because of the architecture of their archive. Designing for permanence makes systems *fragile.* Instead we should design for *adapting* to change. Adapting to change is also a social phenomenon - I might misplace things, change how they are named, and tell you that the same URL means something different, or the same page goes by a different URL now. A newspaper might go out of business and its website might go offline, but someone might save a PDF of the original page and rehost it on their personal website. The tools we need look more like systems for renaming, declaring equivalence, translation, change, than they do an unalterable, permanent append-only blockchain thing.

## Ambiguity is Natural

The [original vision](https://www.w3.org/DesignIssues/LinkedData.html) for Linked Data on the web imagined every concept having a single unique URI, but unambiguous identifiers are fictional for the same reason that unambiguous concepts are fictional. Information is contextual. The same set of words has a different meaning in a different context. Multiple sets of words can have the same meaning. 

Names and locations are *linguistic* not *mathematical.* Rather than trying to design ambiguity out of the system so that web crawlers can deterministically generate algorithmic restaurant reservations, we should design systems that explicitly incorporate context to reference and use.

## Autonomy *and* Convenience Can Coexist

We should neither sacrifice control of the internet to platform giants nor should we insist that self-hosting is the only alternative. If the alternative to using Google Docs or Slack requires me to be a professional sysadmin, or even to keep a raspberry pi plugged in and online at all times, it isn't an alternative for 95% of people.

It should be possible to share resources such that relatively few people need to maintain persistent network infrastructure, and it should be possible to accomodate their leaving at any time. It should also be very difficult for one or a few actors to make a large number of other peers on the network dependent on them, claiming de-facto control over an ostensibly decentralized system (lookin at you mastodon.social).

## Lack of Agency is a tighter bottleneck than Performance

(rather than optimizing for performance of massive queries over huge datasets, we optimize for the ability for individual people to organize the resources that would be relevant to them. The thing that is limiting our ability to make sense of data in neuroscience, for example, is not that our servers aren't fast enough, but the barriers to making well-structured data are too high, as is the expertise to conduct large scale queries. Even then, our ability to *understand* and *make sense of* the information is even less constrained by performance, and more by the absence of infrastructure to link and communicate heterogeneous things. We focus on small-scale computing not only for ethical reasons, but also practical ones.)