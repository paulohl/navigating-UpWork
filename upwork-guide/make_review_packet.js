const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,ShadingType,ImageRun,PageBreak,Footer,PageNumber,HeadingLevel,AlignmentType}=require('docx');
const out='user/workspace/co-scientist-outputs/upwork-guide';
const p=(s,opts={})=>new Paragraph({spacing:{after:100},children:[new TextRun({text:s,size:20})],...opts});
const h=(s)=>new Paragraph({heading:HeadingLevel.HEADING_1,children:[new TextRun(s)],spacing:{before:140,after:140}});
const small=s=>p(s,{spacing:{after:70},children:[new TextRun({text:s,size:18})]});
function table(headers,rows,widths){return new Table({width:{size:10080,type:WidthType.DXA},columnWidths:widths,rows:[headers,...rows].map((row,i)=>new TableRow({tableHeader:i===0,cantSplit:true,children:row.map((s,j)=>new TableCell({width:{size:widths[j],type:WidthType.DXA},margins:{top:85,bottom:85,left:100,right:100},shading:{fill:i===0?'E0EEF0':'FFFFFF',type:ShadingType.CLEAR},children:[new Paragraph({spacing:{after:0},children:[new TextRun({text:s,size:18,bold:i===0})]})]}))}))});}
const children=[
p('EXPERT REVIEW COPY v0.1 | 28 October 2026 | NOT APPROVED FOR DISTRIBUTION',{alignment:AlignmentType.CENTER,children:[new TextRun({text:'EXPERT REVIEW COPY v0.1 | NOT APPROVED FOR DISTRIBUTION',size:18,bold:true})]}),
new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:0},children:[new ImageRun({type:'png',data:fs.readFileSync('user/user-data/tmp/upwork-review/chart.png'),transformation:{width:550,height:871},altText:{title:'Client decision flowchart under expert review',description:'Yes/no pathway for briefing, selection, authorisation, scope changes, delivery review and escalation. Review instructions and issue register follow.',name:'Review flowchart'}})]}),
new Paragraph({children:[new PageBreak()]}),
h('Expert review: evidence and policy audit'),
p('Purpose: review the client-facing flowchart, not endorse the paper or certify legal compliance. All items below are OPEN; this packet prepares a review and does not claim one has occurred.'),
small('Version under review: client flowchart v0.1, 28 October 2026. Source: Leocadio, Navigating Upwork, DOI 10.2139/ssrn.6031034. The PDF is dated 15 July 2024; task metadata says 2026. Confirm the citation before release.'),
small('Reviewer: ____________________  Role/organisation: ____________________  Date: __________'),
small('For each row, record Accept / Revise / Unable to verify, the supporting source and access date, and exact replacement wording if needed. Open release blockers must be resolved or the affected claim removed.'),
table(['ID / owner','Target and release-blocking check','Decision / evidence / correction'],[
['R1 — Author / methods','Evidence footer: verify 218 studies/reports, 495 perspectives and 50 enforcement sources (paper pp. 2–4); explain overlap. Supply included-source inventory, search/extraction details and bias assessment, or retain the low-confidence caveat. Confirm 2024/2026 version.','OPEN\nDecision: __________\nSource/date: __________\nChange: __________'],
['R2 — Policy adviser','Gate 1: verify client fees against source [2] and the relevant plan/account. Check taxes, initiation fees and exceptions. Keep “use live fees”; do not import historical freelancer fee tiers.','OPEN\nDecision: __________\nSource/date: __________\nChange: __________'],
['R3 — Policy adviser','Gate 3: verify active-contract and milestone funding workflow; confirm hourly rate, weekly-limit and time-recording guidance. Ensure no box implies guaranteed quality, payment recovery or a refund. Sources [3–4].','OPEN\nDecision: __________\nSource/date: __________\nChange: __________'],
['R4 — Policy adviser','Watch the clock: verify the 14-day fixed-price window, trigger, change-request/resubmission effects and automatic-release exceptions. Check the client contract workflow. Source [3].','OPEN\nDecision: __________\nSource/date: __________\nChange: __________'],
['R5 — Policy adviser','Gate 6: verify hourly dispute filing deadline, timezone, eligible grounds and filing method. Distinguish formal disputes from support messages and refund requests. Review fixed-price escalation too. Sources [3–4].','OPEN\nDecision: __________\nSource/date: __________\nChange: __________'],
['R6 — Policy / legal adviser','Safety override: verify conversion requirements, permitted exceptions and off-platform restrictions [5]. Check access/privacy advice and local legal implications; avoid implying an exception or guaranteed remedy.','OPEN\nDecision: __________\nSource/date: __________\nChange: __________']
],[1620,5400,3060]),
small('Verification limitation: earlier checks used search-indexed official text; direct official-page retrieval returned HTTP 403. No new live-policy verification or external expert approval was completed for this packet.'),
new Paragraph({children:[new PageBreak()]}),
h('Usability, issue log and release decision'),
small('R = paper-reported, low confidence for generalising. P = stated platform rule, not independent proof of fairness. J = practical judgement, not tested by the paper. These labels are not formal GRADE ratings.'),
p('Client and freelancer reviewers: walk through (a) an unfunded milestone, (b) an extra deliverable beyond scope, (c) defective work against the original brief, and (d) disputed hourly time near a deadline. Record the route taken and whether the next action is clear.'),
small('R7 — Flow and fairness: Can a reviewer distinguish new scope from an agreed correction? Does the return arrow lead to the right gate? Does any correction loop risk missing a dispute deadline? Are “continue” and access close-out clear? Confirm protection against unpaid extras and feedback pressure.'),
small('R8 — Accessibility: Check at intended print size and on a phone; confirm text size, contrast, arrow direction and meaning without colour. The chart is a large-format graphic, not a validated hiring instrument. Add an accessible text companion if needed; the existing client guide provides the full narrative.'),
table(['Issue / gate','Proposed change + source/date','Owner / resolution'],[
['R7 / usability: __________','________________________________\n________________________________','Owner: __________\nResolved/date: __________'],
['R8 / accessibility: __________','________________________________\n________________________________','Owner: __________\nResolved/date: __________'],
['Other: __________','________________________________\n________________________________','Owner: __________\nResolved/date: __________']
],[2350,4800,2930]),
h('Sign-off — complete after corrections'),
small('Each reviewer approves only their scope. “Revise” is not permission to distribute. Final release requires closed blockers, a checked final version and a named release owner.'),
table(['Review scope','Name / signature / date','Decision'],[
['Author / methods','________________________','Accept / Revise / Cannot verify'],
['Platform policy / legal','________________________','Accept / Revise / Cannot verify'],
['Client usability','________________________','Accept / Revise / Cannot verify'],
['Freelancer fairness / usability','________________________','Accept / Revise / Cannot verify']
],[2750,3850,3480]),
small('Final disposition: HOLD / APPROVE FOR DEFINED USE / DO NOT USE. Release owner: ____________________'),
small('Approved version/date: ____________________  Audience/jurisdiction/format: ____________________'),
small('Next policy recheck: ____________________  Outstanding limitations to retain: ____________________'),
small('Source index (same numbering as chart): [1] https://doi.org/10.2139/ssrn.6031034; [2] https://support.upwork.com/hc/en-us/articles/4660220468499; [3] https://support.upwork.com/hc/en-us/articles/17974824831507; [4] https://support.upwork.com/hc/en-us/articles/17976540792467; [5] https://support.upwork.com/hc/en-us/articles/360048105134'),
small('Prepared for expert review only. No expert has signed this copy. Not legal advice; not endorsed by Upwork.')
];
const doc=new Document({styles:{default:{document:{run:{font:'Arial',size:20},paragraph:{spacing:{after:100}}}},paragraphStyles:[{id:'Heading1',name:'Heading 1',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:'Arial',size:28,bold:true,color:'18384E'},paragraph:{outlineLevel:0}}]},sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:700,bottom:700,left:1080,right:1080}}},footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.RIGHT,children:[new TextRun({text:'REVIEW v0.1 — NOT APPROVED | ',size:16}),new TextRun({children:[PageNumber.CURRENT],size:16})]})]})},children}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync(out+'/upwork_client_expert_review.docx',b);console.log('Saved editable expert-review packet');});
