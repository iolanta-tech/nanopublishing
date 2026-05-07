---
"@context":
  - https://nanopublishing.iolanta.tech/context/v0.yamlld
  - iolanta: https://iolanta.tech/
    vann: http://purl.org/vocab/vann/
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    rdfs: http://www.w3.org/2000/01/rdf-schema#
    iolanta:visualizes:
      "@id": https://iolanta.tech/visualizes
      "@type": "@id"

$nanopublication:
  $assertion:
    $id: "rdf:"
    vann:termGroup:
      - rdfs:label: Properties
        $reverse:
          rdf:type:
            - $id: rdf:Property
            - $id: rdf:type
      - rdfs:label: Triples
        $reverse:
          rdf:type:
            - $id: rdf:subject
            - $id: rdf:predicate
            - $id: rdf:object
            - $id: rdf:Statement
      - rdfs:label: Containers
        $reverse:
          rdf:type:
            - $id: rdf:first
            - $id: rdf:rest
            - $id: rdf:List
            - $id: rdf:nil
            - $id: rdf:Bag
            - $id: rdf:Seq
            - $id: rdf:Alt
      - rdfs:label: Language
        $reverse:
          rdf:type:
            - $id: rdf:langString
            - $id: rdf:language
      - $id: rdfs:Datatype
      - rdfs:label: Compound Literal
        $reverse:
          rdf:type:
            - $id: rdf:CompoundLiteral
            - $id: rdf:direction
      - rdfs:label: Value
        $reverse:
          rdf:type:
            - $id: rdf:value

  rdfs:label: RDF ontology visualization
  iolanta:visualizes: "rdf:"
---

# RDF ontology visualization

A visualization for the RDF vocabulary that groups terms for properties,
triples, containers, language values, compound literals, and values. Iolanta
picks this nanopub up via `iolanta:visualizes rdf:` and renders the grouped
terms when the user navigates to the `rdf:` namespace.
