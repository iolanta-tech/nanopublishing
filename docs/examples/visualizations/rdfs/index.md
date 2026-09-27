---
hide: [toc]

"@context":
  - https://nanopublishing.iolanta.tech/context/v0.yamlld
  - iolanta: https://iolanta.tech/
    vann: http://purl.org/vocab/vann/
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    rdfs: http://www.w3.org/2000/01/rdf-schema#
    iolanta:visualizes:
      "@type": "@id"
    terms:
      "@reverse": rdf:type
      "@type": "@id"

$nanopublication:
  $assertion:
    $id: "rdfs:"
    vann:termGroup:
      - rdfs:label: Classes
        terms:
          - $id: rdfs:Resource
            iolanta:icon: ⊤
          - $id: rdfs:Class
          - $id: rdfs:Literal
          - $id: rdfs:Datatype
      - rdfs:label: Semantic properties
        terms:
          - $id: rdfs:domain
            iolanta:icon: ⤚
          - $id: rdfs:range
            iolanta:icon: ⤙
          - $id: rdfs:subClassOf
            iolanta:icon: ⊆
          - $id: rdfs:subPropertyOf
            iolanta:icon: ⥹
      - rdfs:label: Documentation
        terms:
          - $id: rdfs:label
            iolanta:icon: 🏷
          - $id: rdfs:comment
            iolanta:icon: 📃
          - $id: rdfs:seeAlso
            iolanta:icon: ⧉
          - $id: rdfs:isDefinedBy
      - rdfs:label: Containers
        terms:
          - $id: rdfs:Container
          - $id: rdfs:ContainerMembershipProperty
          - $id: rdfs:member
            iolanta:icon: ∋

  rdfs:label: RDFS terms by type
  iolanta:visualizes: "rdfs:"

npx:supersedes: https://w3id.org/np/RAoY6OgaWnz2XrcN65I1-ehZvRnzEowK0S7OXJddTiquI
---

# RDFS ontology visualization

{{ URIRef("http://www.w3.org/2000/01/rdf-schema#") | as('mkdocs-material') }}
