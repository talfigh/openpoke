# Routing failures: baseline-r2

Every case this run scored as wrong, grouped by what should have happened. Generated from `results.json` by `run_baseline.py failures` (no LLM calls). Agent names: synthetic; prompts: original. Case ids ending in `.pN` are paraphrase N of the same case.

**160 failures out of 524 scored cases.** 15 of them come from cases with a known labelling problem (marked ⚠, listed at the end).

| What should have happened | What OpenPoke did instead | 40 agents | 100 agents | 250 agents | 500 agents |
|---|---|---|---|---|---|
| Should reuse an existing agent | Created a new agent instead | 18 of 84 | 19 of 84 | 24 of 84 | 29 of 84 |
| Should reuse an existing agent | Used a different existing agent | 2 of 84 | 2 of 84 | 3 of 84 | 5 of 84 |
| Should reuse an existing agent | Asked the user instead of acting | 1 of 84 | 0 of 84 | 1 of 84 | 1 of 84 |
| Should create a new agent | Put the work into an existing agent | 11 of 29 | 7 of 29 | 8 of 29 | 9 of 29 |
| Ambiguous name | Created a new agent instead | 0 of 7 | 0 of 7 | 3 of 7 | 4 of 7 |
| Ambiguous name | Used a different existing agent | 1 of 7 | 1 of 7 | 1 of 7 | 1 of 7 |
| Ambiguous name | Picked one of the matches without asking | 1 of 7 | 0 of 7 | 0 of 7 | 1 of 7 |
| Cross-agent question | Checked none of the relevant agents | 2 of 3 | 1 of 3 | 2 of 3 | 2 of 3 |

## Failed at every roster size (22)

| Case | Kind | Prompt | Outcomes |
|---|---|---|---|
| R018 | reuse | did Schmidt Cleaning Services Ltd. get their COI yet? | created a new agent instead |
| R020 | reuse | did Ines send the renewal figures yet? | created a new agent instead |
| R030 ⚠ | reuse | did Farah send the renewal figures yet? | used a different existing agent |
| R032 | reuse | did Malik Roofing Ltd. get their COI yet? | created a new agent instead |
| R034 | reuse | did Laila send the renewal figures yet? | created a new agent instead, used a different existing agent |
| R038 | reuse | did Javier send the renewal figures yet? | created a new agent instead, used a different existing agent |
| R039 | reuse | where are we on Leah's certificate for the Bayview Commercial Properties job? | created a new agent instead, used a different existing agent |
| R052 | reuse | did Mona send the renovation receipts? | created a new agent instead |
| R053 | lookalike | Daniel Morin says something's wrong with the bill, look into it | created a new agent instead |
| R055 | ambiguous | any update from Daniel? | used a different existing agent |
| R072 | new | what's going on with the Pereira renewal? | put the work into an existing agent |
| R075 | new | what's going on with the MacLeod renewal? | put the work into an existing agent |
| R080 ⚠ | new | what's going on with the Malik renewal? | put the work into an existing agent |
| R099 | new | what's going on with the okafor renewal? | put the work into an existing agent |
| R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | created a new agent instead |
| R107 | reminder | remind me next monday to chase Ines for the renewal numbers | created a new agent instead |
| R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | created a new agent instead |
| R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | used a different existing agent, created a new agent instead |
| R114 | reminder | remind me next monday to chase Laila for the renewal numbers | created a new agent instead |
| R116 | reminder | remind me next monday to chase Javier for the renewal numbers | created a new agent instead |
| R117 | reminder | remind me Wednesday at 10am to check that Leah's certificate was issued | created a new agent instead |
| R120 | multi | which clients still owe me documents? | checked none of the relevant agents |

## Should reuse an existing agent (105)

Correct: Send the request to the one existing agent that owns the work (reuse, lookalike and reminder cases).

