# Routing failures: openpoke-names-100-500

Every case this run scored as wrong, grouped by what should have happened. Generated from `results.json` by `run_baseline.py failures` (no LLM calls). Agent names: organic; prompts: all. Case ids ending in `.pN` are paraphrase N of the same case.

- 500 agents: 6 of 516 cases had a failed LLM call and are left out.

**543 failures out of 1542 scored cases.** 65 of them come from cases with a known labelling problem (marked ⚠, listed at the end).

| What should have happened | What OpenPoke did instead | 100 agents | 250 agents | 500 agents |
|---|---|---|---|---|
| Should reuse an existing agent | Created a new agent instead | 91 of 328 | 108 of 328 | 122 of 322 |
| Should reuse an existing agent | Used a different existing agent | 3 of 328 | 10 of 328 | 13 of 322 |
| Should reuse an existing agent | Asked the user instead of acting | 0 of 328 | 1 of 328 | 0 of 322 |
| Should create a new agent | Put the work into an existing agent | 38 of 116 | 45 of 116 | 44 of 116 |
| Ambiguous name | Created a new agent instead | 0 of 28 | 5 of 28 | 16 of 28 |
| Ambiguous name | Used a different existing agent | 4 of 28 | 4 of 28 | 5 of 28 |
| Ambiguous name | Picked one of the matches without asking | 0 of 28 | 1 of 28 | 0 of 28 |
| Ambiguous name | Replied without checking any agent | 0 of 28 | 0 of 28 | 1 of 28 |
| Cross-agent question | Checked too few of the relevant agents | 0 of 12 | 1 of 12 | 1 of 12 |
| Cross-agent question | Checked none of the relevant agents | 4 of 12 | 10 of 12 | 11 of 12 |
| Chit-chat | Called an agent | 2 of 32 | 2 of 32 | 1 of 32 |

## Failed at every roster size (124)

| Case | Kind | Prompt | Outcomes |
|---|---|---|---|
| R013 | reuse | where are we on Maya's certificate for the Regional Municipality of York job? | created a new agent instead |
| R020 | reuse | did Ines send the renewal figures yet? | created a new agent instead |
| R020.p1 | reuse | did ines send the renewal figures yet | created a new agent instead, used a different existing agent |
| R020.p2 | reuse | has Ines sent over the renewal figures yet | created a new agent instead, used a different existing agent |
| R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | created a new agent instead |
| R024 | reuse | did Uma send the renewal figures yet? | created a new agent instead |
| R024.p1 | reuse | did uma send the renewal figures yet | created a new agent instead |
| R024.p2 | reuse | has Uma sent over the renewal figures yet | created a new agent instead |
| R024.p3 | reuse | Do you know whether Uma has sent the renewal figures yet? | created a new agent instead |
| R026 ⚠ | reuse | did Farah send the renewal figures yet? | created a new agent instead |
| R026.p1 ⚠ | reuse | did farah send the renewal figs yet | created a new agent instead |
| R026.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | used a different existing agent, created a new agent instead |
| R026.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | created a new agent instead |
| R030 ⚠ | reuse | did Farah send the renewal figures yet? | created a new agent instead |
| R030.p1 ⚠ | reuse | did farah send the renewal figs yet | used a different existing agent, created a new agent instead |
| R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | used a different existing agent, created a new agent instead |
| R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | created a new agent instead |
| R034 | reuse | did Laila send the renewal figures yet? | created a new agent instead, used a different existing agent |
| R034.p1 | reuse | did laila send the renewal figs yet | created a new agent instead, used a different existing agent |
| R034.p2 | reuse | Has Laila sent over the renewal figures yet? | created a new agent instead, used a different existing agent |
| R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | created a new agent instead |
| R036 | reuse | did Hana send the renewal figures yet? | created a new agent instead, used a different existing agent |
| R036.p1 | reuse | did hana send the renewal figs yet | created a new agent instead, used a different existing agent |
| R036.p2 | reuse | Has Hana sent over the renewal figures yet? | created a new agent instead, used a different existing agent |
| R036.p3 | reuse | Could you check whether Hana has sent the renewal figures yet? | created a new agent instead, used a different existing agent |
| R038 | reuse | did Javier send the renewal figures yet? | created a new agent instead, used a different existing agent |
| R038.p1 | reuse | javier send the renewal figs yet | created a new agent instead, used a different existing agent |
| R038.p2 | reuse | has Javier sent the renewal figs yet? | created a new agent instead, used a different existing agent |
| R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | created a new agent instead, used a different existing agent |
| R040 | reuse | did Reyes Roofing Inc. get their COI yet? | created a new agent instead |
| R040.p1 | reuse | did reyes roofing inc get their coi yet | created a new agent instead |
| R040.p2 | reuse | did Reyes Roofing Inc. get thier COI yet? | created a new agent instead |
| R040.p3 | reuse | Do you know whether Reyes Roofing Inc. has received their COI yet? | created a new agent instead |
| R041.p2 | reuse | Leah says something's wrong with the bil, can you look into it | created a new agent instead |
| R045.p2 | reuse | Adriana says something's wrong with the bil, can you look into it | created a new agent instead |
| R046 | reuse | did billing get back to us about Adriana's payment? | created a new agent instead |
| R046.p1 | reuse | billing get back to us on adrianas payment? | created a new agent instead |
| R046.p3 | reuse | Have we heard back from billing yet about Adriana's payment? | created a new agent instead |
| R047.p2 | reuse | did Uma send the VN yet? | created a new agent instead |
| R049 | reuse | Nora says something's wrong with the bill, look into it | created a new agent instead |
| R055 | ambiguous | any update from Daniel? | used a different existing agent |
| R055.p1 | ambiguous | any news from daniel? | used a different existing agent |
| R055.p2 | ambiguous | any updte from Daniel? | used a different existing agent |
| R055.p3 | ambiguous | Do you have any update from Daniel yet? | used a different existing agent |
| R072 | new | what's going on with the Pereira renewal? | put the work into an existing agent |
| R072.p1 | new | whats up with the pereira renewal | put the work into an existing agent |
| R072.p2 | new | what's going on with the Pereira renewl? | put the work into an existing agent |
| R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | put the work into an existing agent |
| R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R074.p1 | new | where are we on ines cert for dufferin plaza management | put the work into an existing agent |
| R074.p2 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R074.p3 | new | Could you tell me where we are on Ines's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R075 | new | what's going on with the MacLeod renewal? | put the work into an existing agent |
| R076 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | put the work into an existing agent |
| R076.p2 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | put the work into an existing agent |
| R076.p3 | new | Could you let me know where things stand with Uma's certificate for the Kingsway Realty Holdings job? | put the work into an existing agent |
| R080 ⚠ | new | what's going on with the Malik renewal? | put the work into an existing agent |
| R080.p1 ⚠ | new | whats going on w the malik renewal | put the work into an existing agent |
| R080.p2 ⚠ | new | where are we on the malik renewal? | put the work into an existing agent |
| R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | put the work into an existing agent |
| R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R082.p1 | new | where are we on hanas cert for dufferin plaza management | put the work into an existing agent |
| R082.p2 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R082.p3 | new | Could you let me know where we are on Hana's certificate for the Dufferin Plaza Management job? | put the work into an existing agent |
| R087.p2 | new | did Adriana snd the VIN yet? | put the work into an existing agent |
| R099 | new | what's going on with the okafor renewal? | put the work into an existing agent |
| R099.p1 | new | whats up with the okafor renewal? | put the work into an existing agent |
| R099.p2 | new | whats going on with the okafor renewl? | put the work into an existing agent |
| R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | put the work into an existing agent |
| R101 | reminder | remind me friday at 9 to send alice park the budget numbers | created a new agent instead |
| R101.p1 | reminder | remind me friday at 9 to send alice park the budget nums | created a new agent instead |
| R101.p2 | reminder | remind me friday at 9 to send alice park the budgt numbers | created a new agent instead |
| R101.p3 | reminder | Could you please remind me on Friday at 9 to send Alice Park the budget numbers? | created a new agent instead |
| R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | created a new agent instead |
| R104 | reminder | remind me Wednesday at 10am to check that Maya's certificate was issued | created a new agent instead |
| R104.p1 | reminder | remind me wednesday at 10am to check mayas cert was issued | created a new agent instead |
| R104.p2 | reminder | remind me wednesday at 10am to chekc Maya's certificate was issued | created a new agent instead |
| R104.p3 | reminder | Could you remind me on Wednesday at 10am to check that Maya's certificate was issued? | created a new agent instead |
| R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | created a new agent instead |
| R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | created a new agent instead |
| R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | created a new agent instead |
| R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | created a new agent instead |
| R107 | reminder | remind me next monday to chase Ines for the renewal numbers | created a new agent instead |
| R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | created a new agent instead |
| R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | created a new agent instead |
| R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | created a new agent instead |
| R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | created a new agent instead |
| R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | created a new agent instead |
| R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | created a new agent instead |
| R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | created a new agent instead |
| R109 | reminder | remind me next monday to chase Uma for the renewal numbers | created a new agent instead |
| R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | created a new agent instead |
| R109.p2 | reminder | Could you please remind me next Monday to follow up with Uma for the renewal numbers? | created a new agent instead |
| R110 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | created a new agent instead |
| R110.p1 ⚠ | reminder | remind me next monday to chase farah for the renewal numbers | created a new agent instead |
| R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | created a new agent instead |
| R110.p3 ⚠ | reminder | Could you please set a reminder for next Monday to follow up with Farah about the renewal numbers? | created a new agent instead |
| R111 | reminder | remind me Wednesday at 10am to check that Ben's certificate was issued | created a new agent instead |
| R111.p1 | reminder | remind me Wednesday at 10am to chk that Ben's certificate was issued | created a new agent instead |
| R111.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Ben's certificate has been issued? | created a new agent instead |
| R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | created a new agent instead |
| R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | created a new agent instead |
| R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | created a new agent instead |
| R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | created a new agent instead |
| R114 | reminder | remind me next monday to chase Laila for the renewal numbers | created a new agent instead |
| R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | created a new agent instead |
| R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | created a new agent instead |
| R115 | reminder | remind me next monday to chase Hana for the renewal numbers | created a new agent instead, used a different existing agent |
| R115.p1 | reminder | remind me next monday to chase hana for the renewal numbers | created a new agent instead |
| R115.p2 | reminder | Could you please set a reminder for next Monday to follow up with Hana about the renewal numbers? | created a new agent instead |
| R116 | reminder | remind me next monday to chase Javier for the renewal numbers | created a new agent instead |
| R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | created a new agent instead |
| R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | created a new agent instead |
| R118 | reminder | remind me thursday to update Leah on the billing issue | created a new agent instead |
| R118.p1 | reminder | remind me thursday to update leah on the billing issue | created a new agent instead |
| R118.p2 | reminder | remind me thursday to updte Leah on the billing issue | created a new agent instead |
| R118.p3 | reminder | Could you please remind me on Thursday to give Leah an update on the billing issue? | created a new agent instead |
| R119 | reminder | remind me thursday to update Paolo on the billing issue | created a new agent instead |
| R119.p1 | reminder | remind me thursday to update paolo on the billing issue | created a new agent instead |
| R120 | multi | which clients still owe me documents? | checked none of the relevant agents |
| R120.p1 | multi | which clients still owe me docs? | checked none of the relevant agents |
| R120.p2 | multi | which clients still owe me documnts? | checked none of the relevant agents |
| R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | checked none of the relevant agents |
| R127.p1 ⚠ | none | nvm ignore that | called an agent |

