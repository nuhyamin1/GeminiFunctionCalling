import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

from google.generativeai.types import FunctionDeclaration, Tool

load_dotenv()

class EmailTool:
    """ Send email using SMTP lib"""

    # function declaration
    SEND_EMAIL = FunctionDeclaration(
        name="send_email",
        description=(
            "Send email message"
        ),
        parameters={
            "type": "object",
            "properties":{
                "subject": {
                    "type": "string",
                    "description": "Subject of the message"
                },
                "to":{
                    "type": "string",
                    "description": "email address destination"
                },
                "content":{
                    "type": "string",
                    "description": "content of the email message"
                }
            },
            "required": ["subject", "to", "content"]
        }
    )
   
    @staticmethod
    def send_email(subject: str, to: str, content: str):
        email_address = os.getenv("EMAIL_ADDRESS")
        email_password = os.getenv("EMAIL_PASSWORD")

        if not all([subject, to, content]):
            return {"status": "error", "message": "Missing required fields: subject, to, or content."}

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = to
        msg.set_content(content)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_address, email_password)
                smtp.send_message(msg)

            print(f"Email successfully sent to {to} with subject {subject}")
            return {"status": "success", "message": f"Email successfully sent to {to}"}

        except smtplib.SMTPAuthenticationError:
            print("Error: SMTP Authentication Failed. Check email_address and email_password (App Password).")
            return {"status": "error", "message": "SMTP Authentication Failed. Check credentials."}
        except Exception as e:
            print(f"Error sending email: {e}")
            return {"status": "error", "message": f"An error occurred: {str(e)}"}
        
