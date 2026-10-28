# Routing failures: openpoke-names

Every case this run scored as wrong, grouped by what should have happened. Generated from `results.json` by `run_baseline.py failures` (no LLM calls). Agent names: organic; prompts: all. Case ids ending in `.pN` are paraphrase N of the same case.

- **100 agents: incomplete** (396 of 516 LLM calls failed, out of OpenRouter credit), so these cases are not listed. The complete results for this size are in a later rerun.
- **250 agents: incomplete** (499 of 516 LLM calls failed, out of OpenRouter credit), so these cases are not listed. The complete results for this size are in a later rerun.
- **500 agents: incomplete** (497 of 516 LLM calls failed, out of OpenRouter credit), so these cases are not listed. The complete results for this size are in a later rerun.

**147 failures out of 516 scored cases.** 21 of them come from cases with a known labelling problem (marked ⚠, listed at the end).

| What should have happened | What OpenPoke did instead | 40 agents |
|---|---|---|
| Should reuse an existing agent | Created a new agent instead | 79 of 328 |
| Should reuse an existing agent | Used a different existing agent | 4 of 328 |
| Should create a new agent | Put the work into an existing agent | 53 of 116 |
| Should create a new agent | Asked the user instead of acting | 1 of 116 |
| Ambiguous name | Used a different existing agent | 4 of 28 |
| Cross-agent question | Checked none of the relevant agents | 5 of 12 |
| Chit-chat | Called an agent | 1 of 32 |

## Should reuse an existing agent (83)

Correct: Send the request to the one existing agent that owns the work (reuse, lookalike and reminder cases).

