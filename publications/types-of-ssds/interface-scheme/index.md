---
"@context":
  - https://json-ld.org/contexts/dollar-convenience.jsonld
  - "@language": en
    wd: http://www.wikidata.org/entity/
    skos: http://www.w3.org/2004/02/skos/core#
    rdfs: http://www.w3.org/2000/01/rdf-schema#
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    owl: http://www.w3.org/2002/07/owl#
    instances:
      "@reverse": rdf:type
      "@type": "@id"
    "skos:related":
      "@type": "@id"
$type: owl:Class
rdfs:label: SSD host protocol
rdfs:comment: |
  Protocol through which a solid-state drive (SSD) communicates with its host.
  SATA, SAS, and NVMe are instances in this graph; AHCI and PCIe appear only as skos:related.
instances:
  - $id: wd:Q188639
    skos:related: wd:Q379598
    skos:prefLabel: SATA
  - $id: wd:Q1135301
    skos:prefLabel: SAS
  - $id: wd:Q17157198
    skos:related: wd:Q206924
    skos:prefLabel: NVMe
---

# SSD host protocol classification

| Protocol | Typical use | Notes |
|----------|---------------|--------|
| **[SATA](https://en.wikipedia.org/wiki/Serial_ATA)** | Laptops, desktops, older systems | Often with AHCI in consumer stacks; ~600 MB/s ceiling (SATA III). |
| **[NVMe](https://en.wikipedia.org/wiki/NVM_Express)** | Fast internal SSDs | Runs over PCIe; higher bandwidth and lower latency than SATA for many designs. |
| **[SAS](https://en.wikipedia.org/wiki/Serial_Attached_SCSI)** | Servers, enterprise storage | Common in racks; not typical in consumer PCs. |
