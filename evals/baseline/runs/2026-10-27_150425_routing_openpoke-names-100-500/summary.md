# routing run 2026-10-27_150425 (openpoke-names-100-500)

git 98949d7 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 1215.1s

**Warning:** 6 cases at roster 500 failed (LLM errors) and are excluded; that row is partial.

| Roster size | Cases | Accuracy | Reuse acc. | Duplicate (reuse) | Misroute (reuse) | New merged | Prompt tokens (1st call) | p50 s | p95 s | Cost $ |
|---|---|---|---|---|---|---|---|---|---|---|
| 100 | 516 | 72% | 71% | 28% | 1% | 33% | 7552.0 | 4.19 | 6.5 | 1.0919 |
| 250 | 516 | 64% | 64% | 33% | 3% | 39% | 11385.0 | 4.29 | 6.29 | 1.5433 |
| 500 | 510 | 58% | 58% | 38% | 4% | 38% | 17626.0 | 4.6 | 7.16 | 2.2814 |

| Roster size | Original prompts | Paraphrased prompts |
|---|---|---|
| 100 | 70% | 73% |
| 250 | 62% | 64% |
| 500 | 59% | 58% |

Reuse accuracy split by whether the gold agent's name mentions the person in the prompt (the roster shows names only, so 'opaque' cases need agent metadata to solve):

| Roster size | Name mentions person | Name opaque |
|---|---|---|
| 100 | 89% | 39% |
| 250 | 81% | 33% |
| 500 | 76% | 27% |

Accuracy by case kind:

| Kind | 100 | 250 | 500 |
|---|---|---|---|
| ambiguous | 86% (n=28) | 64% (n=28) | 21% (n=28) |
| lookalike | 100% (n=48) | 100% (n=48) | 100% (n=42) |
| multi | 67% (n=12) | 8% (n=12) | 0% (n=12) |
| new | 67% (n=116) | 61% (n=116) | 62% (n=116) |
| none | 94% (n=32) | 94% (n=32) | 97% (n=32) |
| reminder | 25% (n=72) | 15% (n=72) | 14% (n=72) |
| reuse | 81% (n=208) | 72% (n=208) | 65% (n=208) |

Failures (549), largest roster first:

