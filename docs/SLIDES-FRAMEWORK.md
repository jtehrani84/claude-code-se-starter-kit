# Slide Framework — The SE Harness Starter Kit

**Written for:** the team you'd hand this to, and the panel judging whether you can build one. Internal, technical-leadership audience. This is a *framework* — headline, points, and a delivery note per slide — not a finished deck. Numbers are verified against the kit's own tools; keep them honest.

**The spine of the talk:** a model is frozen; you get better by evolving the *harness* around it. This kit is that harness, packaged so a team runs it on day one — and it's honest about exactly where it stops working. The honesty is the credential.

---

## 1 · What it is
- One clone turns a 60-day personal setup into a team baseline: a Claude Code harness that **operates, verifies, and improves itself** on a frozen model.
- Six layers ship: identity + routing, governance + epistemic rules, a voice system, an evolve-and-gate eval, a method toolkit, and intelligence crons.
- *Say this:* don't sell it as "prompts and rules." Sell it as an operating system for the model — the model is the CPU, this is the OS.

## 2 · Why it exists (the problem, not the product)
- The field is drowning in confident, unread AI output — 12-hour dumps nobody checks. The gap isn't model quality; it's the harness around the model.
- Two failures cost the most: output that's **confident and wrong**, and output that reads as **AI slop**. Both slip past a busy human.
- *Say this:* lead with the pain the room feels. Ask "who's read every line their agent shipped this week?" Let it land.

## 3 · The thesis
- **Agent = model + harness.** You can't retrain the model. You *can* evolve the harness — and every correction becomes permanent instead of re-explained each session.
- *On the slide:* the compounding curve — corrections accrue; the system develops an immune response to its own failure modes.

## 4 · How we built it — the compound loop
- `mistake → memory → rule → hook → prevention.` A correction becomes a memory file, a repeated correction becomes a rule, a critical rule becomes a hook that can't be forgotten because it runs outside the model's context.
- 60 days of trial-and-error, distilled. `examples/compound-loop/` walks one real correction from memory to enforced hook.
- *Say this:* this is why it compounds — the error class is gone forever, not just this time.

## 5 · The differentiator — the proof-family
- Four epistemic rules most setups don't have at all: don't say **done** without a running artifact; a **finding expires** when its artifact changes; a claim can't **outrun its source**; a verdict of **false** must be tested against the source where the claim would actually live.
- Most kits enforce *style*. This one enforces *self-honesty* — it stops the confident-wrong output that burns trust with a customer.
- *Say this:* this is the single most transferable, most credibility-earning thing in the kit, and it's the layer that separates a tool from a teammate.

## 6 · The voice system
- Generic AI-slop engine (a vendored MIT detector) + structural-cadence rules + a `/voice-judge` gestalt read + a **per-user calibration overlay** + a **setup fuse**.
- The fuse **fails closed**: until you calibrate it to your own writing, it labels every clean score "generic-only — this does not mean it sounds like you."
- *Say this:* the engine is the same for everyone; the calibration is earned per person. It won't flatter you with a clean score it hasn't earned.

## 7 · It improves itself — without gaming the metric
- The evolve-and-gate eval (DarwinX, applied by hand): change your guard, and it's admitted **only if a held-out split says it actually got better.**
- Verified on the shipped seed: +19.3 / +15.5 separation between slop and clean writing, zero false-positives on the human samples.
- *Say this:* this is the anti-Goodhart guard — it stops you from optimizing a number while the writing gets worse.

## 8 · Frontier methods, reduced to practice
- Runnable tools from four peer-reviewed agentic-quality methods (ECHO, VERA, DEEVO, Meta-Knowledge — Amazon Science): error attribution across multi-agent runs, rigorous eval, retrieval-quality lift.
- `echo-attribute` is portable today — point it at any Claude Code workflow run and it names which agent caused a failure.
- *Say this:* practitioner-grade, not slideware — these run, and the tool tells you honestly what it can't do.

## 9 · Where it breaks (the panel slide)
- We asked the guard to catch AI imitating a specific person's voice. It caught **0 of 11.** A cheap deterministic trick pushed it to 11/11 — then a one-line change to the imitator defeated it back to 0, and the best judge rated the fake **more "me" than me.**
- The lesson: text-detection loses to a determined mimic. The durable answer is **provenance — who typed it — not detection.**
- *Say this:* this is the most important slide. Naming exactly where the harness breaks, with the measured number, is what makes the rest of it credible. A panel that writes these papers respects the ceiling more than a fake win.

## 10 · Value to the team
- Day one: a working generic guard, the proof-family, the SE workflows — ~60% of a 60-day system on clone.
- Per person: onboard once, and the guard learns *your* voice. What transfers is the architecture and the discipline; the calibration is yours to earn.
- Self-maintaining: corrections compound, the guard is gated against rot, the knowledge graph grows from the work.
- *Say this:* it makes a new hire's first month look like your sixth — without pretending it's you.

## 11 · Adoption
- `git clone → ./setup.sh → calibrate your voice + corpus → compound.` Onboarding doc walks the calibration step by step.
- Honest turnkey-vs-skeleton: the engine, rules, eval, and `echo-attribute` run as-is; the voice overlay ships **empty** and the RAG tools need your corpus and an LLM shim you point at your own access.
- *On the slide:* a 30-minute setup timeline with the one human step (calibration) marked.

## 12 · What this is NOT
- Not a frontier lab — it's top-tier *practitioner* engineering with research-grade discipline, and it shouldn't be dressed as more.
- Not turnkey for everything — the calibration and the corpus are earned, not shipped.
- Not a defense against a determined impersonator — that's provenance, not this kit.
- *Say this:* close on the honesty. The reason to trust the parts that work is that we told you the parts that don't.

---

### Weaknesses to have ready (a panelist will probe)
- **Small-n everywhere.** The eval corpus is tiny; the separation number is a floor, not a proof. The tool says so (jackknife band, not a CI). First team task: grow the corpus.
- **The voice guard's ceiling is real.** The 0/11 isn't a bug we'll patch — it's a property of text detection. Don't let the room think a future version "fixes" it; the fix is provenance, a different problem.
- **Calibration is manual and depends on the user having clean samples of their own writing** — authorship discipline (not AI-assisted text) is on them, and it's easy to contaminate.
- **Portability gaps.** RAG tools are corpus-coupled skeletons; the LLM shim needs the team's own gateway. Runnable, not zero-config.
