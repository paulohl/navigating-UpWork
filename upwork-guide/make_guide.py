from pathlib import Path
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch

out=Path('user/workspace/co-scientist-outputs/upwork-guide')
pages=[
('Decide before you commit', 'A practical Upwork guide for freelancers', [
('WHO THIS IS FOR', 'New and established freelancers, including agency leads; also useful to clients and freelancer advisers. Use it to decide whether to bid, start or extend work, or escalate a problem. Draft for expert review • 28 October 2026.'),
('1  BID? Check whether the work pays for your time.  [R + J]', 'Write down the scope, likely delivery hours, proposal/interview time, and application costs. Use the fee shown on your actual proposal or offer—not the paper’s historical 20% / 10% / 5% tiers. Upwork currently advertises standard-contract fees of 0%–15% [2].\nNO clear scope or acceptable return? Clarify, renegotiate, or skip. YES? Continue. The paper’s roughly 10% success claim is not a personal forecast or a reason to send dozens of proposals daily [1, pp. 3, 35].'),
('2  START? Check the payment route first.  [P]', 'Fixed-price: confirm an active contract and a fully funded milestone covering the agreed work before starting. Submit through “Submit Work for Payment”; your delivery must match the milestone description [3].\nHourly: use the desktop tracker, relevant work activity and clear memos; check the weekly limit, verified client billing and other eligibility rules [4]. Manual time is not protected.\nNO funding or eligibility? Resolve it before taking on that exposure. YES? Start only the agreed work. Protection is conditional, not guaranteed.'),
('3  MORE WORK? Agree the change before doing it.  [R + J]', 'If a client adds tasks or revisions beyond the agreement, pause the added work—not necessarily the whole contract. Confirm revised deliverables, price and dates in writing; fund a new or changed milestone where needed. Keep the contract, approvals and delivery records. The paper reports scope disputes but does not test this prevention strategy [1, pp. 23–24].'),
('4  ASKED TO BYPASS RULES? Do not take the shortcut.  [R + P + J]', 'Decline fake reviews, borrowed identities and fabricated time. Do not share your login; vet agency access and use available account-security controls. The author’s reported account compromise is a warning, not a measured risk estimate [1, pp. 34–35]. Do not move an Upwork-introduced relationship off-platform just to avoid fees; check current conversion rules and permitted exceptions first [6].'),
('5  PAYMENT OR ACCOUNT PROBLEM? Preserve, then escalate.  [P + J]', 'Save the notice, contract or milestone ID, messages, work diary and delivery proof. Follow the relevant in-account dispute route promptly; deadlines vary. For suspension, use the banner/email instructions or official appeal form; explain the alleged mistake and provide new, relevant facts [5]. Do not assume an appeal will restore access. Suspected account takeover? Secure your email/account and contact official support.'),
('6  KEEP USING UPWORK? Review your own results.  [J]', 'Track net receipts after fees and application costs, divided by all delivery, bidding and admin hours. Compare this with your own minimum acceptable return. If it stays too low, change your bidding strategy or diversify future client acquisition within the rules. No universal cutoff or winning strategy was established by this paper.')
]),
('What you can—and cannot—conclude', 'Evidence, decision-maker actions and review', [
('EVIDENCE KEY: SOURCE CONFIDENCE IS NOT PROVEN BENEFIT', 'R = paper-reported finding: LOW confidence for generalising to all freelancers. P = official platform rule: useful authority on stated requirements, not independent proof of fair treatment. J = practical judgement: a precaution proposed in this guide, not an intervention tested by the paper. These are plain-language ratings, not a formal GRADE assessment.'),
('WHAT THE PAPER ACTUALLY SUPPORTS  [1]', 'The paper describes a systematic review of platform documents, reports, reviews and forums. It reports 218 studies/reports and 495 user perspectives for fairness/trust, plus 50 sources on enforcement equality; whether these sets overlap is unclear [pp. 2–4]. It reports duplicate independent screening, extraction and bias assessment.\nReaders describe a trade-off: access to clients and payment tools versus fees, unpaid search effort and concerns about support and enforcement. The author also recounts seven years on Upwork, an account compromise and an adverse exit [pp. 34–36]. These accounts identify issues worth checking; they do not establish their frequency or prove systematic bias.'),
('WHY THE CAVEATS CHANGE THE ADVICE', 'The supplied PDF does not provide a reproducible search strategy, full included-source inventory, extraction dataset or reported source-level bias ratings. Its data statement says only public citations were used [p. 36]. The stated review counts therefore cannot be independently audited from this PDF. User reviews can overrepresent unusually good or bad experiences; policy descriptions and personal testimony are not controlled comparisons. No causal effect, representative risk estimate or validated decision algorithm is demonstrated.\nVersion warning: the task labels the paper 2026, but this PDF is dated 15 July 2024 and carries ©2024. Its fee tiers are historical. This aid replaces a prediction/scoring algorithm with precautionary decision gates, and treats “loopholes” as warning signs—not instructions.'),
('FOR CLIENTS, PLATFORM TEAMS AND FREELANCER ADVISERS  [J]', 'Clients: agree acceptance criteria, pay for agreed work and fund changes before requesting extras. Platform teams: consider clearer reason-specific enforcement notices, an evidence-based appeal path, and reporting resolution times and outcomes separately for freelancers and clients. Advisers: help users document costs and incidents without promising recovery. These are priorities suggested by the paper’s concerns, not evaluated policy effects.'),
('OPEN SOURCES • NUMBERS MATCH THE GUIDE', '[1] Paulo H. Leocadio. Navigating Upwork: Understanding Corporate Dynamics And Unveiling Freelancer Realities Amid Policy Disruption. Supplied 38-page PDF, dated 2024; task metadata: 2026. DOI: https://doi.org/10.2139/ssrn.6031034 (PDF states CC BY 4.0).\n[2] Upwork, “Is Upwork Free To Join? Our Pricing Breakdown.” https://www.upwork.com/resources/is-upwork-free\n[3] Upwork, “How Fixed-Price Payment Protection works for freelancers on Upwork.” https://support.upwork.com/hc/en-us/articles/211063748\n[4] Upwork, “How Upwork protects your payments.” https://support.upwork.com/hc/en-us/articles/211062568\n[5] Upwork, “How to appeal an account suspension.” https://support.upwork.com/hc/en-us/articles/5313574196627\n[6] Upwork, “Why you shouldn’t get paid outside Upwork.” https://support.upwork.com/hc/en-us/articles/360048105134\nPolicy checks: 28 October 2026, using public search-indexed official text. Direct page retrieval was blocked (HTTP 403); live wording, exceptions and deadlines require rechecking before distribution.'),
('EXPERT SIGN-OFF REQUIRED BEFORE DISTRIBUTION', 'Author/methods reviewer: verify review counts, source traceability and publication version. Upwork-policy specialist or qualified adviser: recheck fees, protection eligibility, conversion rules and dispute/appeal deadlines against live terms; check local legal implications. Freelancer representative: test clarity and usability. Not legal advice; not endorsed by Upwork.\nReviewer(s): ____________________  Date: __________  Version approved: __________')
])]
md=['# Upwork: protect your time, pay and account\n\n**Two-page practitioner decision aid | DRAFT — expert sign-off required**\n']
for title,subtitle,blocks in pages:
    md += ['\n## '+title+'\n', subtitle+'\n']
    for h,b in blocks: md += ['\n### '+h+'\n',b+'\n']