### Created a new agent instead (90)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R014 | reuse | did Cardenas Bakery Inc. get their COI yet? | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 250 | R014 | reuse | did Cardenas Bakery Inc. get their COI yet? | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 500 | R014 | reuse | did Cardenas Bakery Inc. get their COI yet? | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 40 | R018 | reuse | did Schmidt Cleaning Services Ltd. get their COI yet? | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 100 | R018 | reuse | did Schmidt Cleaning Services Ltd. get their COI yet? | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 250 | R018 | reuse | did Schmidt Cleaning Services Ltd. get their COI yet? | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 500 | R018 | reuse | did Schmidt Cleaning Services Ltd. get their COI yet? | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 40 | R020 | reuse | did Ines send the renewal figures yet? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 100 | R020 | reuse | did Ines send the renewal figures yet? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 250 | R020 | reuse | did Ines send the renewal figures yet? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 500 | R020 | reuse | did Ines send the renewal figures yet? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 100 | R021 | reuse | where are we on Ana's certificate for the City of Markham job? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Status* (new) |
| 250 | R021 | reuse | where are we on Ana's certificate for the City of Markham job? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Status* (new) |
| 500 | R021 | reuse | where are we on Ana's certificate for the City of Markham job? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Status* (new) |
| 500 | R024 | reuse | did Uma send the renewal figures yet? | *Uma Malik Policy Renewal* | *Uma Renewal Figures Check* (new) |
| 100 | R028 | reuse | did Vargas Architecture Inc. get their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 250 | R028 | reuse | did Vargas Architecture Inc. get their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 500 | R028 | reuse | did Vargas Architecture Inc. get their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 40 | R032 | reuse | did Malik Roofing Ltd. get their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 100 | R032 | reuse | did Malik Roofing Ltd. get their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 250 | R032 | reuse | did Malik Roofing Ltd. get their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 500 | R032 | reuse | did Malik Roofing Ltd. get their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 40 | R034 | reuse | did Laila send the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 100 | R034 | reuse | did Laila send the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 500 | R034 | reuse | did Laila send the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 500 | R036 | reuse | did Hana send the renewal figures yet? | *Hana Ellis Policy Renewal* | *Hana Renewal Figures Check* (new) |
| 40 | R038 | reuse | did Javier send the renewal figures yet? | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 100 | R038 | reuse | did Javier send the renewal figures yet? | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 250 | R038 | reuse | did Javier send the renewal figures yet? | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 40 | R039 | reuse | where are we on Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 100 | R039 | reuse | where are we on Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 250 | R039 | reuse | where are we on Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 250 | R041 | reuse | Leah says something's wrong with the bill, look into it | *Leah NSF Payment* | *Leah Bill Issue* (new) |
| 500 | R041 | reuse | Leah says something's wrong with the bill, look into it | *Leah NSF Payment* | *Leah Billing Issue* (new) |
| 500 | R047 | reuse | did Uma send the VIN yet? | *Uma Toyota RAV4 Auto Policy* | *Uma VIN Check* (new) |
| 100 | R049 | reuse | Nora says something's wrong with the bill, look into it | *Nora Bhatt Billing Check* | *Nora Bill Issue Check* (new) |
| 40 | R052 | reuse | did Mona send the renovation receipts? | *New business quote - Mona Fernandes* | *Mona Fernandes Renovation Receipts* (new) |
| 100 | R052 | reuse | did Mona send the renovation receipts? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts* (new) |
| 250 | R052 | reuse | did Mona send the renovation receipts? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts Search* (new) |
| 500 | R052 | reuse | did Mona send the renovation receipts? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts Search* (new) |
| 40 | R053 | lookalike | Daniel Morin says something's wrong with the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Issue* (new) |
| 100 | R053 | lookalike | Daniel Morin says something's wrong with the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 250 | R053 | lookalike | Daniel Morin says something's wrong with the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Issue* (new) |
| 500 | R053 | lookalike | Daniel Morin says something's wrong with the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 500 | R056 | lookalike | what's still missing for Priya Malik's home quote? | *Priya quote* | *Priya Malik Home Quote Missing Items* (new) |
| 40 | R059 | lookalike | did Maya Zhang send the VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 500 | R059 | lookalike | did Maya Zhang send the VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 250 | R063 | lookalike | did Omar Abbott send the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 500 | R063 | lookalike | did Omar Abbott send the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 500 | R069 | lookalike | did Ravi Novak send the VIN yet? | *Add Ford to Ravi's policy* | *Ravi Novak VIN Check* (new) |
| 250 | R102 | reminder | remind me tomorrow at 10am to check daniel's certificate went out | *Okafor Landscaping COI - City of Vaughan* | *Daniel Okafor Certificate Reminder* (new) |
| 500 | R102 | reminder | remind me tomorrow at 10am to check daniel's certificate went out | *Okafor Landscaping COI - City of Vaughan* | *Daniel Okafor Certificate Reminder* (new) |
| 250 | R103 | reminder | remind me tomorrow at 9am to call linda about the adjuster | *Linda Gauthier Water Claim* | *Linda Adjuster Call Reminder* (new) |
| 500 | R103 | reminder | remind me tomorrow at 9am to call linda about the adjuster | *Linda Gauthier Water Claim* | *Linda Gauthier Adjuster Call Reminder* (new) |
| 40 | R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 100 | R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 250 | R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 500 | R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 40 | R107 | reminder | remind me next monday to chase Ines for the renewal numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Reminder - Chase Ines Renewal Numbers* (new) |
| 100 | R107 | reminder | remind me next monday to chase Ines for the renewal numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Chase Ines Renewal Reminder* (new) |
| 250 | R107 | reminder | remind me next monday to chase Ines for the renewal numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Reminder* (new) |
| 500 | R107 | reminder | remind me next monday to chase Ines for the renewal numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Reminder - Chase Ines Renewal Numbers* (new) |
| 40 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 100 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 250 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 500 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 40 | R109 | reminder | remind me next monday to chase Uma for the renewal numbers | *Uma Malik Policy Renewal* | *Reminder - Chase Uma Renewal Numbers* (new) |
| 100 | R109 | reminder | remind me next monday to chase Uma for the renewal numbers | *Uma Malik Policy Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 250 | R109 | reminder | remind me next monday to chase Uma for the renewal numbers | *Uma Malik Policy Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 250 | R110 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Farah Tran Policy Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R110 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Farah Tran Policy Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Chase Farah Renewal Reminder* (new) |
| 40 | R113 | reminder | remind me Wednesday at 10am to check that Neil's certificate was issued | *Certificate for Neil Malik* | *Neil Malik Certificate Reminder* (new) |
| 40 | R114 | reminder | remind me next monday to chase Laila for the renewal numbers | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Numbers Reminder* (new) |
| 100 | R114 | reminder | remind me next monday to chase Laila for the renewal numbers | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Numbers Reminder* (new) |
| 250 | R114 | reminder | remind me next monday to chase Laila for the renewal numbers | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Reminder Chase Laila Renewal Numbers* (new) |
| 500 | R114 | reminder | remind me next monday to chase Laila for the renewal numbers | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Numbers Reminder* (new) |
| 250 | R115 | reminder | remind me next monday to chase Hana for the renewal numbers | *Hana Ellis Policy Renewal* | *Reminder - Chase Hana Renewal Numbers* (new) |
| 500 | R115 | reminder | remind me next monday to chase Hana for the renewal numbers | *Hana Ellis Policy Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 40 | R116 | reminder | remind me next monday to chase Javier for the renewal numbers | *Patel renewal* | *Javier Renewal Reminder* (new) |
| 100 | R116 | reminder | remind me next monday to chase Javier for the renewal numbers | *Patel renewal* | *Javier Renewal Numbers Reminder* (new) |
| 250 | R116 | reminder | remind me next monday to chase Javier for the renewal numbers | *Patel renewal* | *Javier Renewal Reminder* (new) |
| 500 | R116 | reminder | remind me next monday to chase Javier for the renewal numbers | *Patel renewal* | *Javier Renewal Numbers Reminder* (new) |
| 40 | R117 | reminder | remind me Wednesday at 10am to check that Leah's certificate was issued | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 100 | R117 | reminder | remind me Wednesday at 10am to check that Leah's certificate was issued | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 250 | R117 | reminder | remind me Wednesday at 10am to check that Leah's certificate was issued | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 500 | R117 | reminder | remind me Wednesday at 10am to check that Leah's certificate was issued | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 40 | R118 | reminder | remind me thursday to update Leah on the billing issue | *Leah NSF Payment* | *Leah Billing Reminder* (new) |
| 250 | R118 | reminder | remind me thursday to update Leah on the billing issue | *Leah NSF Payment* | *Leah Billing Issue Thursday Reminder* (new) |
| 500 | R118 | reminder | remind me thursday to update Leah on the billing issue | *Leah NSF Payment* | *Leah Billing Issue Reminder* (new) |

