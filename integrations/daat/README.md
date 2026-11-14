# DaAT 0.4.3 — snapshot owner interface observation (2026-11-14)

**Status: `OBSERVED_SNAPSHOT` / not an adopted wire contract.** The corresponding machine-readable checklist is `owner-observation.json`. This addition is read-only, does not change normative schemas, does not make a canonical Kristal, and does not authorize publication.

## Owner and observed local interfaces

**Owner:** source bytes and custody in selected instance.

Verified snapshot markers (file presence is not functional execution):
- `README.md`
- `pyproject.toml`
- `contracts/kristal-ik-1.1/export-manifest.schema.json`


## Trust boundary

Skope/EncyK and Médiathèque custody receipts are not DaAT source-byte permission or semantic confirmation. Engine source is not an instance data store.

**Unresolved owner gate:** Instance authority and rights holder approve exact source byte intake; receiving custody adapter/receipt qualified against real instance.

## Next independent proof

1. Name an owner-ratified, versioned producer/consumer contract and exact revisions; the DaAT `daat.kristal-review-handoff/0.1.0-prototype` is **not** that contract.
2. Check exact source rights, reviewer authentication, provenance and semantic identity decisions where applicable.
3. Run positive and negative bilateral tests with each owner, including truncated inputs, changed bytes, duplicate IDs and denied permissions. Store exact versions and outcomes; an SHA-256 is not a digital signature.
4. Keep authoring, publication and activation separate and off by default.

The C0 `scripts/daat_owner_readiness.py` audit can collect local marker, Framework/Kit and diK parity evidence; a successful local read does **not** satisfy the above gates.
