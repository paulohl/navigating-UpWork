# Upwork policy-change timeline

Compiled 2026-10-28. **Four distinct dated changes**, within a ten-entry chronology. This is a bounded reconstruction of general marketplace fee changes, with an explicit gap register for enforcement policies. It is not a complete history of Upwork's terms or products.

## Timeline

| Date | Milestone | Evidence status |
|---|---|---|
| Before 3 May 2023 | General freelancer fees follow 20/10/5% lifetime-client-billing tiers. | Historical baseline; original onset unknown. |
| By 27 Mar 2023 | Archived help article announces the 2023 changes. | Capture date, not publication or effective date. |
| **26 Apr 2023** | **Client contract initiation fee up to USD 4.95 starts on eligible new contracts.** | Explicit effective date; subsequent client-fee changes not reconstructed. |
| **3 May 2023, Pacific Time** | **General freelancer fee becomes 10%; eligible existing 5% contracts remain protected through year-end.** | Explicit effective date; 20% contracts move on the next relevant invoice. |
| 6 May 2023 | Archived help article describes the 10% rule after rollout. | Implementation corroboration, not an additional policy change. |
| **Through 31 Dec 2023** | **Temporary legacy 5% protection expires.** | Explicit end-of-year sunset; applies to eligible contracts, not all special-product fees. |
| 1 Jan 2024 | First day after that sunset. | Calendar inference; not a separately verified literal date or invoice date. |
| By 27 Apr 2025 | Archived article announces a variable fee for new contracts, with existing contract fees unchanged. | Notice observed by capture date; publication date unknown. |
| **1 May 2025** | **New contracts move from fixed 10% to variable freelancer fees.** | Explicit effective date; fee remains fixed over each contract's life. |
| 2026-10-28 | Live article reports a 0–15% per-contract range. | Current observation; exact onset of this numerical range not verified here. |

## The missing transition is now dated

The April 27, 2025 archived Upwork notice states:

> “Starting May 1, 2025, the Freelancer Service Fee for new contracts will change from a fixed 10% to a variable fee based on factors such as client demand for certain work. The fee will stay the same for the life of the contract. Fees on existing contracts will not change.”

This establishes **May 1, 2025**, the new-contract scope and grandfathering of existing contract fees. It does **not** state the numerical launch range. The currently retrieved article supplies 0–15%; this reconstruction deliberately does not combine the two documents into an unsupported claim that 0–15% was necessarily the precise launch range. Current proposal/offer lock-in wording is also not retroactively treated as the verified cutoff rule for pending proposals in May 2025.

![Visual Chronology][logo]

[logo]: /compile-policy-records/policy_change_timeline.png "Chronology"

## Contract scope matters

The 2023 protection attached to eligible existing contracts already at 5%, not all later work with the same client. The September 26, 2023 archive explicitly says new contracts with that client have a 10% fee regardless of client history. Similarly, the 2025 notice preserves existing contract fees, not a permanent fee entitlement for the freelancer or client relationship. Enterprise, Payroll, Any Hire and other special arrangements may differ; do not generalize the standard fee schedule to them.

## Enforcement-policy gaps

The workbook retains **15 undated policy/procedure records** from the original October 23 collection: circumvention, account identity, feedback, enforcement, reporting and appeals. Those sources document the rules at retrieval, not when the rules started or changed. No change date is inferred from article creation or update metadata. Their underlying versions were not all refreshed in this follow-up.

The 2024 transparency report describes outcomes over a year. Its suspension and appeal totals are **not policy-change events**, so they do not appear as timeline changes. A later report or updated help article alone does not establish that the enforcement rule changed. Testing differential treatment requires a separate case-level or disaggregated dataset.

The supplied paper's PDF carries July 15, 2024 dates despite the task citation saying 2026. This timeline provides historical context around that date, but does not resolve bibliographic version history or assume that the later 2025 policy was in force when the PDF was written.

## Sources and evidence handling

The original 42-record dataset is unchanged. This follow-up reuses its eleven preserved source documents and adds three representations: the September 2023 archive HTML, an April 2025 transition-notice excerpt, and refreshed fee-article JSON. All fourteen are described in the workbook Sources sheet and bundled manifest. Not every retained source supports a dated event: some support the undated gap register and prior context.

The April 2025 notice was independently retrieved by the repository-search agent and read through web_fetch. Raw HTML preservation attempts returned HTTP 429. The bundle therefore contains a **labelled verbatim article-body excerpt**, not falsely labelled original HTML. Its SHA-256 identifies that saved excerpt representation. Other source hashes identify preserved original bytes. No rate-limit bypass was attempted. Capture timestamps must not be read as original publication dates.

## Deliverables

- `policy_change_timeline.png`: chronological schematic; green = dated change, grey = observation/baseline, amber = inferred calendar boundary. Row spacing is not elapsed-time proportional.
- `policy_change_timeline.xlsx`: Timeline, Undated rules, Sources, Field guide and Search log sheets. Green rows mark the four distinct dated changes.
- `policy_change_timeline.csv`: ten timeline entries with before/after rules, scope, source quotations, links, date types and limitations.
- `timeline_evidence.zip`: fourteen preserved source representations plus manifest and search log; includes original collection evidence.
- `timeline_notes.md`: this interpretive note and evidence limitations.

## Validation

Unique timeline IDs; exactly four distinct nonempty change IDs; all primary quotations checked against preserved source content with whitespace normalization; source foreign keys validated; all fourteen ZIP hashes checked; workbook and CSV row counts matched. No formulas or inferred numeric rates are used. The capture/announcement/implementation distinctions are encoded explicitly to prevent double-counting policy changes. This is a single-curator reconstruction, not independently duplicated screening or an exhaustive archive crawl.
