---
hide: [toc]

"@context":
  - https://nanopublishing.iolanta.tech/context/v0.yamlld
  - iolanta: https://iolanta.tech/
    vann: http://purl.org/vocab/vann/
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    iolanta:visualizes:
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
          - $id: rdf:Property
            iolanta:icon: →
          - $id: rdf:type
            iolanta:icon: ∈
      - rdfs:label: Triples
        terms:
          - $id: rdf:subject
            iolanta:icon: ○
          - $id: rdf:predicate
            iolanta:icon: →
          - $id: rdf:object
            iolanta:icon: ◉
          - $id: rdf:Statement
            iolanta:icon: ⦀
      - rdfs:label: Containers
        terms:
          - rdf:first
          - rdf:rest
          - $id: rdf:List
            iolanta:icon: ⋮
          - $id: rdf:nil
            iolanta:icon: ∅
          - $id: rdf:Bag
            iolanta:icon: ⊎
          - $id: rdf:Seq
            iolanta:icon: ⋯
          - $id: rdf:Alt
            iolanta:icon: ⊕
      - rdfs:label: Language
        terms:
          - $id: rdf:langString
            iolanta:icon: 🌐
          - $id: rdf:language
            iolanta:icon: 🌐
      - $id: rdfs:Datatype
        iolanta:icon: ⊤
      - rdfs:label: Compound Literal
        terms:
          - $id: rdf:CompoundLiteral
            iolanta:icon: ⊞
          - $id: rdf:direction
            iolanta:icon: ⇄
      - rdfs:label: Value
        terms:
          - rdf:value

  rdfs:label: RDF terms by type
  iolanta:visualizes: "rdf:"

npx:supersedes: https://w3id.org/np/RASsLPDBpyeofCHRTdy2NYLtU-mep--kB7eRzIHFPkawo
---

# RDF ontology visualization

A visualization for the RDF vocabulary that groups terms for properties,
triples, containers, language values, compound literals, and values. Iolanta
picks this nanopub up via `iolanta:visualizes rdf:` and renders the grouped
terms when the user navigates to the `rdf:` namespace.

{{ URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#") | as('mkdocs-material') }}