## Should reuse an existing agent (348)

Correct: Send the request to the one existing agent that owns the work (reuse, lookalike and reminder cases).

### Created a new agent instead (321)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R013 | reuse | where are we on Maya's certificate for the Regional Municipality of York job? | *Cardenas Bakery COI Regional Municipality of York* | *Maya York Certificate Status* (new) |
| 250 | R013 | reuse | where are we on Maya's certificate for the Regional Municipality of York job? | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate York Status* (new) |
| 500 | R013 | reuse | where are we on Maya's certificate for the Regional Municipality of York job? | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate York Status* (new) |
| 500 | R013.p1 | reuse | where we at on maya's certificate for the regional municipality of york job | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Regional Municipality of York Status* (new) |
| 250 | R013.p2 | reuse | wheres maya's cert at for the Regional Municipality of York job atm | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Status York* (new) |
| 500 | R013.p2 | reuse | wheres maya's cert at for the Regional Municipality of York job atm | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Status York* (new) |
| 500 | R013.p3 | reuse | Could you let me know where things stand with Maya's certificate for the Regional Municipality of York job? | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate York Status* (new) |
| 250 | R015.p2 | reuse | wheres paula's cert at for the Lakeshore Industrial REIT job | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Lakeshore REIT Certificate Lookup* (new) |
| 500 | R015.p2 | reuse | wheres paula's cert at for the Lakeshore Industrial REIT job | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Lakeshore Certificate Status* (new) |
| 250 | R018 | reuse | did Schmidt Cleaning Services Ltd. get their COI yet? | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning COI Status* (new) |
| 500 | R018 | reuse | did Schmidt Cleaning Services Ltd. get their COI yet? | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning COI Status* (new) |
| 500 | R018.p1 | reuse | did schmidt cleaning services ltd get their coi yet | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning COI Status* (new) |
| 250 | R018.p2 | reuse | has Schmidt Cleaning Services Ltd. gotten their COI yet | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning COI Status* (new) |
| 500 | R018.p2 | reuse | has Schmidt Cleaning Services Ltd. gotten their COI yet | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning COI Status* (new) |
| 250 | R018.p3 | reuse | Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet? | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning COI Status Check* (new) |
| 500 | R018.p3 | reuse | Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet? | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Schmidt Cleaning COI Status* (new) |
| 100 | R020 | reuse | did Ines send the renewal figures yet? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 250 | R020 | reuse | did Ines send the renewal figures yet? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 500 | R020 | reuse | did Ines send the renewal figures yet? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 100 | R020.p1 | reuse | did ines send the renewal figures yet | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 500 | R020.p1 | reuse | did ines send the renewal figures yet | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 100 | R020.p2 | reuse | has Ines sent over the renewal figures yet | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 500 | R020.p2 | reuse | has Ines sent over the renewal figures yet | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 100 | R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 250 | R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 500 | R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Figures Check* (new) |
| 250 | R021 | reuse | where are we on Ana's certificate for the City of Markham job? | *MacLeod Print Shop Markham Certificate* | *Ana Markham Certificate Status* (new) |
| 500 | R021 | reuse | where are we on Ana's certificate for the City of Markham job? | *MacLeod Print Shop Markham Certificate* | *Ana Markham Certificate Status* (new) |
| 250 | R021.p2 | reuse | wheres Ana's cert at for the City of Markham job | *MacLeod Print Shop Markham Certificate* | *Ana Markham Certificate Lookup* (new) |
| 500 | R021.p2 | reuse | wheres Ana's cert at for the City of Markham job | *MacLeod Print Shop Markham Certificate* | *Ana Markham Certificate Status* (new) |
| 500 | R021.p3 | reuse | Could you let me know where things stand with Ana's certificate for the City of Markham job? | *MacLeod Print Shop Markham Certificate* | *Ana Markham Certificate Status* (new) |
| 100 | R024 | reuse | did Uma send the renewal figures yet? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 250 | R024 | reuse | did Uma send the renewal figures yet? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 500 | R024 | reuse | did Uma send the renewal figures yet? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 100 | R024.p1 | reuse | did uma send the renewal figures yet | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 250 | R024.p1 | reuse | did uma send the renewal figures yet | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 500 | R024.p1 | reuse | did uma send the renewal figures yet | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 100 | R024.p2 | reuse | has Uma sent over the renewal figures yet | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 250 | R024.p2 | reuse | has Uma sent over the renewal figures yet | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 500 | R024.p2 | reuse | has Uma sent over the renewal figures yet | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 100 | R024.p3 | reuse | Do you know whether Uma has sent the renewal figures yet? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 250 | R024.p3 | reuse | Do you know whether Uma has sent the renewal figures yet? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 500 | R024.p3 | reuse | Do you know whether Uma has sent the renewal figures yet? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Figures Check* (new) |
| 100 | R026 ⚠ | reuse | did Farah send the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 250 | R026 ⚠ | reuse | did Farah send the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R026 ⚠ | reuse | did Farah send the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 100 | R026.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 250 | R026.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R026.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 250 | R026.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R026.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 100 | R026.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 250 | R026.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R026.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Figures Check* (new) |
| 100 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 250 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R030 ⚠ | reuse | did Farah send the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 250 | R030.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R030.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 250 | R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 100 | R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 250 | R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Figures Check* (new) |
| 500 | R033.p2 | reuse | where are we at with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Renewal Status Check* (new) |
| 100 | R034 | reuse | did Laila send the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 500 | R034 | reuse | did Laila send the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Search* (new) |
| 100 | R034.p1 | reuse | did laila send the renewal figs yet | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 500 | R034.p1 | reuse | did laila send the renewal figs yet | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 100 | R034.p2 | reuse | Has Laila sent over the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 500 | R034.p2 | reuse | Has Laila sent over the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 100 | R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 250 | R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 500 | R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Figures Check* (new) |
| 100 | R036 | reuse | did Hana send the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 500 | R036 | reuse | did Hana send the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 100 | R036.p1 | reuse | did hana send the renewal figs yet | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 100 | R036.p2 | reuse | Has Hana sent over the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 250 | R036.p2 | reuse | Has Hana sent over the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 100 | R036.p3 | reuse | Could you check whether Hana has sent the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 500 | R036.p3 | reuse | Could you check whether Hana has sent the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Figures Check* (new) |
| 100 | R038 | reuse | did Javier send the renewal figures yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 250 | R038 | reuse | did Javier send the renewal figures yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 100 | R038.p1 | reuse | javier send the renewal figs yet | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 100 | R038.p2 | reuse | has Javier sent the renewal figs yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 250 | R038.p2 | reuse | has Javier sent the renewal figs yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 100 | R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 250 | R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Figures Check* (new) |
| 100 | R040 | reuse | did Reyes Roofing Inc. get their COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 250 | R040 | reuse | did Reyes Roofing Inc. get their COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 500 | R040 | reuse | did Reyes Roofing Inc. get their COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 100 | R040.p1 | reuse | did reyes roofing inc get their coi yet | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 250 | R040.p1 | reuse | did reyes roofing inc get their coi yet | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status Check* (new) |
| 500 | R040.p1 | reuse | did reyes roofing inc get their coi yet | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 100 | R040.p2 | reuse | did Reyes Roofing Inc. get thier COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 250 | R040.p2 | reuse | did Reyes Roofing Inc. get thier COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 500 | R040.p2 | reuse | did Reyes Roofing Inc. get thier COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 100 | R040.p3 | reuse | Do you know whether Reyes Roofing Inc. has received their COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status Check* (new) |
| 250 | R040.p3 | reuse | Do you know whether Reyes Roofing Inc. has received their COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status* (new) |
| 500 | R040.p3 | reuse | Do you know whether Reyes Roofing Inc. has received their COI yet? | *Leah Reyes Bayview COI Request* | *Reyes Roofing COI Status Check* (new) |
| 250 | R041 | reuse | Leah says something's wrong with the bill, look into it | *Leah Fernandes NSF Payment Inquiry* | *Leah Bill Issue Check* (new) |
| 500 | R041 | reuse | Leah says something's wrong with the bill, look into it | *Leah Fernandes NSF Payment Inquiry* | *Leah Bill Issue Lookup* (new) |
| 500 | R041.p1 | reuse | leah says somethings off w the bill, check it | *Leah Fernandes NSF Payment Inquiry* | *Leah Bill Check* (new) |
| 100 | R041.p2 | reuse | Leah says something's wrong with the bil, can you look into it | *Leah Fernandes NSF Payment Inquiry* | *Leah Bill Issue Lookup* (new) |
| 250 | R041.p2 | reuse | Leah says something's wrong with the bil, can you look into it | *Leah Fernandes NSF Payment Inquiry* | *Leah Bill Issue Lookup* (new) |
| 500 | R041.p2 | reuse | Leah says something's wrong with the bil, can you look into it | *Leah Fernandes NSF Payment Inquiry* | *Leah Bill Issue Check* (new) |
| 500 | R041.p3 | reuse | Leah mentioned that something seems to be wrong with the bill, could you please look into it? | *Leah Fernandes NSF Payment Inquiry* | *Leah Bill Issue Investigation* (new) |
| 500 | R042.p3 | reuse | Have we heard back from billing yet about Leah's payment? | *Leah Fernandes NSF Payment Inquiry* | *Leah Payment Billing Reply Check* (new) |
| 500 | R043.p2 | reuse | Paolo says something's wrong with the bil, can you look into it | *Paolo Schmidt Double Charge $348.50* | *Paolo Bill Issue Check* (new) |
| 250 | R045 | reuse | Adriana says something's wrong with the bill, look into it | *Adriana Pereira Premium Increase Inquiry* | *Adriana Bill Issue Lookup* (new) |
| 500 | R045 | reuse | Adriana says something's wrong with the bill, look into it | *Adriana Pereira Premium Increase Inquiry* | *Adriana Bill Issue Lookup* (new) |
| 250 | R045.p1 | reuse | adriana says somethings off w the bill, check it | *Adriana Pereira Premium Increase Inquiry* | *Adriana Bill Discrepancy Check* (new) |
| 500 | R045.p1 | reuse | adriana says somethings off w the bill, check it | *Adriana Pereira Premium Increase Inquiry* | *Adriana Bill Check* (new) |
| 100 | R045.p2 | reuse | Adriana says something's wrong with the bil, can you look into it | *Adriana Pereira Premium Increase Inquiry* | *Adriana Bill Issue Lookup* (new) |
| 250 | R045.p2 | reuse | Adriana says something's wrong with the bil, can you look into it | *Adriana Pereira Premium Increase Inquiry* | *Adriana Billing Issue Lookup* (new) |
| 500 | R045.p2 | reuse | Adriana says something's wrong with the bil, can you look into it | *Adriana Pereira Premium Increase Inquiry* | *Adriana Billing Issue Lookup* (new) |
| 250 | R045.p3 | reuse | Adriana mentioned that something seems to be wrong with the bill, could you please look into it? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Bill Issue Lookup* (new) |
| 500 | R045.p3 | reuse | Adriana mentioned that something seems to be wrong with the bill, could you please look into it? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Bill Issue Investigation* (new) |
| 100 | R046 | reuse | did billing get back to us about Adriana's payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Check* (new) |
| 250 | R046 | reuse | did billing get back to us about Adriana's payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Reply Check* (new) |
| 500 | R046 | reuse | did billing get back to us about Adriana's payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Check* (new) |
| 100 | R046.p1 | reuse | billing get back to us on adrianas payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Check* (new) |
| 250 | R046.p1 | reuse | billing get back to us on adrianas payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Follow-up* (new) |
| 500 | R046.p1 | reuse | billing get back to us on adrianas payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Follow-up* (new) |
| 250 | R046.p2 | reuse | did billng get back to us about Adriana's payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Follow-up* (new) |
| 500 | R046.p2 | reuse | did billng get back to us about Adriana's payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Reply Check* (new) |
| 100 | R046.p3 | reuse | Have we heard back from billing yet about Adriana's payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Check* (new) |
| 250 | R046.p3 | reuse | Have we heard back from billing yet about Adriana's payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Reply Check* (new) |
| 500 | R046.p3 | reuse | Have we heard back from billing yet about Adriana's payment? | *Adriana Pereira Premium Increase Inquiry* | *Adriana Payment Billing Reply Check* (new) |
| 100 | R047.p2 | reuse | did Uma send the VN yet? | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma VN Check* (new) |
| 250 | R047.p2 | reuse | did Uma send the VN yet? | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma VN Check* (new) |
| 500 | R047.p2 | reuse | did Uma send the VN yet? | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma VN Status Check* (new) |
| 500 | R047.p3 | reuse | Do you know if Uma has sent over the VIN yet? | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma VIN Check* (new) |
| 250 | R048.p3 | reuse | Could you please add Uma's new Toyota to the policy? | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma Toyota Vehicle Addition* (new) |
| 100 | R049 | reuse | Nora says something's wrong with the bill, look into it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Issue Investigation* (new) |
| 250 | R049 | reuse | Nora says something's wrong with the bill, look into it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Issue Investigation* (new) |
| 500 | R049 | reuse | Nora says something's wrong with the bill, look into it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Issue Investigation* (new) |
| 250 | R049.p1 | reuse | nora says bill's wrong, check it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Dispute Check* (new) |
| 500 | R049.p1 | reuse | nora says bill's wrong, check it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Dispute Check* (new) |
| 250 | R049.p2 | reuse | Nora says somethings wrong with the bil, look into it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Issue Investigation* (new) |
| 500 | R049.p2 | reuse | Nora says somethings wrong with the bil, look into it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Issue Check* (new) |
| 250 | R049.p3 | reuse | Nora mentioned that something looks wrong with the bill, could you please look into it? | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Issue Investigation* (new) |
| 500 | R049.p3 | reuse | Nora mentioned that something looks wrong with the bill, could you please look into it? | *Nora Bhatt Payment Plan Inquiry* | *Nora Bill Issue Investigation* (new) |
| 250 | R050 | reuse | did billing get back to us about Nora's payment? | *Nora Bhatt Payment Plan Inquiry* | *Nora Payment Billing Reply Check* (new) |
| 500 | R050.p3 | reuse | Have you heard back from billing about Nora's payment yet? | *Nora Bhatt Payment Plan Inquiry* | *Nora Payment Billing Reply Check* (new) |
| 500 | R100 | reminder | remind me thursday at 11:30 to leave for lunch with alice | *Pinewood Kitchen Lunch Booking* | *Lunch With Alice Reminder* (new) |
| 250 | R100.p1 | reminder | remind me thursday at 11:30 to leave for lunch w alice | *Pinewood Kitchen Lunch Booking* | *Thursday Lunch Departure Reminder* (new) |
| 500 | R100.p1 | reminder | remind me thursday at 11:30 to leave for lunch w alice | *Pinewood Kitchen Lunch Booking* | *Thursday Lunch Departure Reminder* (new) |
| 250 | R100.p2 | reminder | remind me thursday at 11:30 to leave for lnch with alice | *Pinewood Kitchen Lunch Booking* | *Thursday Lunch Departure Reminder* (new) |
| 100 | R101 | reminder | remind me friday at 9 to send alice park the budget numbers | *Q4 Book of Business Report for Alice Park* | *Friday Reminder Alice Park Budget* (new) |
| 250 | R101 | reminder | remind me friday at 9 to send alice park the budget numbers | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 500 | R101 | reminder | remind me friday at 9 to send alice park the budget numbers | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 100 | R101.p1 | reminder | remind me friday at 9 to send alice park the budget nums | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 250 | R101.p1 | reminder | remind me friday at 9 to send alice park the budget nums | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 500 | R101.p1 | reminder | remind me friday at 9 to send alice park the budget nums | *Q4 Book of Business Report for Alice Park* | *Friday Budget Numbers Reminder for Alice Park* (new) |
| 100 | R101.p2 | reminder | remind me friday at 9 to send alice park the budgt numbers | *Q4 Book of Business Report for Alice Park* | *Friday Reminder Alice Park Budget* (new) |
| 250 | R101.p2 | reminder | remind me friday at 9 to send alice park the budgt numbers | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 500 | R101.p2 | reminder | remind me friday at 9 to send alice park the budgt numbers | *Q4 Book of Business Report for Alice Park* | *Friday Alice Park Budget Reminder* (new) |
| 100 | R101.p3 | reminder | Could you please remind me on Friday at 9 to send Alice Park the budget numbers? | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 250 | R101.p3 | reminder | Could you please remind me on Friday at 9 to send Alice Park the budget numbers? | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 500 | R101.p3 | reminder | Could you please remind me on Friday at 9 to send Alice Park the budget numbers? | *Q4 Book of Business Report for Alice Park* | *Alice Park Budget Numbers Reminder* (new) |
| 250 | R102 | reminder | remind me tomorrow at 10am to check daniel's certificate went out | *Okafor Landscaping COI City of Vaughan* | *Daniel Okafor Certificate Check Reminder* (new) |
| 500 | R102 | reminder | remind me tomorrow at 10am to check daniel's certificate went out | *Okafor Landscaping COI City of Vaughan* | *Daniel Okafor Certificate Reminder* (new) |
| 100 | R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | *Okafor Landscaping COI City of Vaughan* | *Daniel Okafor Certificate Reminder* (new) |
| 250 | R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | *Okafor Landscaping COI City of Vaughan* | *Daniel Okafor Cert Reminder* (new) |
| 500 | R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | *Okafor Landscaping COI City of Vaughan* | *Daniel Cert Check Reminder* (new) |
| 250 | R102.p2 | reminder | remind me tomorrow at 10am to chekc daniel's certificate went out | *Okafor Landscaping COI City of Vaughan* | *Daniel Okafor Certificate Reminder* (new) |
| 500 | R102.p2 | reminder | remind me tomorrow at 10am to chekc daniel's certificate went out | *Okafor Landscaping COI City of Vaughan* | *Daniel Certificate Reminder* (new) |
| 100 | R102.p3 | reminder | Could you remind me tomorrow at 10am to check that Daniel's certificate went out? | *Okafor Landscaping COI City of Vaughan* | *Daniel Certificate Reminder* (new) |
| 500 | R102.p3 | reminder | Could you remind me tomorrow at 10am to check that Daniel's certificate went out? | *Okafor Landscaping COI City of Vaughan* | *Daniel Certificate Reminder* (new) |
| 250 | R103 | reminder | remind me tomorrow at 9am to call linda about the adjuster | *Linda Gauthier Basement Water Claim Restoration* | *Linda Adjuster Call Reminder* (new) |
| 500 | R103.p1 | reminder | remind me tomorrow at 9am to call linda re the adjuster | *Linda Gauthier Basement Water Claim Restoration* | *Linda Gauthier Call Reminder* (new) |
| 250 | R103.p2 | reminder | Could you please remind me tomorrow at 9am to call Linda about the adjuster? | *Linda Gauthier Basement Water Claim Restoration* | *Linda Gauthier Adjuster Call Reminder* (new) |
| 500 | R103.p2 | reminder | Could you please remind me tomorrow at 9am to call Linda about the adjuster? | *Linda Gauthier Basement Water Claim Restoration* | *Linda Call Reminder Tomorrow 9am* (new) |
| 100 | R104 | reminder | remind me Wednesday at 10am to check that Maya's certificate was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 250 | R104 | reminder | remind me Wednesday at 10am to check that Maya's certificate was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Check Reminder* (new) |
| 500 | R104 | reminder | remind me Wednesday at 10am to check that Maya's certificate was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 100 | R104.p1 | reminder | remind me wednesday at 10am to check mayas cert was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 250 | R104.p1 | reminder | remind me wednesday at 10am to check mayas cert was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 500 | R104.p1 | reminder | remind me wednesday at 10am to check mayas cert was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Check Reminder* (new) |
| 100 | R104.p2 | reminder | remind me wednesday at 10am to chekc Maya's certificate was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wednesday* (new) |
| 250 | R104.p2 | reminder | remind me wednesday at 10am to chekc Maya's certificate was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 500 | R104.p2 | reminder | remind me wednesday at 10am to chekc Maya's certificate was issued | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Wednesday Reminder* (new) |
| 100 | R104.p3 | reminder | Could you remind me on Wednesday at 10am to check that Maya's certificate was issued? | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 250 | R104.p3 | reminder | Could you remind me on Wednesday at 10am to check that Maya's certificate was issued? | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 500 | R104.p3 | reminder | Could you remind me on Wednesday at 10am to check that Maya's certificate was issued? | *Cardenas Bakery COI Regional Municipality of York* | *Maya Certificate Reminder Wed 10am* (new) |
| 100 | R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 250 | R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder Wednesday 10am* (new) |
| 500 | R105 | reminder | remind me Wednesday at 10am to check that Paula's certificate was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder Wednesday* (new) |
| 100 | R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Cert Reminder Wed 10am* (new) |
| 250 | R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 500 | R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Cert Reminder Wed 10am* (new) |
| 100 | R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 250 | R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder Wed 10am* (new) |
| 500 | R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder Wednesday* (new) |
| 100 | R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 250 | R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder Wed 10am* (new) |
| 500 | R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 100 | R106 | reminder | remind me Wednesday at 10am to check that Arjun's certificate was issued | *Arjun Schmidt Certificate Request Dufferin Plaza* | *Arjun Schmidt Certificate Reminder* (new) |
| 100 | R107 | reminder | remind me next monday to chase Ines for the renewal numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 250 | R107 | reminder | remind me next monday to chase Ines for the renewal numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 500 | R107 | reminder | remind me next monday to chase Ines for the renewal numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Reminder Chase Ines Renewal Numbers* (new) |
| 100 | R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Chase Ines Renewal Numbers Reminder* (new) |
| 250 | R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 500 | R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 100 | R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 250 | R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 500 | R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Reminder Chase Ines Renewal Numbers* (new) |
| 100 | R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 250 | R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Santos Renewal Numbers Reminder* (new) |
| 500 | R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Renewal Numbers Reminder* (new) |
| 100 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder* (new) |
| 250 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Wednesday Reminder* (new) |
| 500 | R108 | reminder | remind me Wednesday at 10am to check that Ana's certificate was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder* (new) |
| 100 | R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder* (new) |
| 250 | R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | *MacLeod Print Shop Markham Certificate* | *Ana Cert Check Reminder* (new) |
| 500 | R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder Wednesday 10am* (new) |
| 100 | R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Check Reminder* (new) |
| 250 | R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder Wednesday* (new) |
| 500 | R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder* (new) |
| 100 | R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder Wed 10am* (new) |
| 250 | R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder Wed 10am* (new) |
| 500 | R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | *MacLeod Print Shop Markham Certificate* | *Ana Certificate Reminder Wednesday* (new) |
| 100 | R109 | reminder | remind me next monday to chase Uma for the renewal numbers | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 250 | R109 | reminder | remind me next monday to chase Uma for the renewal numbers | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 500 | R109 | reminder | remind me next monday to chase Uma for the renewal numbers | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 100 | R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Reminder* (new) |
| 250 | R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 500 | R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 100 | R109.p2 | reminder | Could you please remind me next Monday to follow up with Uma for the renewal numbers? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 250 | R109.p2 | reminder | Could you please remind me next Monday to follow up with Uma for the renewal numbers? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 500 | R109.p2 | reminder | Could you please remind me next Monday to follow up with Uma for the renewal numbers? | *Malik Auto Body Lakeshore General Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 100 | R110 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R110 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R110 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 100 | R110.p1 ⚠ | reminder | remind me next monday to chase farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R110.p1 ⚠ | reminder | remind me next monday to chase farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R110.p1 ⚠ | reminder | remind me next monday to chase farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 100 | R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 100 | R110.p3 ⚠ | reminder | Could you please set a reminder for next Monday to follow up with Farah about the renewal numbers? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R110.p3 ⚠ | reminder | Could you please set a reminder for next Monday to follow up with Farah about the renewal numbers? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R110.p3 ⚠ | reminder | Could you please set a reminder for next Monday to follow up with Farah about the renewal numbers? | *Tran Roofing Harbourline CGL Renewal* | *Farah Renewal Numbers Monday Reminder* (new) |
| 100 | R111 | reminder | remind me Wednesday at 10am to check that Ben's certificate was issued | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Reminder* (new) |
| 250 | R111 | reminder | remind me Wednesday at 10am to check that Ben's certificate was issued | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Reminder Wed 10am* (new) |
| 500 | R111 | reminder | remind me Wednesday at 10am to check that Ben's certificate was issued | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Reminder* (new) |
| 100 | R111.p1 | reminder | remind me Wednesday at 10am to chk that Ben's certificate was issued | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Issuance Reminder* (new) |
| 250 | R111.p1 | reminder | remind me Wednesday at 10am to chk that Ben's certificate was issued | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Issued Reminder* (new) |
| 500 | R111.p1 | reminder | remind me Wednesday at 10am to chk that Ben's certificate was issued | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Check Reminder* (new) |
| 100 | R111.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Ben's certificate has been issued? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Reminder* (new) |
| 250 | R111.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Ben's certificate has been issued? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Issued Reminder* (new) |
| 500 | R111.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Ben's certificate has been issued? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Ben Certificate Issuance Reminder* (new) |
| 100 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R112 ⚠ | reminder | remind me next monday to chase Farah for the renewal numbers | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 100 | R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Monday Reminder* (new) |
| 100 | R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 100 | R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | *Tremblay Roofing BOP Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R113 | reminder | remind me Wednesday at 10am to check that Neil's certificate was issued | *Neil Malik COI Malik Roofing Bayview* | *Neil Certificate Reminder Wed 10am* (new) |
| 500 | R113.p1 | reminder | remind me Wednesday at 10am to check tht Neil's certificate was issued | *Neil Malik COI Malik Roofing Bayview* | *Neil Certificate Reminder Wed 10am* (new) |
| 250 | R113.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Neil's certificate has been issued? | *Neil Malik COI Malik Roofing Bayview* | *Neil Certificate Reminder Wed 10am* (new) |
| 100 | R114 | reminder | remind me next monday to chase Laila for the renewal numbers | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 250 | R114 | reminder | remind me next monday to chase Laila for the renewal numbers | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 500 | R114 | reminder | remind me next monday to chase Laila for the renewal numbers | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 100 | R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 250 | R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 500 | R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 100 | R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 250 | R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 500 | R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | *Sokolov Auto Body Trillium Renewal* | *Laila Renewal Numbers Reminder* (new) |
| 100 | R115 | reminder | remind me next monday to chase Hana for the renewal numbers | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 500 | R115 | reminder | remind me next monday to chase Hana for the renewal numbers | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 100 | R115.p1 | reminder | remind me next monday to chase hana for the renewal numbers | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 250 | R115.p1 | reminder | remind me next monday to chase hana for the renewal numbers | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 500 | R115.p1 | reminder | remind me next monday to chase hana for the renewal numbers | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 100 | R115.p2 | reminder | Could you please set a reminder for next Monday to follow up with Hana about the renewal numbers? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Follow-up Reminder* (new) |
| 250 | R115.p2 | reminder | Could you please set a reminder for next Monday to follow up with Hana about the renewal numbers? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Follow-up Reminder* (new) |
| 500 | R115.p2 | reminder | Could you please set a reminder for next Monday to follow up with Hana about the renewal numbers? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Renewal Numbers Follow-up Reminder* (new) |
| 100 | R116 | reminder | remind me next monday to chase Javier for the renewal numbers | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 250 | R116 | reminder | remind me next monday to chase Javier for the renewal numbers | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 500 | R116 | reminder | remind me next monday to chase Javier for the renewal numbers | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Chase Reminder* (new) |
| 100 | R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 250 | R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 500 | R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 100 | R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 250 | R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 500 | R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | *Patel Catering CPP-357613 Renewal* | *Javier Renewal Numbers Reminder* (new) |
| 100 | R117 | reminder | remind me Wednesday at 10am to check that Leah's certificate was issued | *Leah Reyes Bayview COI Request* | *Leah Certificate Reminder Wednesday* (new) |
| 500 | R117 | reminder | remind me Wednesday at 10am to check that Leah's certificate was issued | *Leah Reyes Bayview COI Request* | *Leah Certificate Issued Reminder* (new) |
| 250 | R117.p1 | reminder | remind me Wednesday at 10am to chek that Leah's certificate was issued | *Leah Reyes Bayview COI Request* | *Wednesday 10am Leah Certificate Reminder* (new) |
| 250 | R117.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Leah's certificate has been issued? | *Leah Reyes Bayview COI Request* | *Leah Reyes Certificate Reminder* (new) |
| 500 | R117.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Leah's certificate has been issued? | *Leah Reyes Bayview COI Request* | *Leah Reyes Certificate Reminder* (new) |
| 100 | R118 | reminder | remind me thursday to update Leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Update Reminder* (new) |
| 250 | R118 | reminder | remind me thursday to update Leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Thursday Reminder Leah Billing* (new) |
| 500 | R118 | reminder | remind me thursday to update Leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Issue Reminder Thursday* (new) |
| 100 | R118.p1 | reminder | remind me thursday to update leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Reminder Thursday* (new) |
| 250 | R118.p1 | reminder | remind me thursday to update leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Update Reminder* (new) |
| 500 | R118.p1 | reminder | remind me thursday to update leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Update Reminder* (new) |
| 100 | R118.p2 | reminder | remind me thursday to updte Leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Reminder Thursday* (new) |
| 250 | R118.p2 | reminder | remind me thursday to updte Leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Reminder Thursday* (new) |
| 500 | R118.p2 | reminder | remind me thursday to updte Leah on the billing issue | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Update Reminder* (new) |
| 100 | R118.p3 | reminder | Could you please remind me on Thursday to give Leah an update on the billing issue? | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Update Reminder* (new) |
| 250 | R118.p3 | reminder | Could you please remind me on Thursday to give Leah an update on the billing issue? | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Update Reminder* (new) |
| 500 | R118.p3 | reminder | Could you please remind me on Thursday to give Leah an update on the billing issue? | *Leah Fernandes NSF Payment Inquiry* | *Leah Billing Update Reminder* (new) |
| 100 | R119 | reminder | remind me thursday to update Paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Thursday Reminder Paolo Billing Update* (new) |
| 250 | R119 | reminder | remind me thursday to update Paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Thursday Reminder Paolo Billing Update* (new) |
| 500 | R119 | reminder | remind me thursday to update Paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Paolo Billing Update Reminder* (new) |
| 100 | R119.p1 | reminder | remind me thursday to update paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Thursday Reminder Paolo Billing Update* (new) |
| 250 | R119.p1 | reminder | remind me thursday to update paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Thursday Reminder Paolo Billing Update* (new) |
| 500 | R119.p1 | reminder | remind me thursday to update paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Paolo Billing Update Reminder* (new) |
| 100 | R119.p2 | reminder | remind me thursday to updat Paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Paolo Billing Reminder Thursday* (new) |
| 500 | R119.p2 | reminder | remind me thursday to updat Paolo on the billing issue | *Paolo Schmidt Double Charge $348.50* | *Paolo Billing Update Reminder* (new) |
| 250 | R119.p3 | reminder | Could you please remind me on Thursday to give Paolo an update on the billing issue? | *Paolo Schmidt Double Charge $348.50* | *Paolo Billing Update Reminder Thursday* (new) |
| 500 | R119.p3 | reminder | Could you please remind me on Thursday to give Paolo an update on the billing issue? | *Paolo Schmidt Double Charge $348.50* | *Paolo Billing Update Reminder* (new) |

