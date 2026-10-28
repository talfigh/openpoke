# routing run 2026-10-28_114050 (search-v1)

git 32ae5ef + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 227.9s

**Warning:** 1 cases at roster 500 failed (LLM errors) and are excluded; that row is partial.

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 131 | 85% | 98% | 0% | 2% | 45% | 7354.5 | 4.48 | 7.66 | 0.3078 |
| 500 | 130 | 82% | 94% | 1% | 2% | 41% | 7141.0 | 4.83 | 7.36 | 0.3107 |

Agent search (`--agent-roster search`): how often the correct agent was among the agents shown, and how often the model called `find_relevant_agents`:

| Roster size | Correct agent shown (follow-ups) | Used the search tool |
|---|---|---|
| 40 | 100% | 18% |
| 500 | 100% | 14% |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 40 | 100% | 89% |
| 500 | 97% | 83% |

Accuracy by case kind:

| Kind | 40 | 500 |
|---|---|---|
| ambiguous | 71% (n=7) | 71% (n=7) |
| lookalike | 100% (n=12) | 100% (n=12) |
| multi | 33% (n=3) | 33% (n=3) |
| new | 52% (n=29) | 48% (n=29) |
| none | 100% (n=8) | 100% (n=8) |
| reminder | 95% (n=20) | 85% (n=20) |
| reuse | 98% (n=52) | 96% (n=51) |

Failures (45), largest roster first:

- [500] R008 reuse **error**: "did priya send the VIN yet?" → ['Priya Sharma Auto Policy - Honda CR-V'] (gold: ['Priya Sharma Auto Policy - Honda CR-V'])
- [500] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R049 reuse **answered_without_agent**: "Nora says something's wrong with the bill, look into it" → [] (gold: ['Nora Bhatt Billing Check'])
- [500] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [500] R064 ambiguous **duplicate**: "any update from Omar?" → ['Omar Updates Check'] (gold: ['Omar Kim Billing Check', "Add Mazda to Omar's policy"])
- [500] R072 new **merged_into_existing**: "what's going on with the Pereira renewal?" → ['Naveen Pereira Policy Renewal'] (gold: [])
- [500] R074 new **asked**: "where are we on Ines's certificate for the Dufferin Plaza Management job?" → asked: Checking on that now. The Dufferin Plaza Management certificate I have on file is for Arjun Schmidt, (gold: [])
- [500] R075 new **merged_into_existing**: "what's going on with the MacLeod renewal?" → ['MacLeod Brewing Co. Renewal BOP-857302'] (gold: [])
- [500] R076 new **merged_into_existing**: "where are we on Uma's certificate for the Kingsway Realty Holdings job?" → ['Abbott Architecture Inc. COI - Kingsway Realty Holdings'] (gold: [])
- [500] R077 new **merged_into_existing**: "where are we on Farah's certificate for the Lakeshore Industrial REIT job?" → ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'] (gold: [])
- [500] R078 new **asked**: "what's going on with the Vargas renewal?" → asked: No single Vargas renewal file that I can see. Here's where the Vargas files stand:

- Rachel Vargas: (gold: [])
- [500] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Malik Architecture Ltd. Renewal BOP-801881', 'Uma Malik Policy Renewal', 'Malik Cleaning Services Ltd. Renewal CPP-922123'] (gold: [])
- [500] R082 new **merged_into_existing**: "where are we on Hana's certificate for the Dufferin Plaza Management job?" → ['Certificate for Arjun Schmidt'] (gold: [])
- [500] R085 new **asked**: "start a claim file for Leah's water damage" → asked: Leah Pereira's water claim is already open: CLM-2614663 with Northern Shield. Adjuster Paula Jensen  (gold: [])
- [500] R087 new **merged_into_existing**: "did Adriana send the VIN yet?" → ["Add Volkswagen to Adriana's policy"] (gold: [])
- [500] R089 new **merged_into_existing**: "what's the status of Nora's theft claim?" → ['Nora Ivanova Auto Claim (2025)'] (gold: [])
- [500] R091 new **merged_into_existing**: "start a claim file for Felix's hail damage" → ['Felix Lefebvre Burglary Claim'] (gold: [])
- [500] R093 new **merged_into_existing**: "what's still missing for Owen's auto quote?" → ['Owen Fontaine Vehicle Addition'] (gold: [])
- [500] R094 new **merged_into_existing**: "what's still missing for Ravi's condo quote?" → ['Ravi Fontaine Condo Insurance'] (gold: [])
- [500] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [500] R108 reminder **answered_without_agent**: "remind me Wednesday at 10am to check that Ana's certificate was issued" → [] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R112 reminder **wrong_agent**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R119 reminder **duplicate**: "remind me thursday to update Paolo on the billing issue" → ['Paolo Schmidt Billing Reminder'] (gold: ['Billing issue - Paolo Schmidt'])
- [500] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding client documents'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
- [500] R122 multi **partial**: "any certificates still waiting to go out?" → ['Certificate for Arjun Schmidt', 'Certificate for Neil Malik', 'Okafor Landscaping COI - City of Vaughan'] (gold: ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Maya Cardenas', 'Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [40] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [40] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [40] R061 ambiguous **answered_without_agent**: "any update from Maya?" → [] (gold: ['Maya Tesla Model Y Auto Policy', 'Storm Damage Claim - Maya Ibrahim'])
- [40] R071 new **merged_into_existing**: "what's going on with the Cardenas renewal?" → ['Certificate for Maya Cardenas'] (gold: [])
- [40] R074 new **merged_into_existing**: "where are we on Ines's certificate for the Dufferin Plaza Management job?" → ['Certificate for Arjun Schmidt'] (gold: [])
- [40] R075 new **merged_into_existing**: "what's going on with the MacLeod renewal?" → ['MacLeod Print Shop Ltd. COI - City of Markham'] (gold: [])
- [40] R077 new **merged_into_existing**: "where are we on Farah's certificate for the Lakeshore Industrial REIT job?" → ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'] (gold: [])
- [40] R078 new **merged_into_existing**: "what's going on with the Vargas renewal?" → ['Certificate for Ben Vargas'] (gold: [])
- [40] R079 new **merged_into_existing**: "where are we on Farah's certificate for the City of Mississauga job?" → ['Farah Tran Policy Renewal'] (gold: [])
- [40] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Uma Malik Policy Renewal'] (gold: [])
- [40] R082 new **merged_into_existing**: "where are we on Hana's certificate for the Dufferin Plaza Management job?" → ['Certificate for Arjun Schmidt'] (gold: [])
- [40] R084 new **merged_into_existing**: "what's going on with the Reyes renewal?" → ['COI Reyes Roofing Inc.'] (gold: [])
- [40] R086 new **merged_into_existing**: "what's still missing for Paolo's home and auto quote?" → ['Billing issue - Paolo Schmidt'] (gold: [])
- [40] R087 new **asked**: "did Adriana send the VIN yet?" → asked: Checking on that now. (gold: [])
- [40] R089 new **merged_into_existing**: "what's the status of Nora's theft claim?" → ['Nora Bhatt Billing Check'] (gold: [])
- [40] R092 new **merged_into_existing**: "what's the status of Javier's collision claim?" → ['Patel renewal'] (gold: [])
- [40] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [40] R112 reminder **wrong_agent**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [40] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding Client Documents'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
- [40] R122 multi **missed**: "any certificates still waiting to go out?" → ['COI Pending Status Check'] (gold: ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Maya Cardenas', 'Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
