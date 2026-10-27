# routing run 2026-10-27_134806 (paraphrases)

git 98949d7 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 588.8s

**Warning:** 133 cases at roster 100 failed (LLM errors) and are excluded; that row is partial.
**Warning:** 372 cases at roster 250 failed (LLM errors) and are excluded; that row is partial.
**Warning:** 378 cases at roster 500 failed (LLM errors) and are excluded; that row is partial.

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 385 | 75% | 76% | 21% | 2% | 34% | 5833.5 | 3.99 | 5.76 | 0.6413 |
| 100 | 252 | 73% | 75% | 22% | 2% | 34% | 7179.7 | 4.04 | 6.34 | 0.536 |
| 250 | 13 | 77% | 71% | 29% | 0% | 50% | 10508.5 | 3.57 | 4.3 | 0.0963 |
| 500 | 7 | 14% | 25% | 75% | 0% | - | 16136.9 | 4.89 | 7.11 | 0.1349 |

| Roster size | Original prompts | Paraphrased prompts |
|---|---|---|
| 40 | - | 75% |
| 100 | - | 73% |
| 250 | - | 77% |
| 500 | - | 14% |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 40 | 87% | 44% |
| 100 | 82% | 49% |
| 250 | 80% | 50% |
| 500 | 33% | 0% |

Accuracy by case kind:

| Kind | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| ambiguous | 86% (n=21) | 61% (n=18) | 100% (n=1) | 0% (n=2) |
| lookalike | 78% (n=36) | 78% (n=36) | 0% (n=1) | - (n=0) |
| multi | 56% (n=9) | - (n=0) | - (n=0) | 0% (n=1) |
| new | 66% (n=87) | 66% (n=41) | 50% (n=2) | - (n=0) |
| none | 100% (n=24) | 100% (n=1) | 100% (n=3) | - (n=0) |
| reminder | 56% (n=52) | - (n=0) | 100% (n=1) | 0% (n=2) |
| reuse | 82% (n=156) | 74% (n=156) | 80% (n=5) | 50% (n=2) |

Failures (1057), largest roster first:

