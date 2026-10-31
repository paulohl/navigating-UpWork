from pathlib import Path
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, FancyArrowPatch

out=Path('user/workspace/co-scientist-outputs/upwork-guide')
fig=plt.figure(figsize=(12,19),facecolor='#F8FAFC')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,120);ax.set_ylim(0,190);ax.axis('off')
navy='#18384E';teal='#087F83';ink='#243D50';amber='#A36512';muted='#516170'

def text(x,y,s,size=10,color=ink,weight='normal',ha='center'):
    ax.text(x,y,s,fontsize=size,color=color,weight=weight,ha=ha,va='center',linespacing=1.25)
def box(x,y,w,h,title,body='',kind='normal',size=10):
    colors={'normal':('#E8F4F3',teal),'pause':('#FFF3DE',amber),'note':('#EEF2F6','#718291'),'end':('#DDEFE6','#25724E')}
    fc,ec=colors[kind]
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.35,rounding_size=1.1',facecolor=fc,edgecolor=ec,linewidth=1.1,zorder=2))
    if body:
        text(x,y+h/2-2.6,title,size,ec,'bold')
        text(x,y-1.6,body,size-0.5)
    else:text(x,y,title,size,ec,'bold')
def diamond(x,y,title,body):
    ax.add_patch(Polygon([[x,y+7],[x+21,y],[x,y-7],[x-21,y]],closed=True,facecolor='white',edgecolor=teal,linewidth=1.6,zorder=2))
    text(x,y+1.7,title,10.6,teal,'bold');text(x,y-1.9,body,9.6)
def arrow(points,label=None,lpos=None,dash=False):
    for a,b in zip(points[:-2],points[1:-1]):
        ax.plot([a[0],b[0]],[a[1],b[1]],color=muted,lw=1.1,ls='--' if dash else '-',zorder=1)
    ax.add_patch(FancyArrowPatch(points[-2],points[-1],arrowstyle='-|>',mutation_scale=10,linewidth=1.1,color=muted,linestyle='--' if dash else '-',zorder=1))
    if label:text(*lpos,label,9,muted,'bold')

ax.add_patch(FancyBboxPatch((0,172),120,18,boxstyle='square,pad=0',facecolor=navy,edgecolor='none'))
text(6,184,'UPWORK / CLIENT DECISION FLOWCHART',11,'#9EE0DE','bold',ha='left')
text(6,178,'Hire clearly. Review fairly.',24,'white','bold',ha='left')
text(60,167.4,'For business owners, hiring managers and project leads • DRAFT • 28 October 2026',10)

# Main path is top to bottom. Side routes say explicitly when to return.
diamond(58,156,'1  CLEAR BRIEF?  [R+J]','Scope + budget agreed?')
box(16,156,27,13,'CLARIFY FIRST','Define “done”, revisions,\ndeadline and full budget.\nThen recheck gate 1.','pause',9.6)
arrow([(37,156),(29.9,156)],'NO',(33.4,158))
box(100,156,31,13,'BUDGET CHECK  [J]','Include client fees, taxes\nwhere applicable and your\nreview time. Use live fees [2].','note',9.5)
arrow([(58,149),(58,143)],'YES',(62,146))

diamond(58,136,'2  CONVINCING FIT?  [R+J]','Skills + availability checked?')
box(16,136,27,13,'CHECK OR RESELECT','Discuss relevant samples,\nwho will do the work and\na small paid pilot if useful.\nThen recheck gate 2.','pause',9.3)
arrow([(37,136),(29.9,136)],'NO',(33.4,138))
box(100,136,31,13,'FAIR SELECTION  [J]','Do not rely only on stars\nor the lowest price.\nDo not ask for unpaid\nproduction work.','note',9.5)
arrow([(58,129),(58,123)],'YES',(62,126))

diamond(58,116,'3  READY TO START?  [P+J]','Contract + payment set up?')
box(16,116,27,13,'RESOLVE BEFORE WORK','Confirm scope, contract\nand payment setup.\nThen recheck gate 3.','pause',9.5)
arrow([(37,116),(29.9,116)],'NO',(33.4,118))
box(100,116,31,17,'CHOOSE THE ROUTE  [3–4]','FIXED: fund the agreed\nmilestone before work starts.\nHOURLY: agree rate, weekly\nlimit and time-recording\nmethod; review work diary.','note',9.4)
arrow([(58,109),(58,104)],'YES',(62,106.5))
box(58,100,36,8,'AUTHORISE AGREED WORK',size=10.3)
arrow([(58,96),(58,93)])

