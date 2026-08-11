# PAPER 1 — DIRECTION & GATE (v2.2)
**Version:** v2.2 | **Issued:** 2026-07-19 | **Updated:** 2026-08-04
**Status:** CURRENT DIRECTION; G1 `OPEN — PARTIAL EVIDENCE` | **Source-of-truth level:** 7
**Supersedes:** v2.1 Paper 1 direction. | **Superseded by:** None.
**Change summary:** Aligns G1 priorities with canonical provenance, leakage-safe multi-seed LORO, ResNet1D provenance decision and signed acceptance; no result is promoted.
**RQ1 · WP1 · Chapter 4 · Gate G1 · Target: Sensors (verify rank trước khi khóa)**

## Scope
Run-aware evaluation of low-cost sensor configurations cho vibration-based lab evidence: dataset integrity, run registry, run-aware/LORO, sensor-configuration effect, CEI as by-product. **Không** field diagnosis, **không** lab-to-field transfer.

## Trạng thái claim (BẮT BUỘC ghi nhãn)
Cho tới khi **Gate 1 đóng**, mọi kết luận sau là **"Candidate claim pending Gate 1 closure":**
- Sensor configuration dominates model architecture.
- RF macro-F1 ~0.862 (leads); 1D-CNN S12 ~0.841; ResNet1D ~0.828 (corroborating only).
- ResNet1D corroborates finding — pending sensor-mode & provenance verification.

DSI / ordinal severity: **removed.** CEI mô tả như confidence/evidence indicator (metadata), không phải severity.

## Điều kiện đóng Gate 1
canonical run registry · sensor identity/provenance · file provenance · leakage-safe split · split-before-windowing · train-only preprocessing · run-aware/LORO with multiple seeds · run/fold metrics & uncertainty · ResNet1D provenance confirm-or-remove decision · acceptance matrix and supervisor sign-off.

## Immediate blocker
Verify ResNet1D sensor mode — **không con số ResNet1D nào vào Paper 1 cho tới khi resolved.**

## Claim → Evidence → Limitation → Next action
- **Claim:** Paper 1 định hướng theo trục v2.1, claims đánh dấu candidate.
- **Evidence:** Charter v2.1 §10; matrix v2.1 §5; các file Paper 1 GATE1 hiện có trong thư mục này; evidence base group A (RQ1 lab): `../../02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` (leakage/LORO: M8LMWFQH, RG9FMT8Y, XE9XS6BQ, PEUHYBPS; steel-frame precedent YR2NQWE7).
- **Limitation:** Existing registry/reanalysis documentation is partial/supporting; no accepted provenance-complete G1 package or signed acceptance exists. ResNet1D provenance remains unresolved.
- **Next action:** khóa canonical run registry và sensor provenance → audit split-before-windowing → leakage-safe multi-seed LORO → ResNet1D confirm/remove → run/fold uncertainty → acceptance/sign-off → chỉ sau đó khóa claim.

> Các file thao tác Paper 1 hiện hành (manuscript source, claim-evidence audit, IT requests, reference audit, revision log) nằm cùng thư mục; không file DOCX nào là CURRENT_APPROVED.
