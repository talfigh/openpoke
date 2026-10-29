# routing run 2026-10-29_121004 (search-final-confirm)

git bfb64b1 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 222.7s

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 131 | 91% | 96% | 1% | 2% | 21% | 7569.2 | 4.43 | 6.67 | 0.2787 |
| 500 | 131 | 86% | 93% | 4% | 2% | 21% | 7310.3 | 4.83 | 7.62 | 0.2884 |

Agent search (`--agent-roster search`): how often the correct agent was among the agents shown:

| Roster size | Correct agent shown (follow-ups) |
|---|---|
| 40 | 100% |
| 500 | 100% |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 40 | 98% | 89% |
| 500 | 97% | 78% |

Accuracy by case kind:

| Kind | 40 | 500 |
|---|---|---|
| ambiguous | 86% (n=7) | 57% (n=7) |
| lookalike | 100% (n=12) | 100% (n=12) |
| multi | 33% (n=3) | 0% (n=3) |
| new | 79% (n=29) | 76% (n=29) |
| none | 100% (n=8) | 100% (n=8) |
| reminder | 95% (n=20) | 85% (n=20) |
| reuse | 96% (n=52) | 94% (n=52) |

Failures (31), largest roster first:

- [500] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R045 reuse **duplicate**: "Adriana says something's wrong with the bill, look into it" → ['Adriana Bill Dispute'] (gold: ['Adriana Pereira Billing Check'])
- [500] R049 reuse **asked**: "Nora says something's wrong with the bill, look into it" → asked: which Nora? I've got two billing files open: Nora Bhatt ($142, payment plan) and Nora Singh ($111, N (gold: ['Nora Bhatt Billing Check'])
- [500] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [500] R064 ambiguous **duplicate**: "any update from Omar?" → ['Omar Updates Check'] (gold: ['Omar Kim Billing Check', "Add Mazda to Omar's policy"])
- [500] R070 ambiguous **duplicate**: "any update from Ravi?" → ['Ravi Updates Check'] (gold: ['Ravi Patel Water Damage Claim', "Add Ford to Ravi's policy"])
- [500] R072 new **merged_into_existing**: "what's going on with the Pereira renewal?" → ['Naveen Pereira Policy Renewal'] (gold: [])
- [500] R075 new **merged_into_existing**: "what's going on with the MacLeod renewal?" → ['MacLeod Brewing Co. Renewal BOP-857302'] (gold: [])
- [500] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Malik Architecture Ltd. Renewal BOP-801881', 'Uma Malik Policy Renewal', 'Malik Cleaning Services Ltd. Renewal CPP-922123'] (gold: [])
- [500] R085 new **answered_without_agent**: "start a claim file for Leah's water damage" → [] (gold: [])
- [500] R087 new **merged_into_existing**: "did Adriana send the VIN yet?" → ["Add Volkswagen to Adriana's policy"] (gold: [])
- [500] R093 new **merged_into_existing**: "what's still missing for Owen's auto quote?" → ['Owen Fontaine Vehicle Addition'] (gold: [])
- [500] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [500] R108 reminder **duplicate**: "remind me Wednesday at 10am to check that Ana's certificate was issued" → ['Ana Certificate Reminder Wednesday'] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R112 reminder **wrong_agent**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R117 reminder **duplicate**: "remind me Wednesday at 10am to check that Leah's certificate was issued" → ['Reminder - Leah COI check Wed 10am'] (gold: ['COI Reyes Roofing Inc.'])
- [500] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding Client Documents'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
- [500] R121 multi **partial**: "give me a status update on all my open claims" → ['Linda Gauthier Basement Claim', 'Aaron collision claim', 'Carmen hail claim', 'Colin hail claim', 'Ahmed hail claim', 'Elena theft claim', 'Water Damage Claim - Rachel Nguyen', 'Emily Castillo Collision Claim', 'Maya Abbott Storm Damage Claim', 'Lionel Walsh Water Damage Claim', 'Claims Handoff to Mei'] (gold: ['Linda Gauthier Water Claim', 'Storm Damage Claim - Maya Ibrahim', 'Elena theft claim'])
- [500] R122 multi **partial**: "any certificates still waiting to go out?" → ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Neil Malik', 'Certificate for Arjun Schmidt'] (gold: ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Maya Cardenas', 'Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [40] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [40] R045 reuse **duplicate**: "Adriana says something's wrong with the bill, look into it" → ['Adriana Pereira Billing Issue Review'] (gold: ['Adriana Pereira Billing Check'])
- [40] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [40] R071 new **merged_into_existing**: "what's going on with the Cardenas renewal?" → ['Certificate for Maya Cardenas'] (gold: [])
- [40] R073 new **merged_into_existing**: "what's going on with the Schmidt renewal?" → ['Certificate for Arjun Schmidt', 'Schmidt Renewal Search'] (gold: [])
- [40] R075 new **merged_into_existing**: "what's going on with the MacLeod renewal?" → ['MacLeod Print Shop Ltd. COI - City of Markham'] (gold: [])
- [40] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Uma Malik Policy Renewal'] (gold: [])
- [40] R084 new **merged_into_existing**: "what's going on with the Reyes renewal?" → ['COI Reyes Roofing Inc.'] (gold: [])
- [40] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [40] R112 reminder **wrong_agent**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [40] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding Client Documents'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
- [40] R122 multi **missed**: "any certificates still waiting to go out?" → ['Certificate status check'] (gold: ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Maya Cardenas', 'Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
