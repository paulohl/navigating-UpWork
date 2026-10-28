# Upwork policy and enforcement records — curated primary-source release

Collected: 2026-10-23T06:10:04.234812+00:00. **42 records from 11 preserved primary-source documents**, across Upwork Help Center/attachments, Internet Archive Wayback Machine and SEC EDGAR. This is a bounded, purposive collection, not an exhaustive repository census. All records are real, directly sourced records; none are simulated.

## What this adds to your paper

Scope follows *Navigating Upwork: Understanding Corporate Dynamics And Unveiling Freelancer Realities Amid Policy Disruption*, DOI 10.2139/ssrn.6031034, especially pp. 2–3, 10, 21–24 and 34–36. The supplied PDF is dated **15 July 2024** throughout, despite the task citation specifying 2026. Its design combines a stated systematic review, user experiences and an autobiographical account. It reports 218 studies/reports and 495 perspectives for one observation and 50 sources for another, but provides no item-level source roster or extractable study dataset. Page 36 says no data beyond public citations were used. Those paper-reported counts and illustrative suspension cases were **not imported as repository records**.

The appropriate record types are dated policy provisions, corporate regulatory disclosures, and corporate-reported enforcement aggregates—not experimental observations or independently adjudicated user cases. The recipe was narrowed accordingly. Trustpilot/forum narratives and generic gig-economy statistics were excluded from the primary dataset; these would require a separate sampling and verification protocol.

## Three consequential observations

1. **Fee chronology needs separation.** The paper presents 20/10/5% tiers as the general schedule (pp. 2, 10, 21). Upwork's March 27, 2023 archived help article explicitly announces a **May 3, 2023 Pacific Time** move to 10% on new contracts, with eligible existing 5% contracts protected through end-2023. A May 6 archive and FY2023 10-K corroborate the change. The current article instead reports a 0–15% range. Its onset was not inferred, and a complete transition history to today's regime is not claimed.
2. **There are usable original enforcement totals.** Upwork's own 2024 transparency report states **184,914 accounts suspended**, **827,265 job posts removed**, and **22,528 suspension appeals received**. It reports 10,790 approved temporary-suspension appeals and 4,054 approved permanent-suspension appeals. These are pooled content-moderation measures, not case-level observations and not a freelancer/client comparison.
3. **Approved appeal ≠ enforcement error.** The report attributes approximately 96% of temporary-suspension appeal approvals to completion of required reinstatement actions, and about 4% to a changed enforcement decision. Treating all approvals as wrongful suspensions would overstate evidence. No causal or fairness conclusion is supported by these aggregates alone.

## Files and structure

- `upwork_policy_records.xlsx`: filterable Records, Sources, Dictionary, Uncertainty flags and Search log sheets; yellow cells highlight limitations.
- `upwork_policy_records.csv`: the same 42 records, UTF-8 BOM, one atomic provision or reported measure per row.
- `source_inventory.csv`: 11 source documents with URLs, repository metadata, archive timestamps, access date and SHA-256.
- `source_evidence.zip`: original API JSON, archive HTML, SEC filing HTML and official 2024 report PDF; manifest and search log included.
- `README.md`: scope, findings, quality criteria, date conventions, limitations and validation.

The CSV intentionally mixes numeric measures and qualitative policy provisions using `record_type`; **filter before analysis**. Multiple rows can share a source; corroborating versions must not be counted as separate policy events. Dates are ISO 8601; a blank means unknown/not applicable, never zero. Percentages use the 0–100 scale. Monetary amounts are nominal USD. Exact source quotations and page/section locators remain alongside harmonized paraphrases. No ratios were calculated in the dataset, and no missing values were invented.

## Source selection and access

Included only substantive content retrieved directly from official repositories, or Internet Archive captures of official Upwork pages. Metadata-only or search-snippet matches were insufficient. Upwork's public HTML help/legal pages initially returned HTTP 403; official Zendesk article JSON endpoints successfully exposed the original article bodies and metadata. The Legal Center remained inaccessible and was excluded: support summaries are not represented as a complete binding legal agreement. SEC EDGAR returned 200 with a descriptive User-Agent after an initial 403. Wayback exact-URL lookup succeeded, while broader CDX queries encountered 503 errors. The archive sample comprises two checked snapshots, not all revisions. All eleven source documents are preserved with byte-level hashes.

Quality tier `A_PRIMARY_RETRIEVED` means the original primary content was retrieved and inspected; it is **not** an independent endorsement of corporate reporting accuracy. Search discovery used fee-change, appeals/circumvention/feedback, and transparency-report queries; exact repository queries and exclusions are in Search log and the ZIP. The SEC filing date was checked against accession metadata by the repository-search agent; the filing HTML is preserved. The metadata response itself is not preserved.

## Temporal and interpretive limits

- Historical snapshots, present-day articles and full-year 2024 aggregates remain distinguishable. Current text is **not backdated to July 2024**. Article `created_at` and `updated_at` are repository metadata, not original effective dates.
- The 2024 transparency report does not print its publication date. It was discovered through the current official DSA article; its full-year figures necessarily include months after the supplied PDF's July 2024 date. This is an extension to the paper's evidence base, not evidence the author had available then.
- Report metrics may overlap across reporting, automation and enforcement. Do not add reports, removed jobs and suspended accounts together. Counts of accounts are not proven unique people; no deduplicated case linkage or enforcement-rate denominator is provided.
- The report has rounded graphic breakdowns (e.g. 117k permanent / 68k temporary suspensions). Those were **not substituted for exact prose totals** and are not included as exact counts.
- No role, country, job type or protected-characteristic breakdown supports testing equal treatment. No independent case findings, appeal case files, individual notifications or adjudicated account-level outcomes were collected. Payment-dispute outcomes are not covered by this release; the reported zero out-of-court notices is in a content-moderation context.
- Public access does not imply unrestricted redistribution rights; source copyrights and terms remain applicable. Preserved evidence is for provenance/research review, not an assertion of an open-data licence.

## Validation completed

Unique record IDs, valid source foreign keys, non-PDF quotation substring checks against retrieved originals (whitespace normalized), full source-file SHA-256 verification within the ZIP, CSV/workbook record-count agreement, defined uncertainty flags, and appeal subtotal checks (12,634 + 9,894 = 22,528). The five-page transparency report was read in full; enforcement and appeals pages 3–4 were also checked visually. Exact numeric values were taken from report prose, not rounded chart labels. This is a single-curator release, not duplicate independent screening.

## Reuse and expansion

For historical policy analysis, filter archived/disclosure records and inspect their explicit date precision. For enforcement summaries, filter `reported_aggregate`, retain units and denominator scopes, and do not interpret approvals as errors. Recommended next work: build a 2023–2026 policy version timeline; add the official 2025 report using the same schema; or collect separately coded, verifiable suspension/appeal cases to investigate role-specific treatment.