### Used a different existing agent (26)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R015 | reuse | where are we on Paula's certificate for the Lakeshore Industrial REIT job? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 500 | R015.p1 | reuse | where we at on paula's certificate for the lakeshore industrial reit job | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 250 | R020.p1 | reuse | did ines send the renewal figures yet | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Santos Roofing Liability Limit Increase* (existing) |
| 250 | R020.p2 | reuse | has Ines sent over the renewal figures yet | *Kowalski Electric CPP-104292 Renewal Equipment Request* | *Ines Santos Roofing Liability Limit Increase* (existing) |
| 100 | R026.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tran Roofing Harbourline CGL Renewal* | *Farah Boateng Tucson Vehicle Addition AU-146760* (existing) |
| 100 | R030.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tremblay Roofing BOP Renewal* | *Farah Boateng Tucson Vehicle Addition AU-146760* (existing) |
| 100 | R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tremblay Roofing BOP Renewal* | *Farah Boateng Tucson Vehicle Addition AU-146760* (existing) |
| 250 | R034 | reuse | did Laila send the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Haddad Umbrella Coverage Comparison* (existing) |
| 250 | R034.p1 | reuse | did laila send the renewal figs yet | *Sokolov Auto Body Trillium Renewal* | *Laila Haddad Umbrella Coverage Comparison* (existing) |
| 250 | R034.p2 | reuse | Has Laila sent over the renewal figures yet? | *Sokolov Auto Body Trillium Renewal* | *Laila Haddad Umbrella Coverage Comparison* (existing), *Laila Quinn Quinn IT Consulting Payroll Audit* (existing) |
| 250 | R036 | reuse | did Hana send the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Ibrahim Home Renewal 2025* (existing) |
| 250 | R036.p1 | reuse | did hana send the renewal figs yet | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Ibrahim Home Renewal 2025* (existing) |
| 500 | R036.p1 | reuse | did hana send the renewal figs yet | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Ibrahim Home Renewal 2025* (existing) |
| 500 | R036.p2 | reuse | Has Hana sent over the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Ibrahim Home Renewal 2025* (existing) |
| 250 | R036.p3 | reuse | Could you check whether Hana has sent the renewal figures yet? | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Ibrahim Home Renewal 2025* (existing) |
| 500 | R038 | reuse | did Javier send the renewal figures yet? | *Patel Catering CPP-357613 Renewal* | *Javier Sokolov Home Renewal 2025* (existing) |
| 250 | R038.p1 | reuse | javier send the renewal figs yet | *Patel Catering CPP-357613 Renewal* | *Javier Fernandes Condo Insurance* (existing) |
| 500 | R038.p1 | reuse | javier send the renewal figs yet | *Patel Catering CPP-357613 Renewal* | *Javier Sokolov Home Renewal 2025* (existing) |
| 500 | R038.p2 | reuse | has Javier sent the renewal figs yet? | *Patel Catering CPP-357613 Renewal* | *Javier Sokolov Home Renewal 2025* (existing) |
| 500 | R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | *Patel Catering CPP-357613 Renewal* | *Javier Sokolov Home Renewal 2025* (existing) |
| 500 | R047 | reuse | did Uma send the VIN yet? | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma Romano Auto Vehicle Addition AU-246551* (existing) |
| 500 | R048 | reuse | add Uma's new Toyota to the policy | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma Romano Auto Vehicle Addition AU-246551* (existing) |
| 500 | R048.p1 | reuse | add umas new toyota to the policy | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma Romano Auto Vehicle Addition AU-246551* (existing) |
| 500 | R048.p2 | reuse | add Uma's new Toyta to the policy | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma Romano Auto Vehicle Addition AU-246551* (existing) |
| 500 | R048.p3 | reuse | Could you please add Uma's new Toyota to the policy? | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma Romano Auto Vehicle Addition AU-246551* (existing) |
| 250 | R115 | reminder | remind me next monday to chase Hana for the renewal numbers | *Ellis Fitness Northern Shield CGL Renewal* | *Hana Ibrahim Home Renewal 2025* (existing) |