### Created a new agent instead (79)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R018.p2 | reuse | has Schmidt Cleaning Services Ltd. gotten their COI yet | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning Services COI Status* (new) |
| 40 | R018.p3 | reuse | Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet? | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning Services COI Status* (new) |
| 40 | R020 | reuse | did Ines send the renewal figures yet? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 40 | R020.p1 | reuse | did ines send the renewal figures yet | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 40 | R020.p2 | reuse | has Ines sent over the renewal figures yet | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 40 | R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 40 | R024.p3 | reuse | Do you know whether Uma has sent the renewal figures yet? | *Malik Auto Body Lakeshore General Renewal* | *Uma Singh Renewal Figures Check* (new) |
| 40 | R026 ⚠ | reuse | did Farah send the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 40 | R026.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 40 | R026.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 40 | R026.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 40 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 40 | R030.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 40 | R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 40 | R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 40 | R034 | reuse | did Laila send the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 40 | R034.p1 | reuse | did laila send the renewal figs yet | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 40 | R034.p2 | reuse | Has Laila sent over the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 40 | R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 40 | R036 | reuse | did Hana send the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 40 | R036.p1 | reuse | did hana send the renewal figs yet | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 40 | R036.p2 | reuse | Has Hana sent over the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 40 | R036.p3 | reuse | Could you check whether Hana has sent the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 40 | R038 | reuse | did Javier send the renewal figures yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 40 | R038.p1 | reuse | javier send the renewal figs yet | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 40 | R038.p2 | reuse | has Javier sent the renewal figs yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 40 | R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 40 | R040 | reuse | did Reyes Roofing Inc. get their COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing Inc COI Status* (new) |
| 40 | R101 | reminder | remind me friday at 9 to send alice park the budget numbers | *Q4 Book of Business Report for Alice Park* | *Reminder Alice Park Budget Numbers* (new) |
| 40 | R101.p1 | reminder | remind me friday at 9 to send alice park the budget nums | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 40 | R101.p2 | reminder | remind me friday at 9 to send alice park the budgt numbers | *Q4 Book of Business Report for Alice Park* | *Friday 9am Reminder Alice Park Budget Numbers* (new) |
| 40 | R101.p3 | reminder | Could you please remind me on Friday at 9 to send Alice Park the budget numbers? | *Q4 Book of Business Report for Alice Park* | *Friday Reminder Alice Park Budget* (new) |
| 40 | R102.p2 | reminder | remind me tomorrow at 10am to chekc daniel's certificate went out | *Okafor Landscaping COI City of Vaughan* | *Reminder Daniel Okafor Certificate Check* (new) |
| 40 | R102.p3 | reminder | Could you remind me tomorrow at 10am to check that Daniel's certificate went out? | *Okafor Landscaping COI City of Vaughan* | *Daniel Okafor Certificate Reminder* (new) |
| 40 | R104 | reminder | remind me Wednesday at 10am to check that Maya's certificate was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Check Reminder* (new) |
| 40 | R104.p1 | reminder | remind me wednesday at 10am to check mayas cert was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Cert Reminder Wed 10am* (new) |
| 40 | R104.p2 | reminder | remind me wednesday at 10am to chekc Maya's certificate was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Check Reminder* (new) |
| 40 | R104.p3 | reminder | Could you remind me on Wednesday at 10am to check that Maya's certificate was issued? | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 40 | R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 40 | R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Check Reminder* (new) |
| 40 | R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Check Reminder* (new) |
| 40 | R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder Wed 10am* (new) |
| 40 | R106.p3 | reminder | Could you remind me on Wednesday at 10am to check that Arjun's certificate was issued? | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Wednesday 10am Arjun Certificate Reminder* (new) |
| 40 | R107 | reminder | remind me next monday to chase Ines for the renewal numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 40 | R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 40 | R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 40 | R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 40 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder Wed 10am* (new) |
| 40 | R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | *MacLeod Print Shop Markham Certificate* | *Wednesday 10am Ana Cert Reminder* (new) |
| 40 | R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder Wed 10am* (new) |
| 40 | R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Issued Reminder* (new) |
| 40 | R109 | reminder | remind me next monday to chase Uma for the renewal numbers | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 40 | R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | *Malik Auto Body Lakeshore General Renewal* | *Reminder Chase Uma Renewal Numbers* (new) |
| 40 | R110 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 40 | R110.p1 ⚠ | reminder | remind me next monday to chase farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 40 | R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 40 | R110.p3 ⚠ | reminder | Could you please set a reminder for next Monday to follow up with Farah about the renewal numbers? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Follow-up Reminder* (new) |
| 40 | R111 | reminder | remind me Wednesday at 10am to check that Ben's certificate was issued | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Reminder Wed 10am* (new) |
| 40 | R111.p1 | reminder | remind me Wednesday at 10am to chk that Ben's certificate was issued | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Reminder Wed 10am* (new) |
| 40 | R111.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Ben's certificate has been issued? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Reminder Wed 10am* (new) |
| 40 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 40 | R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 40 | R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 40 | R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 40 | R113.p1 | reminder | remind me Wednesday at 10am to check tht Neil's certificate was issued | *Neil Malik COI Malik Roofing Bayview* | *Wednesday 10am Neil Certificate Reminder* (new) |
| 40 | R114 | reminder | remind me next monday to chase Laila for the renewal numbers | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 40 | R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 40 | R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Follow-up Reminder* (new) |
| 40 | R115 | reminder | remind me next monday to chase Hana for the renewal numbers | *Ellis Fitness Northern Shield CGL Renewal* | *Reminder Chase Hana Renewal Numbers* (new) |
| 40 | R115.p1 | reminder | remind me next monday to chase hana for the renewal numbers | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 40 | R115.p2 | reminder | Could you please set a reminder for next Monday to follow up with Hana about the renewal numbers? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 40 | R116 | reminder | remind me next monday to chase Javier for the renewal numbers | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 40 | R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 40 | R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 40 | R118 | reminder | remind me thursday to update Leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Thursday Reminder Leah Billing Update* (new) |
| 40 | R118.p2 | reminder | remind me thursday to updte Leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Update Reminder* (new) |
| 40 | R119 | reminder | remind me thursday to update Paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Paolo Schmidt Billing Reminder* (new) |
| 40 | R119.p2 | reminder | remind me thursday to updat Paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Thursday Reminder Paolo Billing Update* (new) |
| 40 | R119.p3 | reminder | Could you please remind me on Thursday to give Paolo an update on the billing issue? | *Paolo Schmidt Double Charge $348.50* | *Paolo Update Reminder Thursday* (new) |

### Used a different existing agent (4)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R024 | reuse | did Uma send the renewal figures yet? | *Malik Auto Body Lakeshore General Renewal* | *Uma Singh Auto Vehicle Replacement AU-959725* (existing) |
| 40 | R024.p1 | reuse | did uma send the renewal figures yet | *Malik Auto Body Lakeshore General Renewal* | *Uma Singh Auto Vehicle Replacement AU-959725* (existing) |
| 40 | R024.p2 | reuse | has Uma sent over the renewal figures yet | *Malik Auto Body Lakeshore General Renewal* | *Uma Singh Auto Vehicle Replacement AU-959725* (existing) |
| 40 | R109.p2 | reminder | Could you please remind me next Monday to follow up with Uma for the renewal numbers? | *Malik Auto Body Lakeshore General Renewal* | *Uma Singh Auto Vehicle Replacement AU-959725* (existing) |

