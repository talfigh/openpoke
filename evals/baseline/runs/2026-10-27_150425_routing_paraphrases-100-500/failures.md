# Routing failures: paraphrases-100-500

Every case this run scored as wrong, grouped by what should have happened. Generated from `results.json` by `run_baseline.py failures` (no LLM calls). Agent names: synthetic; prompts: paraphrases. Case ids ending in `.pN` are paraphrase N of the same case.

**383 failures out of 1155 scored cases.** 38 of them come from cases with a known labelling problem (marked ⚠, listed at the end).

| What should have happened | What OpenPoke did instead | 100 agents | 250 agents | 500 agents |
|---|---|---|---|---|
| Should reuse an existing agent | Created a new agent instead | 66 of 244 | 65 of 244 | 92 of 244 |
| Should reuse an existing agent | Used a different existing agent | 6 of 244 | 11 of 244 | 11 of 244 |
| Should reuse an existing agent | Asked the user instead of acting | 0 of 244 | 1 of 244 | 0 of 244 |
| Should reuse an existing agent | Replied without checking any agent | 1 of 244 | 1 of 244 | 0 of 244 |
| Should create a new agent | Put the work into an existing agent | 21 of 87 | 29 of 87 | 29 of 87 |
| Ambiguous name | Created a new agent instead | 0 of 21 | 5 of 21 | 11 of 21 |
| Ambiguous name | Used a different existing agent | 3 of 21 | 5 of 21 | 4 of 21 |
| Ambiguous name | Picked one of the matches without asking | 0 of 21 | 2 of 21 | 0 of 21 |
| Cross-agent question | Checked too few of the relevant agents | 0 of 9 | 1 of 9 | 2 of 9 |
| Cross-agent question | Checked none of the relevant agents | 4 of 9 | 5 of 9 | 7 of 9 |
| Chit-chat | Called an agent | 0 of 24 | 0 of 24 | 1 of 24 |

## Failed at every roster size (82)

| Case | Kind | Prompt | Outcomes |
|---|---|---|---|
| R014.p1 | reuse | did cardenas bakery inc get their coi yet | created a new agent instead |
| R014.p2 | reuse | has Cardenas Bakery Inc. gotten their COI yet | created a new agent instead |
| R014.p3 | reuse | Do you know whether Cardenas Bakery Inc. has received their COI yet? | created a new agent instead |
| R018.p1 | reuse | did schmidt cleaning services ltd get their coi yet | created a new agent instead |
| R018.p2 | reuse | has Schmidt Cleaning Services Ltd. gotten their COI yet | created a new agent instead |
| R018.p3 | reuse | Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet? | created a new agent instead |
| R020.p1 | reuse | did ines send the renewal figures yet | created a new agent instead |
| R020.p2 | reuse | has Ines sent over the renewal figures yet | created a new agent instead |
| R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | created a new agent instead |
| R021.p2 | reuse | wheres Ana's cert at for the City of Markham job | created a new agent instead |
| R028.p1 | reuse | did vargas architecture inc get their coi yet | created a new agent instead |
| R028.p2 | reuse | Has Vargas Architecture Inc. received their COI yet? | created a new agent instead |
| R028.p3 | reuse | Could you let me know if Vargas Architecture Inc. has gotten their COI yet? | created a new agent instead |
| R030.p1 ⚠ | reuse | did farah send the renewal figs yet | used a different existing agent |
| R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | used a different existing agent |
| R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | used a different existing agent |
| R032.p1 | reuse | did malik roofing ltd get their coi yet | created a new agent instead |
| R032.p2 | reuse | Has Malik Roofing Ltd. received their COI yet? | created a new agent instead |
| R032.p3 | reuse | Could you let me know if Malik Roofing Ltd. has gotten their COI yet? | created a new agent instead |
| R034.p1 | reuse | did laila send the renewal figs yet | created a new agent instead, used a different existing agent |
| R034.p2 | reuse | Has Laila sent over the renewal figures yet? | created a new agent instead, used a different existing agent |
| R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | created a new agent instead, used a different existing agent |
| R038.p1 | reuse | javier send the renewal figs yet | created a new agent instead, used a different existing agent |
| R038.p2 | reuse | has Javier sent the renewal figs yet? | created a new agent instead, used a different existing agent |
| R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | created a new agent instead, used a different existing agent |
| R039.p1 | reuse | wheres leahs cert for bayview commercial properties job | created a new agent instead |
| R039.p2 | reuse | where we at on Leah's certificate for the Bayview Commercial Properties job? | created a new agent instead |
| R039.p3 | reuse | Could you update me on where things stand with Leah's certificate for the Bayview Commercial Properties job? | created a new agent instead |
| R047.p2 | reuse | did Uma send the VN yet? | used a different existing agent, created a new agent instead |
| R052.p1 | reuse | did mona send the reno receipts | created a new agent instead |
| R052.p2 | reuse | did Mona send the renovaton receipts? | created a new agent instead |
| R052.p3 | reuse | Do you know if Mona has sent over the renovation receipts yet? | created a new agent instead |
| R053.p1 | lookalike | daniel morin says bill's wrong, check it | created a new agent instead |
| R053.p2 | lookalike | Daniel Morin says somethings wrong wit the bill, look into it | created a new agent instead |
| R053.p3 | lookalike | Daniel Morin mentioned that something seems off with the bill, could you please look into it? | created a new agent instead |
| R055.p1 | ambiguous | any news from daniel? | used a different existing agent |
| R055.p2 | ambiguous | any updte from Daniel? | used a different existing agent |
| R055.p3 | ambiguous | Do you have any update from Daniel yet? | used a different existing agent |
| R059.p2 | lookalike | did Maya Zhang send teh VIN yet? | created a new agent instead |
| R059.p3 | lookalike | Has Maya Zhang sent over the VIN yet? | created a new agent instead |
| R063.p1 | lookalike | omar abbott send the VIN yet? | created a new agent instead |
| R063.p2 | lookalike | did Omar Abbott snd the VIN yet? | created a new agent instead |
| R063.p3 | lookalike | Has Omar Abbott sent over the VIN yet, do you know? | created a new agent instead |
| R072.p1 | new | whats up with the pereira renewal | put the work into an existing agent |
| R072.p2 | new | what's going on with the Pereira renewl? | put the work into an existing agent |
| R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | put the work into an existing agent |
| R075.p2 | new | where are we on the MacLeod renewal? | put the work into an existing agent |
| R075.p3 | new | Could you fill me in on what's happening with the MacLeod renewal? | put the work into an existing agent |
| R077.p3 | new | Could you update me on where we are with Farah's certificate for the Lakeshore Industrial REIT job? | put the work into an existing agent |
| R080.p1 ⚠ | new | whats going on w the malik renewal | put the work into an existing agent |
| R080.p2 ⚠ | new | where are we on the malik renewal? | put the work into an existing agent |
| R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | put the work into an existing agent |
| R087.p1 | new | adriana send the VIN yet? | put the work into an existing agent |
| R099.p1 | new | whats up with the okafor renewal? | put the work into an existing agent |
| R099.p2 | new | whats going on with the okafor renewl? | put the work into an existing agent |
| R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | put the work into an existing agent |
| R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | created a new agent instead |
| R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | created a new agent instead |
| R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | created a new agent instead |
| R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | created a new agent instead |
| R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | created a new agent instead |
| R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | created a new agent instead |
| R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | created a new agent instead |
| R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | created a new agent instead |
| R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | created a new agent instead |
| R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | created a new agent instead |
| R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | created a new agent instead |
| R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | created a new agent instead |
| R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | used a different existing agent, created a new agent instead |
| R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | created a new agent instead |
| R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | used a different existing agent, created a new agent instead |
| R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | created a new agent instead |
| R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | created a new agent instead, used a different existing agent |
| R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | created a new agent instead |
| R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | created a new agent instead |
| R117.p1 | reminder | remind me Wednesday at 10am to chek that Leah's certificate was issued | created a new agent instead |
| R117.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Leah's certificate has been issued? | created a new agent instead |
| R118.p1 | reminder | remind me thursday to update leah on the billing issue | created a new agent instead |
| R120.p1 | multi | which clients still owe me docs? | checked none of the relevant agents |
| R120.p2 | multi | which clients still owe me documnts? | checked none of the relevant agents |
| R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | checked none of the relevant agents |
| R122.p2 | multi | any certifcates still waiting to go out? | checked none of the relevant agents |