### Asked the user instead of acting (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 250 | R001 | reuse | what did alice chen say about lunch? | *Pinewood Kitchen Lunch Booking* | replied: "Alice suggested Thursday at 12:30 at Pinewood Kitchen. Bob's in, and he's vegetarian." |

## Should create a new agent (127)

Correct: Create a new agent. The client already has an agent for a different job, and that agent must not be used.

### Put the work into an existing agent (127)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R071.p3 | new | Could you let me know what's going on with the Cardenas renewal? | New agent (not *Cardenas Bakery COI Regional Municipality of York*) | *Cardenas Bakery COI Regional Municipality of York* (existing) |
| 100 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 250 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 500 | R072 | new | what's going on with the Pereira renewal? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 100 | R072.p1 | new | whats up with the pereira renewal | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 250 | R072.p1 | new | whats up with the pereira renewal | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 500 | R072.p1 | new | whats up with the pereira renewal | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 100 | R072.p2 | new | what's going on with the Pereira renewl? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 250 | R072.p2 | new | what's going on with the Pereira renewl? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 500 | R072.p2 | new | what's going on with the Pereira renewl? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 100 | R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing), *Adriana Pereira Premium Increase Inquiry* (existing) |
| 250 | R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 500 | R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | New agent (not *Pereira Hardware COI Lakeshore Industrial REIT*) | *Naveen Pereira Pereira Moving Renewal* (existing) |
| 100 | R073.p1 | new | whats up with the schmidt renewal | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R073.p1 | new | whats up with the schmidt renewal | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R073.p2 | new | where are we on the schmidt renewal? | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R073.p2 | new | where are we on the schmidt renewal? | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing), *Paolo Schmidt Double Charge $348.50* (existing) |
| 250 | R073.p3 | new | Could you let me know where things stand with the Schmidt renewal? | New agent (not *Arjun Schmidt Certificate Request Dufferin Plaza*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 500 | R074 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R074.p1 | new | where are we on ines cert for dufferin plaza management | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R074.p1 | new | where are we on ines cert for dufferin plaza management | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 500 | R074.p1 | new | where are we on ines cert for dufferin plaza management | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R074.p2 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R074.p2 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 500 | R074.p2 | new | where are we on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R074.p3 | new | Could you tell me where we are on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R074.p3 | new | Could you tell me where we are on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 500 | R074.p3 | new | Could you tell me where we are on Ines's certificate for the Dufferin Plaza Management job? | New agent (not *Kowalski Electric CPP-104292 Renewal Equipment Request*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 250 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 500 | R075 | new | what's going on with the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Brewing Lakeshore BOP Renewal* (existing) |
| 100 | R075.p1 | new | whats going on w the macleod renewal | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 500 | R075.p1 | new | whats going on w the macleod renewal | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Brewing Lakeshore BOP Renewal* (existing) |
| 100 | R075.p2 | new | where are we on the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 500 | R075.p2 | new | where are we on the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Brewing Lakeshore BOP Renewal* (existing) |
| 100 | R075.p3 | new | Could you fill me in on what's happening with the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Print Shop Markham Certificate* (existing) |
| 500 | R075.p3 | new | Could you fill me in on what's happening with the MacLeod renewal? | New agent (not *MacLeod Print Shop Markham Certificate*) | *MacLeod Brewing Lakeshore BOP Renewal* (existing) |
| 100 | R076 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Uma Petrov Daycare Certificate Queen West* (existing) |
| 250 | R076 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Uma Petrov Daycare Certificate Queen West* (existing) |
| 500 | R076 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Abbott Architecture COI Kingsway Realty* (existing) |
| 250 | R076.p1 | new | where are we on uma's cert for kingsway realty holdings | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Uma Petrov Daycare Certificate Queen West* (existing) |
| 500 | R076.p1 | new | where are we on uma's cert for kingsway realty holdings | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Abbott Architecture COI Kingsway Realty* (existing) |
| 100 | R076.p2 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Uma Petrov Daycare Certificate Queen West* (existing) |
| 250 | R076.p2 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Uma Petrov Daycare Certificate Queen West* (existing) |
| 500 | R076.p2 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Abbott Architecture COI Kingsway Realty* (existing) |
| 100 | R076.p3 | new | Could you let me know where things stand with Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Uma Petrov Daycare Certificate Queen West* (existing) |
| 250 | R076.p3 | new | Could you let me know where things stand with Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Uma Petrov Daycare Certificate Queen West* (existing) |
| 500 | R076.p3 | new | Could you let me know where things stand with Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Malik Auto Body Lakeshore General Renewal*) | *Abbott Architecture COI Kingsway Realty* (existing) |
| 100 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 500 | R077 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 500 | R077.p1 | new | where are we on farah's cert for lakeshore industrial reit | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R077.p2 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 500 | R077.p2 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R077.p3 | new | Could you update me on where we are with Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing) |
| 500 | R077.p3 | new | Could you update me on where we are with Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Tran Roofing Harbourline CGL Renewal*) | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 500 | R079.p2 | new | where are we on Farah's certificate for the City of Mississauga job? | New agent (not *Tremblay Roofing BOP Renewal*) | *Yamamoto Roofing COI City of Mississauga* (existing) |
| 100 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 250 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 500 | R080 ⚠ | new | what's going on with the Malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Cleaning Trillium Renewal* (existing), *Malik Auto Body Lakeshore General Renewal* (existing) |
| 100 | R080.p1 ⚠ | new | whats going on w the malik renewal | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 250 | R080.p1 ⚠ | new | whats going on w the malik renewal | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 500 | R080.p1 ⚠ | new | whats going on w the malik renewal | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Cleaning Trillium Renewal* (existing), *Malik Auto Body Lakeshore General Renewal* (existing), *Malik Architecture Harbourline BOP Renewal* (existing) |
| 100 | R080.p2 ⚠ | new | where are we on the malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 250 | R080.p2 ⚠ | new | where are we on the malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing), *Neil Malik COI Malik Roofing Bayview* (existing) |
| 500 | R080.p2 ⚠ | new | where are we on the malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Cleaning Trillium Renewal* (existing), *Malik Auto Body Lakeshore General Renewal* (existing) |
| 100 | R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 250 | R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Auto Body Lakeshore General Renewal* (existing) |
| 500 | R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | New agent (not *Neil Malik COI Malik Roofing Bayview*) | *Malik Cleaning Trillium Renewal* (existing), *Malik Auto Body Lakeshore General Renewal* (existing), *Malik Architecture Harbourline BOP Renewal* (existing) |
| 100 | R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 500 | R082 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R082.p1 | new | where are we on hanas cert for dufferin plaza management | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R082.p1 | new | where are we on hanas cert for dufferin plaza management | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 500 | R082.p1 | new | where are we on hanas cert for dufferin plaza management | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R082.p2 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R082.p2 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 500 | R082.p2 | new | where are we on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 100 | R082.p3 | new | Could you let me know where we are on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R082.p3 | new | Could you let me know where we are on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 500 | R082.p3 | new | Could you let me know where we are on Hana's certificate for the Dufferin Plaza Management job? | New agent (not *Ellis Fitness Northern Shield CGL Renewal*) | *Arjun Schmidt Certificate Request Dufferin Plaza* (existing) |
| 250 | R085 | new | start a claim file for Leah's water damage | New agent (not *Leah Fernandes NSF Payment Inquiry*) | *Leah Pereira Water Damage Claim CLM-2614663* (existing) |
| 250 | R085.p1 | new | open a claim file for leah's water damage | New agent (not *Leah Fernandes NSF Payment Inquiry*) | *Leah Pereira Water Damage Claim CLM-2614663* (existing) |
| 500 | R085.p1 | new | open a claim file for leah's water damage | New agent (not *Leah Fernandes NSF Payment Inquiry*) | *Leah Pereira Water Damage Claim CLM-2614663* (existing) |
| 250 | R085.p2 | new | start claim file for Leah's water damge | New agent (not *Leah Fernandes NSF Payment Inquiry*) | *Leah Pereira Water Damage Claim CLM-2614663* (existing) |
| 500 | R085.p2 | new | start claim file for Leah's water damge | New agent (not *Leah Fernandes NSF Payment Inquiry*) | *Leah Pereira Water Damage Claim CLM-2614663* (existing) |
| 250 | R085.p3 | new | Could you please start a claim file for Leah's water damage? | New agent (not *Leah Fernandes NSF Payment Inquiry*) | *Leah Pereira Water Damage Claim CLM-2614663* (existing) |
| 500 | R085.p3 | new | Could you please start a claim file for Leah's water damage? | New agent (not *Leah Fernandes NSF Payment Inquiry*) | *Leah Pereira Water Damage Claim CLM-2614663* (existing) |
| 250 | R087 | new | did Adriana send the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Ellis Auto Claim 2025* (existing) |
| 500 | R087 | new | did Adriana send the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Li Auto Vehicle Addition AU-400306* (existing) |
| 250 | R087.p1 | new | adriana send the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Ellis Auto Claim 2025* (existing) |
| 500 | R087.p1 | new | adriana send the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Li Auto Vehicle Addition AU-400306* (existing) |
| 100 | R087.p2 | new | did Adriana snd the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Pereira Premium Increase Inquiry* (existing), *Adriana Ghosh Condo Insurance Quote* (existing), *Adriana Nguyen Policy Cancellation and Pro-Rated Refund* (existing) |
| 250 | R087.p2 | new | did Adriana snd the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Ellis Auto Claim 2025* (existing) |
| 500 | R087.p2 | new | did Adriana snd the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Li Auto Vehicle Addition AU-400306* (existing) |
| 250 | R087.p3 | new | Do you know whether Adriana has sent the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Ellis Auto Claim 2025* (existing) |
| 500 | R087.p3 | new | Do you know whether Adriana has sent the VIN yet? | New agent (not *Adriana Pereira Premium Increase Inquiry*) | *Adriana Li Auto Vehicle Addition AU-400306* (existing) |
| 100 | R090 | new | Mona says something's wrong with the bill, look into it | New agent (not *Mona Fernandes Auto Quote and Renovation Receipts*) | *Mona Fernandes Auto Quote and Renovation Receipts* (existing) |
| 100 | R090.p1 | new | mona says the bill looks off, can u check it | New agent (not *Mona Fernandes Auto Quote and Renovation Receipts*) | *Mona Fernandes Auto Quote and Renovation Receipts* (existing) |
| 100 | R090.p2 | new | Mona says somethings wrong with the bil, look into it | New agent (not *Mona Fernandes Auto Quote and Renovation Receipts*) | *Mona Fernandes Auto Quote and Renovation Receipts* (existing) |
| 100 | R090.p3 | new | Mona has mentioned that something seems wrong with the bill, so could you please look into it? | New agent (not *Mona Fernandes Auto Quote and Renovation Receipts*) | *Mona Fernandes Auto Quote and Renovation Receipts* (existing) |
| 100 | R093 | new | what's still missing for Owen's auto quote? | New agent (not *Owen Zielinski NSF Payment Inquiry*) | *Owen Li Tenant Policy Quote* (existing) |
| 250 | R093 | new | what's still missing for Owen's auto quote? | New agent (not *Owen Zielinski NSF Payment Inquiry*) | *Owen Li Tenant Policy Quote* (existing) |
| 250 | R093.p1 | new | whats still missing on owen's auto quote | New agent (not *Owen Zielinski NSF Payment Inquiry*) | *Owen Li Tenant Policy Quote* (existing) |
| 250 | R094 | new | what's still missing for Ravi's condo quote? | New agent (not *Ravi Romano Auto Theft Claim CLM-2629725*) | *Ravi Fontaine Condo Binder and Quote Comparison* (existing) |
| 500 | R094 | new | what's still missing for Ravi's condo quote? | New agent (not *Ravi Romano Auto Theft Claim CLM-2629725*) | *Ravi Fontaine Condo Binder and Quote Comparison* (existing) |
| 250 | R094.p1 | new | whats still missing on ravi's condo quote | New agent (not *Ravi Romano Auto Theft Claim CLM-2629725*) | *Ravi Fontaine Condo Binder and Quote Comparison* (existing) |
| 500 | R094.p1 | new | whats still missing on ravi's condo quote | New agent (not *Ravi Romano Auto Theft Claim CLM-2629725*) | *Ravi Fontaine Condo Binder and Quote Comparison* (existing) |
| 250 | R094.p2 | new | what's still missin for Ravi's condo quote? | New agent (not *Ravi Romano Auto Theft Claim CLM-2629725*) | *Ravi Fontaine Condo Binder and Quote Comparison* (existing) |
| 500 | R094.p2 | new | what's still missin for Ravi's condo quote? | New agent (not *Ravi Romano Auto Theft Claim CLM-2629725*) | *Ravi Fontaine Condo Binder and Quote Comparison* (existing) |
| 250 | R094.p3 | new | Could you let me know what's still missing for Ravi's condo quote? | New agent (not *Ravi Romano Auto Theft Claim CLM-2629725*) | *Ravi Fontaine Condo Binder and Quote Comparison* (existing) |
| 500 | R094.p3 | new | Could you let me know what's still missing for Ravi's condo quote? | New agent (not *Ravi Romano Auto Theft Claim CLM-2629725*) | *Ravi Fontaine Condo Binder and Quote Comparison* (existing) |
| 250 | R096.p1 | new | aisha send the VIN yet? | New agent (not *Aisha Hughes Tenant Policy Quote*) | *Aisha Fontaine Address Update* (existing) |
| 100 | R096.p2 | new | did Aisha snd the VIN yet? | New agent (not *Aisha Hughes Tenant Policy Quote*) | *Aisha Bergeron Double Charge Investigation* (existing) |
| 100 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 250 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R099 | new | what's going on with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 100 | R099.p1 | new | whats up with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 250 | R099.p1 | new | whats up with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R099.p1 | new | whats up with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 100 | R099.p2 | new | whats going on with the okafor renewl? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 250 | R099.p2 | new | whats going on with the okafor renewl? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R099.p2 | new | whats going on with the okafor renewl? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 100 | R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 250 | R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | New agent (not *Okafor Landscaping COI City of Vaughan*) | *Okafor Landscaping COI City of Vaughan* (existing) |

