# routing run 2026-10-27_134806 (openpoke-names)

git 98949d7 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 683.0s

**Warning:** 396 cases at roster 100 failed (LLM errors) and are excluded; that row is partial.
**Warning:** 499 cases at roster 250 failed (LLM errors) and are excluded; that row is partial.
**Warning:** 497 cases at roster 500 failed (LLM errors) and are excluded; that row is partial.

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 516 | 72% | 75% | 24% | 1% | 46% | 6022.0 | 4.05 | 6.21 | 0.9029 |
| 100 | 120 | 83% | 84% | 13% | 2% | 50% | 7553.8 | 4.1 | 5.72 | 0.3248 |
| 250 | 17 | 71% | 78% | 22% | 0% | 60% | 11384.6 | 4.74 | 8.18 | 0.1376 |
| 500 | 19 | 74% | 64% | 27% | 9% | 0% | 17625.4 | 4.05 | 5.78 | 0.2046 |

| Roster size | Original prompts | Paraphrased prompts |
|---|---|---|
| 40 | 72% | 71% |
| 100 | 88% | 82% |
| 250 | 75% | 67% |
| 500 | 75% | 73% |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 40 | 93% | 41% |
| 100 | 94% | 69% |
| 250 | 100% | 33% |
| 500 | 71% | 50% |

Accuracy by case kind:

| Kind | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| ambiguous | 86% (n=28) | - (n=0) | - (n=0) | 100% (n=2) |
| lookalike | 100% (n=48) | 100% (n=1) | 100% (n=1) | - (n=0) |
| multi | 58% (n=12) | - (n=0) | 100% (n=1) | - (n=0) |
| new | 53% (n=116) | 50% (n=2) | 40% (n=5) | 100% (n=2) |
| none | 97% (n=32) | - (n=0) | 100% (n=2) | 75% (n=4) |
| reminder | 28% (n=72) | 100% (n=1) | 0% (n=1) | 0% (n=2) |
| reuse | 85% (n=208) | 84% (n=116) | 86% (n=7) | 78% (n=9) |

Failures (1569), largest roster first:

