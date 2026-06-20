# Interview Prep — Shenzhen Telecom Internship

Built in parallel with the deck during Phase 2 flex hours.
Goal: arrive at any telecom/IoT company interview able to discuss LTE/5G/IoT fluently in both English and Chinese.

---

## Self-test protocol

Run weekly from Phase 2 Day 7 onward (fits the Sunday deload flex slot):

1. **Flashcard drill** — go through deck.md; mark any term you couldn't define in 10 s as `⚠`.
2. **Explain-it-out-loud** — pick 5 random terms; speak a 2-sentence explanation aloud (English first, then Chinese if possible).
3. **Mock question** — answer one question from the bank below. Time yourself (90 s target). Record the answer in the `Attempts` column.
4. **Abstract skim** — read one paper abstract from `telecom-abstracts/` (Phase 2 parallel track); extract 3 new terms → add to deck if not already there.

---

## Question bank

### Fundamentals

| # | Question | Key points to hit | Attempts |
|---|---|---|---|
| F1 | What is OFDM and why does LTE use it instead of CDMA? | multicarrier; orthogonality; ISI resistance via CP; spectrum efficiency | |
| F2 | Explain the difference between FDD and TDD. When would you choose each? | separate vs shared spectrum; uplink/downlink symmetry; China TDD preference for 5G | |
| F3 | What is MIMO? How does it improve throughput? | spatial multiplexing; diversity; beamforming; rank; channel capacity | |
| F4 | Walk me through what happens when a phone connects to an LTE network (attach procedure). | RACH → RRC setup → NAS attach → authentication → bearer setup | |
| F5 | What is the difference between SA and NSA 5G? What are the trade-offs? | anchor; control plane; dual connectivity; deployment cost; latency | |
| F6 | Why does 5G use higher frequency bands, and what problem does that create? | capacity vs coverage trade-off; path loss; mmWave; densification | |
| F7 | What is NB-IoT? How does it differ from eMTC? | bandwidth; mobility; voice; PSM; deployment mode; use cases | |
| F8 | What is HARQ and why is it faster than traditional ARQ? | stop-and-wait vs incremental redundancy; L1 vs L2; RTT | |

### System design / scenario

| # | Question | Key points to hit | Attempts |
|---|---|---|---|
| S1 | You're designing IoT coverage for a 50-floor office building. What technology and deployment strategy would you use? | in-building; NB-IoT vs eMTC; repeaters; small cells; power budget | |
| S2 | A cell site shows high interference and poor SINR on the edge. What would you investigate? | intercell interference; ICIC; power control; antenna tilt; neighbour plan | |
| S3 | How would you test whether a new 5G NSA deployment is performing correctly? | KPIs: throughput, RSRP, SINR, handover success rate; drive test; trace analysis | |
| S4 | Our product needs sub-10 ms latency. Which 5G slice configuration would you recommend? | URLLC; MEC; QoS flow; scheduling priority | |

### Chinese-language questions (练习用)

| # | 问题 | 要点 | 尝试 |
|---|---|---|---|
| C1 | 请介绍一下5G和4G的主要区别。 | 速率、时延、连接密度；SA/NSA；毫米波 | |
| C2 | NB-IoT适合哪些应用场景？ | 低速率、低功耗、广覆盖；抄表、追踪、传感器 | |
| C3 | 你为什么对电信行业感兴趣？ | 个人背景；OFDM项目；学习路径；深圳机会 | |
| C4 | 你对华为/中兴/运营商的了解有多少？ | 国内市场；全球份额；设备/芯片/方案 | |

---

## Pitch draft (self-intro for interview)

Fill in after Phase 2 Day 35 (deck done). Target: 90 s in English + 60 s in Chinese.

**English outline:**
- Background: [math/ops background, career pivot to telecom/IoT]
- Anchor project: OFDM transceiver in Python — implemented [X, Y, Z]
- Why telecom: [Shenzhen ecosystem, 5G/IoT growth, specific company angle]
- What I bring: [signal processing fundamentals, fast learner, bilingual progress]

**Chinese draft (草稿):**
> 您好，我叫___，来自___。我的背景是___，最近一年我一直在系统学习电信技术。
> 我用Python实现了一个OFDM收发器，覆盖了___等模块。
> 我对贵公司___方向特别感兴趣，因为___。
> 我的中文现在达到HSK3水平，每天都在提高。
> 希望能有机会在深圳的团队里学习和贡献。

---

## Abstracts log

Track papers read during the abstract-skim track. One row per paper.

| Date | Title (short) | Source | New terms extracted |
|---|---|---|---|
| | | | |
