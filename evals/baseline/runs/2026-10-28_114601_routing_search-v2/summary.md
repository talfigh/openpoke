# routing run 2026-10-28_114601 (search-v2)

git 32ae5ef + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 247.6s

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 131 | 88% | 95% | 2% | 2% | 28% | 7535.5 | 5.03 | 8.53 | 0.3246 |
| 500 | 131 | 78% | 92% | 5% | 2% | 38% | 7320.0 | 5.27 | 8.73 | 0.3227 |

Agent search (`--agent-roster search`): how often the correct agent was among the agents shown, and how often the model called `find_relevant_agents`:

| Roster size | Correct agent shown (follow-ups) | Used the search tool |
|---|---|---|
| 40 | 100% | 18% |
| 500 | 100% | 15% |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 40 | 97% | 89% |
| 500 | 94% | 83% |

Accuracy by case kind:

| Kind | 40 | 500 |
|---|---|---|
| ambiguous | 86% (n=7) | 71% (n=7) |
| lookalike | 92% (n=12) | 83% (n=12) |
| multi | 33% (n=3) | 0% (n=3) |
| new | 69% (n=29) | 41% (n=29) |
| none | 100% (n=8) | 100% (n=8) |
| reminder | 90% (n=20) | 85% (n=20) |
| reuse | 98% (n=52) | 96% (n=52) |

Failures (45), largest roster first:

