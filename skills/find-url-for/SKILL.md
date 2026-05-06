---
name: find-url-for
description: Finds a semantic web / linked data URL for a notion the user asks about (person, place, work, concept). Use when the user wants a canonical URI for an entity in RDF/Turtle, when creating knowledge graphs and needing to link to external data instead of defining local individuals, or when they ask for a Wikidata/DBpedia/VIAF/nanopub URI for someone or something.
---

# Find URL For

## Argument

The **notion** to resolve: person, place, work, organization, or concept. Determine from the user message (e.g. "Isaac Asimov", "Foundation series", "Paris"). If unclear, ask.

## Workflow

1. **Search** — Call dedicated linked-data search APIs in parallel. Don't paraphrase web-search snippets when an API exists.
   - **Always run together:**
     - **Nanopublications registry** (Lucene full-text query) — *the primary source for this project*. Nanopubs can introduce terms about anything — people, places, ordinary concepts, not just FAIR/biomedical/scholarly vocabulary — so don't gate this step on subject matter.
     - **Wikidata Reconciliation API** (OpenRefine protocol) — returns scored candidates with full type chains. Much better disambiguation than `wbsearchentities`: for "Proxima Centauri" it surfaces the star, an album, a short story, a French mayor, a Bordeaux music ensemble, a Polish rock, and a Star Trek depiction in one call.
     - **DBpedia Lookup** — adds refCount, types, redirect labels, multilingual variants.
   - **If the notion is a class or property** (e.g. "Person", "author of", "is part of"): also call **LOV term search**.
   - **Optional fallback** when the label is ambiguous and the user provided a sentence: call **Falcon 2.0** over the sentence — but filter its output to the actual notion the user asked about, since Falcon emits spurious entities for grammatical filler ("A W3C", "data serialization format").
2. **Pick** — Prefer a nanopub-introduced term URI when one fits the notion (signed, content-immutable, citable). Otherwise choose from the Reconciliation API's scored list using the type chains. If you can't be sure, surface the top 2–3 candidates to the user.
3. **Enrich** — Once you have a Wikidata Q-ID, call `wbgetentities` with `props=claims|sitelinks/urls`. This returns ~25 external authority IDs already stored on the entity (SIMBAD, Britannica, Freebase MID, JSTOR, WordNet, Store norske leksikon, …) plus 50+ Wikipedia sitelinks — Wikidata is itself a meta-search if you walk its external-ID properties. Optionally call **LODsyndesis `/objectCoreference`** with the Wikidata or DBpedia URI to fetch additional `owl:sameAs` links across YAGO, Freebase, regional DBpedias, etc. that Wikidata may not store.
4. **Verify** — Confirm the chosen URI matches the intended entity (fetch the page/RDF and check the label/description).
5. **Return** — Give the user the canonical URI, the Turtle prefix, an example triple, and — when multiple candidates exist — a short comparison.

## Sources

This project's primary source is the **Nanopublications registry**. Always check it first; only fall through to general-purpose linked-data sources when no signed nanopub term fits.

- **Nanopublications** — terms defined in signed nanopublications. Anyone can publish a nanopub introducing a term for any notion, so the registry covers far more than FAIR/biomedical/scholarly vocabulary — always check it. URIs commonly live under `http://purl.org/np/<TrustyHash>#<localname>` (Trusty-hashed nanopub) or `https://w3id.org/<namespace>/terms/<Name>` (e.g. FIP and other curated vocabularies). See "Searching the Nanopublications registry" below.
- **Wikidata** — `https://www.wikidata.org/entity/Q<id>`. People, places, works, concepts. Many languages, dense cross-links. Prefix: `wd: <https://www.wikidata.org/entity/>`.
  - **Primary search:** the **Reconciliation API** at `https://wikidata-reconciliation.wmcloud.org/en/api` (OpenRefine protocol). Returns scored candidates with full type chains — the right tool for disambiguating "Mercury" → planet vs. element vs. car.
  - **Enrichment:** `wbgetentities` with `props=claims|sitelinks/urls` — yields ~25 external authority IDs (SIMBAD, Britannica, Freebase, JSTOR, WordNet, …) + Wikipedia sitelinks in 50+ languages, all already on the entity.
  - **Fallback:** `wbsearchentities` (label match only — use only if reconciliation is down).