(out/'upwork_freelancer_guide.md').write_text('\n'.join(md))
navy='#142F46'; teal='#087F83'; grey='#445261'
with PdfPages(out/'upwork_freelancer_guide.pdf') as pdf:
    for p,(title,subtitle,blocks) in enumerate(pages):
        fig=plt.figure(figsize=(8.27,11.69),facecolor='white')
        ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
        ax.add_patch(FancyBboxPatch((0,.91),1,.09,boxstyle='square,pad=0',facecolor=navy,edgecolor='none'))
        ax.text(.065,.965,'UPWORK  /  PRACTITIONER DECISION AID',color='#9EE0DE',fontsize=9,weight='bold',va='top')
        ax.text(.065,.938,subtitle,color='white',fontsize=15,weight='bold',va='top')
        ax.text(.065,.886,title,color=navy,fontsize=18,weight='bold',va='top')
        y=.846
        # Fixed font and physical line spacing; explicit layout overflow assertion.
        fs=9.1 if p==0 else 8.65
        lineheight=.0140 if p==0 else .01325
        wrapwidth=108 if p==0 else 114
        for h,b in blocks:
            ax.text(.065,y,h,fontsize=9.0,color=teal,weight='bold',va='top'); y-=.022
            lines=[]
            for para in b.split('\n'):
                lines.extend(textwrap.wrap(para,width=wrapwidth,break_long_words=False,break_on_hyphens=False) or [''])
            ax.text(.065,y,'\n'.join(lines),fontsize=fs,color=grey,va='top',linespacing=1.21)
            y-=len(lines)*lineheight+.017
        print('Page',p+1,'remaining bottom position',round(y,3))
        assert y>.055, f'Page {p+1} overflows: {y}'
        ax.plot([.065,.935],[.047,.047],color='#D3DDDF',linewidth=.7)
        ax.text(.065,.029,'DRAFT • 28 OCT 2026 • Expert review required before use',fontsize=8,color=grey)
        ax.text(.935,.029,f'{p+1} / 2',fontsize=8,color=grey,ha='right')
        pdf.savefig(fig);plt.close(fig)
