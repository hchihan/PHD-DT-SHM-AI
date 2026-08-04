# PAPER 1 — DIRECTION & GATE (v2.1)
**Version:** v2.1 | **Date:** 2026-07-19 | **Status:** CURRENT direction (dưới Charter v2.1)
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
run registry khóa · sensor metadata · file provenance · leakage-safe split · split-before-windowing · train-only preprocessing · LORO (common seeds) · run-level metrics & uncertainty · ResNet1D sensor-mode verification.

## Immediate blocker
Verify ResNet1D sensor mode — **không con số ResNet1D nào vào Paper 1 cho tới khi resolved.**

## Claim → Evidence → Limitation → Next action
- **Claim:** Paper 1 định hướng theo trục v2.1, claims đánh dấu candidate.
- **Evidence:** Charter v2.1 §10; matrix v2.1 §5; các file Paper 1 GATE1 hiện có trong thư mục này; evidence base group A (RQ1 lab): `../../02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` (leakage/LORO: M8LMWFQH, RG9FMT8Y, XE9XS6BQ, PEUHYBPS; steel-frame precedent YR2NQWE7).
- **Limitation:** G1 chưa đóng; LORO chưa chạy; ResNet1D provenance pending; run count "6" chưa khóa.
- **Next action:** khóa run registry → LORO → ResNet1D provenance → run-level uncertainty → chỉ sau đó khóa claim.

> Các file thao tác Paper 1 hiện hành (manuscript source, claim-evidence audit, IT requests, reference audit, revision log) nằm cùng thư mục; không file DOCX nào là CURRENT_APPROVED.
