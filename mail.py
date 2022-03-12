# encoding=utf8
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from termcolor import colored

name = ""
eid = ""
pwd = ""

b1 = "May'22 - July'22"
b2 = "COLLEGE_NAME"
b3 = "BRANCH_NAME"
emails = pd.read_csv("test.csv")
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(eid, pwd)
files_M = ["Curriculum_Vitae_BC.pdf", "Tanmay juneja_reference.pdf"]
files_F = files_M

all_emails = emails["Email"]
all_univ = emails["Univ"]
all_names = emails["Name"]
all_pubs = emails["Publications"]
all_regard = ""
all_sig = ""
all_coll = ""
all_coll2 = ""
all_message = ""
bod3 = ""
bod4 = ""

for idx in range(len(emails)):
    email = all_emails[idx]
    uni = all_univ[idx]
    pubs = all_pubs[idx]
    name = all_names[idx]
    subject = "Request For Summer Internship."
    head = f"Dear Professor {name},"
    nl = "\n"
    body1 = ""
    body2 = all_message
    body3 = bod3
    body4 = bod4
    body5 = ""
    signature = all_sig
    coll = all_coll
    coll2 = all_coll2

    msg = MIMEMultipart("alternative")
    msg["From"] = "Tanmay Juneja"
    msg["To"] = email
    msg["Subject"] = subject

    body = (
        "{4}\n"
        "{5}\n\n"
        "{6}\n\n"
        "{7}\n\n"
        "{8}\n"
        "{9}\n\n"
        "{10}\n"
        "{11}\n"
        "{12}\n".format(
            name,
            eid,
            email,
            subject,
            head,
            body1,
            body2,
            body3,
            body4,
            body5,
            signature,
            coll,
            coll2,
        )
    )
    htmlcontent_M = ""#f"""<p style="margin: 0cm; font-size: 12pt; font-family: &quot;Times New Roman&quot;, serif; background: white;"><span style="font-size: 13pt; font-family: Helvetica; color: rgb(14, 16, 26);">Dear Professor {name},</span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-family: Helvetica;">&nbsp;</span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">I am a second-year student at the Indian Institute of Technology, Delhi (<b>IIT-Delhi</b>), currently ranked as the best engineering institute in India. I'm pursuing a Bachelor of Technology degree in&nbsp;<b>Production and Industrial Engineering</b>. I am writing this email to you as an application for a research project/internship under your guidance in the duration of&nbsp;<b>May'22 - July'22.</b></span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-family: Helvetica;">&nbsp;</span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">I went through your profile, publications(<b>{pubs}</b>), and research interests. I found them fascinating and in alignment with my interests.<b>&nbsp;{uni}&nbsp;</b>is one of the best universities and my top priority for pursuing my summer internship.</span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-family: Helvetica;">&nbsp;</span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">I am interested in&nbsp;<b>Blockchain, Artificial Intelligence, Optimization, and Machine Learning.&nbsp;</b>I am currently doing an internship as a&nbsp;<b>Core Blockchain developer</b>&nbsp;at&nbsp;<b>NOKIA</b>.&nbsp;I am responsible for creating the whole private NOKIA blockchain, facilitating in approval of private transactions and adding them onto the Blockchain using different types of encryptions and safety measures.<u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">I am also currently pursuing a&nbsp;<b>Heart&nbsp;Disease Prediction</b>&nbsp;project under our respected IIT Delhi Professor Tapan Kumar Gandhi. We aim to optimize the process and address the gaps in feature selection and the huge data requirement in DL models.&nbsp;(My GitHub -&nbsp;<a href="https://github.com/tanmayjuneja8" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://github.com/tanmayjuneja8&amp;source=gmail&amp;ust=1643649791282000&amp;usg=AOvVaw3Q0jXtILGpWvU5F-1RU8sN" style="color: rgb(17, 85, 204);"><span style="color: black;">https://github.com/<wbr>tanmayjuneja8</span></a>)</span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-family: Helvetica;">&nbsp;</span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">I wish to gain expertise in these fields to complement my theoretical learning with research experience. An opportunity to be mentored by a highly reputed professor like you would help me greatly in achieving my goal.</span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;"><br></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">Attached for your kind perusal, you can find my&nbsp;<b>resume</b>&nbsp;and a&nbsp;<b>letter of</b>&nbsp;<b>recommendation</b>&nbsp;from our renowned Professor<b>&nbsp;</b>Lakshmi Narayan Ramasubramanian.&nbsp;Shall be glad to address any questions that you may have. In anticipation of your response.&nbsp;</span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">&nbsp;</span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">Best Regards</span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">Tanmay Juneja</span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">M: +91 9717600000</span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">E:&nbsp;<a href="mailto:me2201064@iitd.ac.in" target="_blank" style="color: rgb(17, 85, 204);"><span style="color: black;">me2201064@iitd.ac.in</span></a></span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">Indian Institute of Technology (IIT) Delhi</span><span style="font-family: Helvetica;"><u></u><u></u></span></p><p class="MsoNormal" style="margin: 0cm; color: rgb(34, 34, 34); font-size: 12pt; font-family: Calibri, sans-serif; background: white;"><span style="font-size: 13.5pt; font-family: Helvetica;">Delhi – 110016, India</span></p>"""
    htmlcontent_F = htmlcontent_M

    part1 = MIMEText(body, "plain")
    part2 = (
        MIMEText(htmlcontent_F, "html")
        if type == "F"
        else MIMEText(htmlcontent_M, "html")
    )
    msg.attach(part1)
    msg.attach(part2)

    for file in files_F if type == "F" else files_M:
        with open(file, "rb") as f:
            file_data = f.read()
            file_name = f.name
            attachment = MIMEApplication(file_data, _subtype="pdf")
        attachment.add_header("Content-Disposition", "attachment", filename=str(file))
        msg.attach(attachment)

    try:
        server.send_message(msg)
        print("Email to {} successfully sent!\n".format(email))
    except Exception as e:
        print("Email to {} could not be sent :( because {}\n".format(email, str(e)))
server.quit()