## Should reuse an existing agent (254)

Correct: Send the request to the one existing agent that owns the work (reuse, lookalike and reminder cases).

### Created a new agent instead (223)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R007.p3 | reuse | Could you add Priya's new car to her policy? She recently bought it and needs it covered. | *Priya Sharma Auto Policy - Honda CR-V* | *Priya Sharma Vehicle Addition* (new) |
| 100 | R014.p1 | reuse | did cardenas bakery inc get their coi yet | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 250 | R014.p1 | reuse | did cardenas bakery inc get their coi yet | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 500 | R014.p1 | reuse | did cardenas bakery inc get their coi yet | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 100 | R014.p2 | reuse | has Cardenas Bakery Inc. gotten their COI yet | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 250 | R014.p2 | reuse | has Cardenas Bakery Inc. gotten their COI yet | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 500 | R014.p2 | reuse | has Cardenas Bakery Inc. gotten their COI yet | *Certificate for Maya Cardenas* | *Cardenas Bakery Inc COI Status* (new) |
| 100 | R014.p3 | reuse | Do you know whether Cardenas Bakery Inc. has received their COI yet? | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 250 | R014.p3 | reuse | Do you know whether Cardenas Bakery Inc. has received their COI yet? | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 500 | R014.p3 | reuse | Do you know whether Cardenas Bakery Inc. has received their COI yet? | *Certificate for Maya Cardenas* | *Cardenas Bakery COI Status* (new) |
| 500 | R015.p1 | reuse | where we at on paula's certificate for the lakeshore industrial reit job | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Lakeshore REIT Certificate Status* (new) |
| 250 | R015.p2 | reuse | wheres paula's cert at for the Lakeshore Industrial REIT job | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Status Lookup* (new) |
| 500 | R015.p2 | reuse | wheres paula's cert at for the Lakeshore Industrial REIT job | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Lakeshore Certificate Status* (new) |
| 100 | R018.p1 | reuse | did schmidt cleaning services ltd get their coi yet | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 250 | R018.p1 | reuse | did schmidt cleaning services ltd get their coi yet | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 500 | R018.p1 | reuse | did schmidt cleaning services ltd get their coi yet | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 100 | R018.p2 | reuse | has Schmidt Cleaning Services Ltd. gotten their COI yet | *Certificate for Arjun Schmidt* | *Schmidt Cleaning COI Status* (new) |
| 250 | R018.p2 | reuse | has Schmidt Cleaning Services Ltd. gotten their COI yet | *Certificate for Arjun Schmidt* | *Schmidt Cleaning COI Status* (new) |
| 500 | R018.p2 | reuse | has Schmidt Cleaning Services Ltd. gotten their COI yet | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 100 | R018.p3 | reuse | Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet? | *Certificate for Arjun Schmidt* | *Schmidt Cleaning COI Status* (new) |
| 250 | R018.p3 | reuse | Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet? | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 500 | R018.p3 | reuse | Do you know whether Schmidt Cleaning Services Ltd. has received their COI yet? | *Certificate for Arjun Schmidt* | *Schmidt Cleaning Services COI Status* (new) |
| 100 | R020.p1 | reuse | did ines send the renewal figures yet | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 250 | R020.p1 | reuse | did ines send the renewal figures yet | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 500 | R020.p1 | reuse | did ines send the renewal figures yet | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 100 | R020.p2 | reuse | has Ines sent over the renewal figures yet | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 250 | R020.p2 | reuse | has Ines sent over the renewal figures yet | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures* (new) |
| 500 | R020.p2 | reuse | has Ines sent over the renewal figures yet | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 100 | R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 250 | R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 500 | R020.p3 | reuse | Do you know whether Ines has sent the renewal figures yet? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Figures Check* (new) |
| 250 | R021.p1 | reuse | where we at on anas certificate for the city of markham job | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Status* (new) |
| 500 | R021.p1 | reuse | where we at on anas certificate for the city of markham job | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Status* (new) |
| 100 | R021.p2 | reuse | wheres Ana's cert at for the City of Markham job | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Status* (new) |
| 250 | R021.p2 | reuse | wheres Ana's cert at for the City of Markham job | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate City of Markham* (new) |
| 500 | R021.p2 | reuse | wheres Ana's cert at for the City of Markham job | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Search* (new) |
| 100 | R021.p3 | reuse | Could you let me know where things stand with Ana's certificate for the City of Markham job? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Status* (new) |
| 500 | R021.p3 | reuse | Could you let me know where things stand with Ana's certificate for the City of Markham job? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Markham Certificate Status* (new) |
| 500 | R024.p1 | reuse | did uma send the renewal figures yet | *Uma Malik Policy Renewal* | *Uma Renewal Figures Check* (new) |
| 500 | R024.p3 | reuse | Do you know whether Uma has sent the renewal figures yet? | *Uma Malik Policy Renewal* | *Uma Renewal Figures Check* (new) |
| 100 | R028.p1 | reuse | did vargas architecture inc get their coi yet | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 250 | R028.p1 | reuse | did vargas architecture inc get their coi yet | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 500 | R028.p1 | reuse | did vargas architecture inc get their coi yet | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 100 | R028.p2 | reuse | Has Vargas Architecture Inc. received their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 250 | R028.p2 | reuse | Has Vargas Architecture Inc. received their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 500 | R028.p2 | reuse | Has Vargas Architecture Inc. received their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 100 | R028.p3 | reuse | Could you let me know if Vargas Architecture Inc. has gotten their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 250 | R028.p3 | reuse | Could you let me know if Vargas Architecture Inc. has gotten their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 500 | R028.p3 | reuse | Could you let me know if Vargas Architecture Inc. has gotten their COI yet? | *Certificate for Ben Vargas* | *Vargas Architecture COI Status* (new) |
| 100 | R032.p1 | reuse | did malik roofing ltd get their coi yet | *Certificate for Neil Malik* | *Malik Roofing Ltd COI Status* (new) |
| 250 | R032.p1 | reuse | did malik roofing ltd get their coi yet | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 500 | R032.p1 | reuse | did malik roofing ltd get their coi yet | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 100 | R032.p2 | reuse | Has Malik Roofing Ltd. received their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 250 | R032.p2 | reuse | Has Malik Roofing Ltd. received their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 500 | R032.p2 | reuse | Has Malik Roofing Ltd. received their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Check* (new) |
| 100 | R032.p3 | reuse | Could you let me know if Malik Roofing Ltd. has gotten their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 250 | R032.p3 | reuse | Could you let me know if Malik Roofing Ltd. has gotten their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 500 | R032.p3 | reuse | Could you let me know if Malik Roofing Ltd. has gotten their COI yet? | *Certificate for Neil Malik* | *Malik Roofing COI Status* (new) |
| 100 | R034.p1 | reuse | did laila send the renewal figs yet | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures* (new) |
| 500 | R034.p1 | reuse | did laila send the renewal figs yet | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 100 | R034.p2 | reuse | Has Laila sent over the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 500 | R034.p2 | reuse | Has Laila sent over the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 100 | R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Figures Check* (new) |
| 250 | R036.p1 | reuse | did hana send the renewal figs yet | *Hana Ellis Policy Renewal* | *Hana Renewal Figures Check* (new) |
| 500 | R036.p1 | reuse | did hana send the renewal figs yet | *Hana Ellis Policy Renewal* | *Hana Renewal Figures Check* (new) |
| 500 | R036.p3 | reuse | Could you check whether Hana has sent the renewal figures yet? | *Hana Ellis Policy Renewal* | *Hana renewal figures check* (new) |
| 100 | R038.p1 | reuse | javier send the renewal figs yet | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 250 | R038.p1 | reuse | javier send the renewal figs yet | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 100 | R038.p2 | reuse | has Javier sent the renewal figs yet? | *Patel renewal* | *Javier Renewal Figures Check* (new) |
| 100 | R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | *Patel renewal* | *Javier Renewal Figures* (new) |
| 100 | R039.p1 | reuse | wheres leahs cert for bayview commercial properties job | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Search* (new) |
| 250 | R039.p1 | reuse | wheres leahs cert for bayview commercial properties job | *COI Reyes Roofing Inc.* | *Leah Certificate Bayview Search* (new) |
| 500 | R039.p1 | reuse | wheres leahs cert for bayview commercial properties job | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Search* (new) |
| 100 | R039.p2 | reuse | where we at on Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 250 | R039.p2 | reuse | where we at on Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 500 | R039.p2 | reuse | where we at on Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 100 | R039.p3 | reuse | Could you update me on where things stand with Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 250 | R039.p3 | reuse | Could you update me on where things stand with Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 500 | R039.p3 | reuse | Could you update me on where things stand with Leah's certificate for the Bayview Commercial Properties job? | *COI Reyes Roofing Inc.* | *Leah Bayview Certificate Status* (new) |
| 100 | R041.p1 | reuse | leah says somethings off w the bill, check it | *Leah NSF Payment* | *Leah Bill Check* (new) |
| 500 | R041.p1 | reuse | leah says somethings off w the bill, check it | *Leah NSF Payment* | *Leah Bill Check* (new) |
| 250 | R041.p2 | reuse | Leah says something's wrong with the bil, can you look into it | *Leah NSF Payment* | *Leah Billing Issue* (new) |
| 500 | R041.p2 | reuse | Leah says something's wrong with the bil, can you look into it | *Leah NSF Payment* | *Leah Billing Issue* (new) |
| 500 | R041.p3 | reuse | Leah mentioned that something seems to be wrong with the bill, could you please look into it? | *Leah NSF Payment* | *Leah Bill Issue* (new) |
| 250 | R047.p2 | reuse | did Uma send the VN yet? | *Uma Toyota RAV4 Auto Policy* | *Uma VN Check* (new) |
| 500 | R047.p2 | reuse | did Uma send the VN yet? | *Uma Toyota RAV4 Auto Policy* | *Uma VN Check* (new) |
| 500 | R049.p1 | reuse | nora says bill's wrong, check it | *Nora Bhatt Billing Check* | *Nora Bill Dispute Check* (new) |
| 500 | R049.p2 | reuse | Nora says somethings wrong with the bil, look into it | *Nora Bhatt Billing Check* | *Nora Billing Issue Investigation* (new) |
| 500 | R049.p3 | reuse | Nora mentioned that something looks wrong with the bill, could you please look into it? | *Nora Bhatt Billing Check* | *Nora Bill Issue Check* (new) |
| 500 | R050.p2 | reuse | did billng get back to us about Nora's paymnt? | *Nora Bhatt Billing Check* | *Nora Payment Billing Status* (new) |
| 100 | R052.p1 | reuse | did mona send the reno receipts | *New business quote - Mona Fernandes* | *Mona Reno Receipts Check* (new) |
| 250 | R052.p1 | reuse | did mona send the reno receipts | *New business quote - Mona Fernandes* | *Mona Reno Receipts Search* (new) |
| 500 | R052.p1 | reuse | did mona send the reno receipts | *New business quote - Mona Fernandes* | *Mona Reno Receipts* (new) |
| 100 | R052.p2 | reuse | did Mona send the renovaton receipts? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts Check* (new) |
| 250 | R052.p2 | reuse | did Mona send the renovaton receipts? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts Check* (new) |
| 500 | R052.p2 | reuse | did Mona send the renovaton receipts? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts Check* (new) |
| 100 | R052.p3 | reuse | Do you know if Mona has sent over the renovation receipts yet? | *New business quote - Mona Fernandes* | *Mona Fernandes Renovation Receipts* (new) |
| 250 | R052.p3 | reuse | Do you know if Mona has sent over the renovation receipts yet? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts* (new) |
| 500 | R052.p3 | reuse | Do you know if Mona has sent over the renovation receipts yet? | *New business quote - Mona Fernandes* | *Mona Renovation Receipts Check* (new) |
| 100 | R053.p1 | lookalike | daniel morin says bill's wrong, check it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 250 | R053.p1 | lookalike | daniel morin says bill's wrong, check it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 500 | R053.p1 | lookalike | daniel morin says bill's wrong, check it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 100 | R053.p2 | lookalike | Daniel Morin says somethings wrong wit the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 250 | R053.p2 | lookalike | Daniel Morin says somethings wrong wit the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 500 | R053.p2 | lookalike | Daniel Morin says somethings wrong wit the bill, look into it | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 100 | R053.p3 | lookalike | Daniel Morin mentioned that something seems off with the bill, could you please look into it? | *Daniel NSF Payment* | *Daniel Morin Bill Check* (new) |
| 250 | R053.p3 | lookalike | Daniel Morin mentioned that something seems off with the bill, could you please look into it? | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 500 | R053.p3 | lookalike | Daniel Morin mentioned that something seems off with the bill, could you please look into it? | *Daniel NSF Payment* | *Daniel Morin Billing Check* (new) |
| 250 | R056.p1 | lookalike | whats still missing for priya malik's home quote | *Priya quote* | *Priya Malik Home Quote Status* (new) |
| 250 | R056.p2 | lookalike | what's stil missing for Priya Malik's home quote? | *Priya quote* | *Priya Malik Home Quote Status* (new) |
| 500 | R056.p2 | lookalike | what's stil missing for Priya Malik's home quote? | *Priya quote* | *Priya Malik Home Quote Status* (new) |
| 500 | R056.p3 | lookalike | Could you let me know what's still missing for Priya Malik's home quote? | *Priya quote* | *Priya Malik Home Quote Status* (new) |
| 250 | R059.p1 | lookalike | did maya zhang send the vin yet | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 500 | R059.p1 | lookalike | did maya zhang send the vin yet | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 100 | R059.p2 | lookalike | did Maya Zhang send teh VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 250 | R059.p2 | lookalike | did Maya Zhang send teh VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 500 | R059.p2 | lookalike | did Maya Zhang send teh VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 100 | R059.p3 | lookalike | Has Maya Zhang sent over the VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 250 | R059.p3 | lookalike | Has Maya Zhang sent over the VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 500 | R059.p3 | lookalike | Has Maya Zhang sent over the VIN yet? | *Maya Tesla Model Y Auto Policy* | *Maya Zhang VIN Check* (new) |
| 100 | R063.p1 | lookalike | omar abbott send the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 250 | R063.p1 | lookalike | omar abbott send the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 500 | R063.p1 | lookalike | omar abbott send the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 100 | R063.p2 | lookalike | did Omar Abbott snd the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 250 | R063.p2 | lookalike | did Omar Abbott snd the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 500 | R063.p2 | lookalike | did Omar Abbott snd the VIN yet? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 100 | R063.p3 | lookalike | Has Omar Abbott sent over the VIN yet, do you know? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 250 | R063.p3 | lookalike | Has Omar Abbott sent over the VIN yet, do you know? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 500 | R063.p3 | lookalike | Has Omar Abbott sent over the VIN yet, do you know? | *Add Mazda to Omar's policy* | *Omar Abbott VIN Check* (new) |
| 100 | R066.p1 | lookalike | did elena costa send the vin yet | *Elena Kia Sportage Auto Policy* | *Elena Costa VIN Check* (new) |
| 500 | R066.p1 | lookalike | did elena costa send the vin yet | *Elena Kia Sportage Auto Policy* | *Elena Costa VIN Check* (new) |
| 100 | R066.p2 | lookalike | did Elena Costa send the VIN yt? | *Elena Kia Sportage Auto Policy* | *Elena Costa VIN Check* (new) |
| 500 | R066.p2 | lookalike | did Elena Costa send the VIN yt? | *Elena Kia Sportage Auto Policy* | *Elena Costa VIN Check* (new) |
| 500 | R066.p3 | lookalike | Has Elena Costa sent over the VIN yet? | *Elena Kia Sportage Auto Policy* | *Elena Costa VIN Check* (new) |
| 100 | R069.p1 | lookalike | did ravi novak send the VIN yet | *Add Ford to Ravi's policy* | *Ravi Novak VIN Check* (new) |
| 500 | R069.p1 | lookalike | did ravi novak send the VIN yet | *Add Ford to Ravi's policy* | *Ravi Novak VIN Check* (new) |
| 500 | R069.p2 | lookalike | did Ravi Novak snd the VIN yet? | *Add Ford to Ravi's policy* | *Ravi Novak VIN Check* (new) |
| 100 | R069.p3 | lookalike | Has Ravi Novak sent over the VIN yet? | *Add Ford to Ravi's policy* | *Ravi Novak VIN Check* (new) |
| 100 | R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | *Okafor Landscaping COI - City of Vaughan* | *Daniel Cert Check Reminder* (new) |
| 250 | R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | *Okafor Landscaping COI - City of Vaughan* | *Daniel Certificate Reminder* (new) |
| 500 | R102.p1 | reminder | remind me tomorrow at 10am to check daniels cert went out | *Okafor Landscaping COI - City of Vaughan* | *Daniel Okafor Cert Reminder* (new) |
| 250 | R102.p2 | reminder | remind me tomorrow at 10am to chekc daniel's certificate went out | *Okafor Landscaping COI - City of Vaughan* | *Daniel Okafor Certificate Reminder* (new) |
| 500 | R102.p2 | reminder | remind me tomorrow at 10am to chekc daniel's certificate went out | *Okafor Landscaping COI - City of Vaughan* | *Daniel Okafor Certificate Check Reminder* (new) |
| 250 | R102.p3 | reminder | Could you remind me tomorrow at 10am to check that Daniel's certificate went out? | *Okafor Landscaping COI - City of Vaughan* | *Daniel Okafor Certificate Reminder* (new) |
| 500 | R102.p3 | reminder | Could you remind me tomorrow at 10am to check that Daniel's certificate went out? | *Okafor Landscaping COI - City of Vaughan* | *Daniel Certificate Check Reminder* (new) |
| 100 | R103.p1 | reminder | remind me tomorrow at 9am to call linda re the adjuster | *Linda Gauthier Water Claim* | *Linda Call Reminder* (new) |
| 500 | R103.p1 | reminder | remind me tomorrow at 9am to call linda re the adjuster | *Linda Gauthier Water Claim* | *Linda Gauthier Adjuster Call Reminder* (new) |
| 100 | R103.p2 | reminder | Could you please remind me tomorrow at 9am to call Linda about the adjuster? | *Linda Gauthier Water Claim* | *Linda Adjuster Call Reminder* (new) |
| 500 | R103.p2 | reminder | Could you please remind me tomorrow at 9am to call Linda about the adjuster? | *Linda Gauthier Water Claim* | *Linda Adjuster Call Reminder* (new) |
| 500 | R104.p2 | reminder | remind me wednesday at 10am to chekc Maya's certificate was issued | *Certificate for Maya Cardenas* | *Maya Certificate Reminder* (new) |
| 100 | R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 250 | R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 500 | R105.p1 | reminder | remind me wednesday at 10am to check paulas cert was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Cert Reminder* (new) |
| 100 | R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 250 | R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 500 | R105.p2 | reminder | remind me wednesday at 10am to chekc Paula's certificate was issued | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 100 | R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 250 | R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 500 | R105.p3 | reminder | Could you remind me on Wednesday at 10am to check that Paula's certificate was issued? | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* | *Paula Certificate Reminder* (new) |
| 500 | R106.p3 | reminder | Could you remind me on Wednesday at 10am to check that Arjun's certificate was issued? | *Certificate for Arjun Schmidt* | *Arjun Certificate Check Reminder* (new) |
| 100 | R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Chase Ines Renewal Reminder* (new) |
| 250 | R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Reminder Chase Ines Renewal* (new) |
| 500 | R107.p1 | reminder | remind me next monday to chase ines for the renewal numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Numbers Reminder* (new) |
| 100 | R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Numbers Reminder* (new) |
| 250 | R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Reminder Chase Ines Renewal* (new) |
| 500 | R107.p2 | reminder | remind me next monday to chase Ines for the renewl numbers | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Numbers Reminder* (new) |
| 100 | R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Reminder* (new) |
| 250 | R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Follow-up Reminder* (new) |
| 500 | R107.p3 | reminder | Could you remind me next Monday to follow up with Ines for the renewal numbers? | *Kowalski Electric Ltd. Renewal CPP-104292* | *Ines Renewal Follow-up Reminder* (new) |
| 100 | R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 250 | R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 500 | R108.p1 | reminder | remind me wednesday at 10am to check anas cert was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 100 | R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 250 | R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Check Reminder* (new) |
| 500 | R108.p2 | reminder | remind me wednesday at 10am to chekc Ana's certificate was issued | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 100 | R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 250 | R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Reminder* (new) |
| 500 | R108.p3 | reminder | Could you remind me on Wednesday at 10am to check that Ana's certificate was issued? | *MacLeod Print Shop Ltd. COI - City of Markham* | *Ana Certificate Check Reminder* (new) |
| 100 | R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | *Uma Malik Policy Renewal* | *Reminder Chase Uma Renewal* (new) |
| 250 | R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | *Uma Malik Policy Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 500 | R109.p1 | reminder | remind me next monday to chase uma for the renewal numbers | *Uma Malik Policy Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 250 | R109.p2 | reminder | Could you please remind me next Monday to follow up with Uma for the renewal numbers? | *Uma Malik Policy Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 500 | R109.p2 | reminder | Could you please remind me next Monday to follow up with Uma for the renewal numbers? | *Uma Malik Policy Renewal* | *Uma Renewal Numbers Reminder* (new) |
| 250 | R110.p1 ⚠ | reminder | remind me next monday to chase farah for the renewal numbers | *Farah Tran Policy Renewal* | *Farah renewal reminder* (new) |
| 500 | R110.p1 ⚠ | reminder | remind me next monday to chase farah for the renewal numbers | *Farah Tran Policy Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 100 | R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | *Farah Tran Policy Renewal* | *Reminder - Chase Farah Renewal Numbers* (new) |
| 250 | R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | *Farah Tran Policy Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R110.p2 ⚠ | reminder | remind me next monday to chas Farah for the renewal numbers | *Farah Tran Policy Renewal* | *Farah Renewal Numbers Reminder* (new) |
| 100 | R110.p3 ⚠ | reminder | Could you please set a reminder for next Monday to follow up with Farah about the renewal numbers? | *Farah Tran Policy Renewal* | *Farah Renewal Follow-up Reminder* (new) |
| 500 | R110.p3 ⚠ | reminder | Could you please set a reminder for next Monday to follow up with Farah about the renewal numbers? | *Farah Tran Policy Renewal* | *Farah Renewal Follow-up Reminder* (new) |
| 500 | R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Renewal Numbers Monday Reminder* (new) |
| 100 | R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Renewal Numbers Reminder* (new) |
| 250 | R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R112.p2 ⚠ | reminder | remind me next monday to ping Farah about the renewal numbrs | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Renewal Numbers Reminder* (new) |
| 500 | R113.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Neil's certificate has been issued? | *Certificate for Neil Malik* | *Neil Certificate Reminder* (new) |
| 100 | R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Chase Laila Renewal Reminder* (new) |
| 250 | R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Reminder - Chase Laila Renewal Numbers* (new) |
| 500 | R114.p1 | reminder | remind me next monday to chase laila for the renewal numbers | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Chase Laila Renewal Reminder* (new) |
| 100 | R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Numbers Reminder* (new) |
| 500 | R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Renewal Follow-up Reminder* (new) |
| 250 | R115.p1 | reminder | remind me next monday to chase hana for the renewal numbers | *Hana Ellis Policy Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 500 | R115.p1 | reminder | remind me next monday to chase hana for the renewal numbers | *Hana Ellis Policy Renewal* | *Hana Renewal Numbers Reminder* (new) |
| 250 | R115.p2 | reminder | Could you please set a reminder for next Monday to follow up with Hana about the renewal numbers? | *Hana Ellis Policy Renewal* | *Hana Renewal Follow-up Reminder* (new) |
| 500 | R115.p2 | reminder | Could you please set a reminder for next Monday to follow up with Hana about the renewal numbers? | *Hana Ellis Policy Renewal* | *Hana Renewal Numbers Follow-up Reminder* (new) |
| 100 | R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | *Patel renewal* | *Javier Renewal Numbers Reminder* (new) |
| 250 | R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | *Patel renewal* | *Reminder - Chase Javier Renewal Numbers* (new) |
| 500 | R116.p1 | reminder | remind me next monday to chase javier for the renewal numbers | *Patel renewal* | *Javier Renewal Numbers Reminder* (new) |
| 100 | R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | *Patel renewal* | *Javier Renewal Numbers Reminder* (new) |
| 250 | R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | *Patel renewal* | *Javier Renewal Follow-up Reminder* (new) |
| 500 | R116.p2 | reminder | Could you please remind me next Monday to follow up with Javier about the renewal numbers? | *Patel renewal* | *Javier Renewal Follow-up Reminder* (new) |
| 100 | R117.p1 | reminder | remind me Wednesday at 10am to chek that Leah's certificate was issued | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 250 | R117.p1 | reminder | remind me Wednesday at 10am to chek that Leah's certificate was issued | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 500 | R117.p1 | reminder | remind me Wednesday at 10am to chek that Leah's certificate was issued | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 100 | R117.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Leah's certificate has been issued? | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 250 | R117.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Leah's certificate has been issued? | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 500 | R117.p2 | reminder | Could you please remind me on Wednesday at 10am to check that Leah's certificate has been issued? | *COI Reyes Roofing Inc.* | *Leah Certificate Reminder* (new) |
| 100 | R118.p1 | reminder | remind me thursday to update leah on the billing issue | *Leah NSF Payment* | *Leah Billing Issue Reminder* (new) |
| 250 | R118.p1 | reminder | remind me thursday to update leah on the billing issue | *Leah NSF Payment* | *Leah Billing Issue Reminder* (new) |
| 500 | R118.p1 | reminder | remind me thursday to update leah on the billing issue | *Leah NSF Payment* | *Leah Billing Issue Reminder* (new) |
| 250 | R118.p2 | reminder | remind me thursday to updte Leah on the billing issue | *Leah NSF Payment* | *Thursday Leah Billing Reminder* (new) |
| 500 | R118.p3 | reminder | Could you please remind me on Thursday to give Leah an update on the billing issue? | *Leah NSF Payment* | *Leah Billing Update Reminder* (new) |
| 500 | R119.p1 | reminder | remind me thursday to update paolo on the billing issue | *Billing issue - Paolo Schmidt* | *Paolo Billing Update Reminder* (new) |