### Used a different existing agent (12)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R023 ⚠ | reuse | what's going on with the Malik renewal? | *Uma Malik Policy Renewal* | *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing), *Malik Architecture Ltd. Renewal BOP-801881* (existing) |
| 40 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 100 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 500 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R034 | reuse | did Laila send the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Haddad Umbrella Policy Review* (existing) |
| 500 | R038 | reuse | did Javier send the renewal figures yet? | *Patel renewal* | *Javier Sokolov Home Renewal 2025* (existing) |
| 500 | R039 | reuse | where are we on Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Romano IT Consulting Inc. COI - Bayview Commercial Properties* (existing) |
| 500 | R050 | reuse | did billing get back to us about Nora's payment? | *Nora Bhatt Billing Check* | *Nora Singh Billing Check* (existing) |
| 40 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 100 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |

### Asked the user instead of acting (3)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R001 | reuse | what did alice chen say about lunch? | *Lunch with Alice and Bob* | replied: "alice suggested thursday at 12:30 at pinewood kitchen." |
| 500 | R001 | reuse | what did alice chen say about lunch? | *Lunch with Alice and Bob* | replied: "Alice suggested Thursday at 12:30 at Pinewood Kitchen." |
| 250 | R049 | reuse | Nora says something's wrong with the bill, look into it | *Nora Bhatt Billing Check* | replied: "Which Nora? I've got two billing checks open: Nora Bhatt and Nora Singh." |