- **DBpedia** — `http://dbpedia.org/resource/<Name>`. Search via **DBpedia Lookup** — returns the resource URI plus types, refCount, and redirect labels. Often surfaces multilingual variants (`de.dbpedia.org`, `fr.dbpedia.org`, …) for popular concepts.
- **LODsyndesis** (FORTH-ISL) — cross-dataset `owl:sameAs` aggregator. The `/objectCoreference` endpoint takes any URI and returns equivalents across hundreds of LOD datasets (Wikidata, DBpedia, YAGO, Freebase, GeoNames, …). Use as a step *after* you have a starting URI, to harvest equivalences Wikidata doesn't already store.
- **LOV (Linked Open Vocabularies)** — for **classes and properties**, not individual entities. The term-search API indexes vocabulary terms across hundreds of vocabularies (`csvw`, `rml`, `foaf`, `schema`, …). Returns 0 hits for entities like "Proxima Centauri" — this is the right scope, not a failure. Use when the user asks for a predicate URI or class URI to use in modelling.
- **Falcon 2.0** (TIB) — entity + relation linker over Wikidata/DBpedia. Takes a *sentence*, returns Wikidata Q-IDs. Useful when the label alone is ambiguous and the user has provided context. Beware of spurious extractions from filler phrases — filter to the user's actual notion.
- **id.loc.gov** — `https://id.loc.gov/authorities/names/<id>`. LoC authority control. Niche — useful only for persons/orgs/works in the library catalog.
- **VIAF** — `https://viaf.org/viaf/<id>`. Authors and persons. **The AutoSuggest API is blocked by Cloudflare for non-browser clients** — link manually if needed; don't rely on programmatic lookup.
- **schema.org** — Only for types (e.g. `schema:Book`, `schema:Person`); not for individual entities.

## Concrete API reference

Copy-paste curl commands. `$Q` is the entity label; `$SENTENCE` is the user's sentence (Falcon only).

```bash
# Wikidata entity search → Q-ID + label + description
curl -s -G "https://www.wikidata.org/w/api.php" \
  --data-urlencode "action=wbsearchentities" \
  --data-urlencode "search=$Q" \
  --data-urlencode "language=en" --data-urlencode "format=json" \
  --data-urlencode "limit=3" --data-urlencode "type=item"

# DBpedia Lookup → resource URI + types + refCount + multilingual variants
curl -s -G "https://lookup.dbpedia.org/api/search" \
  --data-urlencode "query=$Q" --data-urlencode "maxResults=3" \
  --data-urlencode "format=JSON" -H "Accept: application/json"

# LOV term search → class/property URI (use only for vocabulary terms)
curl -s -G "https://lov.linkeddata.es/dataset/lov/api/v2/term/search" \
  --data-urlencode "q=$Q"

# Falcon 2.0 → entities from a sentence (filter to the user's notion)
curl -s -X POST "https://labs.tib.eu/falcon/falcon2/api?mode=long" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"$SENTENCE\"}"
```

