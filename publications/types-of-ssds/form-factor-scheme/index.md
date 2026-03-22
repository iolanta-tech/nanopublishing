---
"@context":
  wd: "https://www.wikidata.org/entity/"
  schema: "https://schema.org/"
  skos: "http://www.w3.org/2004/02/skos/core#"
  rdfs: "http://www.w3.org/2000/01/rdf-schema#"
  rdf: "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
"@included":
  - "@id": "#formFactorScheme"
    "@type": "schema:CreativeWork"
    "schema:name":
      "@value": "SSD form factor classification"
      "@language": "en"
    "schema:about":
      - "@id": "wd:Q65037415"
      - "@id": "wd:Q15528609"
      - "@id": "wd:Q64538905"
      - "@id": "wd:Q65034999"
      - "@id": "wd:Q216158"
  - "@id": "wd:Q15528609"
    "skos:related":
      - "@id": "wd:Q188639"
      - "@id": "wd:Q17157198"
---

# SSD form factor scheme

This publication asserts a **classification scheme** over **physical form factors** and connectors for SSDs (2.5″, M.2, mSATA, U.2, add-in cards). It also relates [M.2](https://en.wikipedia.org/wiki/M.2) to the SATA and NVMe stacks it can host.

## By form factor (physical package)

These describe **size and connector**, not speed by themselves:

| Form factor | Wikipedia | Comment |
|-------------|-----------|---------|
| **2.5-inch** (often SATA) | [Form factors (SSD)](https://en.wikipedia.org/wiki/Solid-state_drive#Form_factors) | Classic laptop / bay size; most SATA SSDs; same mechanical size as [2.5″ HDDs](https://en.wikipedia.org/wiki/2.5-inch_hard_disk_drive). |
| **M.2** | [M.2](https://en.wikipedia.org/wiki/M.2) | Gumstick module; may be **SATA** or **NVMe (PCIe)** depending on keying and controller—not all M.2 slots support both. |
| **mSATA** | [mSATA](https://en.wikipedia.org/wiki/Mini-SATA) | Older mini module; largely superseded by M.2. |
| **U.2** (SFF-8639) | [U.2](https://en.wikipedia.org/wiki/U.2) | Cable / backplane connector common in servers and some workstations; often NVMe. |
| **Add-in card (AIC)** | [Expansion card](https://en.wikipedia.org/wiki/Expansion_card) | Full-height or half-height PCIe slot cards; NVMe SSDs as a PCIe card. |

## How M.2 fits in

**M.2 is not a single “type” of SSD in the protocol sense.** It is a **module and connector standard**. An M.2 SSD might be:

- **SATA** (same logical interface as a 2.5" SATA drive, different physical shape), or  
- **NVMe** (PCIe), which is what people usually mean by a “fast” M.2 SSD.

Motherboard slots are keyed ([B key, M key, B+M](https://en.wikipedia.org/wiki/M.2#Form_factors_and_keying)) and may support only SATA, only NVMe, or both—check the board manual.

[← Types of SSDs (hub)](../index.md)
