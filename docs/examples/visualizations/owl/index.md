---
hide: [toc]

"@context":
  - https://nanopublishing.iolanta.tech/context/v0.yamlld
  - iolanta: https://iolanta.tech/
    vann: http://purl.org/vocab/vann/
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    rdfs: http://www.w3.org/2000/01/rdf-schema#
    owl: http://www.w3.org/2002/07/owl#
    iolanta:visualizes:
      "@type": "@id"
    terms:
      "@reverse": rdf:type
      "@type": "@id"

$nanopublication:
  $assertion:
    $id: "owl:"
    "@type": owl:Ontology
    vann:termGroup:
      - rdfs:label: Classes
        terms:
          - $id: owl:Thing
            iolanta:icon: ⊤
          - $id: owl:Nothing
            iolanta:icon: ⊥
          - $id: owl:Class
      - rdfs:label: Property classes
        terms:
          - $id: owl:ObjectProperty
          - $id: owl:DatatypeProperty
          - $id: owl:topObjectProperty
            iolanta:icon: ↧
          - $id: owl:bottomObjectProperty
            iolanta:icon: ↥
          - $id: owl:topDataProperty
            iolanta:icon: ↧
          - $id: owl:bottomDataProperty
            iolanta:icon: ↥
      - rdfs:label: Property characteristics
        terms:
          - $id: owl:FunctionalProperty
            iolanta:icon: ⇸
          - $id: owl:InverseFunctionalProperty
            iolanta:icon: ↣
          - $id: owl:ReflexiveProperty
          - $id: owl:IrreflexiveProperty
          - $id: owl:SymmetricProperty
          - $id: owl:AsymmetricProperty
          - $id: owl:TransitiveProperty
      - rdfs:label: Class expressions
        terms:
          - $id: owl:intersectionOf
            iolanta:icon: ⊓
          - $id: owl:unionOf
            iolanta:icon: ⊔
          - $id: owl:complementOf
            iolanta:icon: ¬
          - $id: owl:oneOf
          - $id: owl:disjointUnionOf
          - $id: owl:equivalentClass
            iolanta:icon: ≡
          - $id: owl:disjointWith
          - $id: owl:hasKey
      - rdfs:label: Property relations
        terms:
          - $id: owl:inverseOf
          - $id: owl:equivalentProperty
            iolanta:icon: ⇶
          - $id: owl:propertyDisjointWith
          - $id: owl:propertyChainAxiom
            iolanta:icon: ∘
      - rdfs:label: Restrictions
        terms:
          - $id: owl:Restriction
          - $id: owl:onProperty
          - $id: owl:onProperties
          - $id: owl:onClass
          - $id: owl:onDataRange
          - $id: owl:onDatatype
          - $id: owl:someValuesFrom
            iolanta:icon: ∃
          - $id: owl:allValuesFrom
            iolanta:icon: ∀
          - $id: owl:hasValue
          - $id: owl:hasSelf
      - rdfs:label: Cardinality
        terms:
          - $id: owl:cardinality
          - $id: owl:minCardinality
            iolanta:icon: ⩾
          - $id: owl:maxCardinality
            iolanta:icon: ⩽
          - $id: owl:qualifiedCardinality
          - $id: owl:minQualifiedCardinality
          - $id: owl:maxQualifiedCardinality
      - rdfs:label: Data ranges
        terms:
          - $id: owl:DataRange
          - $id: owl:datatypeComplementOf
            iolanta:icon: ¬
          - $id: owl:withRestrictions
      - rdfs:label: Individuals
        terms:
          - $id: owl:NamedIndividual
          - $id: owl:sameAs
          - $id: owl:differentFrom
            iolanta:icon: ≠
          - $id: owl:AllDifferent
          - $id: owl:distinctMembers
          - $id: owl:AllDisjointClasses
          - $id: owl:AllDisjointProperties
          - $id: owl:members
      - rdfs:label: Assertions
        terms:
          - $id: owl:NegativePropertyAssertion
          - $id: owl:sourceIndividual
          - $id: owl:assertionProperty
          - $id: owl:targetIndividual
          - $id: owl:targetValue
      - rdfs:label: Annotations
        terms:
          - $id: owl:Annotation
          - $id: owl:AnnotationProperty
          - $id: owl:annotatedSource
          - $id: owl:annotatedProperty
          - $id: owl:annotatedTarget
      - rdfs:label: Deprecated
        terms:
          - $id: owl:deprecated
            iolanta:icon: 🗑
          - $id: owl:DeprecatedClass
            iolanta:icon: 🗑
          - $id: owl:DeprecatedProperty
            iolanta:icon: 🗑
      - rdfs:label: Ontologies
        terms:
          - $id: owl:Ontology
          - $id: owl:OntologyProperty
          - $id: owl:imports
          - $id: owl:Axiom
      - rdfs:label: Versions
        terms:
          - $id: owl:versionIRI
          - $id: owl:versionInfo
          - $id: owl:priorVersion
            iolanta:icon: ⎗
          - $id: owl:backwardCompatibleWith
            iolanta:icon: ✓
          - $id: owl:incompatibleWith
            iolanta:icon: ✗

  rdfs:label: OWL terms by type
  iolanta:visualizes: "owl:"

npx:supersedes: https://w3id.org/np/RAZWVzk0nYHkkBr6ql7crPHdXbFxM4sN3UGtQA1IpMR-8
---

# OWL ontology visualization

{{ URIRef("http://www.w3.org/2002/07/owl#") | as('mkdocs-material') }}
