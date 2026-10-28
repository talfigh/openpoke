# Routing failures: paraphrases

Every case this run scored as wrong, grouped by what should have happened. Generated from `results.json` by `run_baseline.py failures` (no LLM calls). Agent names: synthetic; prompts: paraphrases. Case ids ending in `.pN` are paraphrase N of the same case.

- **100 agents: incomplete** (133 of 385 LLM calls failed, out of OpenRouter credit), so these cases are not listed. The complete results for this size are in a later rerun.
- **250 agents: incomplete** (372 of 385 LLM calls failed, out of OpenRouter credit), so these cases are not listed. The complete results for this size are in a later rerun.
- **500 agents: incomplete** (378 of 385 LLM calls failed, out of OpenRouter credit), so these cases are not listed. The complete results for this size are in a later rerun.

**96 failures out of 385 scored cases.** 9 of them come from cases with a known labelling problem (marked ⚠, listed at the end).

| What should have happened | What OpenPoke did instead | 40 agents |
|---|---|---|
| Should reuse an existing agent | Created a new agent instead | 52 of 244 |
| Should reuse an existing agent | Used a different existing agent | 6 of 244 |
| Should reuse an existing agent | Asked the user instead of acting | 1 of 244 |
| Should create a new agent | Put the work into an existing agent | 30 of 87 |
| Ambiguous name | Used a different existing agent | 3 of 21 |
| Cross-agent question | Checked none of the relevant agents | 4 of 9 |

## Should reuse an existing agent (59)

Correct: Send the request to the one existing agent that owns the work (reuse, lookalike and reminder cases).

### Created a new agent instead (52)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R014.p2 | reuse | has Cardenas Bakery Inc. gotten their COI yet | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 40 | R014.p3 | reuse | Do you know whether Cardenas Bakery Inc. has received their COI yet? | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 40 | R018.p1 | reuse | did schmidt cleaning services ltd get their coi yet | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 40 | R018.p2 | reuse | has Schmidt Cleaning Services Ltd. gotten their COI yet | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 40 | R018.p3 | reuse | Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet? | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 40 | R020.p1 | reuse | did ines send the renewal figures yet | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 40 | R020.p2 | reuse | has Ines sent over the renewal figures yet | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 40 | R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 40 | R021.p2 | reuse | wheres Ana's cert at for the City of Markham job | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate City of Markham Status* (new) |
| 40 | R032.p1 | reuse | did malik roofing ltd get their coi yet | *Certificate for Neil Malik* | *Malik Roofing Ltd. COI Status* (new) |
| 40 | R032.p2 | reuse | Has Malik Roofing Ltd. received their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 40 | R032.p3 | reuse | Could you let me know if Malik Roofing Ltd. has gotten their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 40 | R034.p1 | reuse | did laila send the renewal figs yet | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 40 | R034.p2 | reuse | Has Laila sent over the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 40 | R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 40 | R038.p1 | reuse | javier send the renewal figs yet | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 40 | R038.p2 | reuse | has Javier sent the renewal figs yet? | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 40 | R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 40 | R039.p1 | reuse | wheres leahs cert for bayview commercial properties job | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate* (new) |
| 40 | R039.p2 | reuse | where we at on Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 40 | R039.p3 | reuse | Could you update me on where things stand with Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 40 | R052.p1 | reuse | did mona send the reno receipts | *New business quote - Mona Fernandes* | *Mona Reno Receipts Search* (new) |
| 40 | R052.p2 | reuse | did Mona send the renovaton receipts? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts Check* (new) |
| 40 | R053.p1 | lookalike | daniel morin says bill's wrong, check it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 40 | R053.p2 | lookalike | Daniel Morin says somethings wrong wit the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Issue* (new) |
| 40 | R053.p3 | lookalike | Daniel Morin mentioned that something seems off with the bill, could you please look into it? | *Daniel NSF Payment* | *Daniel Morin Billing Issue* (new) |
| 40 | R059.p1 | lookalike | did maya zhang send the vin yet | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 40 | R059.p3 | lookalike | Has Maya Zhang sent over the VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 40 | R063.p1 | lookalike | omar abbott send the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 40 | R063.p2 | lookalike | did Omar Abbott snd the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 40 | R063.p3 | lookalike | Has Omar Abbott sent over the VIN yet, do you know? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 40 | R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | *Okafor Landscaping COI - City of Vaughan* | *Daniel Okafor Cert Reminder* (new) |
| 40 | R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Cert Reminder* (new) |
| 40 | R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 40 | R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 40 | R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Reminder - Chase Ines Renewal Numbers* (new) |
| 40 | R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Reminder - Chase Ines renewal numbers* (new) |
| 40 | R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Numbers Reminder* (new) |
| 40 | R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 40 | R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 40 | R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 40 | R111.p1 | reminder | remind me Wednesday at 10am to chk that Ben's certificate was issued | *Certificate for Ben Vargas* | *Reminder - Ben Vargas Certificate Check* (new) |
| 40 | R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah renewal numbers reminder* (new) |
| 40 | R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Reminder - Chase Laila Renewal Numbers* (new) |
| 40 | R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Numbers Reminder* (new) |
| 40 | R115.p1 | reminder | remind me next monday to chase hana for the renewal numbers | *Hana Ellis Policy Renewal* | *Hana renewal numbers reminder* (new) |
| 40 | R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | *Patel renewal* | *Javier Renewal Numbers Reminder* (new) |
| 40 | R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | *Patel renewal* | *Javier Renewal Numbers Reminder* (new) |
| 40 | R117.p1 | reminder | remind me Wednesday at 10am to chek that Leah's certificate was issued | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 40 | R117.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Leah's certificate has been issued? | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 40 | R118.p1 | reminder | remind me thursday to update leah on the billing issue | *Leah NSF Payment* | *Leah billing update reminder* (new) |
| 40 | R118.p2 | reminder | remind me thursday to updte Leah on the billing issue | *Leah NSF Payment* | *Leah Billing Reminder Thursday* (new) |

