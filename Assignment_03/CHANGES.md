# Assignment 03 — CHANGES

**Name:** Kaung Myat Tun  **Student ID:** 6705140059

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Product stored as a bare tuple `("Laptop", 1200.0, "electronics")`, indexed by position (`pi[1]`, `pi[2]`) | `Product` class with `name`, `price`, `category`, plus `OrderItem` (has-a `Product` + `quantity`) | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 2 | Order stored as a raw tuple `("Alice", "gold", [(0, 1), ...])`; `calc(o)` unpacked it by index (`o[0]`, `o[1]`, `o[2]`) | `Customer` (name + `Tier`) and `Order` (has-a `Customer`, has-many `OrderItem`) | Classes / composition | PASS |
| 3 | Two separate `if t == "none": ... elif t == "silver": ...` chains — one for discount, one for points — each spelling out all four tier names | `Tier` base class with `discount(subtotal)` / `points(total)`, plus `SilverTier`, `GoldTier`, `PlatinumTier` subclasses overriding only `LOW_RATE`, `HIGH_RATE`, `POINTS_MULTIPLIER` | Polymorphism | PASS; grepped the file for `if t ==` / `elif t ==` — zero matches |
| 4 | `calc()` computed subtotal/tax/discount/points **and** called `print()` at almost every step, so you couldn't get a total without also writing to stdout | `Order.subtotal()`, `.tax()`, `.discount()`, `.total()`, `.points()` are pure (no I/O); `Order.receipt()` is the only method that builds text, from those return values | Separation of concerns (calculation vs. I/O) | PASS; also called `order.total()` directly in isolation and confirmed it returns a plain float with no printed output |
| 5 | Magic numbers scattered through `calc()`: `0.07`, `100`, `10`, `0.03`, `0.02`, `0.05`, `0.10`, `0.15`, `10` (points divisor); `global TAXRATE` declared but never reassigned | Named module constants (`TAX_RATE`, `FOOD_TAX_RATE`, `DISCOUNT_THRESHOLD`, `BULK_QTY_THRESHOLD`, `BULK_DISCOUNT_RATE`, `POINTS_DIVISOR`) or named class attributes on each `Tier`; `global` removed entirely | Encapsulation / naming | PASS; searched the file for the string `global` — no matches |
| 6 | `if cat == "food": tax = ... else: tax = ...` inside the order-total logic — totals had to know about product categories | `Product.tax_rate` looks itself up in a `CATEGORY_TAX_RATES` dict (defaulting to `TAX_RATE`); `Product.tax_on(amount)` returns the tax, and `Order`/`OrderItem` never branch on `category` | Encapsulation / polymorphic lookup (stretch F) | PASS; confirmed no `if cat` / `if category` remains outside `Product` |
| 7 | No constructor validation anywhere — a negative price or `quantity = -5` would silently produce a wrong total; nothing to look at in a debugger but `<Order object at 0x...>` | `Product`, `OrderItem`, `Customer`, `Order` constructors raise `ValueError` on invalid input; each class got a `__str__` (e.g. `Order(Alice (gold), 3 items, total=1665.6)`) | Encapsulation & validation; `__str__` (stretch B/G) | PASS; manually tried `OrderItem(product, 0)` and `Customer("Alice", "bronze")` in a REPL and confirmed both raise `ValueError` |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> Honestly the tier subclasses were the biggest win. Before, if I wanted to check gold's discount I had to scroll through two different if/elif blocks and make sure the string matched — now it's just three numbers on one class. Splitting the math out from the printing helped too, since I could actually test order.total() on its own instead of squinting at printed receipts to see if something was off.

---

## 3 · Prompt log (Level 2 — required)

| # | My prompt to the AI                                                                                                                         | What it suggested (summary)                                                                                                                                                   | Accept / reject / edited                                                   | How I checked it                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Asked AI what classes I should create to refactor the store system and how the classes should relate to each other.                         | AI suggested `Product`, `OrderItem`, `Customer`, and `Order` classes, with `OrderItem` having a `Product` and `Order` having a `Customer` and multiple `OrderItem` objects.   | Accepted the suggested class structure and implemented it in my code.      | Checked the class relationships and made sure they matched the assignment requirement for composition.                             |
| 2 | Asked AI how I could replace the customer tier `if/elif` statements with polymorphism.                                                      | AI suggested separate tier classes such as `NoneTier`, `SilverTier`, `GoldTier`, and `PlatinumTier`, where each class provides its own discount and points behaviour.         | Accepted and edited the suggested design to fit my code.                   | Checked that my `Order` class does not use `if tier == ...` for discount or points calculations.                                   |
| 3 | Asked AI how to separate the calculation logic from the receipt printing.                                                                   | AI suggested using pure methods such as `subtotal()`, `discount()`, `tax()`, `total()`, and `points()` that return values, with a separate `receipt()` method for the output. | Accepted the suggestion.                                                   | Tested the methods and checked that the calculation methods return numbers without printing anything.                              |
| 4 | Asked AI which values in the original code should be changed into named constants instead of magic numbers.                                 | AI suggested names such as `TAX_RATE`, `DISCOUNT_THRESHOLD`, `BULK_QTY_THRESHOLD`, `BULK_DISCOUNT_RATE`, and `POINTS_DIVISOR`.                                                | Accepted and edited the names where necessary.                             | Compared the constant values with the original code to make sure the calculations stayed the same.                                 |
| 5 | Asked AI how to add validation to the constructors, especially for product prices and order quantities.                                     | AI suggested checking for valid names, non-negative prices, valid quantities, and valid objects when creating orders and order items.                                         | Accepted and adjusted the validation to match the assignment requirements. | Tested valid and invalid values and checked that invalid values were rejected.                                                     |
| 6 | Asked AI for an idea for the stretch goal where each product decides its own tax instead of checking the category in the order calculation. | AI suggested using product subclasses such as `FoodProduct`, `ElectronicsProduct`, and `StationeryProduct`, each with its own tax behaviour.                                  | Accepted this suggestion and implemented the stretch goal.                 | Checked that `Order.tax()` does not need a category `if` statement and that the calculated tax still matches the legacy behaviour. |
| 7 | Asked AI to review my completed refactor and tell me if it covered the main requirements of the rubric.                                     | AI suggested checking composition, validation, polymorphism, pure calculation methods, named constants, removal of `global`, and the stretch tax requirement.                 | Used the suggestions as a checklist and edited my code where needed.       | Ran `python Assignment_03.py` and confirmed it printed `PASS - behaviour is unchanged. Your refactor is safe.`                     |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*


---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