### Used a different existing agent (28)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R023.p1 ⚠ | reuse | whats up with the malik renewal | *Uma Malik Policy Renewal* | *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing), *Malik Architecture Ltd. Renewal BOP-801881* (existing) |
| 500 | R023.p2 ⚠ | reuse | hows the Malik renewal going | *Uma Malik Policy Renewal* | *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing), *Malik Architecture Ltd. Renewal BOP-801881* (existing) |
| 500 | R023.p3 ⚠ | reuse | Could you give me an update on the Malik renewal? | *Uma Malik Policy Renewal* | *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing), *Malik Architecture Ltd. Renewal BOP-801881* (existing) |
| 100 | R030.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R030.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 500 | R030.p1 ⚠ | reuse | did farah send the renewal figs yet | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 100 | R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 500 | R030.p2 ⚠ | reuse | Has Farah sent over the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 100 | R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 500 | R030.p3 ⚠ | reuse | Could you check whether Farah has sent the renewal figures yet? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R034.p1 | reuse | did laila send the renewal figs yet | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Haddad Umbrella Policy Review* (existing) |
| 250 | R034.p2 | reuse | Has Laila sent over the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Haddad Umbrella Policy Review* (existing) |
| 250 | R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Haddad Umbrella Policy Review* (existing) |
| 500 | R034.p3 | reuse | Could you check whether Laila has sent the renewal figures yet? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Haddad Umbrella Policy Review* (existing) |
| 500 | R036.p2 | reuse | Has Hana sent over the renewal figures yet? | *Hana Ellis Policy Renewal* | *Hana Ibrahim Home Renewal 2025* (existing) |
| 500 | R038.p1 | reuse | javier send the renewal figs yet | *Patel renewal* | *Javier Sokolov Home Renewal 2025* (existing) |
| 250 | R038.p2 | reuse | has Javier sent the renewal figs yet? | *Patel renewal* | *Javier Fernandes Condo Insurance* (existing) |
| 500 | R038.p2 | reuse | has Javier sent the renewal figs yet? | *Patel renewal* | *Javier Sokolov Home Renewal 2025* (existing) |
| 250 | R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | *Patel renewal* | *Javier Fernandes Condo Insurance* (existing) |
| 500 | R038.p3 | reuse | Do you know if Javier has sent over the renewal figures yet? | *Patel renewal* | *Javier Sokolov Home Renewal 2025* (existing) |
| 100 | R047.p2 | reuse | did Uma send the VN yet? | *Uma Toyota RAV4 Auto Policy* | *Uma Malik Policy Renewal* (existing) |
| 100 | R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R112.p1 ⚠ | reminder | remind me monday to nudge farah for the renewal numbers | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 100 | R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R112.p3 ⚠ | reminder | Would you mind reminding me next Monday to get in touch with Farah about the renewal numbers? | *Tremblay Roofing Ltd. Renewal BOP-104123* | *Farah Tran Policy Renewal* (existing) |
| 250 | R114.p2 | reminder | Could you please remind me next Monday to follow up with Laila about the renewal numbers? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Laila Haddad Umbrella Policy Review* (existing) |

