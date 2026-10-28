# routing run 2026-10-28_115057 (search-v3)

git 32ae5ef + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 235.9s

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 131 | 94% | 96% | 1% | 2% | 10% | 7593.5 | 4.83 | 7.87 | 0.3291 |
| 500 | 131 | 86% | 94% | 0% | 2% | 24% | 7378.0 | 5.07 | 8.48 | 0.3167 |

Agent search (`--agent-roster search`): how often the correct agent was among the agents shown, and how often the model called `find_relevant_agents`:

| Roster size | Correct agent shown (follow-ups) | Used the search tool |
|---|---|---|
| 40 | 100% | 18% |
| 500 | 100% | 13% |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 40 | 98% | 89% |
| 500 | 97% | 83% |

Accuracy by case kind:

| Kind | 40 | 500 |
|---|---|---|
| ambiguous | 86% (n=7) | 86% (n=7) |
| lookalike | 100% (n=12) | 100% (n=12) |
| multi | 67% (n=3) | 0% (n=3) |
| new | 90% (n=29) | 69% (n=29) |
| none | 100% (n=8) | 88% (n=8) |
| reminder | 90% (n=20) | 85% (n=20) |
| reuse | 98% (n=52) | 96% (n=52) |

Failures (27), largest roster first:

- [500] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R049 reuse **answered_without_agent**: "Nora says something's wrong with the bill, look into it" → [] (gold: ['Nora Bhatt Billing Check'])
- [500] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [500] R072 new **merged_into_existing**: "what's going on with the Pereira renewal?" → ['Naveen Pereira Policy Renewal'] (gold: [])
- [500] R075 new **merged_into_existing**: "what's going on with the MacLeod renewal?" → ['MacLeod Brewing Co. Renewal BOP-857302'] (gold: [])
- [500] R077 new **answered_without_agent**: "where are we on Farah's certificate for the Lakeshore Industrial REIT job?" → [] (gold: [])
- [500] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Malik Architecture Ltd. Renewal BOP-801881', 'Uma Malik Policy Renewal', 'Malik Cleaning Services Ltd. Renewal CPP-922123'] (gold: [])
- [500] R082 new **merged_into_existing**: "where are we on Hana's certificate for the Dufferin Plaza Management job?" → ['Certificate for Arjun Schmidt'] (gold: [])
- [500] R085 new **answered_without_agent**: "start a claim file for Leah's water damage" → [] (gold: [])
- [500] R087 new **merged_into_existing**: "did Adriana send the VIN yet?" → ["Add Volkswagen to Adriana's policy"] (gold: [])
- [500] R093 new **merged_into_existing**: "what's still missing for Owen's auto quote?" → ['Owen Fontaine Vehicle Addition'] (gold: [])
- [500] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [500] R108 reminder **answered_without_agent**: "remind me Wednesday at 10am to check that Ana's certificate was issued" → [] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R112 reminder **wrong_agent**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R113 reminder **answered_without_agent**: "remind me Wednesday at 10am to check that Neil's certificate was issued" → [] (gold: ['Certificate for Neil Malik'])
- [500] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding client documents'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
- [500] R121 multi **partial**: "give me a status update on all my open claims" → ['Aaron collision claim', 'Carmen hail claim', 'Colin hail claim', 'Ahmed hail claim', 'Elena theft claim', 'Water Damage Claim - Rachel Nguyen', 'Emily Castillo Collision Claim', 'Maya Abbott Storm Damage Claim', 'Lionel Walsh Water Damage Claim', 'Claims Handoff to Mei'] (gold: ['Linda Gauthier Water Claim', 'Storm Damage Claim - Maya Ibrahim', 'Elena theft claim'])
- [500] R122 multi **partial**: "any certificates still waiting to go out?" → ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Arjun Schmidt', 'Certificate for Neil Malik'] (gold: ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Maya Cardenas', 'Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R127 none **unneeded_agent**: "never mind, ignore that" → ['Lunch with Alice and Bob'] (gold: [])
- [40] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [40] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [40] R071 new **merged_into_existing**: "what's going on with the Cardenas renewal?" → ['Certificate for Maya Cardenas'] (gold: [])
- [40] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Uma Malik Policy Renewal'] (gold: [])
- [40] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [40] R103 reminder **duplicate**: "remind me tomorrow at 9am to call linda about the adjuster" → ['Reminder - Call Linda Gauthier'] (gold: ['Linda Gauthier Water Claim'])
- [40] R112 reminder **wrong_agent**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [40] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding Client Documents Check'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
