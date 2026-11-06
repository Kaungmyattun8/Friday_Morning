{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell01"
      },
      "source": [
        "# Week 5 Lab — OOP Design & Refactoring, with AI\n",
        "\n",
        "**192-201 Advanced Computer Programming with Generative AI**\n",
        "\n",
        "Reference: *Think Python, 3rd Edition* — Chapter 14 (pure functions & modifiers) + Chapter 16 (composition) + lecturer supplement on AI-assisted refactoring.\n",
        "Builds on **Weeks 2–4** (classes, encapsulation, inheritance & polymorphism).\n",
        "\n",
        "---\n",
        "\n",
        "### About this lab\n",
        "\n",
        "This is a **guided practice notebook** — it is **not graded**. It follows the **five ideas** from today's slides. Each part is tagged with the slide concept it practises:\n",
        "\n",
        "\u003E **① Refactoring · ② Composition (has-a) · ③ Pure vs modifier · ④ Interface vs implementation · ⑤ AI-assisted refactoring (Level 2)**\n",
        "\n",
        "The rhythm this week is **design → build → verify**, not “type along.” You take code that already works and make it *better*, proving at each step that the behaviour is unchanged.\n",
        "\n",
        "\u003E **Run a cell:** click it, then press **Shift + Enter**.\n",
        "\n",
        "\u003E **AI-use policy — Level 2 this week:** AI may *suggest* cleaner code, but you must **verify every change** and **log every prompt** (Part 7). Never accept a suggestion you haven't checked."
      ],
      "id": "cell01"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell02"
      },
      "source": [
        "## Part 0 — The starting point: working, but ugly\n",
        "\n",
        "Here is a `Rectangle` class that **works** but is hard to read: cryptic names, and the corner is stored as two loose numbers. Run it and note the output — this is the **behaviour we must preserve** while we improve the code."
      ],
      "id": "cell02"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell03"
      },
      "outputs": [],
      "source": [
        "class Rect:\n",
        "    def __init__(self, x, y, w, h):\n",
        "        self.x = x     # corner x\n",
        "        self.y = y     # corner y\n",
        "        self.w = w     # width\n",
        "        self.h = h     # height\n",
        "    def area(self):\n",
        "        return self.w * self.h\n",
        "    def describe(self):\n",
        "        return 'Rect ' + str(self.w) + 'x' + str(self.h) + ' at (' + str(self.x) + ', ' + str(self.y) + ')'\n",
        "\n",
        "r = Rect(30, 20, 4, 5)\n",
        "print(r.area())        # 20\n",
        "print(r.describe())    # Rect 4x5 at (30, 20)"
      ],
      "id": "cell03"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell04"
      },
      "source": [
        "\u003E **Write down the current behaviour** (your safety net): `area()` returns `20`, and `describe()` returns `Rect 4x5 at (30, 20)`. Every refactor below must keep these two results identical."
      ],
      "id": "cell04"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell05"
      },
      "source": [
        "## Part 1 — Refactor #1: clearer names  ·  ① Refactoring\n",
        "\n",
        "\u003E **From the slides — Concept 1 (Refactoring):** *improve the code without changing its behaviour.*\n",
        "\n",
        "Cryptic `w`/`h`/`x`/`y` make the class hard to read. Rename them to `width`, `height`, `corner_x`, `corner_y`. This is a pure refactor: the results must not change."
      ],
      "id": "cell05"
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "cell06",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "executionInfo": {
          "status": "ok",
          "timestamp": 1789658184602,
          "user_tz": -420,
          "elapsed": 33,
          "user": {
            "displayName": "Hrang Kap Lian",
            "userId": "10580178071233366516"
          }
        },
        "outputId": "ec0c9f9c-30eb-43e1-aed2-efc7c9b9e039"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n",
            "Rect 4x5 at (30, 20)\n"
          ]
        }
      ],
      "source": [
        "class Rectangle:\n",
        "    def __init__(self, corner_x, corner_y, width, height):\n",
        "        self.corner_x = corner_x\n",
        "        self.corner_y = corner_y\n",
        "        self.width = width\n",
        "        self.height = height\n",
        "    def area(self):\n",
        "        return self.width * self.height\n",
        "    def describe(self):\n",
        "        return f'Rect {self.width}x{self.height} at ({self.corner_x}, {self.corner_y})'\n",
        "\n",
        "r = Rectangle(30, 20, 4, 5)\n",
        "print(r.area())        # 20         \u003C- SAME as before\n",
        "print(r.describe())    # Rect 4x5 at (30, 20)   \u003C- SAME as before"
      ],
      "id": "cell06"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell07"
      },
      "source": [
        "\u003E Notice we also replaced the clumsy string `+` concatenation in `describe()` with a clean **f-string** — that too is a refactor. The two printed results are **identical** to Part 0, so behaviour is preserved.\n",
        "\n",
        "**Your turn.** Verify it yourself: write two `assert` checks that fail loudly if the behaviour ever changes. (Run it — no output means both passed.)"
      ],
      "id": "cell07"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell08"
      },
      "outputs": [],
      "source": [
        "r = Rectangle(30, 20, 4, 5)\n",
        "assert r.area() == 20\n",
        "assert r.describe() == 'Rect 4x5 at (30, 20)'\n",
        "print('behaviour unchanged ✓')"
      ],
      "id": "cell08"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell09"
      },
      "source": [
        "## Part 2 — Refactor #2: composition  ·  ② Composition (has-a)\n",
        "\n",
        "\u003E **From the slides — Concept 2 (Composition):** *build an object out of other objects — a Rectangle has-a Point.*\n",
        "\n",
        "Two loose numbers `corner_x`, `corner_y` really represent **one thing**: a corner point. Let's give the rectangle a `Point` object instead (Ch. 16's design). Run this:"
      ],
      "id": "cell09"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell10"
      },
      "outputs": [],
      "source": [
        "class Point:\n",
        "    def __init__(self, x, y):\n",
        "        self.x = x\n",
        "        self.y = y\n",
        "\n",
        "class Rectangle:\n",
        "    def __init__(self, corner, width, height):\n",
        "        self.corner = corner       # a Point object (has-a)\n",
        "        self.width = width\n",
        "        self.height = height\n",
        "    def area(self):\n",
        "        return self.width * self.height\n",
        "    def describe(self):\n",
        "        return f'Rect {self.width}x{self.height} at ({self.corner.x}, {self.corner.y})'\n",
        "\n",
        "r = Rectangle(Point(30, 20), 4, 5)\n",
        "print(r.area())        # 20\n",
        "print(r.describe())    # Rect 4x5 at (30, 20)   \u003C- STILL the same"
      ],
      "id": "cell10"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell11"
      },
      "source": [
        "\u003E The corner is now a proper `Point` object — `r.corner` **has-a** point, and we read its data with `r.corner.x`. The behaviour (both printed lines) is *still* identical. That's a successful composition refactor.\n",
        "\n",
        "**Your turn.** Prove the corner is really a `Point`: print `type(r.corner)` and print `r.corner.x` and `r.corner.y`."
      ],
      "id": "cell11"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell12"
      },
      "outputs": [],
      "source": [
        "# Your code here:\n",
        "print(type(r.corner))\n",
        "print(r.corner.x)\n",
        "print(r.corner.y)"
      ],
      "id": "cell12"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell13"
      },
      "source": [
        "## Part 3 — Two ways to move a rectangle  ·  ③ Pure vs modifier\n",
        "\n",
        "\u003E **From the slides — Concept 3 (Pure vs modifier):** *a pure function returns a new object; a modifier changes the object in place.*\n",
        "\n",
        "We'll add movement two ways so the difference is concrete. Run this:"
      ],
      "id": "cell13"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell14"
      },
      "outputs": [],
      "source": [
        "class Point:\n",
        "    def __init__(self, x, y):\n",
        "        self.x = x\n",
        "        self.y = y\n",
        "    def __str__(self):\n",
        "        return f'({self.x}, {self.y})'\n",
        "\n",
        "    # MODIFIER: changes THIS point in place, returns nothing\n",
        "    def move(self, dx, dy):\n",
        "        self.x += dx\n",
        "        self.y += dy\n",
        "\n",
        "    # PURE: leaves this point alone, returns a NEW point\n",
        "    def moved(self, dx, dy):\n",
        "        return Point(self.x + dx, self.y + dy)\n",
        "\n",
        "p = Point(0, 0)\n",
        "q = p.moved(10, 10)      # pure: p unchanged, q is new\n",
        "print(p, q)              # (0, 0) (10, 10)\n",
        "\n",
        "p.move(5, 5)             # modifier: p itself changes\n",
        "print(p)                 # (5, 5)"
      ],
      "id": "cell14"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell15"
      },
      "source": [
        "\u003E `moved()` is **pure** — after `q = p.moved(10,10)`, `p` is still `(0, 0)`. `move()` is a **modifier** — it changes `p` directly. Same idea, opposite effect on the original.\n",
        "\n",
        "**Your turn.** Predict *then* verify: after the code above runs, what is `p`? Write one line that prints `p` and add a comment with your prediction before running."
      ],
      "id": "cell15"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell16"
      },
      "outputs": [],
      "source": [
        "# Your prediction: p == (5, 5)\n",
        "# Your code here:\n",
        "print(p)"
      ],
      "id": "cell16"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell17"
      },
      "source": [
        "## Part 4 — Change the inside, keep the outside  ·  ④ Interface vs implementation\n",
        "\n",
        "\u003E **From the slides — Concept 4 (Interface vs implementation):** *keep how an object is used separate from how it works inside.*\n",
        "\n",
        "The **interface** of `area()` is “call `r.area()`, get the area.” We can change the **implementation** and, as long as the interface still holds, nothing else breaks. Run this alternative `area()`:"
      ],
      "id": "cell17"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell18"
      },
      "outputs": [],
      "source": [
        "class Rectangle:\n",
        "    def __init__(self, corner, width, height):\n",
        "        self.corner = corner\n",
        "        self.width = width\n",
        "        self.height = height\n",
        "    def area(self):\n",
        "        # NEW implementation: add width to itself height-times.\n",
        "        # (Deliberately different inside - same result outside.)\n",
        "        total = 0\n",
        "        for _ in range(self.height):\n",
        "            total += self.width\n",
        "        return total\n",
        "\n",
        "r = Rectangle(Point(30, 20), 4, 5)\n",
        "print(r.area())        # 20   \u003C- interface unchanged, result unchanged"
      ],
      "id": "cell18"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell19"
      },
      "source": [
        "\u003E The insides of `area()` are completely different (a loop instead of `*`), but the **interface** — `r.area()` returning `20` — is exactly the same. Callers never notice. That freedom is what makes refactoring safe.\n",
        "\n",
        "**Your turn.** In one sentence (edit this cell), explain why code elsewhere that calls `r.area()` did **not** need to change when we rewrote the inside.\n",
        "\n",
        "*Your answer:* Code calling `r.area()` only relies on its external behavior (what it returns), not its internal implementation, so changes inside the method do not affect external callers."
      ],
      "id": "cell19"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell20"
      },
      "source": [
        "## Part 5 — AI-assisted refactor, verified  ·  ⑤ AI-assisted refactoring (Level 2)\n",
        "\n",
        "\u003E **From the slides — Concept 5 (the Level-2 loop):** **Capture → Ask AI → Verify → Accept/reject**, and **log the prompt**.\n",
        "\n",
        "Here is a messy function that works. Follow the four-step loop to refactor it **with AI help** — then verify."
      ],
      "id": "cell20"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell21"
      },
      "outputs": [],
      "source": [
        "# CAPTURE: the working code and its current output\n",
        "def process(nums):\n",
        "    r = []\n",
        "    for i in range(len(nums)):\n",
        "        r.append(nums[i] * nums[i])\n",
        "    out = []\n",
        "    for i in range(len(r)):\n",
        "        if r[i] % 2 == 0:\n",
        "            out.append(r[i])\n",
        "    return out\n",
        "\n",
        "print(process([1, 2, 3, 4, 5, 6]))   # [4, 16, 36]  \u003C- the behaviour to preserve"
      ],
      "id": "cell21"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell22"
      },
      "source": [
        "**The loop, step by step:**\n",
        "\n",
        "1. **Capture** — done above: `process([1,2,3,4,5,6])` returns `[4, 16, 36]`.\n",
        "2. **Ask AI** — ask your assistant something like: *\"Refactor this to be more readable using list comprehensions, without changing its behaviour.\"* **Record the exact prompt in Part 7.**\n",
        "3. **Verify** — paste the AI's version into the cell below and run the check. It must still return `[4, 16, 36]`.\n",
        "4. **Accept / reject** — keep it **only** if the check passes.\n",
        "\n",
        "**Your turn.** Put your AI-assisted refactor of `process` in the cell below. The `assert` is your verify step — if it passes, the refactor is safe to accept."
      ],
      "id": "cell22"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell23"
      },
      "outputs": [],
      "source": [
        "# Paste your AI-refactored version here, then run to VERIFY:\n",
        "def process(nums):\n",
        "    # TODO: your cleaner version (e.g. using list comprehensions)\n",
        "    squared_evens = [n*n for n in nums if (n*n) % 2 == 0]\n",
        "    return squared_evens\n",
        "\n",
        "# VERIFY - behaviour must be unchanged:\n",
        "assert process([1, 2, 3, 4, 5, 6]) == [4, 16, 36]\n",
        "assert process([]) == []\n",
        "print('verified - safe to accept ✓')"
      ],
      "id": "cell23"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell24"
      },
      "source": [
        "\u003E A model refactor is `[n*n for n in nums if (n*n) % 2 == 0]` — but **only accept it after your own `assert` passes.** That is the whole discipline of Level 2."
      ],
      "id": "cell24"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell25"
      },
      "source": [
        "## Part 6 — Guided build: refactor the Part 0 class end-to-end  ·  ① ② ④\n",
        "\n",
        "Bring it together. Starting from the ugly `Rect` in **Part 0**, produce a clean `Rectangle` that:\n",
        "1. uses **clear names** (① refactoring),\n",
        "2. stores its corner as a **Point** (② composition),\n",
        "3. keeps the **same interface**: `area()` and `describe()` return exactly what Part 0 returned (④).\n",
        "\n",
        "Fill in the `# TODO`s, then run the verify cell."
      ],
      "id": "cell25"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cell26"
      },
      "outputs": [],
      "source": [
        "class Point:\n",
        "    def __init__(self, x, y):\n",
        "        self.x = x\n",
        "        self.y = y\n",
        "\n",
        "class Rectangle:\n",
        "    def __init__(self, corner, width, height):\n",
        "        # TODO: store corner (a Point), width, height\n",
        "        self.corner = corner\n",
        "        self.width = width\n",
        "        self.height = height\n",
        "    def area(self):\n",
        "        # TODO: return width * height\n",
        "        return self.width * self.height\n",
        "    def describe(self):\n",
        "        # TODO: return f'Rect {width}x{height} at ({corner.x}, {corner.y})'\n",
        "        return f'Rect {self.width}x{self.height} at ({self.corner.x}, {self.corner.y})'\n",
        "\n",
        "# VERIFY against Part 0's behaviour:\n",
        "r = Rectangle(Point(30, 20), 4, 5)\n",
        "assert r.area() == 20\n",
        "assert r.describe() == 'Rect 4x5 at (30, 20)'\n",
        "print('refactor complete, behaviour identical ✓')"
      ],
      "id": "cell26"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell27"
      },
      "source": [
        "**The loop, step by step:**\n",
        "\n",
        "1. **Capture** — done above: `process([1,2,3,4,5,6])` returns `[4, 16, 36]`.\n",
        "2. **Ask AI** — ask your assistant something like: *\"Refactor this to be more readable using list comprehensions, without changing its behaviour.\"* **Record the exact prompt in Part 7.**\n",
        "3. **Verify** — paste the AI's version into the cell below and run the check. It must still return `[4, 16, 36]`.\n",
        "4. **Accept / reject** — keep it **only** if the check passes.\n",
        "\n",
        "| # | The prompt I gave the AI | What it suggested | How I verified behaviour was unchanged | Accepted? |\n",
        "|---|---|---|---|---|\n",
        "| 1 | \"Refactor this to be more readable using list comprehensions, without changing its behaviour.\" | A one-line list comprehension: `[n*n for n in nums if (n*n) % 2 == 0]` | `assert process([1, 2, 3, 4, 5, 6]) == [4, 16, 36]` and `assert process([]) == []` passed. | Yes |\n",
        "| 2 | | | | |\n",
        "| 3 | | | | |"
      ],
      "id": "cell27"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell28"
      },
      "source": [
        "## Part 8 — Working with AI this week (Level 2)\n",
        "\n",
        "Level 2 means **AI-assisted, but verified and logged**. Good moves:\n",
        "\n",
        "- Ask: *\"Suggest a cleaner version of this method without changing its behaviour.\"*\n",
        "- Ask: *\"Is this refactor equivalent to the original? What edge cases might differ?\"*\n",
        "- Then **run your own tests** before accepting anything.\n",
        "\n",
        "**Not allowed:** accepting an AI rewrite you haven't verified, or leaving the prompt log empty. If a suggestion changes the behaviour, **reject it** — a faster-but-wrong function is still wrong."
      ],
      "id": "cell28"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cell29"
      },
      "source": [
        "## Before you finish — quick checklist\n",
        "\n",
        "You should now be able to — and be able to **name** each idea:\n",
        "\n",
        "- [ ] **① Refactoring** — improve code while keeping identical behaviour\n",
        "- [ ] **② Composition** — give an object another object as an attribute (has-a)\n",
        "- [ ] **③ Pure vs modifier** — know whether a method returns new data or changes the object\n",
        "- [ ] **④ Interface vs implementation** — change the inside without breaking the outside\n",
        "- [ ] **⑤ Level-2 loop** — capture, ask AI, verify, accept/reject — with a prompt log"
      ],
      "id": "cell29"
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.x"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}