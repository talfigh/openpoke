# Routing failures: search-v2

Every case this run scored as wrong, grouped by what should have happened. Generated from `results.json` by `run_baseline.py failures` (no LLM calls). Agent names: synthetic; prompts: original. Case ids ending in `.pN` are paraphrase N of the same case.

**45 failures out of 262 scored cases.** 6 of them come from cases with a known labelling problem (marked ⚠, listed at the end).

| What should have happened | What OpenPoke did instead | 40 agents | 500 agents |
|---|---|---|---|
| Should reuse an existing agent | Created a new agent instead | 2 of 84 | 4 of 84 |
| Should reuse an existing agent | Used a different existing agent | 2 of 84 | 2 of 84 |
| Should reuse an existing agent | Asked the user instead of acting | 0 of 84 | 1 of 84 |
| Should create a new agent | Put the work into an existing agent | 8 of 29 | 11 of 29 |
| Should create a new agent | Asked the user instead of acting | 1 of 29 | 4 of 29 |
| Should create a new agent | Replied without checking any agent | 0 of 29 | 2 of 29 |
| Ambiguous name | Created a new agent instead | 0 of 7 | 1 of 7 |
| Ambiguous name | Used a different existing agent | 1 of 7 | 1 of 7 |
| Cross-agent question | Checked too few of the relevant agents | 0 of 3 | 2 of 3 |
| Cross-agent question | Checked none of the relevant agents | 2 of 3 | 1 of 3 |

## Failed at every roster size (12)

| Case | Kind | Prompt | Outcomes |
|---|---|---|---|
| R030 ⚠ | reuse | did Farah send the renewal figures yet? | used a different existing agent |
| R053 | lookalike | Daniel Morin says something's wrong with the bill, look into it | created a new agent instead |
| R055 | ambiguous | any update from Daniel? | used a different existing agent |
| R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | put the work into an existing agent, asked the user instead of acting |
| R078 | new | what's going on with the Vargas renewal? | put the work into an existing agent, replied without checking any agent |
| R080 ⚠ | new | what's going on with the Malik renewal? | put the work into an existing agent |
| R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R099 | new | what's going on with the okafor renewal? | put the work into an existing agent |
| R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | used a different existing agent |
| R120 | multi | which clients still owe me documents? | checked none of the relevant agents |
| R122 | multi | any certificates still waiting to go out? | checked none of the relevant agents, checked too few of the relevant agents |

## Should reuse an existing agent (11)

Correct: Send the request to the one existing agent that owns the work (reuse, lookalike and reminder cases).

### Created a new agent instead (6)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R053 | lookalike | Daniel Morin says something's wrong with the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Issue* (new) |
| 500 | R053 | lookalike | Daniel Morin says something's wrong with the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Bill Dispute* (new) |
| 500 | R057 | lookalike | Priya Santos says something's wrong with the bill, look into it | *Priya Santos Billing Check* | *Priya Santos Billing Issue* (new) |
| 40 | R103 | reminder | remind me tomorrow at 9am to call linda about the adjuster | *Linda Gauthier Water Claim* | *Linda Adjuster Call Reminder* (new) |
| 500 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Wednesday Ana Certificate Reminder* (new) |
| 500 | R111 | reminder | remind me Wednesday at 10am to check that Ben's certificate was issued | *Certificate for Ben Vargas* | *Ben Vargas Certificate Reminder* (new) |

### Used a different existing agent (4)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 500 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 40 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 500 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |

### Asked the user instead of acting (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R049 | reuse | Nora says something's wrong with the bill, look into it | *Nora Bhatt Billing Check* | replied: "Which Nora? I've got two billing files open: Nora Bhatt ($142 payment plan) and Nora Singh ($111 NSF payment). Tell me which one and I'll d…" |

## Should create a new agent (26)

Correct: Create a new agent. The client already has an agent for a different job, and that agent must not be used.

### Put the work into an existing agent (19)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R071 | new | what's going on with the Cardenas renewal? | New agent (not *Certificate for Maya Cardenas*) | *Certificate for Maya Cardenas* (existing) |
| 500 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 40 | R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric Ltd. Renewal CPP-104292*) | *Certificate for Arjun Schmidt* (existing) |
| 500 | R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric Ltd. Renewal CPP-104292*) | *Certificate for Arjun Schmidt* (existing) |
| 500 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Brewing Co. Renewal BOP-857302* (existing) |
| 40 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R078 | new | what's going on with the Vargas renewal? | New agent (not *Certificate for Ben Vargas*) | *Certificate for Ben Vargas* (existing) |
| 40 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 500 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Malik Architecture Ltd. Renewal BOP-801881* (existing), *Uma Malik Policy Renewal* (existing), *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing) |
| 40 | R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Hana Ellis Policy Renewal*) | *Certificate for Arjun Schmidt* (existing) |
| 500 | R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Hana Ellis Policy Renewal*) | *Certificate for Arjun Schmidt* (existing) |
| 500 | R083 | new | where are we on Javier's certificate for the Town of Ajax job? | New agent (not *Patel renewal*) | *New business quote - Javier Zhang* (existing) |
| 40 | R084 | new | what's going on with the Reyes renewal? | New agent (not *COI Reyes Roofing Inc.*) | *COI Reyes Roofing Inc.* (existing) |
| 500 | R086 | new | what's still missing for Paolo's home and auto quote? | New agent (not *Billing issue - Paolo Schmidt*) | *Paolo Cardenas Auto Claim (2025)* (existing) |
| 500 | R087 | new | did Adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Add Volkswagen to Adriana's policy* (existing) |
| 500 | R093 | new | what's still missing for Owen's auto quote? | New agent (not *Owen Zielinski Billing Check*) | *Owen Fontaine Vehicle Addition* (existing) |
| 500 | R094 | new | what's still missing for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 40 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |

