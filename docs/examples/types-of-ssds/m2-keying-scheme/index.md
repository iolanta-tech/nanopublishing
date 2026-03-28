---
"@context":
  - https://json-ld.org/contexts/dollar-convenience.jsonld
  - "@language": en
    wd: http://www.wikidata.org/entity/
    wdt: http://www.wikidata.org/prop/direct/
    rdfs: http://www.w3.org/2000/01/rdf-schema#
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    owl: http://www.w3.org/2002/07/owl#
    this: http://purl.org/nanopub/temp/np/
    instances:
      "@reverse": rdf:type
      "@type": "@id"
    compatible-with:
      "@type": "@id"
      "@id": wd:P8956

$id: this:M2SSDKey
$type: owl:Class
rdfs:label: M.2 SSD key
rdfs:comment: Keying pattern relevant to solid-state drive modules in the M.2 connector family
compatible-with: wd:Q15528609
instances:
  - $id: this:BKey
    rdfs:label: B key
    rdfs:comment: M.2 SSD keying associated with some SATA designs and some lower-lane PCIe designs
    compatible-with:
      - wd:Q188639
      - wd:Q206924
  - $id: this:MKey
    rdfs:label: M key
    rdfs:comment: M.2 SSD keying commonly used for PCIe x4 and NVMe SSDs
    compatible-with:
      - wd:Q206924
      - wd:Q17157198
  - $id: this:BPlusMKey
    rdfs:label: B+M key
    rdfs:comment: M.2 SSD module keying with both B and M notches for broader mechanical compatibility
    compatible-with: wd:Q188639
---

# M.2 keying scheme for SSDs

M.2 sockets and modules use **keys**: notches and matching socket blocks that constrain what can be inserted and what signals are expected. For SSDs, the practically important keys are **B key**, **M key**, and **B+M key**.

## SSD-relevant M.2 keys

| Keying | Typical SSD use | Common interface notes |
|--------|------------------|------------------------|
| **B key** | Less common for modern NVMe SSDs; seen in some SATA or PCIe x2 designs | Often associated with SATA or with fewer PCIe lanes than M key |
| **M key** | The common keying for NVMe SSDs | Commonly used for PCIe x4 / NVMe SSDs |
| **B+M key** | Module has both notches for broader physical compatibility | Often used by SATA M.2 SSDs, and sometimes by devices that do not use the full lane width of M-key-only NVMe drives |

## Practical interpretation

- **M.2 is not one interface.** It is a physical form factor and connector family.
- **Keying is not the whole story.** A module fitting mechanically does not guarantee protocol support by the host.
- **For SSDs, keying and interface interact.** In practice, readers often want to know whether a given M.2 device is SATA, PCIe/NVMe, or both mechanically possible but host-dependent.

## Scope note

This document is about **M.2 keying as it matters for SSDs**. Other M.2 key types exist for non-SSD devices such as wireless modules, but they are outside the current scope.