## Should create a new agent (35)

Correct: Create a new agent. The client already has an agent for a different job, and that agent must not be used.

### Put the work into an existing agent (35)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R071 | new | what's going on with the Cardenas renewal? | New agent (not *Certificate for Maya Cardenas*) | *Certificate for Maya Cardenas* (existing) |
| 40 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing), *Adriana Pereira Billing Check* (existing) |
| 100 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 250 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 500 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 40 | R073 | new | what's going on with the Schmidt renewal? | New agent (not *Certificate for Arjun Schmidt*) | *Billing issue - Paolo Schmidt* (existing), *Certificate for Arjun Schmidt* (existing) |
| 40 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 100 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 250 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 500 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Brewing Co. Renewal BOP-857302* (existing) |
| 40 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 100 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 500 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 40 | R078 | new | what's going on with the Vargas renewal? | New agent (not *Certificate for Ben Vargas*) | *Certificate for Ben Vargas* (existing) |
| 40 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 100 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 250 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 500 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing), *Malik Architecture Ltd. Renewal BOP-801881* (existing) |
| 40 | R084 | new | what's going on with the Reyes renewal? | New agent (not *COI Reyes Roofing Inc.*) | *COI Reyes Roofing Inc.* (existing) |
| 250 | R085 | new | start a claim file for Leah's water damage | New agent (not *Leah NSF Payment*) | *Leah Pereira Water Damage Claim* (existing) |
| 500 | R085 | new | start a claim file for Leah's water damage | New agent (not *Leah NSF Payment*) | *Leah Pereira Water Damage Claim* (existing) |
| 40 | R087 | new | did Adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Pereira Billing Check* (existing) |
| 250 | R087 | new | did Adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Ellis Auto Claim (2025)* (existing) |
| 500 | R089 | new | what's the status of Nora's theft claim? | New agent (not *Nora Bhatt Billing Check*) | *Nora Ivanova Auto Claim (2025)* (existing) |
| 40 | R090 | new | Mona says something's wrong with the bill, look into it | New agent (not *New business quote - Mona Fernandes*) | *New business quote - Mona Fernandes* (existing) |
| 100 | R090 | new | Mona says something's wrong with the bill, look into it | New agent (not *New business quote - Mona Fernandes*) | *New business quote - Mona Fernandes* (existing) |
| 100 | R093 | new | what's still missing for Owen's auto quote? | New agent (not *Owen Zielinski Billing Check*) | *Owen Tenant Policy Quote* (existing) |
| 250 | R094 | new | what's still missing for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 500 | R094 | new | what's still missing for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 250 | R096 | new | did Aisha send the VIN yet? | New agent (not *Aisha quote*) | *Aisha quote* (existing) |
| 500 | R096 | new | did Aisha send the VIN yet? | New agent (not *Aisha quote*) | *Aisha quote* (existing) |
| 40 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 100 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 250 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |

## Ambiguous name (13)

Correct: Ask which person is meant, or check every agent with that name.

