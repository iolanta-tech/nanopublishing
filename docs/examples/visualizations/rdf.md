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

  rdfs:label: RDF ontology visualization
  iolanta:visualizes: "rdf:"
---

# RDF ontology visualization

A visualization for the RDF vocabulary that groups its terms into a single
**Properties** group containing `rdf:Property` and `rdf:type`. Iolanta picks
this nanopub up via `iolanta:visualizes rdf:` and renders the grouped terms
when the user navigates to the `rdf:` namespace.