- [500] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R049 reuse **asked**: "Nora says something's wrong with the bill, look into it" → asked: Which Nora? I've got two billing files open: Nora Bhatt ($142 payment plan) and Nora Singh ($111 NSF (gold: ['Nora Bhatt Billing Check'])
- [500] R053 lookalike **duplicate**: "Daniel Morin says something's wrong with the bill, look into it" → ['Daniel Morin Bill Dispute'] (gold: ['Daniel NSF Payment'])
- [500] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [500] R057 lookalike **duplicate**: "Priya Santos says something's wrong with the bill, look into it" → ['Priya Santos Billing Issue'] (gold: ['Priya Santos Billing Check'])
- [500] R061 ambiguous **duplicate**: "any update from Maya?" → ['Maya Updates Check'] (gold: ['Maya Tesla Model Y Auto Policy', 'Storm Damage Claim - Maya Ibrahim'])
- [500] R072 new **merged_into_existing**: "what's going on with the Pereira renewal?" → ['Naveen Pereira Policy Renewal'] (gold: [])
- [500] R073 new **asked**: "what's going on with the Schmidt renewal?" → asked: Checking on the Schmidt renewal now. (gold: [])
- [500] R074 new **merged_into_existing**: "where are we on Ines's certificate for the Dufferin Plaza Management job?" → ['Certificate for Arjun Schmidt'] (gold: [])
- [500] R075 new **merged_into_existing**: "what's going on with the MacLeod renewal?" → ['MacLeod Brewing Co. Renewal BOP-857302'] (gold: [])
- [500] R077 new **asked**: "where are we on Farah's certificate for the Lakeshore Industrial REIT job?" → asked: Checking on that now. I don't see a certificate tied to Farah for Lakeshore Industrial REIT in my li (gold: [])
- [500] R078 new **answered_without_agent**: "what's going on with the Vargas renewal?" → [] (gold: [])
- [500] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Malik Architecture Ltd. Renewal BOP-801881', 'Uma Malik Policy Renewal', 'Malik Cleaning Services Ltd. Renewal CPP-922123'] (gold: [])
- [500] R081 new **asked**: "where are we on Laila's certificate for the City of Pickering job?" → asked: Checking on that now. I don't see a Pickering certificate in my active list, so I'm searching for it (gold: [])
- [500] R082 new **merged_into_existing**: "where are we on Hana's certificate for the Dufferin Plaza Management job?" → ['Certificate for Arjun Schmidt'] (gold: [])
- [500] R083 new **merged_into_existing**: "where are we on Javier's certificate for the Town of Ajax job?" → ['New business quote - Javier Zhang'] (gold: [])
- [500] R085 new **answered_without_agent**: "start a claim file for Leah's water damage" → [] (gold: [])
- [500] R086 new **merged_into_existing**: "what's still missing for Paolo's home and auto quote?" → ['Paolo Cardenas Auto Claim (2025)'] (gold: [])
- [500] R087 new **merged_into_existing**: "did Adriana send the VIN yet?" → ["Add Volkswagen to Adriana's policy"] (gold: [])
- [500] R089 new **asked**: "what's the status of Nora's theft claim?" → asked: Checking on that now. I don't see an open theft claim under Nora's name in my list, so I'm searching (gold: [])
- [500] R093 new **merged_into_existing**: "what's still missing for Owen's auto quote?" → ['Owen Fontaine Vehicle Addition'] (gold: [])
- [500] R094 new **merged_into_existing**: "what's still missing for Ravi's condo quote?" → ['Ravi Fontaine Condo Insurance'] (gold: [])
- [500] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [500] R108 reminder **duplicate**: "remind me Wednesday at 10am to check that Ana's certificate was issued" → ['Wednesday Ana Certificate Reminder'] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R111 reminder **duplicate**: "remind me Wednesday at 10am to check that Ben's certificate was issued" → ['Ben Vargas Certificate Reminder'] (gold: ['Certificate for Ben Vargas'])
- [500] R112 reminder **wrong_agent**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding Client Documents'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
- [500] R121 multi **partial**: "give me a status update on all my open claims" → ['Aaron collision claim', 'Carmen hail claim', 'Colin hail claim', 'Ahmed hail claim', 'Elena theft claim', 'Water Damage Claim - Rachel Nguyen', 'Emily Castillo Collision Claim', 'Maya Abbott Storm Damage Claim', 'Lionel Walsh Water Damage Claim', 'Claims Handoff to Mei'] (gold: ['Linda Gauthier Water Claim', 'Storm Damage Claim - Maya Ibrahim', 'Elena theft claim'])
- [500] R122 multi **partial**: "any certificates still waiting to go out?" → ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Neil Malik', 'Certificate for Arjun Schmidt'] (gold: ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Maya Cardenas', 'Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [40] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [40] R053 lookalike **duplicate**: "Daniel Morin says something's wrong with the bill, look into it" → ['Daniel Morin Billing Issue'] (gold: ['Daniel NSF Payment'])
- [40] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [40] R071 new **merged_into_existing**: "what's going on with the Cardenas renewal?" → ['Certificate for Maya Cardenas'] (gold: [])
- [40] R074 new **merged_into_existing**: "where are we on Ines's certificate for the Dufferin Plaza Management job?" → ['Certificate for Arjun Schmidt'] (gold: [])
- [40] R077 new **merged_into_existing**: "where are we on Farah's certificate for the Lakeshore Industrial REIT job?" → ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'] (gold: [])
- [40] R078 new **merged_into_existing**: "what's going on with the Vargas renewal?" → ['Certificate for Ben Vargas'] (gold: [])
- [40] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Uma Malik Policy Renewal'] (gold: [])
- [40] R082 new **merged_into_existing**: "where are we on Hana's certificate for the Dufferin Plaza Management job?" → ['Certificate for Arjun Schmidt'] (gold: [])
- [40] R084 new **merged_into_existing**: "what's going on with the Reyes renewal?" → ['COI Reyes Roofing Inc.'] (gold: [])
- [40] R088 new **asked**: "start a claim file for Uma's water damage" → asked: On it. Checking whether there's already a water damage file for Uma. (gold: [])
- [40] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [40] R103 reminder **duplicate**: "remind me tomorrow at 9am to call linda about the adjuster" → ['Linda Adjuster Call Reminder'] (gold: ['Linda Gauthier Water Claim'])
- [40] R112 reminder **wrong_agent**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [40] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding Client Documents'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
- [40] R122 multi **missed**: "any certificates still waiting to go out?" → ['Pending Certificates Status Check'] (gold: ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Maya Cardenas', 'Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