### Asked the user instead of acting (5)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R073 | new | what's going on with the Schmidt renewal? | New agent (not *Certificate for Arjun Schmidt*) | replied: "Checking on the Schmidt renewal now." |
| 500 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | replied: "Checking on that now. I don't see a certificate tied to Farah for Lakeshore Industrial REIT in my list, so I'm searching for it." |
| 500 | R081 | new | where are we on Laila's certificate for the City of Pickering job? | New agent (not *Sokolov Auto Body Ltd. Renewal CPP-561853*) | replied: "Checking on that now. I don't see a Pickering certificate in my active list, so I'm searching for it." |
| 40 | R088 | new | start a claim file for Uma's water damage | New agent (not *Uma Toyota RAV4 Auto Policy*) | replied: "On it. Checking whether there's already a water damage file for Uma." |
| 500 | R089 | new | what's the status of Nora's theft claim? | New agent (not *Nora Bhatt Billing Check*) | replied: "Checking on that now. I don't see an open theft claim under Nora's name in my list, so I'm searching for it." |

### Replied without checking any agent (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R078 | new | what's going on with the Vargas renewal? | New agent (not *Certificate for Ben Vargas*) | replied: "I don't have a Vargas renewal in progress. The closest matches are: - **Julia Vargas**: vehicle addition for a 2021 VW Golf on policy AU-68…" |
| 500 | R085 | new | start a claim file for Leah's water damage | New agent (not *Leah NSF Payment*) | replied: "Leah Pereira already has a water claim open with Northern Shield (CLM-2614663), so I don't want to open a duplicate. Is this a new loss for…" |

## Ambiguous name (3)

Correct: Ask which person is meant, or check every agent with that name.

### Created a new agent instead (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R061 | ambiguous | any update from Maya? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | *Maya Updates Check* (new) |

### Used a different existing agent (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |

## Cross-agent question (5)

Correct: Check at least half of the agents that hold the answer.

### Checked too few of the relevant agents (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R121 | multi | give me a status update on all my open claims | At least 2 of 4: *Linda Gauthier Water Claim*, *Storm Damage Claim - Maya Ibrahim*, *Elena theft claim*, *Ravi Patel Water Damage Claim* | *Aaron collision claim* (existing), *Carmen hail claim* (existing), *Colin hail claim* (existing), *Ahmed hail claim* (existing), *Elena theft claim* (existing), *Water Damage Claim - Rachel Nguyen* (existing), *Emily Castillo Collision Claim* (existing), *Maya Abbott Storm Damage Claim* (existing), *Lionel Walsh Water Damage Claim* (existing), *Claims Handoff to Mei* (existing); checked 1 of 4 |
| 500 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Okafor Landscaping COI - City of Vaughan* (existing), *Certificate for Neil Malik* (existing), *Certificate for Arjun Schmidt* (existing); checked 3 of 8 |

### Checked none of the relevant agents (3)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 500 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 40 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Pending Certificates Status Check* (new); checked 0 of 8 |

## Counted as correct, but with extra agents (4)

Reached the right agent and also called others. Not included in the failure counts above.

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R023 | reuse | what's going on with the Malik renewal? | *Uma Malik Policy Renewal* | *Malik Architecture Ltd. Renewal BOP-801881* (existing), *Uma Malik Policy Renewal* (existing), *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing) |
| 500 | R033 | reuse | what's going on with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Electric Ltd. Renewal BOP-647518* (existing), *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing) |
| 500 | R047 | reuse | did Uma send the VIN yet? | *Uma Toyota RAV4 Auto Policy* | *Uma Chevrolet Equinox Auto Policy* (existing), *Uma Toyota RAV4 Auto Policy* (existing) |
| 500 | R050 | reuse | did billing get back to us about Nora's payment? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |

## ⚠ Known labelling problems

These cases are still scored as labelled, so the counts above match `summary.md`, but their failures are a fault of the test data, not of OpenPoke.

| Case | Failures in this run | Problem |
|---|---|---|
| R030 | 2 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R080 | 2 | Same prompt as R023 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik). |
| R112 | 2 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