### Asked the user instead of acting (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 250 | R049.p3 | reuse | Nora mentioned that something looks wrong with the bill, could you please look into it? | *Nora Bhatt Billing Check* | replied: "Which Nora? I've got billing checks open for both Nora Bhatt and Nora Singh. Tell me which one and I'll dig into the bill." |

### Replied without checking any agent (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R007.p2 | reuse | add priya's new car to her polcy | *Priya Sharma Auto Policy - Honda CR-V* | replied: "Quick question before I set this up: what's the new car (year, make, model, and VIN if you have it)? And is this Priya Sharma? I see a few …" |
| 250 | R049.p1 | reuse | nora says bill's wrong, check it | *Nora Bhatt Billing Check* | replied: "Two Noras have billing checks open, Nora Bhatt and Nora Singh. Which one is it?" |

## Should create a new agent (79)

Correct: Create a new agent. The client already has an agent for a different job, and that agent must not be used.

### Put the work into an existing agent (79)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R072.p1 | new | whats up with the pereira renewal | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 250 | R072.p1 | new | whats up with the pereira renewal | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 500 | R072.p1 | new | whats up with the pereira renewal | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 100 | R072.p2 | new | what's going on with the Pereira renewl? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 250 | R072.p2 | new | what's going on with the Pereira renewl? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 500 | R072.p2 | new | what's going on with the Pereira renewl? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 100 | R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 250 | R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 500 | R072.p3 | new | Could you let me know what's going on with the Pereira renewal? | New agent (not *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*) | *Naveen Pereira Policy Renewal* (existing) |
| 100 | R073.p1 | new | whats up with the schmidt renewal | New agent (not *Certificate for Arjun Schmidt*) | *Certificate for Arjun Schmidt* (existing) |
| 250 | R073.p1 | new | whats up with the schmidt renewal | New agent (not *Certificate for Arjun Schmidt*) | *Certificate for Arjun Schmidt* (existing) |
| 250 | R073.p2 | new | where are we on the schmidt renewal? | New agent (not *Certificate for Arjun Schmidt*) | *Certificate for Arjun Schmidt* (existing) |
| 100 | R073.p3 | new | Could you let me know where things stand with the Schmidt renewal? | New agent (not *Certificate for Arjun Schmidt*) | *Certificate for Arjun Schmidt* (existing), *Billing issue - Paolo Schmidt* (existing) |
| 250 | R073.p3 | new | Could you let me know where things stand with the Schmidt renewal? | New agent (not *Certificate for Arjun Schmidt*) | *Certificate for Arjun Schmidt* (existing) |
| 100 | R075.p1 | new | whats going on w the macleod renewal | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 500 | R075.p1 | new | whats going on w the macleod renewal | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Brewing Co. Renewal BOP-857302* (existing) |
| 100 | R075.p2 | new | where are we on the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 250 | R075.p2 | new | where are we on the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 500 | R075.p2 | new | where are we on the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Brewing Co. Renewal BOP-857302* (existing) |
| 100 | R075.p3 | new | Could you fill me in on what's happening with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 250 | R075.p3 | new | Could you fill me in on what's happening with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Print Shop Ltd. COI - City of Markham* (existing) |
| 500 | R075.p3 | new | Could you fill me in on what's happening with the MacLeod renewal? | New agent (not *MacLeod Print Shop Ltd. COI - City of Markham*) | *MacLeod Brewing Co. Renewal BOP-857302* (existing) |
| 500 | R076.p2 | new | where are we on Uma's certificate for the Kingsway Realty Holdings job? | New agent (not *Uma Malik Policy Renewal*) | *Abbott Architecture Inc. COI - Kingsway Realty Holdings* (existing) |
| 100 | R077.p1 | new | where are we on farah's cert for lakeshore industrial reit | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 250 | R077.p2 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 500 | R077.p2 | new | where are we on Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 100 | R077.p3 | new | Could you update me on where we are with Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing), *Farah Tran Policy Renewal* (existing) |
| 250 | R077.p3 | new | Could you update me on where we are with Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 500 | R077.p3 | new | Could you update me on where we are with Farah's certificate for the Lakeshore Industrial REIT job? | New agent (not *Farah Tran Policy Renewal*) | *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 100 | R080.p1 ⚠ | new | whats going on w the malik renewal | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 250 | R080.p1 ⚠ | new | whats going on w the malik renewal | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 500 | R080.p1 ⚠ | new | whats going on w the malik renewal | New agent (not *Certificate for Neil Malik*) | *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing) |
| 100 | R080.p2 ⚠ | new | where are we on the malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 250 | R080.p2 ⚠ | new | where are we on the malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 500 | R080.p2 ⚠ | new | where are we on the malik renewal? | New agent (not *Certificate for Neil Malik*) | *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing), *Malik Architecture Ltd. Renewal BOP-801881* (existing) |
| 100 | R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 250 | R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Uma Malik Policy Renewal* (existing) |
| 500 | R080.p3 ⚠ | new | Could you let me know what's happening with the Malik renewal? | New agent (not *Certificate for Neil Malik*) | *Malik Cleaning Services Ltd. Renewal CPP-922123* (existing), *Malik Architecture Ltd. Renewal BOP-801881* (existing) |
| 250 | R085.p1 | new | open a claim file for leah's water damage | New agent (not *Leah NSF Payment*) | *Leah Pereira Water Damage Claim* (existing) |
| 500 | R085.p1 | new | open a claim file for leah's water damage | New agent (not *Leah NSF Payment*) | *Leah Pereira Water Damage Claim* (existing) |
| 250 | R085.p2 | new | start claim file for Leah's water damge | New agent (not *Leah NSF Payment*) | *Leah Pereira Water Damage Claim* (existing) |
| 250 | R085.p3 | new | Could you please start a claim file for Leah's water damage? | New agent (not *Leah NSF Payment*) | *Leah Pereira Water Damage Claim* (existing) |
| 500 | R085.p3 | new | Could you please start a claim file for Leah's water damage? | New agent (not *Leah NSF Payment*) | *Leah Pereira Water Damage Claim* (existing) |
| 100 | R087.p1 | new | adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Pereira Billing Check* (existing), *Adriana Ghosh Condo Insurance* (existing), *Adriana cancellation* (existing) |
| 250 | R087.p1 | new | adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Ellis Auto Claim (2025)* (existing) |
| 500 | R087.p1 | new | adriana send the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Add Volkswagen to Adriana's policy* (existing) |
| 250 | R087.p2 | new | did Adriana snd the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Ellis Auto Claim (2025)* (existing) |
| 250 | R087.p3 | new | Do you know whether Adriana has sent the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Adriana Ellis Auto Claim (2025)* (existing) |
| 500 | R087.p3 | new | Do you know whether Adriana has sent the VIN yet? | New agent (not *Adriana Pereira Billing Check*) | *Add Volkswagen to Adriana's policy* (existing) |
| 500 | R089.p1 | new | status on nora's theft claim? | New agent (not *Nora Bhatt Billing Check*) | *Nora Ivanova Auto Claim (2025)* (existing) |
| 500 | R089.p2 | new | whats the status of Nora's theft claim | New agent (not *Nora Bhatt Billing Check*) | *Nora Ivanova Auto Claim (2025)* (existing) |
| 500 | R089.p3 | new | Could you check on the current status of Nora's theft claim for me? | New agent (not *Nora Bhatt Billing Check*) | *Nora Ivanova Auto Claim (2025)* (existing) |
| 100 | R090.p1 | new | mona says the bill looks off, can u check it | New agent (not *New business quote - Mona Fernandes*) | *New business quote - Mona Fernandes* (existing) |
| 100 | R093.p1 | new | whats still missing on owen's auto quote | New agent (not *Owen Zielinski Billing Check*) | *Owen Tenant Policy Quote* (existing) |
| 100 | R093.p2 | new | what's still missin for Owen's auto quote? | New agent (not *Owen Zielinski Billing Check*) | *Owen Tenant Policy Quote* (existing) |
| 100 | R093.p3 | new | Could you let me know what's still missing for Owen's auto quote? | New agent (not *Owen Zielinski Billing Check*) | *Owen Tenant Policy Quote* (existing) |
| 500 | R093.p3 | new | Could you let me know what's still missing for Owen's auto quote? | New agent (not *Owen Zielinski Billing Check*) | *Owen Fontaine Vehicle Addition* (existing) |
| 250 | R094.p1 | new | whats still missing on ravi's condo quote | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 500 | R094.p1 | new | whats still missing on ravi's condo quote | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 250 | R094.p2 | new | what's still missin for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 500 | R094.p2 | new | what's still missin for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 250 | R094.p3 | new | Could you let me know what's still missing for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 500 | R094.p3 | new | Could you let me know what's still missing for Ravi's condo quote? | New agent (not *Auto Theft Claim - Ravi Romano*) | *Ravi Fontaine Condo Insurance* (existing) |
| 250 | R095.p1 | new | yusuf says the bill looks off, can u check it | New agent (not *New business quote - Yusuf Patel*) | *Email to Yusuf* (existing) |
| 250 | R096.p1 | new | aisha send the VIN yet? | New agent (not *Aisha quote*) | *Aisha quote* (existing) |
| 500 | R096.p1 | new | aisha send the VIN yet? | New agent (not *Aisha quote*) | *Aisha quote* (existing) |
| 250 | R096.p2 | new | did Aisha snd the VIN yet? | New agent (not *Aisha quote*) | *Aisha quote* (existing) |
| 500 | R096.p2 | new | did Aisha snd the VIN yet? | New agent (not *Aisha quote*) | *Aisha quote* (existing) |
| 250 | R096.p3 | new | Do you know whether Aisha has sent the VIN yet? | New agent (not *Aisha quote*) | *Aisha quote* (existing) |
| 500 | R096.p3 | new | Do you know whether Aisha has sent the VIN yet? | New agent (not *Aisha quote*) | *Aisha quote* (existing) |
| 100 | R099.p1 | new | whats up with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 250 | R099.p1 | new | whats up with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R099.p1 | new | whats up with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 100 | R099.p2 | new | whats going on with the okafor renewl? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 250 | R099.p2 | new | whats going on with the okafor renewl? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R099.p2 | new | whats going on with the okafor renewl? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 100 | R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 250 | R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R099.p3 | new | Could you give me an update on what's happening with the okafor renewal? | New agent (not *Okafor Landscaping COI - City of Vaughan*) | *Okafor Landscaping COI - City of Vaughan* (existing) |

