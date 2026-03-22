---
"@context":
  "@language": "en"
  wd: "https://www.wikidata.org/entity/"
  schema: "https://schema.org/"
  skos: "http://www.w3.org/2004/02/skos/core#"
  rdfs: "http://www.w3.org/2000/01/rdf-schema#"
  rdf: "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  dct: "http://purl.org/dc/terms/"
"@included":
  - "@id": "index.md"
    "@type": "schema:TechArticle"
    "schema:name": "Types of SSDs"
    "schema:about":
      "@id": "wd:Q487343"
    "schema:mentions":
      - "@id": "wd:Q188639"
      - "@id": "wd:Q17157198"
      - "@id": "wd:Q206924"
      - "@id": "wd:Q1135301"
      - "@id": "wd:Q379598"
      - "@id": "wd:Q15528609"
      - "@id": "wd:Q64538905"
      - "@id": "wd:Q65034999"
      - "@id": "wd:Q216158"
      - "@id": "wd:Q65037415"
    "dct:references":
      - "@id": "interface-scheme/index.md"
      - "@id": "form-factor-scheme/index.md"
  - "@id": "interface-scheme/index.md"
    "schema:name": "SSD host interface classification"
  - "@id": "form-factor-scheme/index.md"
    "schema:name": "SSD form factor scheme"
---

# Types of SSDs

[Solid-state drives](https://en.wikipedia.org/wiki/Solid-state_drive) (SSDs) are usually classified along **two independent dimensions**: the **data interface / protocol** (how bits move) and the **form factor** (shape and connector). The same protocol can appear in several form factors, and one physical shape—especially [M.2](https://en.wikipedia.org/wiki/M.2)—can carry more than one protocol.

Detailed **RDF assertion graphs** for each classification scheme live in companion publications:

- **[SSD host interface classification](interface-scheme/index.md)** — Anonymous OWL class (blank node) with SATA, SAS, and NVMe as instances; related facts (AHCI, PCIe).
- **[Form factor scheme](form-factor-scheme/index.md)** — 2.5″, M.2, mSATA, U.2, add-in cards; how M.2 relates to SATA and NVMe.

## Short mental model

1. **Protocol**: SATA vs NVMe (PCIe) vs SAS — this is the main performance and software stack split for most readers.  
2. **Package**: 2.5", M.2, U.2, etc. — where the electronics live and how they plug in.  

**SATA** and **PCIe** name **buses**: consumer SSDs today are either SATA SSDs or **NVMe over PCIe** SSDs; “PCIe SSD” in marketing almost always means NVMe unless the context is legacy gear.
