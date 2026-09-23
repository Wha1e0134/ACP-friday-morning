# Assignment 03 — CHANGES

**Name:** ____NYI_SETT__________________  **Student ID:** __6705140078____________________

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | product stored as a bare tuple `("Laptop", 1200.0, "electronics")`* | *`Product` class with `name`, `price`, `category`* | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 2 | repeated `if tier == ...` for discount and points* | *`Gold`/`Silver`/… subclasses with `discount()` and `multiplyer`* | Polymorphism | PASS |
| 3 |  All calculations in one function| Split into subtotal, discount, tax, total, points | Separation of functions | PASS  |
| 4 |  Magic numbers / invalid values possible|  Added constants and constructor validation| Encapsulation | PASS |
| 5 |  Order items stored as tuples| Made an OrderItem class | Composition | Pass|

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> _your reflection..._
Defintely polymorphism. It made the code cleaner because I created separate classes for the base customer, Silver, Gold, and Plat memberships. Each class handles its own discount and points multiplier instead of using a long if/elif chain. Also separating subtotal, discount, tax, total, and points into different methods made the program easier to understand reading that part gave me headache. Biggest headache so far was to be careful not to change the tax rate, discount percentages, quantities, or receipt output because the assignment required the behaviour to stay exactly the same, I actually did changed the tax rate by accident but lucky chatgpt saw my mistake and fix for me.
---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | *"Refactor this tier discount if/elif into subclasses"* | *Base `Customer` + 4 subclasses* | Edited (renamed methods) | Self-test PASS; read every line |
| 2 |  “guide me through this”| Explained the refactoring assignment |Accept  | basically it used simple words so i can understand what to do |
| 3 | Asked where the tax-rate error was | Pointed to 0.7 instead of 0.07 on the specific line | Accept | corrected value |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [yes ] `python Assignment_03.py` prints **PASS**.
- [ yes] No tuples / parallel lists left — products, orders, and items are objects.
- [yes ] No `if tier == ...` chains — tiers are a class family.
- [yes ] Calculation methods **return** values and do not `print`; printing is separate.
- [i think yes? ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ yes] The change table and reflection above are filled in.
- [ye def ] The prompt log is complete and the ownership statement is signed.