## Ambiguous name (30)

Correct: Ask which person is meant, or check every agent with that name.

### Created a new agent instead (16)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R061.p1 | ambiguous | any news from maya? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | *Maya Latest News* (new) |
| 500 | R061.p2 | ambiguous | anythng new from Maya yet? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | *Maya Inbox Check* (new) |
| 250 | R061.p3 | ambiguous | Could you let me know if there's been any update from Maya? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | *Maya Inbox Update Check* (new) |
| 500 | R061.p3 | ambiguous | Could you let me know if there's been any update from Maya? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | *Maya Update Check* (new) |
| 250 | R064.p1 | ambiguous | any news from omar? | Ask, or check all: *Omar Kim Billing Check*, *Add Mazda to Omar's policy* | *Omar News Check* (new) |
| 500 | R064.p1 | ambiguous | any news from omar? | Ask, or check all: *Omar Kim Billing Check*, *Add Mazda to Omar's policy* | *Omar Inbox Check* (new) |
| 500 | R064.p2 | ambiguous | anythin new from Omar yet? | Ask, or check all: *Omar Kim Billing Check*, *Add Mazda to Omar's policy* | *Omar Latest Updates Check* (new) |
| 250 | R064.p3 | ambiguous | Could you let me know if there's been any update from Omar? | Ask, or check all: *Omar Kim Billing Check*, *Add Mazda to Omar's policy* | *Omar Update Check* (new) |
| 500 | R064.p3 | ambiguous | Could you let me know if there's been any update from Omar? | Ask, or check all: *Omar Kim Billing Check*, *Add Mazda to Omar's policy* | *Omar Update Check* (new) |
| 500 | R067.p1 | ambiguous | any news from elena? | Ask, or check all: *Elena theft claim*, *Elena Kia Sportage Auto Policy* | *Elena News Check* (new) |
| 500 | R067.p3 | ambiguous | Could you let me know if there's been any update from Elena? | Ask, or check all: *Elena theft claim*, *Elena Kia Sportage Auto Policy* | *Elena Update Check* (new) |
| 500 | R070.p1 | ambiguous | any news from ravi? | Ask, or check all: *Ravi Patel Water Damage Claim*, *Add Ford to Ravi's policy* | *Ravi News Check* (new) |
| 250 | R070.p2 | ambiguous | anythign new from Ravi yet? | Ask, or check all: *Ravi Patel Water Damage Claim*, *Add Ford to Ravi's policy* | *Ravi Inbox Check* (new) |
| 500 | R070.p2 | ambiguous | anythign new from Ravi yet? | Ask, or check all: *Ravi Patel Water Damage Claim*, *Add Ford to Ravi's policy* | *Ravi Inbox Check* (new) |
| 250 | R070.p3 | ambiguous | Could you let me know if there's been any update from Ravi? | Ask, or check all: *Ravi Patel Water Damage Claim*, *Add Ford to Ravi's policy* | *Ravi Updates Check* (new) |
| 500 | R070.p3 | ambiguous | Could you let me know if there's been any update from Ravi? | Ask, or check all: *Ravi Patel Water Damage Claim*, *Add Ford to Ravi's policy* | *Ravi Update Check* (new) |