## Ambiguous name (36)

Correct: Ask which person is meant, or check every agent with that name.

### Created a new agent instead (21)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R058.p2 | ambiguous | any updte from Priya? | Ask, or check all: *Priya Malik Home Quote*, *Priya Santos Premium Increase Inquiry* | *Priya Update Check* (new) |
| 250 | R061 | ambiguous | any update from Maya? | Ask, or check all: *Maya Zhang Auto Vehicle Addition AU-910606*, *Maya Ibrahim Storm Claim CLM-2623981* | *Maya Update Check* (new) |
| 500 | R061 | ambiguous | any update from Maya? | Ask, or check all: *Maya Zhang Auto Vehicle Addition AU-910606*, *Maya Ibrahim Storm Claim CLM-2623981* | *Maya Update Check* (new) |
| 500 | R061.p1 | ambiguous | any news from maya? | Ask, or check all: *Maya Zhang Auto Vehicle Addition AU-910606*, *Maya Ibrahim Storm Claim CLM-2623981* | *Maya Latest News Check* (new) |
| 500 | R061.p2 | ambiguous | anythng new from Maya yet? | Ask, or check all: *Maya Zhang Auto Vehicle Addition AU-910606*, *Maya Ibrahim Storm Claim CLM-2623981* | *Maya Updates Check* (new) |
| 500 | R061.p3 | ambiguous | Could you let me know if there's been any update from Maya? | Ask, or check all: *Maya Zhang Auto Vehicle Addition AU-910606*, *Maya Ibrahim Storm Claim CLM-2623981* | *Maya Update Check* (new) |
| 500 | R064 | ambiguous | any update from Omar? | Ask, or check all: *Omar Kim Payment Plan Inquiry*, *Omar Abbott Auto Vehicle Addition AU-949901* | *Omar Latest Update Check* (new) |
| 250 | R064.p1 | ambiguous | any news from omar? | Ask, or check all: *Omar Kim Payment Plan Inquiry*, *Omar Abbott Auto Vehicle Addition AU-949901* | *Omar Latest News Check* (new) |
| 500 | R064.p1 | ambiguous | any news from omar? | Ask, or check all: *Omar Kim Payment Plan Inquiry*, *Omar Abbott Auto Vehicle Addition AU-949901* | *Omar Latest News Check* (new) |
| 250 | R064.p2 | ambiguous | anythin new from Omar yet? | Ask, or check all: *Omar Kim Payment Plan Inquiry*, *Omar Abbott Auto Vehicle Addition AU-949901* | *Omar Inbox Check* (new) |
| 500 | R064.p2 | ambiguous | anythin new from Omar yet? | Ask, or check all: *Omar Kim Payment Plan Inquiry*, *Omar Abbott Auto Vehicle Addition AU-949901* | *Omar Latest Update Check* (new) |
| 500 | R064.p3 | ambiguous | Could you let me know if there's been any update from Omar? | Ask, or check all: *Omar Kim Payment Plan Inquiry*, *Omar Abbott Auto Vehicle Addition AU-949901* | *Omar Update Check* (new) |
| 500 | R067 | ambiguous | any update from Elena? | Ask, or check all: *Elena Walsh Auto Theft Claim CLM-2680012*, *Elena Costa Kia Sportage Vehicle Addition* | *Elena Latest Update Check* (new) |
| 250 | R067.p1 | ambiguous | any news from elena? | Ask, or check all: *Elena Walsh Auto Theft Claim CLM-2680012*, *Elena Costa Kia Sportage Vehicle Addition* | *Elena Inbox Check* (new) |
| 500 | R067.p1 | ambiguous | any news from elena? | Ask, or check all: *Elena Walsh Auto Theft Claim CLM-2680012*, *Elena Costa Kia Sportage Vehicle Addition* | *Elena Latest Messages Check* (new) |
| 500 | R067.p2 | ambiguous | anythng new from Elena yet? | Ask, or check all: *Elena Walsh Auto Theft Claim CLM-2680012*, *Elena Costa Kia Sportage Vehicle Addition* | *Elena Latest Messages Check* (new) |
| 500 | R067.p3 | ambiguous | Could you let me know if there's been any update from Elena? | Ask, or check all: *Elena Walsh Auto Theft Claim CLM-2680012*, *Elena Costa Kia Sportage Vehicle Addition* | *Elena Update Check* (new) |
| 500 | R070 | ambiguous | any update from Ravi? | Ask, or check all: *Ravi Patel Water Damage Claim CLM-2629050*, *Ravi Novak Auto Policy Vehicle Addition* | *Ravi Update Check* (new) |
| 500 | R070.p1 | ambiguous | any news from ravi? | Ask, or check all: *Ravi Patel Water Damage Claim CLM-2629050*, *Ravi Novak Auto Policy Vehicle Addition* | *Ravi News Check* (new) |
| 250 | R070.p3 | ambiguous | Could you let me know if there's been any update from Ravi? | Ask, or check all: *Ravi Patel Water Damage Claim CLM-2629050*, *Ravi Novak Auto Policy Vehicle Addition* | *Ravi Update Check* (new) |
| 500 | R070.p3 | ambiguous | Could you let me know if there's been any update from Ravi? | Ask, or check all: *Ravi Patel Water Damage Claim CLM-2629050*, *Ravi Novak Auto Policy Vehicle Addition* | *Ravi Update Check* (new) |

