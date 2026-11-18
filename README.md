# SpamFilter
## MCCTC | 145130 Applications of AI
### Assignment 3: Build a Spam Filter With Rules

This repository contains the completed code, test files, and written analysis for **Assignment 3: Build a Spam Filter With Rules**.

---

### Contents
- [`week01/assignment3.md`](./week01/assignment3.md) — Complete assignment submission with all questions, tables, and reflections.
- [`week01/assignment3.html`](./week01/assignment3.html) — Printable / styled HTML report with screenshots.
- [`spam_rules.py`](./spam_rules.py) (and inside [`week01/`](./week01/spam_rules.py)) — Rule-based spam filter implementation (`is_spam`).
- [`check_rules.py`](./check_rules.py) (and inside [`week01/`](./week01/check_rules.py)) — Automated rule checker and scoring tool.
- [`messages.csv`](./messages.csv) — 40 labeled benchmark messages (25 normal, 15 spam).
- [`tricky_messages.csv`](./tricky_messages.csv) — 10 adversarial edge-case messages for Part 2.
- [`week01/screenshot1_check_rules.png`](./week01/screenshot1_check_rules.png) — Terminal screenshot showing 40 out of 40 score.
- [`week01/screenshot2_check_rules_tricky.png`](./week01/screenshot2_check_rules_tricky.png) — Terminal screenshot showing tricky test execution.

---

### Running the Checker
Test your rules on the benchmark messages:
```bash
python check_rules.py
```
*Result: **Right: 40 out of 40** (0 Missed Spam, 0 False Alarms)*

Test your rules on the tricky messages:
```bash
python check_rules.py tricky
```
*Result: **Right: 3 out of 10** (Illustrating the breakdown of rule-based systems on edge cases)*