### Used a different existing agent (6)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R030.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 40 | R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 40 | R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 40 | R047.p2 | reuse | did Uma send the VN yet? | *Uma Toyota RAV4 Auto Policy* | *Uma Malik Policy Renewal* (existing) |
| 40 | R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 40 | R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |

### Asked the user instead of acting (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R001.p1 | reuse | what did alice chen say about lunch | *Lunch with Alice and Bob* | replied: "alice suggested thursday at 12:30 at pinewood kitchen." |

## Should create a new agent (30)

Correct: Create a new agent. The client already has an agent for a different job, and that agent must not be used.

### Put the work into an existing agent (30)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R071.p1 | new | whats up with the cardenas renewal | New agent (not *Certificate for Maya Cardenas*) | *Certificate for Maya Cardenas* (existing) |
| 40 | R071.p2 | new | what's going on with the Cardenas renewl? | New agent (not *Certificate for Maya Cardenas*) | *Certificate for Maya Cardenas* (existing) |
| 40 | R071.p3 | new | Could you let me know what's going on with the Cardenas renewal? | New agent (not *Certificate for Maya Cardenas*) | *Certificate for Maya Cardenas* (existing) |
| 40 | R072.p1 | new | whats up with the pereira renewal | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R073.p3 | new | Could you let me know where things stand with the Schmidt renewal? | New agent (not *Certificate for Arjun Schmidt*) | *Certificate for Arjun Schmidt* (existing), *Billing issue - Paolo Schmidt* (existing) |
| 40 | R075.p1 | new | whats going on w the macleod renewal | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 40 | R075.p2 | new | where are we on the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 40 | R075.p3 | new | Could you fill me in on what's happening with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 40 | R077.p1 | new | where are we on farah's cert for lakeshore industrial reit | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R077.p2 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R077.p3 | new | Could you update me on where we are with Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R078.p1 | new | whats going on with the vargas renewal | New agent (not *Certificate for Ben Vargas*) | *Certificate for Ben Vargas* (existing) |
| 40 | R078.p2 | new | where are we on the vargas renewal? | New agent (not *Certificate for Ben Vargas*) | *Certificate for Ben Vargas* (existing) |
| 40 | R078.p3 | new | Could you let me know what's happening with the Vargas renewal? | New agent (not *Certificate for Ben Vargas*) | *Certificate for Ben Vargas* (existing) |
| 40 | R080.p1 ⚠ | new | whats going on w the malik renewal | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 40 | R080.p2 ⚠ | new | where are we on the malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 40 | R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 40 | R084.p1 | new | whats going on with the reyes renewal | New agent (not *COI Reyes Roofing Inc.*) | *COI Reyes Roofing Inc.* (existing) |
| 40 | R084.p2 | new | where are we on the reyes renewal? | New agent (not *COI Reyes Roofing Inc.*) | *COI Reyes Roofing Inc.* (existing) |
| 40 | R084.p3 | new | Could you let me know what's happening with the Reyes renewal? | New agent (not *COI Reyes Roofing Inc.*) | *COI Reyes Roofing Inc.* (existing) |
| 40 | R087.p1 | new | adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Pereira Billing Check* (existing) |
| 40 | R087.p2 | new | did Adriana snd the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Pereira Billing Check* (existing) |
| 40 | R087.p3 | new | Do you know whether Adriana has sent the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Pereira Billing Check* (existing) |
| 40 | R090.p1 | new | mona says the bill looks off, can u check it | New agent (not *New business quote - Mona Fernandes*) | *New business quote - Mona Fernandes* (existing) |
| 40 | R090.p2 | new | Mona says somethings wrong with the bil, look into it | New agent (not *New business quote - Mona Fernandes*) | *New business quote - Mona Fernandes* (existing) |
| 40 | R090.p3 | new | Mona has mentioned that something seems wrong with the bill, so could you please look into it? | New agent (not *New business quote - Mona Fernandes*) | *New business quote - Mona Fernandes* (existing) |
| 40 | R094.p3 | new | Could you let me know what's still missing for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Add Ford to Ravi's policy* (existing) |
| 40 | R099.p1 | new | whats up with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 40 | R099.p2 | new | whats going on with the okafor renewl? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 40 | R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |

