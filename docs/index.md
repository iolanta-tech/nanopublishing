---
title: nanopublishing
subtitle: A coding-agent workflow for nanopublications
hide:
  - navigation
  - toc
---

# nanopublishing

<p class="site-subtitle">A coding-agent workflow for nanopublications</p>

This repository is a working nanopublishing workflow for coding agents.
Here is what using it looks like in one small end-to-end session.

## Installation

Install all skills from this repository into the current project for your agent of choice:

```bash
npx skills add https://github.com/iolanta-tech/nanopublishing \
  --skill '*' \
  -a claude-code
```

Replace `claude-code` with `codex` or `cursor`.
Add `-g` if you want a global install instead of a project-local one.

## Example session

<div class="session-step" markdown="1">
<div markdown="1">
<div class="chat-block user">
  <div class="chat-speaker"><img class="chat-avatar dave-avatar" src="assets/images/dave.png" alt="Dave avatar"/><span>Dave</span></div>
  Please write, in <code>index.md</code>, which SSD form factors can use what connection interfaces.
</div>
<div class="chat-block agent">
  <div class="chat-speaker"><img class="chat-avatar hal-avatar" src="assets/images/hal9000-sharper-reflections.svg" alt="HAL 9000 avatar"/><span>HAL 9000</span></div>
  Here you are.
</div>
</div>
<div markdown="1">

```markdown title="index.md"
--8<-- "examples/types-of-ssds/interface-to-form-factor-mapping/index.md:25:41"
```

</div>
</div>

<div class="session-step chat-only" markdown="1">
<div markdown="1">

<div class="chat-block user">
  <div class="chat-speaker"><img class="chat-avatar dave-avatar" src="assets/images/dave.png" alt="Dave avatar"/><span>Dave</span></div>
  How do we express that one thing is compatible to another? <strong>/find-url-for</strong>&nbsp;<em>compatible with</em>
</div>
<div class="chat-block agent" markdown="1">
  <div class="chat-speaker"><img class="chat-avatar hal-avatar" src="assets/images/hal9000-sharper-reflections.svg" alt="HAL 9000 avatar"/><span>HAL 9000</span></div>
  We can use [ :fontawesome-brands-wikipedia-w: <code>wd:P8956</code> ](https://www.wikidata.org/wiki/Property:P8956).
</div>

</div>
</div>

<div class="session-step" markdown="1">
<div markdown="1">

<div class="chat-block user">
  <div class="chat-speaker"><img class="chat-avatar dave-avatar" src="assets/images/dave.png" alt="Dave avatar"/><span>Dave</span></div>
  Okay, let's rely upon wikidata. <strong>/semantify</strong> <code>index.md</code>, then.
</div>
<div class="chat-block agent" markdown="1">
  <div class="chat-speaker"><img class="chat-avatar hal-avatar" src="assets/images/hal9000-sharper-reflections.svg" alt="HAL 9000 avatar"/><span>HAL 9000</span></div>
  I've added [ :simple-yaml: YAML-LD ](https://w3c.github.io/yaml-ld/spec/) frontmatter and mapped the compatibility facts to linked data.
</div>

</div>
<div markdown="1">

```markdown
--8<-- "examples/types-of-ssds/interface-to-form-factor-mapping/index.md:1:27"

...
```

</div>
</div>

<div class="session-step" markdown="1">
<div markdown="1">

<div class="chat-block user">
  <div class="chat-speaker"><img class="chat-avatar dave-avatar" src="assets/images/dave.png" alt="Dave avatar"/><span>Dave</span></div>
  Okay, that looks fine. <strong>/nanopublish</strong> <code>index.md</code>.
</div>
<div class="chat-block agent">
  <div class="chat-speaker"><img class="chat-avatar hal-avatar" src="assets/images/hal9000-sharper-reflections.svg" alt="HAL 9000 avatar"/><span>HAL 9000</span></div>
  It is published. The signed artifact remains beside the Markdown source.
</div>

[Open nanopublication](https://w3id.org/np/RAMIHkOctLsK2ZlbWS0gr0kz9wFffP0fHSIN-N_aKrgC8){ .md-button .md-button--primary }

[See the full example](examples/types-of-ssds/interface-to-form-factor-mapping/index.md){ .md-button }

</div>
<div markdown="1">

![Published nanopublication screenshot](assets/images/nanopublication.png){ .publish-preview }

</div>
</div>

<p class="avatar-attribution">
  HAL 9000 avatar: <a href="https://commons.wikimedia.org/wiki/File:HAL9000_-_Sharper_Reflections.svg">“HAL9000 - Sharper Reflections.svg”</a> by Cryteria and MorningLemon, licensed under <a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a>, via Wikimedia Commons.
</p>

## More examples

### :material-harddisk: Types of SSDs

<div class="grid cards" markdown>

-   [SSD host protocol classification](examples/types-of-ssds/interface-scheme/index.md)

    SATA, SAS, and NVMe as SSD host protocols.

-   [SSD form factor scheme](examples/types-of-ssds/form-factor-scheme/index.md)

    M.2, mSATA, U.2, 2.5-inch, and add-in card form factors.

-   [M.2 keying scheme for SSDs](examples/types-of-ssds/m2-keying-scheme/index.md)

    B key, M key, and B+M key as SSD-relevant M.2 keying patterns.

</div>

<style>
.site-subtitle {
  margin-top: -0.8rem;
  font-size: 1.15rem;
  color: var(--md-default-fg-color--light);
}

.session-step {
  display: grid;
  gap: 1.2rem;
  margin: 1.8rem 0 2.2rem;
  align-items: start;
}

.chat-block {
  display: inline-block;
  width: fit-content;
  max-width: 100%;
  margin: 1rem 0 0.6rem;
  padding: 0.75rem 0.95rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.9rem;
  background: rgba(255, 255, 255, 0.03);
  font-family: var(--md-code-font);
  font-size: 0.95rem;
}

.chat-speaker {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  margin-bottom: 0.7rem;
  font-family: var(--md-text-font);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.chat-avatar {
  flex: none;
  display: inline-block;
  width: 1.1rem;
  height: 1.1rem;
  object-fit: cover;
}

.dave-avatar {
}

.hal-avatar {
}

.avatar-attribution {
  margin-top: -0.4rem;
  margin-bottom: 2rem;
  font-size: 0.72rem;
  color: var(--md-default-fg-color--light);
}

.publish-preview {
  display: block;
  width: 100%;
  border-radius: 0.9rem;
}

.chat-block.user {
  display: table;
  margin-right: 12%;
  color: var(--md-accent-fg-color);
}

.chat-block.agent {
  display: table;
  margin-left: auto;
  margin-right: 0;
  color: var(--md-default-fg-color--light);
  background: rgba(255, 255, 255, 0.05);
  text-align: right;
}

.chat-block.agent .chat-speaker {
  justify-content: flex-end;
}

@media screen and (min-width: 76.25em) {
  .session-step {
    grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.35fr);
  }

  .session-step.chat-only {
    grid-template-columns: minmax(0, 0.95fr);
  }
}
</style>
