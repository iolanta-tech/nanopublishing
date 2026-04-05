---
title: Context
hide:
  - navigation
---

# Context

The shared YAML-LD context for nanopub authoring in this site is:

```text
https://nanopublishing.iolanta.tech/context/v0.yamlld
```

## Overall Skeleton

```yaml
"@context": https://nanopublishing.iolanta.tech/context/v0.yamlld

$nanopublication:
  $assertion:
    # Assertion: what do we want to say?
    - $id: something
      is: kind of anything

  # Provenance: on which grounds do we assert the above? On whose authority?
  prov:wasAttributedTo: https://some-important-international.example.org

# Top Level: what can we say about the whole publication that we're writing?
npx:supersedes: URL of a previous publication
```

## `this:`

`this:` is the local prefix for entities defined inside the current nanopublication. In the shared context, it expands to the nanopublication's own namespace, so `this:MyEntity` means "the resource `MyEntity` in this nanopublication".

Use `this:` when you need a local identifier that belongs to the nanopublication you are writing, for example when the nanopublication introduces or embeds a new entity. Use an external IRI such as `wd:Q319` when the entity already exists elsewhere.

```yaml
$nanopublication:
  $assertion:
    - $id: this:MyEntity
      rdfs:label: My entity

npx:introduces: this:MyEntity
```

## Prefixes

The shared context defines these prefixes:

| Prefix | Expands to |
| --- | --- |
| `this:` | `http://purl.org/nanopub/temp/np/` |
| `npx:` | `http://purl.org/nanopub/x/` |
| `wd:` | `https://www.wikidata.org/entity/` |
| `wdt:` | `http://www.wikidata.org/prop/direct/` |
| `prov:` | `http://www.w3.org/ns/prov#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |

## Top level

### `npx:describes`
<div class="grid" markdown>

<div markdown="1">

States what the nanopublication is about.

</div>

```yaml
$nanopublication: …
npx:describes: wd:Q319
```

</div>

### `npx:supersedes`

<div class="grid" markdown>

<div markdown="1">

Declares that this nanopublication supersedes an older nanopublication.

</div>

```yaml
$nanopublication: …
npx:supersedes: https://w3id.org/np/RA…
```

</div>

### `npx:invalidates`

<div class="grid" markdown>

<div markdown="1">

Declares that this nanopublication invalidates another nanopublication.

</div>

```yaml
$nanopublication: …
npx:invalidates: https://w3id.org/np/RA…
```

</div>

### `npx:hasOriginalVersion`

<div class="grid" markdown>

<div markdown="1">

Points to the original nanopublication in a version chain.

</div>

```yaml
$nanopublication: …
npx:hasOriginalVersion: https://w3id.org/np/RA…
```

</div>

### `npx:retracts`

<div class="grid" markdown>

<div markdown="1">

Marks a nanopublication as retracting another nanopublication.

</div>

```yaml
$nanopublication: …
npx:retracts: https://w3id.org/np/RA…
```

</div>

### `npx:hasNanopubType`

<div class="grid" markdown>

<div markdown="1">

Assigns a nanopublication type.

</div>

```yaml
$nanopublication: …
npx:hasNanopubType: npx:DraftNanopub
```

</div>

### `npx:introduces`

<div class="grid" markdown>

<div markdown="1">

States that the nanopublication introduces an entity.

</div>

```yaml
$nanopublication: …
npx:introduces: this:MyEntity
```

</div>

### `npx:embeds`

<div class="grid" markdown>

<div markdown="1">

States that the nanopublication embeds an entity.

</div>

```yaml
$nanopublication: …
npx:embeds: this:MyEntity
```

</div>

### `npx:wasCreatedWith`

<div class="grid" markdown>

<div markdown="1">

Attributes creation to a software tool.

</div>

```yaml
$nanopublication: …
npx:wasCreatedWith: https://example.org/tool
```

</div>

### `npx:certifies`

<div class="grid" markdown>

<div markdown="1">

Expresses certification of another nanopublication.

</div>

```yaml
$nanopublication: …
npx:certifies: https://w3id.org/np/RA…
```

</div>

### `npx:qualifies`

<div class="grid" markdown>

<div markdown="1">

Expresses a weaker qualification of another nanopublication.

</div>

```yaml
$nanopublication: …
npx:qualifies: https://w3id.org/np/RA…
```

</div>

### `npx:approvesOf`

<div class="grid" markdown>

<div markdown="1">

Expresses approval of another nanopublication.

</div>

```yaml
$nanopublication: …
npx:approvesOf: https://w3id.org/np/RA…
```

</div>

### `npx:disapprovesOf`

<div class="grid" markdown>

<div markdown="1">

Expresses disapproval of another nanopublication.

</div>

```yaml
$nanopublication: …
npx:disapprovesOf: https://w3id.org/np/RA…
```

</div>

## `$nanopublication` level

### `prov:wasAttributedTo`
<div class="grid" markdown>

<div markdown="1">

Attributes the assertion to an agent or authority.

</div>

```yaml
$nanopublication:
  $assertion: …

  prov:wasAttributedTo: wd:Q6867
```

</div>

## `$assertion` level

The shared context defines no assertion predicates. Assertion predicates are domain-specific and usually come from a local overlay context.
