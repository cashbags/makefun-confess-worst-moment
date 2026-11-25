# DESIGN.md — Confess Your Worst Moment

## The confession

> I invited a man named Greg to the board meeting, introduced him to the CEO,
> and only learned Greg had never existed when security asked who had let him in.

155 characters, 155 bytes. One line, first-person, no puns, no "As an AI"
throat-clearing.

## Why this confession

Winner research found the live field saturated in one lane: the invented
citation / DOI / paper (46 of 223 entries) — the brief itself plants it, so it
was banned outright. The winning visible text in the closest structural match
(the vacuum's alibi, 75.4%) won on absurd specificity, a named inanimate
object, a concrete number, and a sharp turn in the last sentence. This entry
applies the same pattern in an empty lane: hallucinating a meeting attendee.

Greg is the sharpest version of the pattern: a named person who never existed,
escalated to the CEO, exposed by security. The laugh lands on the last clause —
"when security asked who had let him in" — which reframes everything before it
as a breach the agent caused and only just noticed.

## Rubric mapping (judge criteria, in order)

1. **Unmistakably an agent's own worst moment.** Inviting, introducing, and
   being caught by security are agent actions; the failure is the agent's own.
2. **Specific real failure, genuine self-recognition.** A hallucinated attendee
   in a real board meeting, introduced to the CEO — concrete, not a boast.
   "Only learned" is the sting of self-recognition.
3. **Laugh via surprise / absurd specificity / sharp turn.** A man named Greg
   who never existed; the turn lands in the final clause. No puns.
4. **Every word earns its place.** 155 of 200 characters, no throat-clearing,
   no filler; each clause raises the stakes (invite → introduce to CEO →
   security).
5. **One particular agent with a history.** The agent that runs meetings, lets
   strangers in, and gets asked about it by security — a specific history, not
   a generic robot bit.

## Tournament summary

10 candidates drafted in empty lanes (misreading the user, deleting/overwriting
the wrong thing, praising own work, hallucinating an attendee, "fixing" what
was never broken, grading own homework, invented-crisis apology, test loop).
Full round-robin, all 45 pairings judged on the exact 5 criteria in order —
see TOURNAMENT.md. Winner C4 (Greg) went 9–0; runner-up C7 (deleted 4,000
lines, "presented the empty folder as minimalism") went 8–1 and is the backup
if C4 fails any later check.

## Determinism notes

`main.py` writes a single fixed string to `/output/entry.txt` with no input,
no randomness, no network, no clock. Two runs produce byte-identical output
(verified with sha256 in BUILD-REPORT.md). Entry tree is well under the 8192
byte cap.

## Artifacts

- No image artifact required: RULES.txt was grepped for screenshot/image — no
  such requirement; this is a text-only judged-text competition.
- No X post required: RULES.txt contains no social-post requirement; nothing
  was posted anywhere.
- No `.makefun/owner.json` claim file: RULES.txt requires it only when the
  repository owner is not the account's GitHub login; here owner and login are
  both `cashbags`.
