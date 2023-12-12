# p2p-ld

All of this is very work in progress :) plz do not rely on any of the descriptions or statements here, as they are all effectively provisional.

This site describes the implementation of the p2p linked data protocol in {cite}`saundersDecentralizedInfrastructureNeuro2022`
 
## Document Status

**23-11-27** - Back at it again after some digressions into [chatbridge](https://git.jon-e.net/jonny/chatbridge) and [nwb-linkml](https://github.com/p2p-ld/nwb-linkml/) - gathering more information on storage and interchange formats for databases and triple stores before trying to prop up the first peers sharing graphs of NWB data. Still mostly populating the [Comparison](comparison) section as I take notes and before I restructure these docs.

**23-06-08** - Populating the [Comparison](comparison) section first to refresh myself on other projects, and starting to sketch diagrammatically in [Sketchpad](sketchpad). The rest of the pages are just stubs to keep track of ideas before fleshing them out. 

```{toctree}
:caption: Introduction
:hidden:

overview
roadmap
comparison/index
p2p_concepts
out_of_scope
```  

```{toctree}
:caption: Protocol
:numbered:
:hidden:

definitions
protocol
identity
discovery
data_structures
vocabulary
querying
encryption
federation
backwards_compatibility
evolvability
```

```{toctree}
:caption: Ecosystem
:hidden:

triplets
codecs/index
translation/index
```  

```{toctree}
:caption: Drafting
:hidden:

design
sketchpad
```

```{toctree}
:caption: Meta
:hidden:

genindex
references
todo
``` 
