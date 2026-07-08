# Sample session (condensed)

What a triage → formulate exchange looks like in practice. Any capable agent
following `AGENTS.md` should produce something of this shape.

---

**User:** Help me learn this paragraph from a networking course:

> DNS resolution is hierarchical: resolvers start at the root, which points
> to TLD servers, which point to authoritative servers. Records carry a TTL
> in seconds that controls caching — the default in BIND 9.16 is 86400.
> An A record maps a hostname to an IPv4 address; AAAA to IPv6; MX lists
> mail servers. CNAME aliases one name to another but cannot exist at a
> zone apex alongside SOA/NS. DNS was designed by Paul Mockapetris in 1983.
> To debug, run `dig +trace example.com`.

**Agent:** Context applied: networking is one of your **core** domains
(LEARNER.md), budget ≤15 new items/day.

| # | Knowledge unit | Verdict | Why |
|---|---|---|---|
| 1 | Resolution is hierarchical (root → TLD → authoritative) | MEMORIZE | foundation |
| 2 | TTL controls caching duration | MEMORIZE | judgment anchor (debugging) |
| 3 | BIND 9.16 default TTL = 86400 | OFFLOAD | version-specific value, instant lookup |
| 4 | A / AAAA / MX record meanings | MEMORIZE | core vocabulary, high frequency |
| 5 | CNAME can't sit at zone apex | MEMORIZE | discrimination, bites in practice |
| 6 | Designed by Mockapetris, 1983 | DISCARD | trivia, no connective value |
| 7 | `dig +trace` syntax | OFFLOAD | tool-in-hand procedure, verifiable on the spot |

**4 MEMORIZE → ~7 cards, 0 MAP, 2 OFFLOAD, 1 DISCARD.** Well inside your
budget. Anything you'd overrule? Otherwise say the word and I'll formulate.

**User:** Go ahead.

**Agent:** 7 cards from the 4 MEMORIZE units; nothing carded from #3/#6/#7.
Saved as `cards/dns-basics-2026-07-08.txt`:

```
q: DNS: why does recursive resolution start at the root servers?
a: it's a delegation hierarchy — root → TLD → authoritative

q: DNS: what does a record's TTL limit?
a: how long resolvers may cache it

q: prod incident: users still get the old IP after a DNS change — first thing to check?
a: TTL / resolver caches

q: DNS: what does an A record map?
a: hostname → IPv4 address

q: DNS: record type that maps a hostname to an IPv6 address?
a: AAAA

q: DNS: the [...] record lists the mail servers that accept mail for a domain
a: MX

q: DNS: CNAME vs A — why can't you use CNAME at a zone apex?
a: CNAME can't coexist with the apex's SOA/NS records
```

Import in SuperMemo: **File : Import : Q&A text**, pick the file, then set
priorities honestly with **Alt+P** (0% = highest; these deserve ~30% in a
core domain, not 1%).

---

Notes on what happened here:

- Two units the source presented as facts to learn were **refused** (default
  TTL value, dig syntax) — that refusal is the product working as designed.
- The historical attribution was discarded without apology.
- Unit 1 became a *mechanism* card ("why"), unit 2 became both a definition
  and a *judgment* card, unit 5 a *discrimination* card — not verbatim
  restatements of the source.