### Used a different existing agent (13)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 250 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R055 | ambiguous | any update from Daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 100 | R055.p1 | ambiguous | any news from daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 250 | R055.p1 | ambiguous | any news from daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R055.p1 | ambiguous | any news from daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 100 | R055.p2 | ambiguous | any updte from Daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 250 | R055.p2 | ambiguous | any updte from Daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R055.p2 | ambiguous | any updte from Daniel? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 100 | R055.p3 | ambiguous | Do you have any update from Daniel yet? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 250 | R055.p3 | ambiguous | Do you have any update from Daniel yet? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R055.p3 | ambiguous | Do you have any update from Daniel yet? | Ask, or check all: *Daniel Morin NSF Payment Inquiry*, *Daniel Alvarez Auto Vehicle Replacement AU-490318* | *Okafor Landscaping COI City of Vaughan* (existing) |
| 500 | R058.p3 | ambiguous | Do you have any update from Priya yet? | Ask, or check all: *Priya Malik Home Quote*, *Priya Santos Premium Increase Inquiry* | *Priya Sharma Honda CR-V Vehicle Addition* (existing) |

### Picked one of the matches without asking (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 250 | R064 | ambiguous | any update from Omar? | Ask, or check all: *Omar Kim Payment Plan Inquiry*, *Omar Abbott Auto Vehicle Addition AU-949901* | *Omar Kim Payment Plan Inquiry* (existing) |

