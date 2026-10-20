from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
import shutil,json,pypdfium2
from pypdf import PdfReader

root=Path(__file__).resolve().parent
pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='ArialBold')
teal=HexColor('#28777B');dark=HexColor('#25383A')
data={
'fr':dict(role='Étudiant en développement web full stack',special='Spécialisation JavaScript',profile='PROFIL',summary='Étudiant à IT-Högskolan, je développe mes compétences frontend et backend à travers des projets web. Mon expérience du service client et de la gestion des stocks nourrit mon intérêt pour les applications utiles aux entreprises.',education='FORMATION',current='Août 2026 - juin 2028 | En cours',currenttext='Full stack webbutveckling med inriktning JavaScript.',jensen='Octobre 2025 - juillet 2026 | Formation terminée',jensentext='Programmation, développement web, programmation côté serveur, informatique et communication, support et service.',older='2012-2015 : agriculture et technologie agricole.<br/>2010-2012 : études universitaires en littérature française, Cameroun.',projects='PROJETS',erp='Plateforme en développement : clients, produits, factures et stocks. Next.js, React, NestJS, PostgreSQL et Prisma.',poussin='Application JavaScript / HTML / CSS : élevages, stocks, ventes, commandes et rapports ; PWA et sauvegarde locale.',python='Outils Python pour l’inventaire et l’automatisation.',experience='EXPÉRIENCE PROFESSIONNELLE',ica='Janvier 2020 - aujourd’hui | Temps partiel pendant les études',icatext='Service client, caisse, réassort et suivi des stocks.',otherwork='ISKO AB - Agent de nettoyage | Suède | 12/2019 - 06/2020<br/>Boulanger | Mauritanie | 2018<br/>Mauritel - Vente | Mauritanie | 2017',skills='COMPÉTENCES',languages='LANGUES',langtext='Français<br/>Suédois<br/>Anglais',location='Upplands-Bro<br/>Région de Stockholm, Suède',references='Références disponibles sur demande.'),
'en':dict(role='Full stack web development student',special='JavaScript specialisation',profile='PROFILE',summary='Student at IT-Högskolan, building frontend and backend skills through practical web projects. My experience in customer service and stock management informs my interest in useful business applications.',education='EDUCATION',current='August 2026 - June 2028 | Ongoing',currenttext='Full stack webbutveckling med inriktning JavaScript.',jensen='October 2025 - July 2026 | Completed',jensentext='Programming, web development, server-side programming, computer and communication technology, support and service.',older='2012-2015: agriculture and agricultural technology.<br/>2010-2012: university studies in French literature, Cameroon.',projects='PROJECTS',erp='Platform under development: customers, products, invoices and inventory. Next.js, React, NestJS, PostgreSQL and Prisma.',poussin='JavaScript / HTML / CSS app: flocks, inventory, sales, orders and reports; PWA functionality and local backups.',python='Python tools for inventory and automation.',experience='WORK EXPERIENCE',ica='January 2020 - present | Part-time alongside studies',icatext='Customer service, checkout, replenishment and stock management.',otherwork='ISKO AB - Cleaner | Sweden | 12/2019 - 06/2020<br/>Baker | Mauritania | 2018<br/>Mauritel - Sales | Mauritania | 2017',skills='SKILLS',languages='LANGUAGES',langtext='French<br/>Swedish<br/>English',location='Upplands-Bro<br/>Stockholm region, Sweden',references='References available on request.'),
'sv':dict(role='Studerande inom fullstack webbutveckling',special='Inriktning JavaScript',profile='PROFIL',summary='Jag studerar på IT-Högskolan och utvecklar mina kunskaper inom frontend och backend genom praktiska webbprojekt. Min erfarenhet av kundservice och lagerhantering väcker mitt intresse för användbara verksamhetssystem.',education='UTBILDNING',current='Augusti 2026 - juni 2028 | Pågående',currenttext='Full stack webbutveckling med inriktning JavaScript.',jensen='Oktober 2025 - juli 2026 | Avslutad',jensentext='Programmering, webbutveckling, webbserverprogrammering, dator- och kommunikationsteknik samt support och service.',older='2012-2015: jordbruk och jordbruksteknik.<br/>2010-2012: universitetsstudier i fransk litteratur, Kamerun.',projects='PROJEKT',erp='Plattform under utveckling: kunder, produkter, fakturor och lager. Next.js, React, NestJS, PostgreSQL och Prisma.',poussin='App i JavaScript / HTML / CSS: uppfödning, lager, försäljning, beställningar och rapporter; PWA och lokal säkerhetskopiering.',python='Python-verktyg för inventering och automatisering.',experience='ARBETSLIVSERFARENHET',ica='Januari 2020 - pågående | Deltid vid sidan av studierna',icatext='Kundservice, kassaarbete, varuplock och lagerhantering.',otherwork='ISKO AB - Lokalvårdare | Sverige | 12/2019 - 06/2020<br/>Bagare | Mauretanien | 2018<br/>Mauritel - Försäljning | Mauretanien | 2017',skills='KOMPETENSER',languages='SPRÅK',langtext='Franska<br/>Svenska<br/>Engelska',location='Upplands-Bro<br/>Stockholmsregionen, Sverige',references='Referenser lämnas på begäran.')}
for lang,d in data.items():
 path=root/f'issa-bakari-cv-{lang}.pdf';c=canvas.Canvas(str(path),pagesize=(595.28,841.89))
 c.setTitle('Issa Bakari Ndam Njounkou - CV - '+lang.upper());c.setAuthor('Issa Bakari Ndam Njounkou')
 c.setFillColor(teal);c.rect(0,0,190,842,fill=1,stroke=0)
 def p(text,x,y,w=350,size=10,color=dark,bold=False,leading=None):
  st=ParagraphStyle('p',fontName='ArialBold' if bold else 'Arial',fontSize=size,leading=leading or size*1.35,textColor=color)
  para=Paragraph(text,st);_,h=para.wrap(w,800);para.drawOn(c,x,y-h);return y-h-5
 c.drawImage(ImageReader(str(root/'profile-photo.png')),28,650,width=134,height=134,mask='auto')
 y=p('CONTACT',22,621,146,12,white,True)
 for txt in ['070-736 45 55','bakarii447@gmail.com',d['location']]:y=p(txt,22,y-4,146,9.3,white)
 y=p('<link href="https://isbakari447.github.io/portfolio/" color="#FFFFFF">Portfolio</link> · <link href="https://github.com/IsBakari447" color="#FFFFFF">GitHub</link><br/><link href="https://www.linkedin.com/in/issa-issa-bakari-06712319a" color="#FFFFFF">LinkedIn</link>',22,y-5,146,9.3,white)
 y=p(d['skills'],22,y-20,146,12,white,True)
 for title,body in [('Frontend','JavaScript, TypeScript<br/>React, Next.js<br/>HTML5, CSS3, Sass'),('Backend','Node.js, NestJS<br/>API REST'),('Data','PostgreSQL, Prisma<br/>SQLite, SQL Server'),('Tools','Git, GitHub, VS Code<br/>Visual Studio'),('Other','C#, ASP.NET Core<br/>Python')]:
  y=p(title,22,y-4,146,10,white,True);y=p(body,22,y,146,9.3,white)
 y=p(d['languages'],22,y-14,146,12,white,True);y=p(d['langtext'],22,y,146,9.3,white)
 assert y>25,(lang,'sidebar',y)
 y=p('ISSA BAKARI',214,800,357,23,teal,True)
 y=p('NDAM NJOUNKOU',214,y,357,19,teal,True)
 y=p(d['role'],214,y-3,357,12,dark,True);y=p(d['special'],214,y,357,11,teal)
 def heading(label):
  global y
  y=p(label,214,y-10,357,11,teal,True)
  c.setStrokeColor(teal);c.setLineWidth(.5);c.line(214,y+2,571,y+2)
 heading(d['profile']);y=p(d['summary'],214,y-3,357,9.4)
 heading(d['education'])
 for title,date,txt in [('IT-Högskolan',d['current'],d['currenttext']),('Jensen Komvux - IT',d['jensen'],d['jensentext'])]:
  y=p(title,214,y-3,357,10,dark,True);y=p(date,214,y,357,8.8,teal);y=p(txt,214,y,357,9.2)
 y=p(d['older'],214,y-3,357,8.6)
 heading(d['projects'])
 for name,url,txt in [('EnterpriseERP','EnterpriseERP-Plate-forme-',d['erp']),('Poussin d’or','Poussin-D-Ore',d['poussin']),('Python','systemInventering_Mattaffar',d['python'])]:
  y=p('<link href="https://github.com/IsBakari447/'+url+'">'+name+'</link>',214,y-3,357,10,dark,True);y=p(txt,214,y,357,9.2)
 heading(d['experience']);y=p('ICA Nära Enebytorg - Butiksmedarbetare',214,y-3,357,10,dark,True);y=p(d['ica'],214,y,357,8.8,teal);y=p(d['icatext'],214,y,357,9.2);y=p(d['otherwork'],214,y-3,357,8.8)
 assert y>35,(lang,'main',y)
 p(d['references'],214,26,357,8,teal)
 c.save()
 pdf=PdfReader(path);assert len(pdf.pages)==1
 text=pdf.pages[0].extract_text();assert '2028' in text and 'Jensen' in text and '070-736 45 55' in text
 out=Path('tmp/pdfs');out.mkdir(exist_ok=True,parents=True)
 rendered=pypdfium2.PdfDocument(str(path));rendered[0].render(scale=1.4).to_pil().save(out/f'portfolio-cv-{lang}.png')
 if lang=='fr':shutil.copyfile(out/f'portfolio-cv-{lang}.png',root/'cv-preview.png')
 print(lang,'one page; content ends at',round(y), 'pt')
shutil.copyfile(root/'issa-bakari-cv-fr.pdf',root/'cv-issa-bakari.pdf')
