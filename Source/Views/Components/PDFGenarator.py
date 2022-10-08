from fpdf import FPDF,HTMLMixin
from datetime import datetime
from Services import EquipementServices

class PDF(FPDF, HTMLMixin):
    pass
def generateBonTravailPDF(record):
    pdf = PDF()
    pdf.set_font("helvetica",size=14)
    pdf.add_page()
    pdf.write_html(
        f"""
        <table border="1">
            <thead>
                <tr>
                    <th width="10%">{"FBC"}</th>
                    <th width="35%">{"Manuel des Formulaires"}</th>
                    <th width="30%">{str(record[0])}</th>
                    <th width="25%">{"Page 1/1"}</th>
                </tr>
            </thead>
            <tbody>
                <tr >
                    <td>{""}</td>
                    <td align="center">{"Bon de travail"}</td>
                    <td align="center">{datetime.now().strftime("%Y / %m / %d")}</td>
                    <td align="center">{"Edition 1"}</td>
                </tr>
            
            </tbody>
        </table>
        """,
        table_line_separators=True,
    )
    typeBonLabel="Type de bon : "
    if record[7]=="Curatif":
        typeBon=f"""{f"Curatif ( refDIM : {record[9]} )"}"""
    else :
        typeBon=f"""{f"Preventif ( frequence : {record[10]} )"}"""

    dateCreationLabel = "Date de Création : "
    dateCreation = f"""{datetime.date(record[6]).strftime("%Y / %m / %d , %H:%M:%S")}"""

    emetteurLabel="Emetteur : "
    emetteur=f"""{record[1]}"""

    destinateurLabel="Destinateur : "
    destinateur=f"""{record[2]}"""

    status,equipementRec=EquipementServices.getEquipement(record[8])
    equipementLabel = "Equipement : "
    equipement = f"""Designation : {equipementRec[0][1]}   Code : {record[8]}"""

    sectionLabel="Section : "
    section=f"""{record[5]}"""

    travauxLabel = "Travaux à exécuter (voir fiche d action) : "
    travaux = f"""{record[3]}"""

    bonTravail=[(typeBonLabel,typeBon),(dateCreationLabel,dateCreation),(emetteurLabel,emetteur),(destinateurLabel,destinateur),(equipementLabel,equipement),(sectionLabel,section),(travauxLabel,travaux)]
    for item in bonTravail:
        pdf.set_font_size(22)
        pdf.set_text_color(31, 48, 94)
        pdf.multi_cell(0,10,item[0],'L',align="L")
        pdf.ln(10)
        pdf.set_font_size(16)
        pdf.set_text_color(5, 5, 5)
        pdf.cell(0,10,item[1],align="L")
        pdf.ln(25)
    pdf.set_font_size(22)
    pdf.set_text_color(31, 48, 94)
    pdf.multi_cell(0,10,"Reception",'B',align="C")
    pdf.ln(10)
    pdf.set_font_size(14)
    pdf.set_text_color(5, 5, 5)
    pdf.write_html(
        f"""
        <table border="1">
            <thead>
                <tr>
                    <th width="20%"></th>
                    <th width="35%"></th>
                    <th width="45%"></th>
                </tr>
            </thead>
            <tbody>
                <tr >
                    <td>{"Date :..../../.."}</td>
                    <td align="center">{"Heure : ......h......mn"}</td>
                    <td align="left">{"Visa Production : "}</td>
                </tr>
            
            </tbody>
        </table>
        """,
        table_line_separators=True,
    )

    pdf.output(f"""PDFs/BonTravail{record[0]}.pdf""")

def generateDemandeInterventionPDF(record):
    pdf = PDF()
    pdf.set_font("helvetica",size=14)
    pdf.add_page()
    pdf.write_html(
        f"""
        <table border="1">
            <thead>
                <tr>
                    <th width="5%">{"FBC"}</th>
                    <th width="50%">{"Manuel des Formulaires"}</th>
                    <th width="25%">{str(record[0])}</th>
                    <th width="20%">{"Page 1/1"}</th>
                </tr>
            </thead>
            <tbody>
                <tr >
                    <td>{""}</td>
                    <td align="center">{"Demande Intervention Maintenance"}</td>
                    <td align="center">{datetime.now().strftime("%Y / %m / %d")}</td>
                    <td align="center">{"Edition 1"}</td>
                </tr>
            
            </tbody>
        </table>
        """,
        table_line_separators=True,
    )
    dateCreationLabel = "Date de Création : "
    dateCreation = f"""{datetime.date(record[5]).strftime("%Y / %m / %d , %H:%M:%S")}"""

    emetteurLabel="Emetteur : "
    emetteur=f"""{record[1]}"""

    status,equipementRec=EquipementServices.getEquipement(record[3])
    equipementLabel = "Equipement : "
    equipement = f"""Designation : {equipementRec[0][1]}   Code : {record[3]}"""

    sectionLabel="Section : "
    section=f"""{record[4]}"""


    motifLabel="Motif de l appel : "
    if record[6]=="ArretComplet":
        motif="Arret Complet"
    else :
        motif="Anomalie Pouvant Entrainer unePanne"

    
    descriptionLabel = "Constat (symptôme observés) : "
    description = f"""{record[7]}"""


    

    

    demandeIntervention=[(dateCreationLabel,dateCreation),(emetteurLabel,emetteur),(equipementLabel,equipement),(sectionLabel,section),(motifLabel,motif),(descriptionLabel,description)]
    for item in demandeIntervention:
        pdf.set_font_size(22)
        pdf.set_text_color(31, 48, 94)
        pdf.multi_cell(0,10,item[0],'L',align="L")
        pdf.ln(10)
        pdf.set_font_size(16)
        pdf.set_text_color(5, 5, 5)
        pdf.cell(0,10,item[1],align="L")
        pdf.ln(25)

    pdf.set_font_size(22)
    pdf.set_text_color(31, 48, 94)
    pdf.multi_cell(0,10,"Reception",'B',align="C")
    pdf.ln(10)
    pdf.set_font_size(14)
    pdf.set_text_color(5, 5, 5)
    pdf.write_html(
        f"""
        <table border="1">
            <thead>
                <tr>
                    <th width="20%"></th>
                    <th width="35%"></th>
                    <th width="45%"></th>
                </tr>
            </thead>
            <tbody>
                <tr >
                    <td>{"Date :..../../.."}</td>
                    <td align="center">{"Heure : ......h......mn"}</td>
                    <td align="left">{"Visa Production : "}</td>
                </tr>
            
            </tbody>
        </table>
        """,
        table_line_separators=True,
    )

    pdf.output(f"""PDFs/DemandeIntervention{record[0]}.pdf""")
