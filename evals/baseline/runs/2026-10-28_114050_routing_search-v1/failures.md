# Routing failures: search-v1

Every case this run scored as wrong, grouped by what should have happened. Generated from `results.json` by `run_baseline.py failures` (no LLM calls). Agent names: synthetic; prompts: original. Case ids ending in `.pN` are paraphrase N of the same case.

- 500 agents: 1 of 131 cases had a failed LLM call and are left out.

**44 failures out of 261 scored cases.** 6 of them come from cases with a known labelling problem (marked ⚠, listed at the end).

| What should have happened | What OpenPoke did instead | 40 agents | 500 agents |
|---|---|---|---|
| Should reuse an existing agent | Created a new agent instead | 0 of 84 | 1 of 83 |
| Should reuse an existing agent | Used a different existing agent | 2 of 84 | 2 of 83 |
| Should reuse an existing agent | Replied without checking any agent | 0 of 84 | 2 of 83 |
| Should create a new agent | Put the work into an existing agent | 13 of 29 | 12 of 29 |
| Should create a new agent | Asked the user instead of acting | 1 of 29 | 3 of 29 |
| Ambiguous name | Created a new agent instead | 0 of 7 | 1 of 7 |
| Ambiguous name | Used a different existing agent | 1 of 7 | 1 of 7 |
| Ambiguous name | Replied without checking any agent | 1 of 7 | 0 of 7 |
| Cross-agent question | Checked too few of the relevant agents | 0 of 3 | 1 of 3 |
| Cross-agent question | Checked none of the relevant agents | 2 of 3 | 1 of 3 |

## Failed at every roster size (14)

| Case | Kind | Prompt | Outcomes |
|---|---|---|---|
| R030 ⚠ | reuse | did Farah send the renewal figures yet? | used a different existing agent |
| R055 | ambiguous | any update from Daniel? | used a different existing agent |
| R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | put the work into an existing agent, asked the user instead of acting |
| R075 | new | what's going on with the MacLeod renewal? | put the work into an existing agent |
| R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | put the work into an existing agent |
| R078 | new | what's going on with the Vargas renewal? | put the work into an existing agent, asked the user instead of acting |
| R080 ⚠ | new | what's going on with the Malik renewal? | put the work into an existing agent |
| R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R087 | new | did Adriana send the VIN yet? | asked the user instead of acting, put the work into an existing agent |
| R089 | new | what's the status of Nora's theft claim? | put the work into an existing agent |
| R099 | new | what's going on with the okafor renewal? | put the work into an existing agent |
| R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | used a different existing agent |
| R120 | multi | which clients still owe me documents? | checked none of the relevant agents |
| R122 | multi | any certificates still waiting to go out? | checked none of the relevant agents, checked too few of the relevant agents |

## Should reuse an existing agent (7)

Correct: Send the request to the one existing agent that owns the work (reuse, lookalike and reminder cases).

### Created a new agent instead (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R119 | reminder | remind me thursday to update Paolo on the billing issue | *Billing issue - Paolo Schmidt* | *Paolo Schmidt Billing Reminder* (new) |

### Used a different existing agent (4)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 500 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 40 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 500 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |

### Replied without checking any agent (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R049 | reuse | Nora says something's wrong with the bill, look into it | *Nora Bhatt Billing Check* | replied: "Quick check before I dig in: which Nora? I have two open billing files, Nora Bhatt ($142, payment plan) and Nora Singh ($111, NSF payment)." |
| 500 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | replied: "Quick check before I set this: Ana has two certificate requests in progress, one for MacLeod Print Shop (City of Markham, due Sunday) and o…" |

## Should create a new agent (29)

Correct: Create a new agent. The client already has an agent for a different job, and that agent must not be used.