- [500] R001.p1 reuse **error**: "what did alice chen say about lunch" → [] (gold: ['Lunch with Alice and Bob'])
- [500] R001.p2 reuse **error**: "whats alice chen saying about lunch? didnt catch it" → [] (gold: ['Lunch with Alice and Bob'])
- [500] R001.p3 reuse **error**: "Could you remind me what Alice Chen said about lunch? I think she mentioned it earlier and I want to make sure I have the details right." → [] (gold: ['Lunch with Alice and Bob'])
- [500] R002.p1 reuse **error**: "is bob coming to lunch he said smth about food" → [] (gold: ['Lunch with Alice and Bob'])
- [500] R002.p2 reuse **error**: "is bob coming to lunch? he mentoned something about food" → asked: yep, bob's in. he's vegetarian, so that's probably the food thing. lunch is thursday 12:30 at pinewo (gold: ['Lunch with Alice and Bob'])
- [500] R002.p3 reuse **error**: "Do you know if Bob is coming to lunch? I think he mentioned something about food, and I want to check before I plan anything." → [] (gold: ['Lunch with Alice and Bob'])
- [500] R003.p1 reuse **error**: "draft a reply to alice park, say ill send the budget numbers thursday" → [] (gold: ['Q4 Budget Numbers for Alice Park'])
- [500] R003.p2 reuse **error**: "draft a reply to alice park saying ill send the budgt numbers thursday" → ['Q4 Budget Numbers for Alice Park'] (gold: ['Q4 Budget Numbers for Alice Park'])
- [500] R003.p3 reuse **error**: "Could you draft a reply to Alice Park letting her know I'll send the budget numbers on Thursday?" → [] (gold: ['Q4 Budget Numbers for Alice Park'])
- [500] R004.p1 reuse **error**: "what numbers does alice park need for the budget" → [] (gold: ['Q4 Budget Numbers for Alice Park'])
- [500] R004.p2 reuse **error**: "wat numbers does alice park need for the budget?" → [] (gold: ['Q4 Budget Numbers for Alice Park'])
- [500] R004.p3 reuse **error**: "Could you tell me which numbers Alice Park needs for the budget? I want to make sure I send her the right information." → [] (gold: ['Q4 Budget Numbers for Alice Park'])
- [500] R005.p1 reuse **error**: "prep the certificate daniel needs for the city contract" → [] (gold: ['Okafor Landscaping COI - City of Vaughan'])
- [500] R005.p2 reuse **error**: "prepare the cerificate Daniel needs for the city contract" → [] (gold: ['Okafor Landscaping COI - City of Vaughan'])
- [500] R005.p3 reuse **error**: "Could you prepare the certificate that Daniel needs for the city contract? He's waiting on it for that project." → [] (gold: ['Okafor Landscaping COI - City of Vaughan'])
- [500] R006.p1 reuse **error**: "daniel fixed the certificate holder name, use the new one" → [] (gold: ['Okafor Landscaping COI - City of Vaughan'])
- [500] R006.p2 reuse **error**: "daniel corrected the certifcate holder name, make sure we use the new one" → [] (gold: ['Okafor Landscaping COI - City of Vaughan'])
- [500] R006.p3 reuse **error**: "Daniel has corrected the certificate holder name, so please make sure we use the new version when we prepare or send it." → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Okafor Landscaping COI - City of Vaughan'])
- [500] R007.p1 reuse **error**: "add priyas new car to her policy" → [] (gold: ['Priya Sharma Auto Policy - Honda CR-V'])
- [500] R007.p2 reuse **error**: "add priya's new car to her polcy" → ['Priya Sharma Auto Policy - Honda CR-V'] (gold: ['Priya Sharma Auto Policy - Honda CR-V'])
- [500] R007.p3 reuse **error**: "Could you add Priya's new car to her policy? She recently bought it and needs it covered." → [] (gold: ['Priya Sharma Auto Policy - Honda CR-V'])
- [500] R008.p1 reuse **error**: "did priya send the vin yet" → [] (gold: ['Priya Sharma Auto Policy - Honda CR-V'])
- [500] R008.p2 reuse **error**: "did priya send the VIN yt?" → [] (gold: ['Priya Sharma Auto Policy - Honda CR-V'])
- [500] R008.p3 reuse **error**: "Has Priya sent the VIN yet? I need it to finish updating her policy for the new car." → [] (gold: ['Priya Sharma Auto Policy - Honda CR-V'])
- [500] R009.p1 reuse **error**: "marco says he got double charged, can you look into it" → [] (gold: ['Marco Rossi Billing Check'])
- [500] R009.p2 reuse **error**: "marco says he was double chrged, look into it pls" → [] (gold: ['Marco Rossi Billing Check'])
- [500] R009.p3 reuse **error**: "Marco says he was charged twice, so could you please look into it and see what happened?" → [] (gold: ['Marco Rossi Billing Check'])
- [500] R010.p1 reuse **error**: "open a claim file for lindas basement" → [] (gold: ['Linda Gauthier Water Claim'])
- [500] R010.p2 reuse **error**: "start a claim fle for linda's basement" → [] (gold: ['Linda Gauthier Water Claim'])
- [500] R010.p3 reuse **error**: "Could you open a new claim file for Linda's basement? She's reported damage and we need to get it started." → ['Linda Gauthier Water Claim'] (gold: ['Linda Gauthier Water Claim'])
- [500] R011.p1 reuse **error**: "whats still missing for jordans home and auto quote" → [] (gold: ['Jordan Whitfield Home and Auto Quote'])
- [500] R011.p2 reuse **error**: "whats still missng for jordan's home and auto quote?" → [] (gold: ['Jordan Whitfield Home and Auto Quote'])
- [500] R011.p3 reuse **error**: "Could you let me know what is still missing for Jordan's home and auto quote so I can follow up on it?" → [] (gold: ['Jordan Whitfield Home and Auto Quote'])
- [500] R012.p1 reuse **error**: "when is the team meeting this week" → [] (gold: ['Team Meeting Schedule'])
- [500] R012.p2 reuse **error**: "when is the team meting this week?" → [] (gold: ['Team Meeting Schedule'])
- [500] R012.p3 reuse **error**: "Do you know when the team meeting is this week? I want to make sure I block the time on my calendar." → [] (gold: ['Team Meeting Schedule'])
- [500] R013.p1 reuse **error**: "where we at on maya's certificate for the regional municipality of york job" → [] (gold: ['Certificate for Maya Cardenas'])
- [500] R013.p2 reuse **error**: "wheres maya's cert at for the Regional Municipality of York job atm" → [] (gold: ['Certificate for Maya Cardenas'])
- [500] R013.p3 reuse **error**: "Could you let me know where things stand with Maya's certificate for the Regional Municipality of York job?" → [] (gold: ['Certificate for Maya Cardenas'])
- [500] R014.p1 reuse **error**: "did cardenas bakery inc get their coi yet" → [] (gold: ['Certificate for Maya Cardenas'])
- [500] R014.p2 reuse **error**: "has Cardenas Bakery Inc. gotten their COI yet" → [] (gold: ['Certificate for Maya Cardenas'])
- [500] R014.p3 reuse **error**: "Do you know whether Cardenas Bakery Inc. has received their COI yet?" → ['Cardenas Bakery COI Status'] (gold: ['Certificate for Maya Cardenas'])
- [500] R015.p1 reuse **error**: "where we at on paula's certificate for the lakeshore industrial reit job" → [] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R015.p2 reuse **error**: "wheres paula's cert at for the Lakeshore Industrial REIT job" → [] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R015.p3 reuse **error**: "Could you let me know where things stand with Paula's certificate for the Lakeshore Industrial REIT job?" → [] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R016.p1 reuse **error**: "did pereira hardware inc get their coi yet" → [] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R016.p2 reuse **error**: "has Pereira Hardware Inc. gotten their COI yet" → ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R016.p3 reuse **error**: "Do you know whether Pereira Hardware Inc. has received their COI yet?" → [] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R017.p1 reuse **error**: "where we at on arjun's certificate for the dufferin plaza management job" → [] (gold: ['Certificate for Arjun Schmidt'])
- [500] R017.p2 reuse **error**: "wheres arjun's cert at for the Dufferin Plaza Management job" → [] (gold: ['Certificate for Arjun Schmidt'])
- [500] R017.p3 reuse **error**: "Could you let me know where things stand with Arjun's certificate for the Dufferin Plaza Management job?" → [] (gold: ['Certificate for Arjun Schmidt'])
- [500] R018.p1 reuse **error**: "did schmidt cleaning services ltd get their coi yet" → [] (gold: ['Certificate for Arjun Schmidt'])
- [500] R018.p2 reuse **error**: "has Schmidt Cleaning Services Ltd. gotten their COI yet" → [] (gold: ['Certificate for Arjun Schmidt'])
- [500] R018.p3 reuse **error**: "Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet?" → [] (gold: ['Certificate for Arjun Schmidt'])
- [500] R019.p1 reuse **error**: "whats up with the kowalski renewal" → [] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R019.p2 reuse **error**: "hows the Kowalski renewal going" → ['Kowalski Electric Ltd. Renewal CPP-104292'] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R019.p3 reuse **error**: "Could you give me an update on the Kowalski renewal?" → [] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R020.p1 reuse **error**: "did ines send the renewal figures yet" → [] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R020.p2 reuse **error**: "has Ines sent over the renewal figures yet" → [] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R020.p3 reuse **error**: "Do you know whether Ines has sent the renewal figures yet?" → [] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