- [500] R002.p2 reuse **error**: "is bob coming to lunch? he mentoned something about food" → ['Pinewood Kitchen Lunch Booking'] (gold: ['Pinewood Kitchen Lunch Booking'])
- [500] R002.p3 reuse **error**: "Do you know if Bob is coming to lunch? I think he mentioned something about food, and I want to check before I plan anything." → ['Pinewood Kitchen Lunch Booking'] (gold: ['Pinewood Kitchen Lunch Booking'])
- [500] R003 reuse **error**: "draft a reply to alice park saying I'll send the budget numbers thursday" → ['Q4 Book of Business Report for Alice Park'] (gold: ['Q4 Book of Business Report for Alice Park'])
- [500] R003.p1 reuse **error**: "draft a reply to alice park, say ill send the budget numbers thursday" → ['Alice Park Reply Draft Budget Numbers'] (gold: ['Q4 Book of Business Report for Alice Park'])
- [500] R003.p2 reuse **error**: "draft a reply to alice park saying ill send the budgt numbers thursday" → ['Q4 Book of Business Report for Alice Park'] (gold: ['Q4 Book of Business Report for Alice Park'])
- [500] R004 reuse **error**: "what numbers does alice park need for the budget?" → [] (gold: ['Q4 Book of Business Report for Alice Park'])
- [500] R004.p1 reuse **error**: "what numbers does alice park need for the budget" → [] (gold: ['Q4 Book of Business Report for Alice Park'])
- [500] R004.p2 reuse **error**: "wat numbers does alice park need for the budget?" → ['Q4 Book of Business Report for Alice Park'] (gold: ['Q4 Book of Business Report for Alice Park'])
- [500] R004.p3 reuse **error**: "Could you tell me which numbers Alice Park needs for the budget? I want to make sure I send her the right information." → ['Q4 Book of Business Report for Alice Park'] (gold: ['Q4 Book of Business Report for Alice Park'])
- [500] R005 reuse **error**: "prepare the certificate Daniel needs for the city contract" → [] (gold: ['Okafor Landscaping COI City of Vaughan'])
- [500] R005.p1 reuse **error**: "prep the certificate daniel needs for the city contract" → [] (gold: ['Okafor Landscaping COI City of Vaughan'])
- [500] R005.p2 reuse **error**: "prepare the cerificate Daniel needs for the city contract" → [] (gold: ['Okafor Landscaping COI City of Vaughan'])
- [500] R005.p3 reuse **error**: "Could you prepare the certificate that Daniel needs for the city contract? He's waiting on it for that project." → [] (gold: ['Okafor Landscaping COI City of Vaughan'])
- [500] R006 reuse **error**: "daniel corrected the certificate holder name, make sure we use the new one" → [] (gold: ['Okafor Landscaping COI City of Vaughan'])
- [500] R006.p1 reuse **error**: "daniel fixed the certificate holder name, use the new one" → ['Okafor Landscaping COI City of Vaughan'] (gold: ['Okafor Landscaping COI City of Vaughan'])
- [500] R006.p2 reuse **error**: "daniel corrected the certifcate holder name, make sure we use the new one" → [] (gold: ['Okafor Landscaping COI City of Vaughan'])
- [500] R006.p3 reuse **error**: "Daniel has corrected the certificate holder name, so please make sure we use the new version when we prepare or send it." → [] (gold: ['Okafor Landscaping COI City of Vaughan'])
- [500] R007 reuse **error**: "add priya's new car to her policy" → [] (gold: ['Priya Sharma Honda CR-V Vehicle Addition'])
- [500] R007.p1 reuse **error**: "add priyas new car to her policy" → [] (gold: ['Priya Sharma Honda CR-V Vehicle Addition'])
- [500] R007.p2 reuse **error**: "add priya's new car to her polcy" → [] (gold: ['Priya Sharma Honda CR-V Vehicle Addition'])
- [500] R007.p3 reuse **error**: "Could you add Priya's new car to her policy? She recently bought it and needs it covered." → [] (gold: ['Priya Sharma Honda CR-V Vehicle Addition'])
- [500] R008 reuse **error**: "did priya send the VIN yet?" → [] (gold: ['Priya Sharma Honda CR-V Vehicle Addition'])
- [500] R008.p1 reuse **error**: "did priya send the vin yet" → ['Priya Sharma Honda CR-V Vehicle Addition'] (gold: ['Priya Sharma Honda CR-V Vehicle Addition'])
- [500] R008.p2 reuse **error**: "did priya send the VIN yt?" → [] (gold: ['Priya Sharma Honda CR-V Vehicle Addition'])
- [500] R008.p3 reuse **error**: "Has Priya sent the VIN yet? I need it to finish updating her policy for the new car." → [] (gold: ['Priya Sharma Honda CR-V Vehicle Addition'])
- [500] R009 reuse **error**: "marco says he was double charged, look into it" → [] (gold: ['Marco Rossi Double Charge Billing Fix'])
- [500] R009.p1 reuse **error**: "marco says he got double charged, can you look into it" → [] (gold: ['Marco Rossi Double Charge Billing Fix'])
- [500] R009.p2 reuse **error**: "marco says he was double chrged, look into it pls" → [] (gold: ['Marco Rossi Double Charge Billing Fix'])
- [500] R009.p3 reuse **error**: "Marco says he was charged twice, so could you please look into it and see what happened?" → [] (gold: ['Marco Rossi Double Charge Billing Fix'])
- [500] R010 reuse **error**: "start a claim file for linda's basement" → [] (gold: ['Linda Gauthier Basement Water Claim Restoration'])
- [500] R010.p1 reuse **error**: "open a claim file for lindas basement" → [] (gold: ['Linda Gauthier Basement Water Claim Restoration'])
- [500] R010.p2 reuse **error**: "start a claim fle for linda's basement" → [] (gold: ['Linda Gauthier Basement Water Claim Restoration'])
- [500] R010.p3 reuse **error**: "Could you open a new claim file for Linda's basement? She's reported damage and we need to get it started." → [] (gold: ['Linda Gauthier Basement Water Claim Restoration'])
- [500] R011 reuse **error**: "what's still missing for jordan's home and auto quote?" → ['Jordan Whitfield Home and Auto Quote'] (gold: ['Jordan Whitfield Home and Auto Quote'])
- [500] R011.p1 reuse **error**: "whats still missing for jordans home and auto quote" → [] (gold: ['Jordan Whitfield Home and Auto Quote'])
- [500] R011.p2 reuse **error**: "whats still missng for jordan's home and auto quote?" → [] (gold: ['Jordan Whitfield Home and Auto Quote'])
- [500] R011.p3 reuse **error**: "Could you let me know what is still missing for Jordan's home and auto quote so I can follow up on it?" → [] (gold: ['Jordan Whitfield Home and Auto Quote'])
- [500] R012 reuse **error**: "when is the team meeting this week?" → ['Team Meeting Reschedule Wed 10am'] (gold: ['Team Meeting Reschedule Wed 10am'])
- [500] R012.p1 reuse **error**: "when is the team meeting this week" → ['Team Meeting Reschedule Wed 10am'] (gold: ['Team Meeting Reschedule Wed 10am'])
- [500] R012.p2 reuse **error**: "when is the team meting this week?" → [] (gold: ['Team Meeting Reschedule Wed 10am'])
- [500] R012.p3 reuse **error**: "Do you know when the team meeting is this week? I want to make sure I block the time on my calendar." → [] (gold: ['Team Meeting Reschedule Wed 10am'])
- [500] R013 reuse **error**: "where are we on Maya's certificate for the Regional Municipality of York job?" → [] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R013.p1 reuse **error**: "where we at on maya's certificate for the regional municipality of york job" → [] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R013.p2 reuse **error**: "wheres maya's cert at for the Regional Municipality of York job atm" → [] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R013.p3 reuse **error**: "Could you let me know where things stand with Maya's certificate for the Regional Municipality of York job?" → ['Maya Certificate York Status'] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R014 reuse **error**: "did Cardenas Bakery Inc. get their COI yet?" → [] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R014.p1 reuse **error**: "did cardenas bakery inc get their coi yet" → [] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R014.p2 reuse **error**: "has Cardenas Bakery Inc. gotten their COI yet" → [] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R014.p3 reuse **error**: "Do you know whether Cardenas Bakery Inc. has received their COI yet?" → ['Cardenas Bakery COI Regional Municipality of York'] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R015 reuse **error**: "where are we on Paula's certificate for the Lakeshore Industrial REIT job?" → [] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R015.p1 reuse **error**: "where we at on paula's certificate for the lakeshore industrial reit job" → [] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R015.p2 reuse **error**: "wheres paula's cert at for the Lakeshore Industrial REIT job" → [] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R015.p3 reuse **error**: "Could you let me know where things stand with Paula's certificate for the Lakeshore Industrial REIT job?" → ['Vargas Architecture COI Lakeshore Industrial REIT', 'Pereira Hardware COI Lakeshore Industrial REIT'] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R016 reuse **error**: "did Pereira Hardware Inc. get their COI yet?" → [] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R016.p1 reuse **error**: "did pereira hardware inc get their coi yet" → ['Pereira Hardware COI Lakeshore Industrial REIT'] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R016.p2 reuse **error**: "has Pereira Hardware Inc. gotten their COI yet" → [] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R016.p3 reuse **error**: "Do you know whether Pereira Hardware Inc. has received their COI yet?" → [] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R017 reuse **error**: "where are we on Arjun's certificate for the Dufferin Plaza Management job?" → [] (gold: ['Arjun Schmidt Certificate Request Dufferin Plaza'])
- [500] R017.p1 reuse **error**: "where we at on arjun's certificate for the dufferin plaza management job" → [] (gold: ['Arjun Schmidt Certificate Request Dufferin Plaza'])
- [500] R017.p2 reuse **error**: "wheres arjun's cert at for the Dufferin Plaza Management job" → [] (gold: ['Arjun Schmidt Certificate Request Dufferin Plaza'])
