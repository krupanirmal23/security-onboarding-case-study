import json
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
R='/workspace/portfolio/security-onboarding-case-study/'
INK=RGBColor(0x1b,0x1f,0x1d); MUTE=RGBColor(0x6b,0x6f,0x6a); TEAL=RGBColor(0x1f,0x6f,0x5c); RED=RGBColor(0x9a,0x3b,0x3b)
d=Document()
sec=d.sections[0]; sec.page_width=Cm(21); sec.page_height=Cm(29.7)
for s in d.sections: s.left_margin=s.right_margin=Cm(2.1); s.top_margin=Cm(1.8); s.bottom_margin=Cm(1.8)
st=d.styles['Normal']; st.font.name='Geist'; st.font.size=Pt(10); st.font.color.rgb=INK
st.element.rPr.rFonts.set(qn('w:eastAsia'),'Geist')
st.paragraph_format.space_after=Pt(4); st.paragraph_format.line_spacing=1.2
def run(p,t,b=False,c=None,s=None,i=False,f=None):
    r=p.add_run(t); r.bold=b; r.italic=i
    if c: r.font.color.rgb=c
    if s: r.font.size=Pt(s)
    if f: r.font.name=f
    return r
def P(t='',b=False,c=None,s=None,after=4,al=None):
    p=d.add_paragraph(); p.paragraph_format.space_after=Pt(after)
    if al: p.alignment=al
    if t: run(p,t,b,c,s)
    return p
def H(t,lvl=1):
    p=d.add_paragraph(); p.paragraph_format.space_before=Pt(14 if lvl==1 else 8); p.paragraph_format.space_after=Pt(4)
    p.paragraph_format.keep_with_next=True
    run(p,t,lvl!=1,INK if lvl==1 else TEAL,20 if lvl==1 else 11,f='Instrument Serif' if lvl==1 else None)
    return p
def kicker(t):
    p=P(after=0); run(p,t.upper(),True,MUTE,7.5); p.paragraph_format.keep_with_next=True
def B(items,size=None):
    for it in items:
        p=d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after=Pt(2)
        if isinstance(it,tuple): run(p,it[0],True,s=size); run(p,it[1],s=size)
        else: run(p,it,s=size)
def shade(cell,hexc):
    tcPr=cell._tc.get_or_add_tcPr(); sh=OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:color'),'auto'); sh.set(qn('w:fill'),hexc); tcPr.append(sh)
def borders(tbl):
    tblPr=tbl._tbl.tblPr; b=OxmlElement('w:tblBorders')
    for e in ('top','bottom','insideH'):
        x=OxmlElement(f'w:{e}'); x.set(qn('w:val'),'single'); x.set(qn('w:sz'),'4'); x.set(qn('w:color'),'E4E0D6'); b.append(x)
    for e in ('left','right','insideV'):
        x=OxmlElement(f'w:{e}'); x.set(qn('w:val'),'nil'); b.append(x)
    tblPr.append(b)
def T(head,rows,widths=None,size=8.5,first_bold=False):
    t=d.add_table(rows=1,cols=len(head)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; borders(t)
    for i,h in enumerate(head):
        c=t.rows[0].cells[i]; c.text=''; run(c.paragraphs[0],h,True,MUTE,7.5); shade(c,'F6F4EF')
    for r in rows:
        cells=t.add_row().cells
        for i,v in enumerate(r):
            cells[i].text=''; run(cells[i].paragraphs[0],str(v),first_bold and i==0,s=size)
    if widths:
        t.autofit=False
        grid=t._tbl.tblGrid
        for i,gc in enumerate(grid.findall(qn('w:gridCol'))): gc.set(qn('w:w'),str(int(widths[i]*567)))
        for i,w in enumerate(widths): t.columns[i].width=Cm(w)
        for row in t.rows:
            for i,w in enumerate(widths): row.cells[i].width=Cm(w)
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs: p.paragraph_format.space_after=Pt(1); p.paragraph_format.space_before=Pt(1)
    P(after=2)
    return t
def IMG(path,w=16.8,cap=None):
    p=P(after=1,al=WD_ALIGN_PARAGRAPH.CENTER); p.add_run().add_picture(path,width=Cm(w)); p.paragraph_format.keep_with_next=bool(cap)
    if cap: q=P(after=8,al=WD_ALIGN_PARAGRAPH.CENTER); run(q,cap,c=MUTE,s=7.5)
TD='[Team to decide]'