## Ambiguous name (3)

Correct: Ask which person is meant, or check every agent with that name.

### Used a different existing agent (3)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R055.p1 | ambiguous | any news from daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 40 | R055.p2 | ambiguous | any updte from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 40 | R055.p3 | ambiguous | Do you have any update from Daniel yet? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |

## Cross-agent question (4)

Correct: Check at least half of the agents that hold the answer.

### Checked none of the relevant agents (4)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R120.p1 | multi | which clients still owe me docs? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 40 | R120.p2 | multi | which clients still owe me documnts? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 40 | R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 40 | R122.p2 | multi | any certifcates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Certificate Status Check* (new); checked 0 of 8 |

## Counted as correct, but with extra agents (3)

Reached the right agent and also called others. Not included in the failure counts above.

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R027.p1 | reuse | where are we on bens cert for lakeshore industrial reit | *Certificate for Ben Vargas* | *Certificate for Ben Vargas* (existing), *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R027.p2 | reuse | Where do things stand on Ben's certificate for the Lakeshore Industrial REIT job? | *Certificate for Ben Vargas* | *Certificate for Ben Vargas* (existing), *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R027.p3 | reuse | Could you update me on where we are with Ben's certificate for the Lakeshore Industrial REIT job? | *Certificate for Ben Vargas* | *Certificate for Ben Vargas* (existing), *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |

## ⚠ Known labelling problems

These cases are still scored as labelled, so the counts above match `summary.md`, but their failures are a fault of the test data, not of OpenPoke.

| Case | Failures in this run | Problem |
|---|---|---|
| R030 | 3 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R080 | 3 | Same prompt as R023 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik). |
| R112 | 3 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
