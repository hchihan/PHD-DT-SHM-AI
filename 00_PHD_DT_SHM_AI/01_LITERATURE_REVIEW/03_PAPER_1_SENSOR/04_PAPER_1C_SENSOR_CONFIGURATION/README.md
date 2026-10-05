# Paper 1B — Sensor Configuration

**Mục tiêu:** sensor subsets, số lượng/thành phần cảm biến, performance retention, marginal benefit và robustness giữa run/campaign.

**Vị trí logic:** supporting scope của RQ1/WP1; không có RQ, WP hoặc Gate riêng.

**Deep-read dùng chung:** `02_DEEP_READ_CURRENT/02_RQ1_GATE1/`; protocol validity do Paper 1A sở hữu.

**Được phép claim:** hiệu ứng cấu hình cảm biến sau khi evaluation protocol hợp lệ; mọi kết luận hiện tại là candidate.

**Thiếu:** locked subset matrix, retention/marginal-benefit tables, uncertainty và cross-run/campaign robustness.

**Ranh giới/overlap:** không lặp leakage/provenance/G1 acceptance của 1A; không dùng “optimal sensor placement” như claim luận án.

## Trạng thái 13/09/2026 (sync)

- Paper 1 (v8.1, `SCIENCE LOCKED`) chỉ phân tích cấu hình đầy đủ nhất: S12 ở CP1, S123 ở CP2/CP3. Kết quả trên các tập con cảm biến nằm ngoài phạm vi Paper 1 và thuộc Paper 1B.
- Khối sensor-subset hiện có (ResNet1D, 17 cấu hình × 30 split, **một seed**; kết luận kỹ thuật 07/09/2026) không tách được hiệu ứng cấu hình khỏi nhiễu fold ở CP2 và CP3.
- Claim "sensor configuration dominates / influences more than model architecture" (Charter v1.1 §13; Charter v2.1 §10) **không được Paper 1 đưa ra và không được bằng chứng hiện có hỗ trợ.** Đang chờ thầy quyết định (`01_CURRENT_CONTROL/PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md`, C-02). Không dùng claim này ở dạng khẳng định.