diamond(58,86,'4  SCOPE CHANGED?  [R+J]','New work, not a correction?')
box(100,86,31,13,'AGREE THE CHANGE','Confirm extra cost, delivery\nand deadline in writing;\nfund milestone if needed.\nThen authorise revised work.','pause',9.3)
arrow([(79,86),(84.1,86)],'YES',(82,89))
arrow([(100,92.5),(100,100),(76.4,100)],dash=True)
arrow([(58,79),(58,75)],'NO',(62,77))
box(58,70,36,10,'5  REVIEW DELIVERY  [P+J]','Use the agreed acceptance\ncriteria and contract workflow.',size=10)
box(100,69,31,14,'WATCH THE CLOCK  [3–4]','FIXED: 14-day review window;\ninaction can release funds.\nHOURLY: check bills weekly;\ndispute deadlines apply.','note',9.2)
arrow([(58,65),(58,61)])

diamond(58,54,'MATCHES AGREEMENT?','Check output, not just activity.')
box(100,54,31,9,'APPROVE / CONTINUE','Pay for agreed work.\nClose out access when finished.','end',9.5)
arrow([(79,54),(84.1,54)],'YES',(82,57))
box(16,54,27,13,'SPECIFY THE MISMATCH','Request agreed corrections,\nnot unpaid extras.\nResolved? Review again.','pause',9.5)
arrow([(37,54),(29.9,54)],'NO',(33.4,57))
arrow([(16,60.5),(16,70),(39.6,70)],'REVIEW AGAIN',(27,72.3),dash=True)
box(31,38,56,11,'6  UNRESOLVED? DOCUMENT + ESCALATE  [P+J]','Preserve the brief, approvals, work and billing records.\nUse the official dispute/refund route promptly [3–4].\nCheck your deadline; a support message is not a filed dispute.',size=9.7)
arrow([(16,47.5),(16,44)],'UNRESOLVED',(24.5,46))
box(91,38,45,11,'SAFETY OVERRIDE AT ANY STAGE  [P+J]','Decline fake reviews, identity misuse or fee-avoidance\nworkarounds. Check conversion rules [5].\nLimit access to business systems; secure compromised access.',kind='note',size=9.3)

# Evidence and source note travel with the image, rather than living only in chat.
ax.plot([4,116],[30,30],color='#CBD5DF',lw=.8)
text(5,27.6,'HOW TO READ THE EVIDENCE',10,teal,'bold',ha='left')
text(5,24.7,'R = paper-reported; LOW confidence for generalising. P = stated platform rule, not proof of fair outcomes.',9.1,ha='left')
text(5,22.3,'J = practical judgement, not tested by the paper. These are plain-language labels, not formal GRADE ratings.',9.1,ha='left')
text(5,19.5,'LIMITS: The paper reports 218 studies/reports, 495 perspectives and 50 enforcement sources; overlap is unclear.',8.9,ha='left')
text(5,17.3,'The PDF lacks a full auditable source inventory and extraction dataset. No validated hiring algorithm or risk estimate.',8.9,ha='left')
text(5,15.1,'Supplied PDF: 15 July 2024; task metadata: 2026. Policy checks: 28 October 2026, search-indexed official text only;',8.9,ha='left')
text(5,12.9,'direct pages blocked (403). Recheck live terms, exceptions and deadlines. No guarantee of quality or a refund.',8.9,ha='left')
refs=[
('[1] Leocadio, Navigating Upwork, pp. 2–4, 22–24, 34–36. https://doi.org/10.2139/ssrn.6031034','https://doi.org/10.2139/ssrn.6031034'),
('[2] Upwork: Client Marketplace Fee. https://support.upwork.com/hc/en-us/articles/4660220468499','https://support.upwork.com/hc/en-us/articles/4660220468499'),
('[3] Upwork: Fixed-price review. https://support.upwork.com/hc/en-us/articles/17974824831507','https://support.upwork.com/hc/en-us/articles/17974824831507'),
('[4] Upwork: Hourly disputes. https://support.upwork.com/hc/en-us/articles/17976540792467','https://support.upwork.com/hc/en-us/articles/17976540792467'),
('[5] Upwork: Off-platform payments. https://support.upwork.com/hc/en-us/articles/360048105134','https://support.upwork.com/hc/en-us/articles/360048105134')]
for y,(s,url) in zip([10.3,8.6,6.9,5.2,3.5],refs):
    ax.text(5,y,s,fontsize=8.0,color=ink,ha='left',va='center',url=url)
text(5,1.3,'EXPERT SIGN-OFF: Author/methods + platform-policy adviser + client/freelancer usability review. Not legal advice; not Upwork-endorsed.',8.1,navy,'bold',ha='left')
fig.savefig(out/'upwork_client_flowchart.pdf',facecolor=fig.get_facecolor())
fig.savefig(out/'upwork_client_flowchart.png',dpi=180,facecolor=fig.get_facecolor())
print('Saved one-page flowchart PDF and PNG (2160 × 3420 pixels).')