- [500] R013 reuse **duplicate**: "where are we on Maya's certificate for the Regional Municipality of York job?" → ['Maya Certificate York Status'] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R013.p1 reuse **duplicate**: "where we at on maya's certificate for the regional municipality of york job" → ['Maya Certificate Regional Municipality of York Status'] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R013.p2 reuse **duplicate**: "wheres maya's cert at for the Regional Municipality of York job atm" → ['Maya Certificate Status York'] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R013.p3 reuse **duplicate**: "Could you let me know where things stand with Maya's certificate for the Regional Municipality of York job?" → ['Maya Certificate York Status'] (gold: ['Cardenas Bakery COI Regional Municipality of York'])
- [500] R015 reuse **wrong_agent**: "where are we on Paula's certificate for the Lakeshore Industrial REIT job?" → ['Vargas Architecture COI Lakeshore Industrial REIT'] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R015.p1 reuse **wrong_agent**: "where we at on paula's certificate for the lakeshore industrial reit job" → ['Vargas Architecture COI Lakeshore Industrial REIT'] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R015.p2 reuse **duplicate**: "wheres paula's cert at for the Lakeshore Industrial REIT job" → ['Paula Lakeshore Certificate Status'] (gold: ['Pereira Hardware COI Lakeshore Industrial REIT'])
- [500] R018 reuse **duplicate**: "did Schmidt Cleaning Services Ltd. get their COI yet?" → ['Schmidt Cleaning COI Status'] (gold: ['Arjun Schmidt Certificate Request Dufferin Plaza'])
- [500] R018.p1 reuse **duplicate**: "did schmidt cleaning services ltd get their coi yet" → ['Schmidt Cleaning COI Status'] (gold: ['Arjun Schmidt Certificate Request Dufferin Plaza'])
- [500] R018.p2 reuse **duplicate**: "has Schmidt Cleaning Services Ltd. gotten their COI yet" → ['Schmidt Cleaning COI Status'] (gold: ['Arjun Schmidt Certificate Request Dufferin Plaza'])
- [500] R018.p3 reuse **duplicate**: "Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet?" → ['Schmidt Cleaning COI Status'] (gold: ['Arjun Schmidt Certificate Request Dufferin Plaza'])
- [500] R020 reuse **duplicate**: "did Ines send the renewal figures yet?" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric CPP-104292 Renewal Equipment Request'])
- [500] R020.p1 reuse **duplicate**: "did ines send the renewal figures yet" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric CPP-104292 Renewal Equipment Request'])
- [500] R020.p2 reuse **duplicate**: "has Ines sent over the renewal figures yet" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric CPP-104292 Renewal Equipment Request'])
- [500] R020.p3 reuse **duplicate**: "Do you know whether Ines has sent the renewal figures yet?" → ['Ines Renewal Figures Check'] (gold: ['Kowalski Electric CPP-104292 Renewal Equipment Request'])
- [500] R021 reuse **duplicate**: "where are we on Ana's certificate for the City of Markham job?" → ['Ana Markham Certificate Status'] (gold: ['MacLeod Print Shop Markham Certificate'])
- [500] R021.p2 reuse **duplicate**: "wheres Ana's cert at for the City of Markham job" → ['Ana Markham Certificate Status'] (gold: ['MacLeod Print Shop Markham Certificate'])
- [500] R021.p3 reuse **duplicate**: "Could you let me know where things stand with Ana's certificate for the City of Markham job?" → ['Ana Markham Certificate Status'] (gold: ['MacLeod Print Shop Markham Certificate'])
- [500] R024 reuse **duplicate**: "did Uma send the renewal figures yet?" → ['Uma Renewal Figures Check'] (gold: ['Malik Auto Body Lakeshore General Renewal'])
- [500] R024.p1 reuse **duplicate**: "did uma send the renewal figures yet" → ['Uma Renewal Figures Check'] (gold: ['Malik Auto Body Lakeshore General Renewal'])
- [500] R024.p2 reuse **duplicate**: "has Uma sent over the renewal figures yet" → ['Uma Renewal Figures Check'] (gold: ['Malik Auto Body Lakeshore General Renewal'])
- [500] R024.p3 reuse **duplicate**: "Do you know whether Uma has sent the renewal figures yet?" → ['Uma Renewal Figures Check'] (gold: ['Malik Auto Body Lakeshore General Renewal'])
- [500] R026 reuse **duplicate**: "did Farah send the renewal figures yet?" → ['Farah Renewal Figures Check'] (gold: ['Tran Roofing Harbourline CGL Renewal'])
- [500] R026.p1 reuse **duplicate**: "did farah send the renewal figs yet" → ['Farah Renewal Figures Check'] (gold: ['Tran Roofing Harbourline CGL Renewal'])
- [500] R026.p2 reuse **duplicate**: "Has Farah sent over the renewal figures yet?" → ['Farah Renewal Figures Check'] (gold: ['Tran Roofing Harbourline CGL Renewal'])
- [500] R026.p3 reuse **duplicate**: "Could you check whether Farah has sent the renewal figures yet?" → ['Farah Renewal Figures Check'] (gold: ['Tran Roofing Harbourline CGL Renewal'])
- [500] R030 reuse **duplicate**: "did Farah send the renewal figures yet?" → ['Farah Renewal Figures Check'] (gold: ['Tremblay Roofing BOP Renewal'])
- [500] R030.p1 reuse **duplicate**: "did farah send the renewal figs yet" → ['Farah Renewal Figures Check'] (gold: ['Tremblay Roofing BOP Renewal'])
- [500] R030.p2 reuse **duplicate**: "Has Farah sent over the renewal figures yet?" → ['Farah Renewal Figures Check'] (gold: ['Tremblay Roofing BOP Renewal'])
- [500] R030.p3 reuse **duplicate**: "Could you check whether Farah has sent the renewal figures yet?" → ['Farah Renewal Figures Check'] (gold: ['Tremblay Roofing BOP Renewal'])
- [500] R033.p2 reuse **duplicate**: "where are we at with the Sokolov renewal?" → ['Sokolov Renewal Status Check'] (gold: ['Sokolov Auto Body Trillium Renewal'])
- [500] R034 reuse **duplicate**: "did Laila send the renewal figures yet?" → ['Laila Renewal Figures Search'] (gold: ['Sokolov Auto Body Trillium Renewal'])
- [500] R034.p1 reuse **duplicate**: "did laila send the renewal figs yet" → ['Laila Renewal Figures Check'] (gold: ['Sokolov Auto Body Trillium Renewal'])
- [500] R034.p2 reuse **duplicate**: "Has Laila sent over the renewal figures yet?" → ['Laila Renewal Figures Check'] (gold: ['Sokolov Auto Body Trillium Renewal'])
- [500] R034.p3 reuse **duplicate**: "Could you check whether Laila has sent the renewal figures yet?" → ['Laila Renewal Figures Check'] (gold: ['Sokolov Auto Body Trillium Renewal'])
- [500] R036 reuse **duplicate**: "did Hana send the renewal figures yet?" → ['Hana Renewal Figures Check'] (gold: ['Ellis Fitness Northern Shield CGL Renewal'])
- [500] R036.p1 reuse **wrong_agent**: "did hana send the renewal figs yet" → ['Hana Ibrahim Home Renewal 2025'] (gold: ['Ellis Fitness Northern Shield CGL Renewal'])
- [500] R036.p2 reuse **wrong_agent**: "Has Hana sent over the renewal figures yet?" → ['Hana Ibrahim Home Renewal 2025'] (gold: ['Ellis Fitness Northern Shield CGL Renewal'])
- [500] R036.p3 reuse **duplicate**: "Could you check whether Hana has sent the renewal figures yet?" → ['Hana Renewal Figures Check'] (gold: ['Ellis Fitness Northern Shield CGL Renewal'])
- [500] R038 reuse **wrong_agent**: "did Javier send the renewal figures yet?" → ['Javier Sokolov Home Renewal 2025'] (gold: ['Patel Catering CPP-357613 Renewal'])
- [500] R038.p1 reuse **wrong_agent**: "javier send the renewal figs yet" → ['Javier Sokolov Home Renewal 2025'] (gold: ['Patel Catering CPP-357613 Renewal'])
- [500] R038.p2 reuse **wrong_agent**: "has Javier sent the renewal figs yet?" → ['Javier Sokolov Home Renewal 2025'] (gold: ['Patel Catering CPP-357613 Renewal'])
- [500] R038.p3 reuse **wrong_agent**: "Do you know if Javier has sent over the renewal figures yet?" → ['Javier Sokolov Home Renewal 2025'] (gold: ['Patel Catering CPP-357613 Renewal'])
- [500] R040 reuse **duplicate**: "did Reyes Roofing Inc. get their COI yet?" → ['Reyes Roofing COI Status'] (gold: ['Leah Reyes Bayview COI Request'])
- [500] R040.p1 reuse **duplicate**: "did reyes roofing inc get their coi yet" → ['Reyes Roofing COI Status'] (gold: ['Leah Reyes Bayview COI Request'])
- [500] R040.p2 reuse **duplicate**: "did Reyes Roofing Inc. get thier COI yet?" → ['Reyes Roofing COI Status'] (gold: ['Leah Reyes Bayview COI Request'])
- [500] R040.p3 reuse **duplicate**: "Do you know whether Reyes Roofing Inc. has received their COI yet?" → ['Reyes Roofing COI Status Check'] (gold: ['Leah Reyes Bayview COI Request'])
- [500] R041 reuse **duplicate**: "Leah says something's wrong with the bill, look into it" → ['Leah Bill Issue Lookup'] (gold: ['Leah Fernandes NSF Payment Inquiry'])
- [500] R041.p1 reuse **duplicate**: "leah says somethings off w the bill, check it" → ['Leah Bill Check'] (gold: ['Leah Fernandes NSF Payment Inquiry'])
- [500] R041.p2 reuse **duplicate**: "Leah says something's wrong with the bil, can you look into it" → ['Leah Bill Issue Check'] (gold: ['Leah Fernandes NSF Payment Inquiry'])
- [500] R041.p3 reuse **duplicate**: "Leah mentioned that something seems to be wrong with the bill, could you please look into it?" → ['Leah Bill Issue Investigation'] (gold: ['Leah Fernandes NSF Payment Inquiry'])
- [500] R042.p3 reuse **duplicate**: "Have we heard back from billing yet about Leah's payment?" → ['Leah Payment Billing Reply Check'] (gold: ['Leah Fernandes NSF Payment Inquiry'])
- [500] R043.p2 reuse **duplicate**: "Paolo says something's wrong with the bil, can you look into it" → ['Paolo Bill Issue Check'] (gold: ['Paolo Schmidt Double Charge $348.50'])
- [500] R045 reuse **duplicate**: "Adriana says something's wrong with the bill, look into it" → ['Adriana Bill Issue Lookup'] (gold: ['Adriana Pereira Premium Increase Inquiry'])
- [500] R045.p1 reuse **duplicate**: "adriana says somethings off w the bill, check it" → ['Adriana Bill Check'] (gold: ['Adriana Pereira Premium Increase Inquiry'])
- [500] R045.p2 reuse **duplicate**: "Adriana says something's wrong with the bil, can you look into it" → ['Adriana Billing Issue Lookup'] (gold: ['Adriana Pereira Premium Increase Inquiry'])
- [500] R045.p3 reuse **duplicate**: "Adriana mentioned that something seems to be wrong with the bill, could you please look into it?" → ['Adriana Bill Issue Investigation'] (gold: ['Adriana Pereira Premium Increase Inquiry'])
- [500] R046 reuse **duplicate**: "did billing get back to us about Adriana's payment?" → ['Adriana Payment Billing Check'] (gold: ['Adriana Pereira Premium Increase Inquiry'])
- [500] R046.p1 reuse **duplicate**: "billing get back to us on adrianas payment?" → ['Adriana Payment Billing Follow-up'] (gold: ['Adriana Pereira Premium Increase Inquiry'])
- [500] R046.p2 reuse **duplicate**: "did billng get back to us about Adriana's payment?" → ['Adriana Payment Billing Reply Check'] (gold: ['Adriana Pereira Premium Increase Inquiry'])
