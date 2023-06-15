```{index} Linked Data; Platform
```
# Linked Data Platform

```{index} Containers
```
## Containers

https://www.w3.org/TR/ldp/#ldpc

We extend the notion of LDP containers! 

Terms:
- Containment Triples
- Membership Triples

Types:
- Direct Containers

```turtle
@prefix dcterms: <http://purl.org/dc/terms/>.
@prefix ldp: <http://www.w3.org/ns/ldp#>.

<http://example.org/c1/>
   a ldp:BasicContainer;
   dcterms:title "A very simple container";
   ldp:contains <r1>, <r2>, <r3>.
```

- Indirect Containers - a way of interacting with existing data

Given: 

```turtle
@prefix ldp: <http://www.w3.org/ns/ldp#>.
@prefix o: <http://example.org/ontology#>.

<http://example.org/netWorth/nw1/>
   a o:NetWorth;
   o:netWorthOf <http://example.org/users/JohnZSmith>;
   o:asset 
      <assets/a1>,
      <assets/a2>;
   o:liability 
      <liabilities/l1>,
      <liabilities/l2>,
      <liabilities/l3>.
```

we can make direct containers that describe the assets and liabilities as containers without modifying the original data

```turtle
@prefix ldp: <http://www.w3.org/ns/ldp#>.
@prefix dcterms: <http://purl.org/dc/terms/>.
@prefix o: <http://example.org/ontology#>.

<http://example.org/netWorth/nw1/assets/>
   a ldp:DirectContainer;
   dcterms:title "The assets of JohnZSmith";
   ldp:membershipResource <http://example.org/netWorth/nw1/>;
   ldp:hasMemberRelation o:asset;
   ldp:contains <a1>, <a2>.
```

Additionally, if one were to add a new set of "advisors," we would make an indirect container that tells us we need an additional triple when creating new members of the container (`foaf:primaryTopic`):

```turtle
<advisors/>
   a ldp:IndirectContainer;
   dcterms:title "The asset advisors of JohnZSmith";
   ldp:membershipResource <>;
   ldp:hasMemberRelation o:advisor;
   ldp:insertedContentRelation foaf:primaryTopic;
   ldp:contains
   	 <advisors/bob>,     # URI of a document a.k.a. an information resource
   	 <advisors/marsha>.  # describing a person
```

(still unclear to me what is different about that, still reading.)

| Completed Request |	Membership Effect | Containment Effect |
| ----------------- | ------------------- | ------------------ |
| Create in Basic Container | New triple: (LDPC, ldp:contains, LDPR) | Same
| Create in Direct Container |	New triple links LDP-RS to created LDPR. LDP-RS URI may be same as LDP-DC | New triple: (LDPC, ldp:contains, LDPR) |
| Create in Indirect Container | New triple links LDP-RS to content indicated URI | New triple: (LDPC, ldp:contains, LDPR) |
| Resource deleted | Membership triple may be removed | (LDPC, ldp:contains, LDPR) triple is removed |
| Container deleted | Triples and member resources may be removed | Triples of form (LDPC, ldp:contains, LDPR) and contained LDPRs may be removed |

## Similarities

- Separation between container data and metadata - "minimal-container triples," what remains in the container when the container has zero members and zero contained resources


## Differences

- Containers are not recursive??or at least that is suggested by the 'net worth' example that explains why we can't just turn the original subject into a container: "can't mix assets and liabilities" and i am like why not make one container for the person and then subcontainers for each of the types?


## References

- Spec: https://www.w3.org/TR/ldp/
- Use cases and requirements: https://www.w3.org/TR/ldp-ucr/
- eg. using virtuoso. https://github.com/vemonet/virtuoso-ldp