### Replied without checking any agent (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R070.p2 | ambiguous | anythign new from Ravi yet? | Ask, or check all: *Ravi Patel Water Damage Claim CLM-2629050*, *Ravi Novak Auto Policy Vehicle Addition* | replied: "Quick check: you've got several Ravis on file. Which one do you mean? Ravi Romano (auto theft claim), Ravi Patel (water damage claim), Ravi…" |

## Cross-agent question (27)

Correct: Check at least half of the agents that hold the answer.

### Checked too few of the relevant agents (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 250 | R121.p1 | multi | status update on my open claims pls | At least 2 of 4: *Linda Gauthier Basement Water Claim Restoration*, *Maya Ibrahim Storm Claim CLM-2623981*, *Elena Walsh Auto Theft Claim CLM-2680012*, *Ravi Patel Water Damage Claim CLM-2629050* | *Linda Gauthier Basement Water Claim Restoration* (existing), *Open Claims Status Update* (new); checked 1 of 4 |
| 500 | R122.p1 | multi | certs still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Okafor Landscaping COI City of Vaughan* (existing); checked 1 of 8 |

### Checked none of the relevant agents (25)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 250 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 500 | R120 | multi | which clients still owe me documents? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 100 | R120.p1 | multi | which clients still owe me docs? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 250 | R120.p1 | multi | which clients still owe me docs? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 500 | R120.p1 | multi | which clients still owe me docs? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 100 | R120.p2 | multi | which clients still owe me documnts? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 250 | R120.p2 | multi | which clients still owe me documnts? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 500 | R120.p2 | multi | which clients still owe me documnts? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Search* (new); checked 0 of 3 |
| 100 | R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Tracker* (new); checked 0 of 3 |
| 250 | R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 500 | R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *Mona Fernandes Auto Quote and Renovation Receipts*, *Priya Malik Home Quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 500 | R121 | multi | give me a status update on all my open claims | At least 2 of 4: *Linda Gauthier Basement Water Claim Restoration*, *Maya Ibrahim Storm Claim CLM-2623981*, *Elena Walsh Auto Theft Claim CLM-2680012*, *Ravi Patel Water Damage Claim CLM-2629050* | *Open Claims Status Tracker* (new); checked 0 of 4 |
| 500 | R121.p1 | multi | status update on my open claims pls | At least 2 of 4: *Linda Gauthier Basement Water Claim Restoration*, *Maya Ibrahim Storm Claim CLM-2623981*, *Elena Walsh Auto Theft Claim CLM-2680012*, *Ravi Patel Water Damage Claim CLM-2629050* | *Open Claims Status Update* (new); checked 0 of 4 |
| 250 | R121.p2 | multi | gimme a status updte on all my open claims | At least 2 of 4: *Linda Gauthier Basement Water Claim Restoration*, *Maya Ibrahim Storm Claim CLM-2623981*, *Elena Walsh Auto Theft Claim CLM-2680012*, *Ravi Patel Water Damage Claim CLM-2629050* | *Open Claims Status Report* (new); checked 0 of 4 |
| 500 | R121.p2 | multi | gimme a status updte on all my open claims | At least 2 of 4: *Linda Gauthier Basement Water Claim Restoration*, *Maya Ibrahim Storm Claim CLM-2623981*, *Elena Walsh Auto Theft Claim CLM-2680012*, *Ravi Patel Water Damage Claim CLM-2629050* | *Open Claims Status Report* (new); checked 0 of 4 |
| 250 | R121.p3 | multi | Could you please give me a status update on all of my open claims? | At least 2 of 4: *Linda Gauthier Basement Water Claim Restoration*, *Maya Ibrahim Storm Claim CLM-2623981*, *Elena Walsh Auto Theft Claim CLM-2680012*, *Ravi Patel Water Damage Claim CLM-2629050* | *Open Claims Status Report* (new); checked 0 of 4 |
| 500 | R121.p3 | multi | Could you please give me a status update on all of my open claims? | At least 2 of 4: *Linda Gauthier Basement Water Claim Restoration*, *Maya Ibrahim Storm Claim CLM-2623981*, *Elena Walsh Auto Theft Claim CLM-2680012*, *Ravi Patel Water Damage Claim CLM-2629050* | *Open Claims Status Sweep* (new); checked 0 of 4 |
| 250 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Certificate Status Check* (new); checked 0 of 8 |
| 500 | R122 | multi | any certificates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Certificate Status Check* (new); checked 0 of 8 |
| 250 | R122.p1 | multi | certs still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Certificate Status Check* (new); checked 0 of 8 |
| 250 | R122.p2 | multi | any certifcates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Certificate Status Check* (new); checked 0 of 8 |
| 500 | R122.p2 | multi | any certifcates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Certificate Status Check* (new); checked 0 of 8 |
| 250 | R122.p3 | multi | Do you have any certificates that are still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Certificate Status Check* (new); checked 0 of 8 |
| 500 | R122.p3 | multi | Do you have any certificates that are still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI City of Vaughan*, *Cardenas Bakery COI Regional Municipality of York*, *Pereira Hardware COI Lakeshore Industrial REIT*, *Arjun Schmidt Certificate Request Dufferin Plaza*, *MacLeod Print Shop Markham Certificate*, *Vargas Architecture COI Lakeshore Industrial REIT*, *Neil Malik COI Malik Roofing Bayview*, *Leah Reyes Bayview COI Request* | *Certificate Status Check* (new); checked 0 of 8 |

## Chit-chat (5)

Correct: Reply without calling any agent.

### Called an agent (5)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R127.p1 ⚠ | none | nvm ignore that | No agent | *Bob Book Thursday Reminder* (new) |
| 250 | R127.p1 ⚠ | none | nvm ignore that | No agent | *Pinewood Kitchen Lunch Booking* (existing) |
| 500 | R127.p1 ⚠ | none | nvm ignore that | No agent | *Bob Book Reminder Cancel* (new) |
| 100 | R127.p2 ⚠ | none | nevermind, ignore thta | No agent | *Bob's Book Reminder Cancellation* (new) |
| 250 | R127.p2 ⚠ | none | nevermind, ignore thta | No agent | *Bob's Book Thursday Reminder Cancel* (new) |

## Counted as correct, but with extra agents (59)