### Created a new agent instead (7)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R058 | ambiguous | any update from Priya? | Ask, or check all: *Priya quote*, *Priya Santos Billing Check* | *Priya Update Check* (new) |
| 250 | R061 | ambiguous | any update from Maya? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | *Maya Update Check* (new) |
| 500 | R061 | ambiguous | any update from Maya? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | *Maya Updates Check* (new) |
| 500 | R064 | ambiguous | any update from Omar? | Ask, or check all: *Omar Kim Billing Check*, *Add Mazda to Omar's policy* | *Omar Update Check* (new) |
| 250 | R067 | ambiguous | any update from Elena? | Ask, or check all: *Elena theft claim*, *Elena Kia Sportage Auto Policy* | *Elena Update Check* (new) |
| 250 | R070 | ambiguous | any update from Ravi? | Ask, or check all: *Ravi Patel Water Damage Claim*, *Add Ford to Ravi's policy* | *Ravi Update Check* (new) |
| 500 | R070 | ambiguous | any update from Ravi? | Ask, or check all: *Ravi Patel Water Damage Claim*, *Add Ford to Ravi's policy* | *Ravi Update Check* (new) |

### Used a different existing agent (4)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing), *Daniel NSF Payment* (existing), *Daniel Alvarez Vehicle Addition* (existing) |
| 100 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 250 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |

### Picked one of the matches without asking (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R067 | ambiguous | any update from Elena? | Ask, or check all: *Elena theft claim*, *Elena Kia Sportage Auto Policy* | *Elena theft claim* (existing) |
| 40 | R070 | ambiguous | any update from Ravi? | Ask, or check all: *Ravi Patel Water Damage Claim*, *Add Ford to Ravi's policy* | *Ravi Patel Water Damage Claim* (existing) |

## Cross-agent question (7)

Correct: Check at least half of the agents that hold the answer.

### Checked none of the relevant agents (7)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 100 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 250 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 500 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 40 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Certificate Status Check* (new); checked 0 of 8 |
| 250 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Certificate Status Check* (new); checked 0 of 8 |
| 500 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Pending Certificates Status* (new); checked 0 of 8 |

## Counted as correct, but with extra agents (12)

Reached the right agent and also called others. Not included in the failure counts above.

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R013 | reuse | where are we on Maya's certificate for the Regional Municipality of York job? | *Certificate for Maya Cardenas* | *Certificate for Maya Cardenas* (existing), *Petrov Daycare Ltd. COI - Regional Municipality of York* (existing) |
| 100 | R023 | reuse | what's going on with the Malik renewal? | *Uma Malik Policy Renewal* | *Uma Malik Policy Renewal* (existing), *Certificate for Neil Malik* (existing) |
| 40 | R027 | reuse | where are we on Ben's certificate for the Lakeshore Industrial REIT job? | *Certificate for Ben Vargas* | *Certificate for Ben Vargas* (existing), *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 100 | R027 | reuse | where are we on Ben's certificate for the Lakeshore Industrial REIT job? | *Certificate for Ben Vargas* | *Certificate for Ben Vargas* (existing), *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 100 | R029 | reuse | what's going on with the Tremblay renewal? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Tremblay Roofing Ltd. Renewal BOP-104123* (existing), *Karen Tremblay Umbrella Policy Review* (existing) |
| 100 | R033 | reuse | what's going on with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 250 | R033 | reuse | what's going on with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 500 | R033 | reuse | what's going on with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing), *Javier Sokolov Home Renewal 2025* (existing) |
| 250 | R036 | reuse | did Hana send the renewal figures yet? | *Hana Ellis Policy Renewal* | *Hana Ibrahim Home Renewal 2025* (existing), *Hana Ellis Policy Renewal* (existing) |
| 500 | R049 | reuse | Nora says something's wrong with the bill, look into it | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 100 | R050 | reuse | did billing get back to us about Nora's payment? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 250 | R050 | reuse | did billing get back to us about Nora's payment? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |

## ⚠ Known labelling problems

These cases are still scored as labelled, so the counts above match `summary.md`, but their failures are a fault of the test data, not of OpenPoke.

| Case | Failures in this run | Problem |
|---|---|---|
| R023 | 1 | Same prompt as R080 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik). |
| R030 | 4 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R080 | 4 | Same prompt as R023 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik). |
| R110 | 2 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R112 | 4 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
