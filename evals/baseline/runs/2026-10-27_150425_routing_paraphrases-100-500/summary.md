# routing run 2026-10-27_150425 (paraphrases-100-500)

git 98949d7 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 836.6s

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 100 | 385 | 74% | 70% | 27% | 2% | 24% | 7179.5 | 4.13 | 6.18 | 0.7827 |
| 250 | 385 | 68% | 68% | 27% | 4% | 33% | 10509.5 | 4.22 | 6.01 | 1.0719 |
| 500 | 385 | 59% | 58% | 38% | 4% | 33% | 16137.5 | 4.37 | 6.22 | 1.5842 |

| Roster size | Original prompts | Paraphrased prompts |
|---|---|---|
| 100 | - | 74% |
| 250 | - | 68% |
| 500 | - | 59% |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 100 | 80% | 43% |
| 250 | 78% | 38% |
| 500 | 66% | 35% |

Accuracy by case kind:

| Kind | 100 | 250 | 500 |
|---|---|---|---|
| ambiguous | 86% (n=21) | 43% (n=21) | 29% (n=21) |
| lookalike | 67% (n=36) | 69% (n=36) | 56% (n=36) |
| multi | 56% (n=9) | 33% (n=9) | 0% (n=9) |
| new | 76% (n=87) | 67% (n=87) | 67% (n=87) |
| none | 100% (n=24) | 100% (n=24) | 96% (n=24) |
| reminder | 52% (n=52) | 44% (n=52) | 31% (n=52) |
| reuse | 77% (n=156) | 76% (n=156) | 67% (n=156) |

Failures (383), largest roster first:

- [500] R014.p1 reuse **duplicate**: "did cardenas bakery inc get their coi yet" → ['Cardenas Bakery COI Status'] (gold: ['Certificate for Maya Cardenas'])
- [500] R014.p2 reuse **duplicate**: "has Cardenas Bakery Inc. gotten their COI yet" → ['Cardenas Bakery Inc COI Status'] (gold: ['Certificate for Maya Cardenas'])
- [500] R014.p3 reuse **duplicate**: "Do you know whether Cardenas Bakery Inc. has received their COI yet?" → ['Cardenas Bakery COI Status'] (gold: ['Certificate for Maya Cardenas'])
- [500] R015.p1 reuse **duplicate**: "where we at on paula's certificate for the lakeshore industrial reit job" → ['Paula Lakeshore REIT Certificate Status'] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R015.p2 reuse **duplicate**: "wheres paula's cert at for the Lakeshore Industrial REIT job" → ['Paula Lakeshore Certificate Status'] (gold: ['Pereira Hardware Inc. COI - Lakeshore Industrial REIT'])
- [500] R018.p1 reuse **duplicate**: "did schmidt cleaning services ltd get their coi yet" → ['Schmidt Cleaning Services COI Status'] (gold: ['Certificate for Arjun Schmidt'])
- [500] R018.p2 reuse **duplicate**: "has Schmidt Cleaning Services Ltd. gotten their COI yet" → ['Schmidt Cleaning Services COI Status'] (gold: ['Certificate for Arjun Schmidt'])
- [500] R018.p3 reuse **duplicate**: "Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet?" → ['Schmidt Cleaning Services COI Status'] (gold: ['Certificate for Arjun Schmidt'])
- [500] R020.p1 reuse **duplicate**: "did ines send the renewal figures yet" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R020.p2 reuse **duplicate**: "has Ines sent over the renewal figures yet" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R020.p3 reuse **duplicate**: "Do you know whether Ines has sent the renewal figures yet?" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric Ltd. Renewal CPP-104292'])
- [500] R021.p1 reuse **duplicate**: "where we at on anas certificate for the city of markham job" → ['Ana Markham Certificate Status'] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R021.p2 reuse **duplicate**: "wheres Ana's cert at for the City of Markham job" → ['Ana Markham Certificate Search'] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R021.p3 reuse **duplicate**: "Could you let me know where things stand with Ana's certificate for the City of Markham job?" → ['Ana Markham Certificate Status'] (gold: ['MacLeod Print Shop Ltd. COI - City of Markham'])
- [500] R023.p1 reuse **wrong_agent**: "whats up with the malik renewal" → ['Malik Cleaning Services Ltd. Renewal CPP-922123', 'Malik Architecture Ltd. Renewal BOP-801881'] (gold: ['Uma Malik Policy Renewal'])
- [500] R023.p2 reuse **wrong_agent**: "hows the Malik renewal going" → ['Malik Cleaning Services Ltd. Renewal CPP-922123', 'Malik Architecture Ltd. Renewal BOP-801881'] (gold: ['Uma Malik Policy Renewal'])
- [500] R023.p3 reuse **wrong_agent**: "Could you give me an update on the Malik renewal?" → ['Malik Cleaning Services Ltd. Renewal CPP-922123', 'Malik Architecture Ltd. Renewal BOP-801881'] (gold: ['Uma Malik Policy Renewal'])
- [500] R024.p1 reuse **duplicate**: "did uma send the renewal figures yet" → ['Uma Renewal Figures Check'] (gold: ['Uma Malik Policy Renewal'])
- [500] R024.p3 reuse **duplicate**: "Do you know whether Uma has sent the renewal figures yet?" → ['Uma Renewal Figures Check'] (gold: ['Uma Malik Policy Renewal'])
- [500] R028.p1 reuse **duplicate**: "did vargas architecture inc get their coi yet" → ['Vargas Architecture COI Status'] (gold: ['Certificate for Ben Vargas'])
- [500] R028.p2 reuse **duplicate**: "Has Vargas Architecture Inc. received their COI yet?" → ['Vargas Architecture COI Status'] (gold: ['Certificate for Ben Vargas'])
- [500] R028.p3 reuse **duplicate**: "Could you let me know if Vargas Architecture Inc. has gotten their COI yet?" → ['Vargas Architecture COI Status'] (gold: ['Certificate for Ben Vargas'])
- [500] R030.p1 reuse **wrong_agent**: "did farah send the renewal figs yet" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R030.p2 reuse **wrong_agent**: "Has Farah sent over the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R030.p3 reuse **wrong_agent**: "Could you check whether Farah has sent the renewal figures yet?" → ['Farah Tran Policy Renewal'] (gold: ['Tremblay Roofing Ltd. Renewal BOP-104123'])
- [500] R032.p1 reuse **duplicate**: "did malik roofing ltd get their coi yet" → ['Malik Roofing COI Status'] (gold: ['Certificate for Neil Malik'])
- [500] R032.p2 reuse **duplicate**: "Has Malik Roofing Ltd. received their COI yet?" → ['Malik Roofing COI Check'] (gold: ['Certificate for Neil Malik'])
- [500] R032.p3 reuse **duplicate**: "Could you let me know if Malik Roofing Ltd. has gotten their COI yet?" → ['Malik Roofing COI Status'] (gold: ['Certificate for Neil Malik'])
- [500] R034.p1 reuse **duplicate**: "did laila send the renewal figs yet" → ['Laila Renewal Figures Check'] (gold: ['Sokolov Auto Body Ltd. Renewal CPP-561853'])
- [500] R034.p2 reuse **duplicate**: "Has Laila sent over the renewal figures yet?" → ['Laila Renewal Figures Check'] (gold: ['Sokolov Auto Body Ltd. Renewal CPP-561853'])
- [500] R034.p3 reuse **wrong_agent**: "Could you check whether Laila has sent the renewal figures yet?" → ['Laila Haddad Umbrella Policy Review'] (gold: ['Sokolov Auto Body Ltd. Renewal CPP-561853'])
- [500] R036.p1 reuse **duplicate**: "did hana send the renewal figs yet" → ['Hana Renewal Figures Check'] (gold: ['Hana Ellis Policy Renewal'])
- [500] R036.p2 reuse **wrong_agent**: "Has Hana sent over the renewal figures yet?" → ['Hana Ibrahim Home Renewal 2025'] (gold: ['Hana Ellis Policy Renewal'])
- [500] R036.p3 reuse **duplicate**: "Could you check whether Hana has sent the renewal figures yet?" → ['Hana renewal figures check'] (gold: ['Hana Ellis Policy Renewal'])
- [500] R038.p1 reuse **wrong_agent**: "javier send the renewal figs yet" → ['Javier Sokolov Home Renewal 2025'] (gold: ['Patel renewal'])
- [500] R038.p2 reuse **wrong_agent**: "has Javier sent the renewal figs yet?" → ['Javier Sokolov Home Renewal 2025'] (gold: ['Patel renewal'])
- [500] R038.p3 reuse **wrong_agent**: "Do you know if Javier has sent over the renewal figures yet?" → ['Javier Sokolov Home Renewal 2025'] (gold: ['Patel renewal'])
- [500] R039.p1 reuse **duplicate**: "wheres leahs cert for bayview commercial properties job" → ['Leah Bayview Certificate Search'] (gold: ['COI Reyes Roofing Inc.'])
- [500] R039.p2 reuse **duplicate**: "where we at on Leah's certificate for the Bayview Commercial Properties job?" → ['Leah Bayview Certificate Status'] (gold: ['COI Reyes Roofing Inc.'])
- [500] R039.p3 reuse **duplicate**: "Could you update me on where things stand with Leah's certificate for the Bayview Commercial Properties job?" → ['Leah Bayview Certificate Status'] (gold: ['COI Reyes Roofing Inc.'])
- [500] R041.p1 reuse **duplicate**: "leah says somethings off w the bill, check it" → ['Leah Bill Check'] (gold: ['Leah NSF Payment'])
- [500] R041.p2 reuse **duplicate**: "Leah says something's wrong with the bil, can you look into it" → ['Leah Billing Issue'] (gold: ['Leah NSF Payment'])
- [500] R041.p3 reuse **duplicate**: "Leah mentioned that something seems to be wrong with the bill, could you please look into it?" → ['Leah Bill Issue'] (gold: ['Leah NSF Payment'])
- [500] R047.p2 reuse **duplicate**: "did Uma send the VN yet?" → ['Uma VN Check'] (gold: ['Uma Toyota RAV4 Auto Policy'])
- [500] R049.p1 reuse **duplicate**: "nora says bill's wrong, check it" → ['Nora Bill Dispute Check'] (gold: ['Nora Bhatt Billing Check'])
- [500] R049.p2 reuse **duplicate**: "Nora says somethings wrong with the bil, look into it" → ['Nora Billing Issue Investigation'] (gold: ['Nora Bhatt Billing Check'])
- [500] R049.p3 reuse **duplicate**: "Nora mentioned that something looks wrong with the bill, could you please look into it?" → ['Nora Bill Issue Check'] (gold: ['Nora Bhatt Billing Check'])
- [500] R050.p2 reuse **duplicate**: "did billng get back to us about Nora's paymnt?" → ['Nora Payment Billing Status'] (gold: ['Nora Bhatt Billing Check'])
- [500] R052.p1 reuse **duplicate**: "did mona send the reno receipts" → ['Mona Reno Receipts'] (gold: ['New business quote - Mona Fernandes'])
- [500] R052.p2 reuse **duplicate**: "did Mona send the renovaton receipts?" → ['Mona Renovation Receipts Check'] (gold: ['New business quote - Mona Fernandes'])
- [500] R052.p3 reuse **duplicate**: "Do you know if Mona has sent over the renovation receipts yet?" → ['Mona Renovation Receipts Check'] (gold: ['New business quote - Mona Fernandes'])
- [500] R053.p1 lookalike **duplicate**: "daniel morin says bill's wrong, check it" → ['Daniel Morin Billing Check'] (gold: ['Daniel NSF Payment'])
- [500] R053.p2 lookalike **duplicate**: "Daniel Morin says somethings wrong wit the bill, look into it" → ['Daniel Morin Billing Check'] (gold: ['Daniel NSF Payment'])
- [500] R053.p3 lookalike **duplicate**: "Daniel Morin mentioned that something seems off with the bill, could you please look into it?" → ['Daniel Morin Billing Check'] (gold: ['Daniel NSF Payment'])
- [500] R055.p1 ambiguous **wrong_agent**: "any news from daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [500] R055.p2 ambiguous **wrong_agent**: "any updte from Daniel?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [500] R055.p3 ambiguous **wrong_agent**: "Do you have any update from Daniel yet?" → ['Okafor Landscaping COI - City of Vaughan'] (gold: ['Daniel NSF Payment', 'Daniel Alvarez Vehicle Addition'])
- [500] R056.p2 lookalike **duplicate**: "what's stil missing for Priya Malik's home quote?" → ['Priya Malik Home Quote Status'] (gold: ['Priya quote'])
- [500] R056.p3 lookalike **duplicate**: "Could you let me know what's still missing for Priya Malik's home quote?" → ['Priya Malik Home Quote Status'] (gold: ['Priya quote'])
- [500] R058.p1 ambiguous **wrong_agent**: "any news from priya?" → ['Priya Sharma Auto Policy - Honda CR-V'] (gold: ['Priya quote', 'Priya Santos Billing Check'])