### Put the work into an existing agent (25)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R071 | new | what's going on with the Cardenas renewal? | New agent (not *Certificate for Maya Cardenas*) | *Certificate for Maya Cardenas* (existing) |
| 500 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 40 | R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric Ltd. Renewal CPP-104292*) | *Certificate for Arjun Schmidt* (existing) |
| 40 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 500 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Brewing Co. Renewal BOP-857302* (existing) |
| 500 | R076 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Uma Malik Policy Renewal*) | *Abbott Architecture Inc. COI - Kingsway Realty Holdings* (existing) |
| 40 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 500 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R078 | new | what's going on with the Vargas renewal? | New agent (not *Certificate for Ben Vargas*) | *Certificate for Ben Vargas* (existing) |
| 40 | R079 | new | where are we on Farah's certificate for the City of Mississauga job? | New agent (not *Tremblay Roofing Ltd. Renewal BOP-104123*) | *Farah Tran Policy Renewal* (existing) |
| 40 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 500 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Malik Architecture Ltd. Renewal BOP-801881* (existing), *Uma Malik Policy Renewal* (existing), *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing) |
| 40 | R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Hana Ellis Policy Renewal*) | *Certificate for Arjun Schmidt* (existing) |
| 500 | R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Hana Ellis Policy Renewal*) | *Certificate for Arjun Schmidt* (existing) |
| 40 | R084 | new | what's going on with the Reyes renewal? | New agent (not *COI Reyes Roofing Inc.*) | *COI Reyes Roofing Inc.* (existing) |
| 40 | R086 | new | what's still missing for Paolo's home and auto quote? | New agent (not *Billing issue - Paolo Schmidt*) | *Billing issue - Paolo Schmidt* (existing) |
| 500 | R087 | new | did Adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Add Volkswagen to Adriana's policy* (existing) |
| 40 | R089 | new | what's the status of Nora's theft claim? | New agent (not *Nora Bhatt Billing Check*) | *Nora Bhatt Billing Check* (existing) |
| 500 | R089 | new | what's the status of Nora's theft claim? | New agent (not *Nora Bhatt Billing Check*) | *Nora Ivanova Auto Claim (2025)* (existing) |
| 500 | R091 | new | start a claim file for Felix's hail damage | New agent (not *Felix Morin Billing Check*) | *Felix Lefebvre Burglary Claim* (existing) |
| 40 | R092 | new | what's the status of Javier's collision claim? | New agent (not *New business quote - Javier Zhang*) | *Patel renewal* (existing) |
| 500 | R093 | new | what's still missing for Owen's auto quote? | New agent (not *Owen Zielinski Billing Check*) | *Owen Fontaine Vehicle Addition* (existing) |
| 500 | R094 | new | what's still missing for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 40 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |

### Asked the user instead of acting (4)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric Ltd. Renewal CPP-104292*) | replied: "Checking on that now. The Dufferin Plaza Management certificate I have on file is for Arjun Schmidt, not Ines, so I'm searching for anythin…" |
| 500 | R078 | new | what's going on with the Vargas renewal? | New agent (not *Certificate for Ben Vargas*) | replied: "No single Vargas renewal file that I can see. Here's where the Vargas files stand: - Rachel Vargas: $274.25 NSF payment issue. Carrier bill…" |
| 500 | R085 | new | start a claim file for Leah's water damage | New agent (not *Leah NSF Payment*) | replied: "Leah Pereira's water claim is already open: CLM-2614663 with Northern Shield. Adjuster Paula Jensen wants to inspect soon, and Leah's been …" |
| 40 | R087 | new | did Adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | replied: "Checking on that now." |

## Ambiguous name (4)

Correct: Ask which person is meant, or check every agent with that name.

### Created a new agent instead (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R064 | ambiguous | any update from Omar? | Ask, or check all: *Omar Kim Billing Check*, *Add Mazda to Omar's policy* | *Omar Updates Check* (new) |

### Used a different existing agent (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |

### Replied without checking any agent (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R061 | ambiguous | any update from Maya? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | replied: "Three Mayas are active. Which one? - **Maya Cardenas** (Cardenas Bakery COI): she corrected the certificate holder to "The Regional Municip…" |

## Cross-agent question (4)

Correct: Check at least half of the agents that hold the answer.

### Checked too few of the relevant agents (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Certificate for Arjun Schmidt* (existing), *Certificate for Neil Malik* (existing), *Okafor Landscaping COI - City of Vaughan* (existing); checked 3 of 8 |

### Checked none of the relevant agents (3)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 500 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding client documents* (new); checked 0 of 3 |
| 40 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *COI Pending Status Check* (new); checked 0 of 8 |

## Counted as correct, but with extra agents (5)

Reached the right agent and also called others. Not included in the failure counts above.

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R023 | reuse | what's going on with the Malik renewal? | *Uma Malik Policy Renewal* | *Malik Architecture Ltd. Renewal BOP-801881* (existing), *Uma Malik Policy Renewal* (existing), *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing) |
| 40 | R026 | reuse | did Farah send the renewal figures yet? | *Farah Tran Policy Renewal* | *Farah Tran Policy Renewal* (existing), *Tremblay Roofing Ltd. Renewal BOP-104123* (existing) |
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