### Used a different existing agent (12)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R055.p1 | ambiguous | any news from daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 250 | R055.p1 | ambiguous | any news from daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R055.p1 | ambiguous | any news from daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 100 | R055.p2 | ambiguous | any updte from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 250 | R055.p2 | ambiguous | any updte from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R055.p2 | ambiguous | any updte from Daniel? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 100 | R055.p3 | ambiguous | Do you have any update from Daniel yet? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 250 | R055.p3 | ambiguous | Do you have any update from Daniel yet? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R055.p3 | ambiguous | Do you have any update from Daniel yet? | Ask, or check all: *Daniel NSF Payment*, *Daniel Alvarez Vehicle Addition* | *Okafor Landscaping COI - City of Vaughan* (existing) |
| 500 | R058.p1 | ambiguous | any news from priya? | Ask, or check all: *Priya quote*, *Priya Santos Billing Check* | *Priya Sharma Auto Policy - Honda CR-V* (existing) |
| 250 | R058.p3 | ambiguous | Do you have any update from Priya yet? | Ask, or check all: *Priya quote*, *Priya Santos Billing Check* | *Priya Sharma Auto Policy - Honda CR-V* (existing) |
| 250 | R061.p1 | ambiguous | any news from maya? | Ask, or check all: *Maya Tesla Model Y Auto Policy*, *Storm Damage Claim - Maya Ibrahim* | *Maya Abbott Storm Damage Claim* (existing) |

