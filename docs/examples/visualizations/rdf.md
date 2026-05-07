---
"@context":
  - https://nanopublishing.iolanta.tech/context/v0.yamlld
  - iolanta: https://iolanta.tech/
    vann: http://purl.org/vocab/vann/
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    iolanta:visualizes:
      "@id": https://iolanta.tech/visualizes
      "@type": "@id"
    terms:
      "@reverse": rdf:type
      "@type": "@id"

$nanopublication:
  $assertion:
    $id: "rdf:"
    vann:termGroup:
      - rdfs:label: Properties
        terms:
          - rdf:Property
          - rdf:type
      - rdfs:label: Triples
        terms:
          - rdf:subject
          - rdf:predicate
          - rdf:object
          - rdf:Statement
      - rdfs:label: Containers
        terms:
          - rdf:first
          - rdf:rest
          - rdf:List
          - rdf:nil
          - rdf:Bag
          - rdf:Seq
          - rdf:Alt
      - rdfs:label: Language
        terms:
          - rdf:langString
          - rdf:language
      - $id: rdfs:Datatype
      - rdfs:label: Compound Literal
        terms:
          - rdf:CompoundLiteral
          - rdf:direction
      - rdfs:label: Value
        terms:
          - rdf:value

  rdfs:label: RDF terms by type
  iolanta:visualizes: "rdf:"

npx:supersedes: https://w3id.org/np/RAXhiZMoa3JldEhxcgVyp8UIJL_N0PhEJpCTRXdKl7H_Q
---

# RDF ontology visualization

A visualization for the RDF vocabulary that groups terms for properties,
triples, containers, language values, compound literals, and values. Iolanta
picks this nanopub up via `iolanta:visualizes rdf:` and renders the grouped
terms when the user navigates to the `rdf:` namespace.
