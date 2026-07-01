from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def create_summary_pdf(summary):

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b><font size=18>SmartStudy AI</font></b>", styles["Title"])
    )

    story.append(
        Paragraph("<b>AI Generated Study Summary</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"])
    )

    document.build(story)

    buffer.seek(0)

    return buffer