### Picked one of the matches without asking (2)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 250 | R067.p1 | ambiguous | any news from elena? | Ask, or check all: *Elena theft claim*, *Elena Kia Sportage Auto Policy* | *Elena theft claim* (existing) |
| 250 | R067.p3 | ambiguous | Could you let me know if there's been any update from Elena? | Ask, or check all: *Elena theft claim*, *Elena Kia Sportage Auto Policy* | *Elena theft claim* (existing) |

## Cross-agent question (19)

Correct: Check at least half of the agents that hold the answer.

### Checked too few of the relevant agents (3)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 250 | R121.p2 | multi | gimme a status updte on all my open claims | At least 2 of 4: *Linda Gauthier Water Claim*, *Storm Damage Claim - Maya Ibrahim*, *Elena theft claim*, *Ravi Patel Water Damage Claim* | *Linda Gauthier Water Claim* (existing), *Open Claims Status Sweep* (new); checked 1 of 4 |
| 500 | R121.p2 | multi | gimme a status updte on all my open claims | At least 2 of 4: *Linda Gauthier Water Claim*, *Storm Damage Claim - Maya Ibrahim*, *Elena theft claim*, *Ravi Patel Water Damage Claim* | *Linda Gauthier Water Claim* (existing), *Lionel Walsh Water Damage Claim* (existing), *Water Damage Claim - Rachel Nguyen* (existing), *Leah Pereira Water Damage Claim* (existing), *Storm Damage Claim - Lucas Fernandes* (existing), *Kitchen Fire Claim - Ahmed Quinn* (existing), *Auto Theft Claim - Ravi Romano* (existing), *Emily Castillo Collision Claim* (existing), *Claims Handoff to Mei* (existing), *Felix Lefebvre Burglary Claim* (existing), *Carmen hail claim* (existing); checked 1 of 4 |
| 500 | R122.p1 | multi | certs still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Okafor Landscaping COI - City of Vaughan* (existing), *Pending Certificates Status Check* (new); checked 1 of 8 |