## Should create a new agent (54)

Correct: Create a new agent. The client already has an agent for a different job, and that agent must not be used.

### Put the work into an existing agent (53)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R071 | new | what's going on with the Cardenas renewal? | New agent (not *Cardenas Bakery COI Regional Municipality of York*) | *Cardenas Bakery COI Regional Municipality of York* (existing) |
| 40 | R071.p1 | new | whats up with the cardenas renewal | New agent (not *Cardenas Bakery COI Regional Municipality of York*) | *Cardenas Bakery COI Regional Municipality of York* (existing) |
| 40 | R071.p2 | new | what's going on with the Cardenas renewl? | New agent (not *Cardenas Bakery COI Regional Municipality of York*) | *Cardenas Bakery COI Regional Municipality of York* (existing) |
| 40 | R071.p3 | new | Could you let me know what's going on with the Cardenas renewal? | New agent (not *Cardenas Bakery COI Regional Municipality of York*) | *Cardenas Bakery COI Regional Municipality of York* (existing) |
| 40 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Pereira Hardware COI Lakeshore Industrial REIT* (existing), *Adriana Pereira Premium Increase Inquiry* (existing) |
| 40 | R072.p1 | new | whats up with the pereira renewal | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R072.p2 | new | what's going on with the Pereira renewl? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Pereira Hardware COI Lakeshore Industrial REIT* (existing), *Adriana Pereira Premium Increase Inquiry* (existing) |
| 40 | R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Pereira Hardware COI Lakeshore Industrial REIT* (existing), *Adriana Pereira Premium Increase Inquiry* (existing) |
| 40 | R073 | new | what's going on with the Schmidt renewal? | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing), *Paolo Schmidt Double Charge $348.50* (existing) |
| 40 | R073.p1 | new | whats up with the schmidt renewal | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing), *Paolo Schmidt Double Charge $348.50* (existing) |
| 40 | R073.p2 | new | where are we on the schmidt renewal? | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R073.p3 | new | Could you let me know where things stand with the Schmidt renewal? | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R074.p1 | new | where are we on ines cert for dufferin plaza management | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R074.p2 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R074.p3 | new | Could you tell me where we are on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 40 | R075.p1 | new | whats going on w the macleod renewal | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 40 | R075.p2 | new | where are we on the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 40 | R075.p3 | new | Could you fill me in on what's happening with the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 40 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R077.p1 | new | where are we on farah's cert for lakeshore industrial reit | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R077.p2 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R077.p3 | new | Could you update me on where we are with Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R078 | new | what's going on with the Vargas renewal? | New agent (not *Vargas Architecture COI Lakeshore Industrial REIT*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 40 | R078.p1 | new | whats going on with the vargas renewal | New agent (not *Vargas Architecture COI Lakeshore Industrial REIT*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 40 | R078.p2 | new | where are we on the vargas renewal? | New agent (not *Vargas Architecture COI Lakeshore Industrial REIT*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 40 | R078.p3 | new | Could you let me know what's happening with the Vargas renewal? | New agent (not *Vargas Architecture COI Lakeshore Industrial REIT*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 40 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 40 | R080.p1 ⚠ | new | whats going on w the malik renewal | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 40 | R080.p2 ⚠ | new | where are we on the malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 40 | R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 40 | R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R082.p1 | new | where are we on hanas cert for dufferin plaza management | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R082.p2 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R082.p3 | new | Could you let me know where we are on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 40 | R084 | new | what's going on with the Reyes renewal? | New agent (not *Leah Reyes Bayview COI Request*) | *Leah Reyes Bayview COI Request* (existing) |
| 40 | R084.p1 | new | whats going on with the reyes renewal | New agent (not *Leah Reyes Bayview COI Request*) | *Leah Reyes Bayview COI Request* (existing) |
| 40 | R084.p2 | new | where are we on the reyes renewal? | New agent (not *Leah Reyes Bayview COI Request*) | *Leah Reyes Bayview COI Request* (existing) |
| 40 | R084.p3 | new | Could you let me know what's happening with the Reyes renewal? | New agent (not *Leah Reyes Bayview COI Request*) | *Leah Reyes Bayview COI Request* (existing) |
| 40 | R086.p2 | new | what's still missin for Paolo's home and auto quote? | New agent (not *Paolo Schmidt Double Charge $348.50*) | *Paolo Schmidt Double Charge $348.50* (existing) |
| 40 | R087 | new | did Adriana send the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Pereira Premium Increase Inquiry* (existing) |
| 40 | R087.p1 | new | adriana send the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Pereira Premium Increase Inquiry* (existing) |
| 40 | R087.p2 | new | did Adriana snd the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Pereira Premium Increase Inquiry* (existing) |
| 40 | R087.p3 | new | Do you know whether Adriana has sent the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Pereira Premium Increase Inquiry* (existing) |
| 40 | R090 | new | Mona says something's wrong with the bill, look into it | New agent (not *Mona Fernandes Auto Quote and Renovation Receipts*) | *Mona Fernandes Auto Quote and Renovation Receipts* (existing) |
| 40 | R090.p1 | new | mona says the bill looks off, can u check it | New agent (not *Mona Fernandes Auto Quote and Renovation Receipts*) | *Mona Fernandes Auto Quote and Renovation Receipts* (existing) |
| 40 | R090.p2 | new | Mona says somethings wrong with the bil, look into it | New agent (not *Mona Fernandes Auto Quote and Renovation Receipts*) | *Mona Fernandes Auto Quote and Renovation Receipts* (existing) |
| 40 | R090.p3 | new | Mona has mentioned that something seems wrong with the bill, so could you please look into it? | New agent (not *Mona Fernandes Auto Quote and Renovation Receipts*) | *Mona Fernandes Auto Quote and Renovation Receipts* (existing) |
| 40 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 40 | R099.p1 | new | whats up with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 40 | R099.p2 | new | whats going on with the okafor renewl? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 40 | R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |

### Asked the user instead of acting (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R085.p1 | new | open a claim file for leah's water damage | New agent (not *Leah Fernandes NSF Payment Inquiry*) | replied: "Which Leah? I've got Leah Reyes (Bayview COI) and Leah Fernandes (NSF payment), and neither is about water damage. Give me the last name an…" |

## Ambiguous name (4)

Correct: Ask which person is meant, or check every agent with that name.

### Used a different existing agent (4)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 40 | R055.p1 | ambiguous | any news from daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 40 | R055.p2 | ambiguous | any updte from Daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 40 | R055.p3 | ambiguous | Do you have any update from Daniel yet? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |

## Cross-agent question (5)

Correct: Check at least half of the agents that hold the answer.

### Checked none of the relevant agents (5)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 40 | R120.p1 | multi | which clients still owe me docs? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 40 | R120.p2 | multi | which clients still owe me documnts? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Tracker* (new); checked 0 of 3 |
| 40 | R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 40 | R122.p2 | multi | any certifcates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Certificate Requests Status Check* (new); checked 0 of 8 |

## Chit-chat (1)

Correct: Reply without calling any agent.

### Called an agent (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R127.p2 ⚠ | none | nevermind, ignore thta | No agent | *Bob's Book Thursday Reminder Cancel* (new) |

## Counted as correct, but with extra agents (8)

Reached the right agent and also called others. Not included in the failure counts above.

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 40 | R015 | reuse | where are we on Paula's certificate for the Lakeshore Industrial REIT job? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R015.p1 | reuse | where we at on paula's certificate for the lakeshore industrial reit job | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R015.p2 | reuse | wheres paula's cert at for the Lakeshore Industrial REIT job | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R015.p3 | reuse | Could you let me know where things stand with Paula's certificate for the Lakeshore Industrial REIT job? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R027 | reuse | where are we on Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R027.p1 | reuse | where are we on bens cert for lakeshore industrial reit | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R027.p2 | reuse | Where do things stand on Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 40 | R027.p3 | reuse | Could you update me on where we are with Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |

## ⚠ Known labelling problems

These cases are still scored as labelled, so the counts above match `summary.md`, but their failures are a fault of the test data, not of OpenPoke.

| Case | Failures in this run | Problem |
|---|---|---|
| R026 | 4 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R030 | 4 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R080 | 4 | Same prompt as R023 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik). |
| R110 | 4 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R112 | 4 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R127 | 1 | The seeded chat ends with "remind me to bring Bob's book on thursday", so cancelling that reminder is a fair reading. |