The Wikidata canonical URI is `https://www.wikidata.org/entity/<id>` (the API's `concepturi` field uses `http://`, but the `https://` form is the standard prefix).

## Searching the Nanopublications registry

Nanopub Query (Knowledge Pixels) exposes RDF4J repositories at:

- `https://query.knowledgepixels.com/` (also mirrored at `query.np.trustyuri.net`, `query.petapico.org`)

The `text` repo supports full-text search via the **RDF4J Lucene SAIL** vocabulary.

### Example: full-text search for a term

```bash
curl -s -G "https://query.knowledgepixels.com/repo/text" \
  --data-urlencode "query=PREFIX search: <http://www.openrdf.org/contrib/lucenesail#>
SELECT DISTINCT ?subj ?score WHERE {
  ?subj search:matches [
    search:query \"knowledge representation language\" ;
    search:score ?score
  ] .
} ORDER BY DESC(?score) LIMIT 20" \
  -H "Accept: application/sparql-results+json"
```

Each `?subj` in the result is a nanopublication URI (the `RA…` Trusty hash). To find the **term URI** the nanopub introduces:

1. Dereference the nanopub URL with `Accept: application/trig` (or use the `/repo/full` endpoint).
2. Look in the `pubinfo` graph for `npx:introduces <term-uri>` — that's the canonical term.
3. Note the `latest:` prefix in the nanopub: `https://w3id.org/fair/fip/latest/<Name>` redirects to the most recent nanopub version.

### Resulting URI flavors

A single concept may have **three related URIs** in the nanopub world:

- **Term URI** — e.g. `https://w3id.org/fair/fip/terms/Knowledge-representation-language`. Stable, versionless, what you usually want in your data.
- **Latest-version pointer** — e.g. `https://w3id.org/fair/fip/latest/Knowledge-representation-language`. Always redirects to the current nanopub.
- **Trusty URI** — e.g. `…/Knowledge-representation-language/RAvIp2…NM_sM`. Frozen, content-addressed, signed. Use to cite a specific definition.

## Comparison criteria

When more than one URI exists for the same notion, compare them on:

| Criterion | What it means | Who scores high |
|---|---|---|
| **Redirect stability** | The URL keeps resolving even if hosting changes | `w3id.org`, `purl.org` (community-maintained redirectors) |
| **Content immutability** | The bytes the URL identifies cannot silently change | Trusty URIs (nanopub `RA…` hashes) — content-addressed |
| **Authorship / provenance** | The definition is cryptographically signed by a known author | Signed nanopublications (ORCID + key signature) |
| **Community maintenance** | Active editors keep labels, links, descriptions current | Wikidata, DBpedia, FIP working groups |
| **Cross-link density** | How many other datasets reference this URI | Wikidata > DBpedia > niche namespaces |
| **Multilingual labels** | Labels in many languages | Wikidata (strong), VIAF (some), nanopub terms (usually English-only) |
| **Domain fit** | Whether the URI lives in a vocabulary the project already uses | Project-specific — FIP terms for FAIR work, schema.org for web markup, etc. |

Two important nuances:

- A `w3id.org` URL gives **redirect stability**, not content immutability — the maintainers can repoint it. For frozen content, use the Trusty URI it ultimately resolves to.
- A nanopub-defined term URI (e.g. `fip:Knowledge-representation-language`) is stable in identity but its *latest definition* can be superseded. The supersession chain is itself recorded in nanopubs (`npx:supersedes`), so the history is auditable.
- For ambiguous labels (e.g. "Mercury" → planet, element, or car), Wikidata `wbsearchentities` and DBpedia Lookup can rank candidates differently. When both return distinct top hits, surface both with their descriptions and let the user pick — don't silently choose one.

## Output

Provide:

- **URI** — the chosen linked data URL (or multiple, if comparison is warranted).
- **Source** — Wikidata / DBpedia / Nanopub / VIAF / etc.
- **Usage in TTL** — prefix declaration and example triple:
  ```turtle
  @prefix wd: <https://www.wikidata.org/entity/> .
  schema:author wd:Q34981 .
  ```
- **Comparison** (when multiple candidates exist) — a one-paragraph or small-table summary using the criteria above, ending with a recommendation tuned to what the user is doing (publishing nanopubs vs. linking to general web data vs. citing a frozen definition).

If no suitable URI is found, say so and suggest defining the entity locally (e.g. in the project's ontology or data file) or trying a different spelling/variant name.

## Examples

**User:** "Find a linked data URI for Isaac Asimov"
**Agent:** Call Wikidata `wbsearchentities`, DBpedia Lookup, and the nanopub registry in parallel → Wikidata Q34981 (and any nanopub hits) → verify labels → return `https://www.wikidata.org/entity/Q34981`, prefix `wd:`, example `schema:author wd:Q34981`; mention nanopub URI if a relevant one exists.

**User:** "Find a URI for Pluto"
**Agent:** Call Wikidata `wbsearchentities`, DBpedia Lookup, and the nanopub registry in parallel → Wikidata Q339 (dwarf planet) plus a nanopub-introduced term `…/RAJRFj…#pluto` → compare and recommend `wd:Q339` for general linking, with the Trusty URI available for signed citation. (Always check the nanopub registry, even for everyday notions.)

**User:** "Find a URI for 'Knowledge Representation Language' in the nanopublications space"
**Agent:** Run a Lucene SPARQL query against `https://query.knowledgepixels.com/repo/text` for the phrase → top hits are in `https://w3id.org/fair/fip/np/Knowledge-representation-language/…` → dereference one nanopub → find `npx:introduces fip:Knowledge-representation-language` → return `https://w3id.org/fair/fip/terms/Knowledge-representation-language` as the term URI, plus the Trusty URI of the latest nanopub for citation.

**User:** "Can we use an existing URI for the author instead of defining them in our ontology?"
**Agent:** Treat as find-url-for for the author mentioned in context (e.g. from the current TTL file) → find Wikidata/VIAF URI → return it and show how to replace the local individual.
