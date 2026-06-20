# Telecom Seed Deck

Running count: **0 / 200**

Format: `| # | EN Term | 中文 | Category | Usage note (one real sentence) |`

Mark unknown Chinese with `?` — resolve before finalising the row.

---

## RF / Radio fundamentals (target: 25)

| # | EN Term | 中文 | Category | Usage note |
|---|---|---|---|---|
| 1 | OFDM — Orthogonal Frequency-Division Multiplexing | 正交频分复用 | RF | LTE and 5G NR both use OFDM in the downlink to divide the channel into orthogonal subcarriers. |
| 2 | subcarrier spacing (SCS) | 子载波间隔 | RF | 5G NR supports multiple SCS values (15, 30, 60, 120, 240 kHz) to serve different deployment scenarios. |
| 3 | SINR — Signal-to-Interference-plus-Noise Ratio | 信干噪比 | RF | A UE reports SINR to the gNB to guide modulation and coding scheme selection. |
| 4 | path loss | 路径损耗 | RF | Free-space path loss increases with the square of distance and the square of carrier frequency. |
| 5 | fading | 衰落 | RF | Multipath fading causes rapid fluctuations in received signal power in urban environments. |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |

---

## LTE / 4G core (target: 30)

| # | EN Term | 中文 | Category | Usage note |
|---|---|---|---|---|
| 26 | eNB — Evolved Node B | 演进型基站 | LTE | The eNB is the LTE base station that handles radio resource management and connects to the EPC via the S1 interface. |
| 27 | EPC — Evolved Packet Core | 演进分组核心网 | LTE | The EPC consists of the MME, SGW, PGW, and HSS, forming the control and user planes of LTE. |
| 28 | MME — Mobility Management Entity | 移动性管理实体 | LTE | The MME handles UE attach, authentication, and handover signalling in the LTE control plane. |
| 29 | S1 interface | S1接口 | LTE | The S1 interface connects the eNB to the EPC: S1-MME carries control plane signalling, S1-U carries user data. |
| 30 | X2 interface | X2接口 | LTE | The X2 interface between adjacent eNBs enables direct handover signalling without routing through the EPC. |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |

---

## 5G NR / SA / NSA (target: 35)

| # | EN Term | 中文 | Category | Usage note |
|---|---|---|---|---|
| 56 | gNB — Next Generation Node B | 5G基站 | 5G | The gNB is the 5G NR base station; it connects to the 5GC via the NG interface and to other gNBs via Xn. |
| 57 | 5GC — 5G Core | 5G核心网 | 5G | The 5GC uses a service-based architecture (SBA) with network functions such as AMF, SMF, and UPF. |
| 58 | SA — Standalone | 独立组网 | 5G | In SA mode, 5G NR connects directly to the 5GC without relying on an LTE anchor. |
| 59 | NSA — Non-Standalone | 非独立组网 | 5G | In NSA mode (Option 3x), the LTE eNB provides the control plane anchor while NR adds capacity in dual connectivity. |
| 60 | AMF — Access and Mobility Management Function | 接入和移动性管理功能 | 5G | The AMF replaces the LTE MME, handling registration, connection management, and mobility in the 5GC. |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |

---

## IoT / NB-IoT / eMTC (target: 25)

| # | EN Term | 中文 | Category | Usage note |
|---|---|---|---|---|
| 91 | NB-IoT — Narrowband IoT | 窄带物联网 | IoT | NB-IoT operates in a 180 kHz bandwidth and is deployed in-band, guard-band, or standalone within LTE spectrum. |
| 92 | eMTC — enhanced Machine-Type Communication | 增强型机器类通信 | IoT | eMTC (LTE-M) supports voice and mobility, making it suitable for wearables and asset trackers alongside NB-IoT. |
| 93 | PSM — Power Saving Mode | 省电模式 | IoT | PSM allows an IoT device to enter a deep-sleep state for hours or days, extending battery life to several years. |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |

---

## Protocol stack / L1–L3 (target: 25)

| # | EN Term | 中文 | Category | Usage note |
|---|---|---|---|---|
| 116 | PDCP — Packet Data Convergence Protocol | 分组数据汇聚协议 | Protocol | PDCP performs IP header compression, ciphering, and integrity protection in both LTE and 5G NR. |
| 117 | RLC — Radio Link Control | 无线链路控制 | Protocol | RLC provides segmentation, reassembly, and ARQ retransmission between the UE and the base station. |
| 118 | MAC — Medium Access Control | 媒体访问控制 | Protocol | The MAC layer schedules uplink and downlink transmissions and performs HARQ retransmissions. |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |

---

## Network architecture (target: 20)

| # | EN Term | 中文 | Category | Usage note |
|---|---|---|---|---|
| 141 | fronthaul | 前传 | Architecture | In C-RAN, fronthaul connects the BBU pool to the RRH over fibre or microwave, carrying IQ data via CPRI or eCPRI. |
| 142 | midhaul | 中传 | Architecture | In 5G disaggregated RAN, midhaul connects the DU to the CU, carrying F1 interface traffic. |
| 143 | backhaul | 回传 | Architecture | Backhaul connects the base station site to the core network, typically over fibre, microwave, or millimetre-wave links. |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |

---

## Operations / KPIs (target: 20)

| # | EN Term | 中文 | Category | Usage note |
|---|---|---|---|---|
| 161 | throughput | 吞吐量 | KPI | Peak downlink throughput is a key marketing metric; sustained average throughput is more relevant to user experience. |
| 162 | latency | 时延 | KPI | 5G NR targets 1 ms user-plane latency for URLLC use cases, compared to ~10 ms for LTE. |
| 163 | RRC — Radio Resource Control | 无线资源控制 | KPI | RRC state (IDLE / INACTIVE / CONNECTED) determines a UE's power consumption and data-access speed. |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |

---

## Chinese telecom terms / 业务词 (target: 20)

| # | EN equivalent | 中文 | Pinyin | Usage note |
|---|---|---|---|---|
| 181 | base station | 基站 | jīzhàn | 深圳华为总部附近有大量5G基站密集部署。 |
| 182 | operator | 运营商 | yùnyíngshāng | 中国三大运营商是中国移动、中国联通和中国电信。 |
| 183 | spectrum / frequency band | 频段 | pínduàn | 5G毫米波频段在中国尚未大规模商用。 |
| 184 | chip / chipset | 芯片 | xīnpiàn | 华为海思麒麟芯片曾是国内5G手机的主要选择。 |
| 185 | network coverage | 网络覆盖 | wǎngluò fùgài | 运营商在农村地区加大网络覆盖投入以缩小数字鸿沟。 |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
| — | | | | |
