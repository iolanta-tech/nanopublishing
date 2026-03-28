---
"@context":
  - https://json-ld.org/contexts/dollar-convenience.jsonld
  - "@language": en
    wd: https://www.wikidata.org/entity/
    wdt: http://www.wikidata.org/prop/direct/
    compatible-with:
      "@type": "@id"
      "@id": wd:P8956
"@included":
  - $id: wd:Q15528609
    compatible-with:
      - wd:Q188639
      - wd:Q206924
  - $id: wd:Q64538905
    compatible-with: wd:Q188639
  - $id: wd:Q65034999
    compatible-with: wd:Q206924
  - $id: wd:Q216158
    compatible-with: wd:Q206924
  - $id: wd:Q65037415
    compatible-with: wd:Q188639
---

# SSD interface to form factor mapping

This publication records common compatibility facts between SSD form factors and the interfaces they can use.

## Common pairings

| Form factor | Interface | Note |
|-------------|-----------|------|
| **M.2** | **SATA** or **PCIe** | M.2 is a physical form factor and connector family, not a single protocol. |
| **mSATA** | **SATA** | Older mini-card SATA form factor. |
| **U.2** | **PCIe** | Commonly used for NVMe SSDs over PCIe in servers and workstations. |
| **Add-in card (AIC)** | **PCIe** | SSD implemented as a PCIe expansion card. |
| **2.5-inch** | **SATA** | The common consumer SSD pairing. |

## Caveat

These are common compatibility pairings, not an exhaustive compatibility matrix. Connector keying, controller support, and system design still determine what a given device or slot actually supports.
