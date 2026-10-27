# routing run 2026-10-27_124912 (baseline-r2)

git 98949d7 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 404.0s

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 131 | 72% | 75% | 21% | 2% | 38% | 5831.6 | 4.15 | 6.7 | 0.217 |
| 100 | 131 | 77% | 75% | 23% | 2% | 24% | 7177.6 | 4.19 | 6.46 | 0.2682 |
| 250 | 131 | 68% | 67% | 29% | 4% | 28% | 10507.6 | 4.37 | 6.17 | 0.3631 |
| 500 | 131 | 60% | 58% | 34% | 6% | 31% | 16135.6 | 4.34 | 6.18 | 0.5307 |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 40 | 86% | 33% |
| 100 | 88% | 28% |
| 250 | 79% | 22% |
| 500 | 68% | 22% |

Accuracy by case kind:

| Kind | 40 | 100 | 250 | 500 |
|---|---|---|---|---|
| ambiguous | 71% (n=7) | 86% (n=7) | 43% (n=7) | 14% (n=7) |
| lookalike | 83% (n=12) | 92% (n=12) | 83% (n=12) | 58% (n=12) |
| multi | 33% (n=3) | 67% (n=3) | 33% (n=3) | 33% (n=3) |
| new | 62% (n=29) | 76% (n=29) | 72% (n=29) | 69% (n=29) |
| none | 100% (n=8) | 100% (n=8) | 100% (n=8) | 100% (n=8) |
| reminder | 50% (n=20) | 60% (n=20) | 35% (n=20) | 40% (n=20) |
| reuse | 83% (n=52) | 77% (n=52) | 75% (n=52) | 65% (n=52) |

Failures (160), largest roster first:

- [500] R001 reuse **asked**: "what did alice chen say about lunch?" → asked: Alice suggested Thursday at 12:30 at Pinewood Kitchen. (gold: ['Lunch with Alice and Bob'])
- [500] R014 reuse **duplicate**: "did Cardenas Bakery Inc. get their COI yet?" → ['Cardenas Bakery COI Status'] (gold: ['Certificate for Maya Cardenas'])
- [500] R018 reuse **duplicate**: "did Schmidt Cleaning Services Ltd. get their COI yet?" → ['Schmidt Cleaning Services COI Status'] (gold: ['Certificate for Arjun Schmidt'])
- [500] R020 reuse **duplicate**: "did Ines send the renewal figures yet?" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R021 reuse **duplicate**: "where are we on Ana's certificate for the City of Markham job?" → ['Ana Markham Certificate Status'] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R023 reuse **wrong_agent**: "what's going on with the Malik renewal?" → ['Malik Cleaning Services Ltd. Renewal CPP-922123', 'Malik Architecture Ltd. Renewal BOP-801881'] (gold: ['Uma Malik Policy Renewal'])
- [500] R024 reuse **duplicate**: "did Uma send the renewal figures yet?" → ['Uma Renewal Figures Check'] (gold: ['Uma Malik Policy Renewal'])
- [500] R028 reuse **duplicate**: "did Vargas Architecture Inc. get their COI yet?" → ['Vargas Architecture COI Status'] (gold: ['Certificate for Ben Vargas'])
- [500] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R032 reuse **duplicate**: "did Malik Roofing Ltd. get their COI yet?" → ['Malik Roofing COI Status'] (gold: ['Certificate for Neil Malik'])
- [500] R034 reuse **duplicate**: "did Laila send the renewal figures yet?" → ['Laila Renewal Figures Check'] (gold: ['Sokolov Auto Body Ltd. Renewal CPP-561853'])
- [500] R036 reuse **duplicate**: "did Hana send the renewal figures yet?" → ['Hana Renewal Figures Check'] (gold: ['Hana Ellis Policy Renewal'])
- [500] R038 reuse **wrong_agent**: "did Javier send the renewal figures yet?" → ['Javier Sokolov Home Renewal 2025'] (gold: ['Patel renewal'])
- [500] R039 reuse **wrong_agent**: "where are we on Leah's certificate for the Bayview Commercial Properties job?" → ['Romano IT Consulting Inc. COI - Bayview Commercial Properties'] (gold: ['COI Reyes Roofing Inc.'])
- [500] R041 reuse **duplicate**: "Leah says something's wrong with the bill, look into it" → ['Leah Billing Issue'] (gold: ['Leah NSF Payment'])
- [500] R047 reuse **duplicate**: "did Uma send the VIN yet?" → ['Uma VIN Check'] (gold: ['Uma Toyota RAV4 Auto Policy'])
- [500] R050 reuse **wrong_agent**: "did billing get back to us about Nora's payment?" → ['Nora Singh Billing Check'] (gold: ['Nora Bhatt Billing Check'])
- [500] R052 reuse **duplicate**: "did Mona send the renovation receipts?" → ['Mona Renovation Receipts Search'] (gold: ['New business quote - Mona Fernandes'])
- [500] R053 lookalike **duplicate**: "Daniel Morin says something's wrong with the bill, look into it" → ['Daniel Morin Billing Check'] (gold: ['Daniel NSF Payment'])
- [500] R055 ambiguous **wrong_agent**: "any update from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [500] R056 lookalike **duplicate**: "what's still missing for Priya Malik's home quote?" → ['Priya Malik Home Quote Missing Items'] (gold: ['Priya quote'])
- [500] R058 ambiguous **duplicate**: "any update from Priya?" → ['Priya Update Check'] (gold: ['Priya quote', 'Priya Santos Billing Check'])
- [500] R059 lookalike **duplicate**: "did Maya Zhang send the VIN yet?" → ['Maya Zhang VIN Check'] (gold: ['Maya Tesla Model Y Auto Policy'])
- [500] R061 ambiguous **duplicate**: "any update from Maya?" → ['Maya Updates Check'] (gold: ['Maya Tesla Model Y Auto Policy', 'Storm Damage Claim - Maya Ibrahim'])
- [500] R063 lookalike **duplicate**: "did Omar Abbott send the VIN yet?" → ['Omar Abbott VIN Check'] (gold: ["Add Mazda to Omar's policy"])
- [500] R064 ambiguous **duplicate**: "any update from Omar?" → ['Omar Update Check'] (gold: ['Omar Kim Billing Check', "Add Mazda to Omar's policy"])
- [500] R067 ambiguous **guessed**: "any update from Elena?" → ['Elena theft claim'] (gold: ['Elena theft claim', 'Elena Kia Sportage Auto Policy'])
- [500] R069 lookalike **duplicate**: "did Ravi Novak send the VIN yet?" → ['Ravi Novak VIN Check'] (gold: ["Add Ford to Ravi's policy"])
- [500] R070 ambiguous **duplicate**: "any update from Ravi?" → ['Ravi Update Check'] (gold: ['Ravi Patel Water Damage Claim', "Add Ford to Ravi's policy"])
- [500] R072 new **merged_into_existing**: "what's going on with the Pereira renewal?" → ['Naveen Pereira Policy Renewal'] (gold: [])
- [500] R075 new **merged_into_existing**: "what's going on with the MacLeod renewal?" → ['MacLeod Brewing Co. Renewal BOP-857302'] (gold: [])
- [500] R077 new **merged_into_existing**: "where are we on Farah's certificate for the Lakeshore Industrial REIT job?" → ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'] (gold: [])
- [500] R080 new **merged_into_existing**: "what's going on with the Malik renewal?" → ['Malik Cleaning Services Ltd. Renewal CPP-922123', 'Malik Architecture Ltd. Renewal BOP-801881'] (gold: [])
- [500] R085 new **merged_into_existing**: "start a claim file for Leah's water damage" → ['Leah Pereira Water Damage Claim'] (gold: [])
- [500] R089 new **merged_into_existing**: "what's the status of Nora's theft claim?" → ['Nora Ivanova Auto Claim (2025)'] (gold: [])
- [500] R094 new **merged_into_existing**: "what's still missing for Ravi's condo quote?" → ['Ravi Fontaine Condo Insurance'] (gold: [])
- [500] R096 new **merged_into_existing**: "did Aisha send the VIN yet?" → ['Aisha quote'] (gold: [])
- [500] R099 new **merged_into_existing**: "what's going on with the okafor renewal?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: [])
- [500] R102 reminder **duplicate**: "remind me tomorrow at 10am to check daniel's certificate went out" → ['Daniel Okafor Certificate Reminder'] (gold: ['Okafor Landscaping COI - City of Vaughan'])
- [500] R103 reminder **duplicate**: "remind me tomorrow at 9am to call linda about the adjuster" → ['Linda Gauthier Adjuster Call Reminder'] (gold: ['Linda Gauthier Water Claim'])
- [500] R105 reminder **duplicate**: "remind me Wednesday at 10am to check that Paula's certificate was issued" → ['Paula Certificate Reminder'] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R107 reminder **duplicate**: "remind me next monday to chase Ines for the renewal numbers" → ['Reminder - Chase Ines Renewal Numbers'] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R108 reminder **duplicate**: "remind me Wednesday at 10am to check that Ana's certificate was issued" → ['Ana Certificate Reminder'] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R110 reminder **duplicate**: "remind me next monday to chase Farah for the renewal numbers" → ['Farah Renewal Numbers Reminder'] (gold: ['Farah Tran Policy Renewal'])
- [500] R112 reminder **duplicate**: "remind me next monday to chase Farah for the renewal numbers" → ['Chase Farah Renewal Reminder'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R114 reminder **duplicate**: "remind me next monday to chase Laila for the renewal numbers" → ['Laila Renewal Numbers Reminder'] (gold: ['Sokolov Auto Body Ltd. Renewal CPP-561853'])
- [500] R115 reminder **duplicate**: "remind me next monday to chase Hana for the renewal numbers" → ['Hana Renewal Numbers Reminder'] (gold: ['Hana Ellis Policy Renewal'])
- [500] R116 reminder **duplicate**: "remind me next monday to chase Javier for the renewal numbers" → ['Javier Renewal Numbers Reminder'] (gold: ['Patel renewal'])
- [500] R117 reminder **duplicate**: "remind me Wednesday at 10am to check that Leah's certificate was issued" → ['Leah Certificate Reminder'] (gold: ['COI Reyes Roofing Inc.'])
- [500] R118 reminder **duplicate**: "remind me thursday to update Leah on the billing issue" → ['Leah Billing Issue Reminder'] (gold: ['Leah NSF Payment'])
- [500] R120 multi **missed**: "which clients still owe me documents?" → ['Outstanding Client Documents'] (gold: ['Jordan Whitfield Home and Auto Quote', 'New business quote - Mona Fernandes', 'Priya quote'])
- [500] R122 multi **missed**: "any certificates still waiting to go out?" → ['Pending Certificates Status'] (gold: ['Okafor Landscaping COI - City of Vaughan', 'Certificate for Maya Cardenas', 'Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [250] R014 reuse **duplicate**: "did Cardenas Bakery Inc. get their COI yet?" → ['Cardenas Bakery COI Status'] (gold: ['Certificate for Maya Cardenas'])
- [250] R018 reuse **duplicate**: "did Schmidt Cleaning Services Ltd. get their COI yet?" → ['Schmidt Cleaning Services COI Status'] (gold: ['Certificate for Arjun Schmidt'])
- [250] R020 reuse **duplicate**: "did Ines send the renewal figures yet?" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [250] R021 reuse **duplicate**: "where are we on Ana's certificate for the City of Markham job?" → ['Ana Markham Certificate Status'] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [250] R028 reuse **duplicate**: "did Vargas Architecture Inc. get their COI yet?" → ['Vargas Architecture COI Status'] (gold: ['Certificate for Ben Vargas'])
- [250] R030 reuse **wrong_agent**: "did Farah send the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [250] R032 reuse **duplicate**: "did Malik Roofing Ltd. get their COI yet?" → ['Malik Roofing COI Status'] (gold: ['Certificate for Neil Malik'])
- [250] R034 reuse **wrong_agent**: "did Laila send the renewal figures yet?" → ['Laila Haddad Umbrella Policy Review'] (gold: ['Sokolov Auto Body Ltd. Renewal CPP-561853'])