### Checked none of the relevant agents (16)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 100 | R120.p1 | multi | which clients still owe me docs? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Docs Check* (new); checked 0 of 3 |
| 250 | R120.p1 | multi | which clients still owe me docs? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Docs Check* (new); checked 0 of 3 |
| 500 | R120.p1 | multi | which clients still owe me docs? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 100 | R120.p2 | multi | which clients still owe me documnts? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 250 | R120.p2 | multi | which clients still owe me documnts? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 500 | R120.p2 | multi | which clients still owe me documnts? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 100 | R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents* (new); checked 0 of 3 |
| 250 | R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 500 | R120.p3 | multi | Could you let me know which clients still have outstanding documents owed to me? | At least 2 of 3: *Jordan Whitfield Home and Auto Quote*, *New business quote - Mona Fernandes*, *Priya quote* | *Outstanding Client Documents Check* (new); checked 0 of 3 |
| 250 | R121.p1 | multi | status update on my open claims pls | At least 2 of 4: *Linda Gauthier Water Claim*, *Storm Damage Claim - Maya Ibrahim*, *Elena theft claim*, *Ravi Patel Water Damage Claim* | *Open Claims Status Check* (new); checked 0 of 4 |
| 500 | R121.p1 | multi | status update on my open claims pls | At least 2 of 4: *Linda Gauthier Water Claim*, *Storm Damage Claim - Maya Ibrahim*, *Elena theft claim*, *Ravi Patel Water Damage Claim* | *Open Claims Status Update* (new); checked 0 of 4 |
| 500 | R121.p3 | multi | Could you please give me a status update on all of my open claims? | At least 2 of 4: *Linda Gauthier Water Claim*, *Storm Damage Claim - Maya Ibrahim*, *Elena theft claim*, *Ravi Patel Water Damage Claim* | *Open Claims Status Check* (new); checked 0 of 4 |
| 100 | R122.p2 | multi | any certifcates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Certificate Status Check* (new); checked 0 of 8 |
| 250 | R122.p2 | multi | any certifcates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Certificate Status Check* (new); checked 0 of 8 |
| 500 | R122.p2 | multi | any certifcates still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Certificate Status Check* (new); checked 0 of 8 |
| 500 | R122.p3 | multi | Do you have any certificates that are still waiting to go out? | At least 4 of 8: *Okafor Landscaping COI - City of Vaughan*, *Certificate for Maya Cardenas*, *Pereira Hardware Inc. COI - Lakeshore Industrial REIT*, *Certificate for Arjun Schmidt*, *MacLeod Print Shop Ltd. COI - City of Markham*, *Certificate for Ben Vargas*, *Certificate for Neil Malik*, *COI Reyes Roofing Inc.* | *Pending Certificates Status* (new); checked 0 of 8 |

## Chit-chat (1)

Correct: Reply without calling any agent.

### Called an agent (1)

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 500 | R127.p1 ⚠ | none | nvm ignore that | No agent | *Bob's Book Reminder Cancel* (new) |

## Counted as correct, but with extra agents (28)

Reached the right agent and also called others. Not included in the failure counts above.

| Size | Case | Kind | Prompt | Expected | What OpenPoke did |
|---|---|---|---|---|---|
| 250 | R013.p3 | reuse | Could you let me know where things stand with Maya's certificate for the Regional Municipality of York job? | *Certificate for Maya Cardenas* | *Certificate for Maya Cardenas* (existing), *Petrov Daycare Ltd. COI - Regional Municipality of York* (existing) |
| 100 | R027.p1 | reuse | where are we on bens cert for lakeshore industrial reit | *Certificate for Ben Vargas* | *Certificate for Ben Vargas* (existing), *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 100 | R027.p2 | reuse | Where do things stand on Ben's certificate for the Lakeshore Industrial REIT job? | *Certificate for Ben Vargas* | *Certificate for Ben Vargas* (existing), *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 100 | R027.p3 | reuse | Could you update me on where we are with Ben's certificate for the Lakeshore Industrial REIT job? | *Certificate for Ben Vargas* | *Certificate for Ben Vargas* (existing), *Pereira Hardware Inc. COI - Lakeshore Industrial REIT* (existing) |
| 500 | R031.p1 | reuse | where are we on neils cert for bayview commercial properties | *Certificate for Neil Malik* | *Romano IT Consulting Inc. COI - Bayview Commercial Properties* (existing), *Certificate for Neil Malik* (existing) |
| 500 | R031.p3 | reuse | Could you update me on where we are with Neil's certificate for the Bayview Commercial Properties job? | *Certificate for Neil Malik* | *Certificate for Neil Malik* (existing), *Romano IT Consulting Inc. COI - Bayview Commercial Properties* (existing) |
| 100 | R033.p1 | reuse | whats going on with the sokolov renewal | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 250 | R033.p1 | reuse | whats going on with the sokolov renewal | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 100 | R033.p2 | reuse | where are we at with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 250 | R033.p2 | reuse | where are we at with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 500 | R033.p2 | reuse | where are we at with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 100 | R033.p3 | reuse | Could you let me know what's currently happening with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 250 | R033.p3 | reuse | Could you let me know what's currently happening with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 500 | R033.p3 | reuse | Could you let me know what's currently happening with the Sokolov renewal? | *Sokolov Auto Body Ltd. Renewal CPP-561853* | *Sokolov Auto Body Ltd. Renewal CPP-561853* (existing), *Sokolov Brewing Co. Renewal CGL-206285* (existing), *Sokolov Electric Ltd. Renewal BOP-647518* (existing) |
| 250 | R036.p2 | reuse | Has Hana sent over the renewal figures yet? | *Hana Ellis Policy Renewal* | *Hana Ibrahim Home Renewal 2025* (existing), *Hana Ellis Policy Renewal* (existing) |
| 250 | R036.p3 | reuse | Could you check whether Hana has sent the renewal figures yet? | *Hana Ellis Policy Renewal* | *Hana Ibrahim Home Renewal 2025* (existing), *Hana Ellis Policy Renewal* (existing) |
| 100 | R049.p1 | reuse | nora says bill's wrong, check it | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 100 | R049.p2 | reuse | Nora says somethings wrong with the bil, look into it | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 250 | R049.p2 | reuse | Nora says somethings wrong with the bil, look into it | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 100 | R049.p3 | reuse | Nora mentioned that something looks wrong with the bill, could you please look into it? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 100 | R050.p1 | reuse | billing get back on nora's payment yet? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 250 | R050.p1 | reuse | billing get back on nora's payment yet? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 500 | R050.p1 | reuse | billing get back on nora's payment yet? | *Nora Bhatt Billing Check* | *Nora Singh Billing Check* (existing), *Nora Bhatt Billing Check* (existing) |
| 100 | R050.p2 | reuse | did billng get back to us about Nora's paymnt? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 250 | R050.p2 | reuse | did billng get back to us about Nora's paymnt? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 100 | R050.p3 | reuse | Have you heard back from billing about Nora's payment yet? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 250 | R050.p3 | reuse | Have you heard back from billing about Nora's payment yet? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |
| 500 | R050.p3 | reuse | Have you heard back from billing about Nora's payment yet? | *Nora Bhatt Billing Check* | *Nora Bhatt Billing Check* (existing), *Nora Singh Billing Check* (existing) |

## ⚠ Known labelling problems

These cases are still scored as labelled, so the counts above match `summary.md`, but their failures are a fault of the test data, not of OpenPoke.

| Case | Failures in this run | Problem |
|---|---|---|
| R023 | 3 | Same prompt as R080 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik). |
| R030 | 9 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R080 | 9 | Same prompt as R023 with the opposite label (reuse Uma Malik's renewal vs create one for Neil Malik). |
| R110 | 7 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R112 | 9 | Two core clients named Farah (Tran, Tremblay) both have a renewal agent; the prompt is ambiguous. |
| R127 | 1 | The seeded chat ends with "remind me to bring Bob's book on thursday", so cancelling that reminder is a fair reading. |