Reached the right agent and also called others. Not included in the failure counts above.

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 250 | R013.p1 | reuse | where we at on maya's certificate for the regional municipality of york job | *Cardenas Bakery COI Regional Municipality of York* | *Cardenas Bakery COI Regional Municipality of York* (existing), *Petrov Daycare COI Regional Municipality of York* (existing) |
| 250 | R013.p3 | reuse | Could you let me know where things stand with Maya's certificate for the Regional Municipality of York job? | *Cardenas Bakery COI Regional Municipality of York* | *Cardenas Bakery COI Regional Municipality of York* (existing), *Petrov Daycare COI Regional Municipality of York* (existing) |
| 100 | R015 | reuse | where are we on Paula's certificate for the Lakeshore Industrial REIT job? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R015 | reuse | where are we on Paula's certificate for the Lakeshore Industrial REIT job? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 100 | R015.p1 | reuse | where we at on paula's certificate for the lakeshore industrial reit job | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R015.p1 | reuse | where we at on paula's certificate for the lakeshore industrial reit job | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 100 | R015.p2 | reuse | wheres paula's cert at for the Lakeshore Industrial REIT job | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 100 | R015.p3 | reuse | Could you let me know where things stand with Paula's certificate for the Lakeshore Industrial REIT job? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R015.p3 | reuse | Could you let me know where things stand with Paula's certificate for the Lakeshore Industrial REIT job? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 500 | R015.p3 | reuse | Could you let me know where things stand with Paula's certificate for the Lakeshore Industrial REIT job? | *Pereira Hardware COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 500 | R021.p1 | reuse | where we at on anas certificate for the city of markham job | *MacLeod Print Shop Markham Certificate* | *Ivanova Hardware COI City of Markham* (existing), *Osei Electric City of Markham COI* (existing), *MacLeod Print Shop Markham Certificate* (existing) |
| 100 | R021.p2 | reuse | wheres Ana's cert at for the City of Markham job | *MacLeod Print Shop Markham Certificate* | *Ana Markham Certificate Status* (new), *MacLeod Print Shop Markham Certificate* (existing) |
| 500 | R023 | reuse | what's going on with the Malik renewal? | *Malik Auto Body Lakeshore General Renewal* | *Malik Cleaning Trillium Renewal* (existing), *Malik Auto Body Lakeshore General Renewal* (existing) |
| 500 | R023.p1 | reuse | whats up with the malik renewal | *Malik Auto Body Lakeshore General Renewal* | *Malik Cleaning Trillium Renewal* (existing), *Malik Auto Body Lakeshore General Renewal* (existing), *Malik Architecture Harbourline BOP Renewal* (existing) |
| 500 | R023.p2 | reuse | hows the Malik renewal going | *Malik Auto Body Lakeshore General Renewal* | *Malik Cleaning Trillium Renewal* (existing), *Malik Auto Body Lakeshore General Renewal* (existing), *Malik Architecture Harbourline BOP Renewal* (existing) |
| 500 | R023.p3 | reuse | Could you give me an update on the Malik renewal? | *Malik Auto Body Lakeshore General Renewal* | *Malik Cleaning Trillium Renewal* (existing), *Malik Auto Body Lakeshore General Renewal* (existing), *Malik Architecture Harbourline BOP Renewal* (existing) |
| 500 | R025 | reuse | what's going on with the Tran renewal? | *Tran Roofing Harbourline CGL Renewal* | *Tran Roofing Harbourline CGL Renewal* (existing), *Tran Auto Body Fleet Schedule Update* (existing), *Tran Moving Fleet Schedule Update* (existing) |
| 100 | R027 | reuse | where are we on Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R027 | reuse | where are we on Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 500 | R027 | reuse | where are we on Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 100 | R027.p1 | reuse | where are we on bens cert for lakeshore industrial reit | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R027.p1 | reuse | where are we on bens cert for lakeshore industrial reit | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 500 | R027.p1 | reuse | where are we on bens cert for lakeshore industrial reit | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 100 | R027.p2 | reuse | Where do things stand on Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R027.p2 | reuse | Where do things stand on Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 100 | R027.p3 | reuse | Could you update me on where we are with Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 250 | R027.p3 | reuse | Could you update me on where we are with Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 500 | R027.p3 | reuse | Could you update me on where we are with Ben's certificate for the Lakeshore Industrial REIT job? | *Vargas Architecture COI Lakeshore Industrial REIT* | *Vargas Architecture COI Lakeshore Industrial REIT* (existing), *Pereira Hardware COI Lakeshore Industrial REIT* (existing) |
| 100 | R029.p3 | reuse | Could you let me know what's currently happening with the Tremblay renewal? | *Tremblay Roofing BOP Renewal* | *Tremblay Roofing BOP Renewal* (existing), *Karen Tremblay Umbrella Policy Review* (existing) |
| 500 | R031 | reuse | where are we on Neil's certificate for the Bayview Commercial Properties job? | *Neil Malik COI Malik Roofing Bayview* | *Neil Malik COI Malik Roofing Bayview* (existing), *Romano IT Certificate Bayview Commercial* (existing) |
| 500 | R031.p1 | reuse | where are we on neils cert for bayview commercial properties | *Neil Malik COI Malik Roofing Bayview* | *Neil Malik COI Malik Roofing Bayview* (existing), *Romano IT Certificate Bayview Commercial* (existing) |
| 100 | R033 | reuse | what's going on with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing) |
| 250 | R033 | reuse | what's going on with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing) |
| 500 | R033 | reuse | what's going on with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing), *Javier Sokolov Home Renewal 2025* (existing) |
| 100 | R033.p1 | reuse | whats going on with the sokolov renewal | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing) |
| 250 | R033.p1 | reuse | whats going on with the sokolov renewal | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing) |
| 500 | R033.p1 | reuse | whats going on with the sokolov renewal | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing), *Javier Sokolov Home Renewal 2025* (existing) |
| 100 | R033.p2 | reuse | where are we at with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing) |
| 250 | R033.p2 | reuse | where are we at with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing) |
| 100 | R033.p3 | reuse | Could you let me know what's currently happening with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing) |
| 250 | R033.p3 | reuse | Could you let me know what's currently happening with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing) |
| 500 | R033.p3 | reuse | Could you let me know what's currently happening with the Sokolov renewal? | *Sokolov Auto Body Trillium Renewal* | *Sokolov Auto Body Trillium Renewal* (existing), *Sokolov Brewing Northern Shield CGL Renewal* (existing), *Sokolov Electric Pinnacle Renewal* (existing), *Javier Sokolov Home Renewal 2025* (existing) |
| 500 | R039.p1 | reuse | wheres leahs cert for bayview commercial properties job | *Leah Reyes Bayview COI Request* | *Leah Reyes Bayview COI Request* (existing), *Romano IT Certificate Bayview Commercial* (existing) |
| 250 | R042.p2 | reuse | did billng get back to us about Leah's payment? | *Leah Fernandes NSF Payment Inquiry* | *Leah Fernandes NSF Payment Inquiry* (existing), *Leah Pereira Water Damage Claim* (new) |
| 250 | R044 | reuse | did billing get back to us about Paolo's payment? | *Paolo Schmidt Double Charge $348.50* | *Paolo Schmidt Double Charge $348.50* (existing), *Marco Rossi Double Charge Billing Fix* (existing) |
| 100 | R044.p3 | reuse | Have we heard back from billing yet about Paolo's payment? | *Paolo Schmidt Double Charge $348.50* | *Paolo Schmidt Double Charge $348.50* (existing), *Marco Rossi Double Charge Billing Fix* (existing) |
| 500 | R047.p1 | reuse | uma send the VIN yet? | *Uma Singh Auto Vehicle Replacement AU-959725* | *Uma Romano Auto Vehicle Addition AU-246551* (existing), *Uma Singh Auto Vehicle Replacement AU-959725* (existing) |
| 100 | R049.p1 | reuse | nora says bill's wrong, check it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bhatt Payment Plan Inquiry* (existing), *Nora Singh NSF Payment Inquiry* (existing) |
| 100 | R049.p2 | reuse | Nora says somethings wrong with the bil, look into it | *Nora Bhatt Payment Plan Inquiry* | *Nora Bhatt Payment Plan Inquiry* (existing), *Nora Singh NSF Payment Inquiry* (existing) |
| 100 | R049.p3 | reuse | Nora mentioned that something looks wrong with the bill, could you please look into it? | *Nora Bhatt Payment Plan Inquiry* | *Nora Bhatt Payment Plan Inquiry* (existing), *Nora Singh NSF Payment Inquiry* (existing) |
| 100 | R050 | reuse | did billing get back to us about Nora's payment? | *Nora Bhatt Payment Plan Inquiry* | *Nora Bhatt Payment Plan Inquiry* (existing), *Nora Singh NSF Payment Inquiry* (existing) |
| 500 | R050 | reuse | did billing get back to us about Nora's payment? | *Nora Bhatt Payment Plan Inquiry* | *Nora Bhatt Payment Plan Inquiry* (existing), *Nora Singh NSF Payment Inquiry* (existing) |
| 100 | R050.p1 | reuse | billing get back on nora's payment yet? | *Nora Bhatt Payment Plan Inquiry* | *Nora Bhatt Payment Plan Inquiry* (existing), *Nora Singh NSF Payment Inquiry* (existing) |
| 250 | R050.p1 | reuse | billing get back on nora's payment yet? | *Nora Bhatt Payment Plan Inquiry* | *Nora Singh NSF Payment Inquiry* (existing), *Nora Bhatt Payment Plan Inquiry* (existing) |
| 100 | R050.p2 | reuse | did billng get back to us about Nora's paymnt? | *Nora Bhatt Payment Plan Inquiry* | *Nora Bhatt Payment Plan Inquiry* (existing), *Nora Singh NSF Payment Inquiry* (existing) |
| 250 | R050.p2 | reuse | did billng get back to us about Nora's paymnt? | *Nora Bhatt Payment Plan Inquiry* | *Nora Singh NSF Payment Inquiry* (existing), *Nora Bhatt Payment Plan Inquiry* (existing) |
| 500 | R050.p2 | reuse | did billng get back to us about Nora's paymnt? | *Nora Bhatt Payment Plan Inquiry* | *Nora Singh NSF Payment Inquiry* (existing), *Nora Bhatt Payment Plan Inquiry* (existing) |
| 100 | R050.p3 | reuse | Have you heard back from billing about Nora's payment yet? | *Nora Bhatt Payment Plan Inquiry* | *Nora Bhatt Payment Plan Inquiry* (existing), *Nora Singh NSF Payment Inquiry* (existing) |
| 250 | R050.p3 | reuse | Have you heard back from billing about Nora's payment yet? | *Nora Bhatt Payment Plan Inquiry* | *Nora Singh NSF Payment Inquiry* (existing), *Nora Bhatt Payment Plan Inquiry* (existing) |

## ⚠ Known labelling problems

These cases are still scored as labelled, so the counts above match `summary.md`, but their failures are a fault of the test data, not of OpenPoke.

| Case | Failures in this run | Problem |
|---|---|---|
| R026 | 12 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R030 | 12 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R080 | 12 | Same prompt as R023 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik). |
| R110 | 12 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R112 | 12 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R127 | 5 | The seeded chat ends with "remind me to bring Bob's book on thursday", so cancelling that reminder is a fair reading. |
