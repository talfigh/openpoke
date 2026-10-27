# grow-roster run 2026-10-27_130131 (openpoke-names)

git 98949d7 + uncommitted server changes · models ['anthropic/claude-haiku-5.5'] · 2352.3s

- Topics handed to OpenPoke in creation order: 500
- Distinct agents it created: 483 · topics put into an already existing agent: 14 (12 same person, 2 unrelated) · no agent at all: 3
- Names identical to the generator's: 75

| | Generator names | OpenPoke names |
|---|---|---|
| Name mentions the person | 95% | 96% |
| Name mentions the company (commercial clients) | 100% | 100% |
| Mean words per name | 4.3 | 5.2 |
| Near-duplicate name pairs (token overlap ≥ 60%) | 297 | 32 |
| Names that collide on the log-file slug (NOTES 3.3) | 0 | 0 |
| LLM cost | | $1.3784 |

Side by side (random sample):

| Generator | OpenPoke |
|---|---|
| Billing issue - Abena Adeyemi | Abena Adeyemi NSF Payment Follow-up |
| Naveen Rahman Home Renewal 2025 | Naveen Rahman Home Renewal 2025 |
| Inbox Split with Kevin (September) | Kevin Client Inbox Split Proposal |
| Chowdhury Bakery Fleet Schedule Update | Felix Chowdhury Bakery Fleet Schedule Update |
| Certificate for Maya Cardenas | Cardenas Bakery COI Regional Municipality of York |
| Billing issue - Rachel Vargas | Rachel Vargas NSF Payment Inquiry |
| COI Castillo Auto Body Inc. | Castillo Auto Body Bayview COI Request |
| Fontaine Brewing Co. Renewal BOP-621778 | Yara Fontaine Northern Shield BOP Renewal |
| Felix Haddad Policy Renewal | Haddad Fitness Studio Pinnacle Renewal |
| Thanksgiving Plans | Thanksgiving Hosting vs Travel Options |
| Lionel Kim Address Change | Lionel Kim Address Change |
| Deepa Fontaine Umbrella Policy Review | Deepa Fontaine Umbrella Policy Review |
| Laila Haddad Umbrella Policy Review | Laila Haddad Umbrella Coverage Comparison |
| Carmen Evans Condo Insurance | Carmen Evans Condo Insurance Setup |
| Nora Singh Billing Check | Nora Singh NSF Payment Inquiry |
| Passport Renewal | Passport Renewal Requirements |
| Mona address change | Mona Ivanova Address Update |
| Mila Costa Home Renewal 2025 | Mila Costa Home Renewal 2025 |
| Tomas quote | Tomas Kowalski Tenant Policy Quote |
| Amir Zhang Umbrella Policy Review | Amir Zhang Umbrella Policy Review |
| Dubois Catering Payroll Audit | Ravi Dubois Catering Payroll Audit |
| Diego Zhang Condo Insurance | Diego Zhang Condo Insurance Comparison |
| Cardenas Fitness Studio Fleet Schedule Update | Cardenas Fitness Studio Fleet Schedule Update |
| Victor Morin Collision Claim | Victor Morin Collision Claim CLM-2652972 |
| Chowdhury Fitness Studio Fleet Schedule Update | Chowdhury Fitness Studio Fleet Schedule Update |
| Sofia Tremblay Auto Claim (2025) | Sofia Tremblay Auto Claim 2025 |
| Maya Chowdhury Condo Insurance | Maya Chowdhury Downtown Condo Quote |
| Arjun Travel Insurance | Arjun Romano Travel Insurance Lisbon |
| Ivan Cardenas Billing Check | Ivan Cardenas Payment Plan |
| Evans Roofing Cyber Coverage Quote | Evans Roofing Cyber Quote |

New work put into an existing agent at creation time:

- **unrelated**: "Can you put together my Weekly Inbox Digest so I can see what needs attention from the past week?" → Daily 8am Email Summary (should be new: Weekly Inbox Digest)
- same person: "Kenji Nakamura is hosting us at his Muskoka cottage the weekend of the 14th. Can you check drive times and put" → Kenji Nakamura Cottage Weekend Packing and Forecast (should be new: Muskoka Cottage Weekend)
- same person: "I need help picking Mom's birthday gift with Jess Rivera before the 18th. Can you compare a few options?" → Mom Birthday Gift Ideas (should be new: Mom's Birthday Gift (August))
- same person: "Can you map out Thanksgiving plans with Luis Rivera, including the drive from Toronto to his place in Hamilton" → Thanksgiving Hosting vs Travel Options (should be new: Thanksgiving Plans)
- **unrelated**: "Can you check the Aurora Air booking for my Vancouver flight and make sure the confirmation details are saved " → Vancouver Conference Registration (should be new: Vancouver Trip)
- same person: "Jess Rivera's move is coming up and I'm on the hook for Saturday. Can you line up dollies and a few helpers?" → Jess Rivera Moving Day Truck and Crew (should be new: Help Jess Move (September))
- same person: "After that three-day callback complaint, can you draft a split for the inbox between me and Kevin? Keep it sim" → Kevin Client Inbox Split Proposal (should be new: Inbox Split with Kevin (September))
- same person: "Can you find a squash court for Thursday evening and book it for me and Tomas Novak?" → Tomas Novak Squash Court Booking (should be new: Squash with Tomas)
- same person: "Alice wants the 'renewal strategy' field filled in on every renewal at 60 days out starting next month. Could " → Alice Renewal Strategy Field (should be new: CRM Renewal Fields (September))
- same person: "Bob Martin's board game night is Saturday. Can you pick a few games and confirm the headcount?" → Game Night Suggestions (should be new: Board Game Night)
- same person: "Hey, HR signed off on my time off from the 22nd of December through January 2nd. Could you update the team cal" → Northbay HR Holiday Calendar Block (should be new: Holiday Vacation (October))
- same person: "Alice, the annual E&O attestation is due on the 15th. Can you take it on and complete the form in the shared d" → E&O Attestation Due 15th (should be new: E&O Attestation)
- same person: "Tomas Novak and I want Raptors tickets. Can you check prices for two seats in the lower bowl this Sunday?" → Raptors Tickets Tomas Novak (should be new: Raptors Tickets)
- same person: "Mei Tanaka confirmed the carrier recovered the Delgado auto deductible through subrogation. Can you draft the " → Delgado Subrogation Deductible Reimbursement (should be new: Delgado Subrogation)

Near-duplicate OpenPoke names:

- Reyes Moving Fleet Schedule Update ≈ Tran Moving Fleet Schedule Update
- Tran Auto Body Fleet Schedule Update ≈ Kim Auto Body Fleet Schedule Update
- Adriana Ellis Auto Claim 2025 ≈ Adriana Boateng Auto Claim 2025
- Mila Costa Home Renewal 2025 ≈ Graham Costa Home Renewal 2025
- Mila Costa Home Renewal 2025 ≈ Lucas Costa Home Renewal 2025
- Reyes Hardware Payroll Audit ≈ Morin Hardware Payroll Audit
- Graham Costa Home Renewal 2025 ≈ Lucas Costa Home Renewal 2025
- Naveen Ivanova Home Renewal 2025 ≈ Naveen Rahman Home Renewal 2025
- Aisha Yamamoto Tenant Policy Quote ≈ Aisha Hughes Tenant Policy Quote
- Yara Dimitrov Umbrella Policy Review ≈ Yara Tremblay Umbrella Policy Review
- Carmen Garcia Architecture Fleet Schedule Update ≈ Carmen Lefebvre Architecture Fleet Schedule Update
- Amir Zhang Umbrella Policy Review ≈ Amir Osei Umbrella Policy Review
- Andre Fontaine Umbrella Policy Review ≈ Deepa Fontaine Umbrella Policy Review
- Ana Bergeron Home Renewal 2025 ≈ Ana Novak Home Renewal 2025
- Emeka Vargas Umbrella Policy Review ≈ Jin Vargas Umbrella Policy Review

No agent created:

- "Can you take care of Anjali Saleh's address update? She moved and we need her policy records changed" → Sure. What's Anjali's new address? And if you have the policy number, send that too so I can get the
- "Could you handle the address update for Chloe Bergeron? She's moved and needs her policies corrected" → (plain reply)
- "Rob, can you send me your new business and retention numbers for October by Friday? Rough is fine, I" → I'm not Rob, so I don't have his October numbers. Did this one go to me by mistake? If you want, I c
