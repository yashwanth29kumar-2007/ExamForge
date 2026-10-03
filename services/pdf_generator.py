from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


# ============================================
# GENERATE PDF
# ============================================

def generate_pdf(paper, file_path):

    # ----------------------------------------
    # PDF DOCUMENT
    # ----------------------------------------

    document = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm
    )


    # ----------------------------------------
    # STYLES
    # ----------------------------------------

    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        "ExamTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        leading=24,
        spaceAfter=8
    )


    subtitle_style = ParagraphStyle(
        "ExamSubtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=11,
        leading=15,
        spaceAfter=15
    )


    question_style = ParagraphStyle(
        "Question",
        parent=styles["Normal"],
        fontSize=11,
        leading=16
    )


    normal_style = ParagraphStyle(
        "NormalText",
        parent=styles["Normal"],
        fontSize=10,
        leading=14
    )


    # ----------------------------------------
    # PDF CONTENT
    # ----------------------------------------

    content = []


    # ----------------------------------------
    # TITLE
    # ----------------------------------------

    content.append(
        Paragraph(
            "EXAMFORGE",
            title_style
        )
    )


    content.append(
        Paragraph(
            "DESIGN AND ANALYSIS OF ALGORITHMS",
            subtitle_style
        )
    )


    content.append(
        Paragraph(
            "Generated Question Paper",
            subtitle_style
        )
    )


    content.append(
        Spacer(
            1,
            10
        )
    )


    # ----------------------------------------
    # PAPER INFORMATION
    # ----------------------------------------

    information = [
        [
            "Total Marks",
            str(paper["total_marks"])
        ],
        [
            "Total Questions",
            str(len(paper["questions"]))
        ],
        [
            "Selection Method",
            paper["method"]
        ]
    ]


    info_table = Table(
        information,
        colWidths=[
            45 * mm,
            115 * mm
        ]
    )


    info_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.lightgrey
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, -1),
                "Helvetica"
            ),
            (
                "FONTNAME",
                (0, 0),
                (0, -1),
                "Helvetica-Bold"
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                8
            )
        ])
    )


    content.append(
        info_table
    )


    content.append(
        Spacer(
            1,
            20
        )
    )


    # ----------------------------------------
    # QUESTIONS HEADING
    # ----------------------------------------

    content.append(
        Paragraph(
            "QUESTIONS",
            styles["Heading2"]
        )
    )


    content.append(
        Spacer(
            1,
            8
        )
    )


    # ----------------------------------------
    # QUESTIONS
    # ----------------------------------------

    for index, question in enumerate(
        paper["questions"],
        start=1
    ):

        question_text = (
            f"<b>{index}. "
            f"{question['question']}</b>"
        )


        content.append(
            Paragraph(
                question_text,
                question_style
            )
        )


        details = (
            f"Unit {question['unit']} "
            f"| Topic: {question['topic']} "
            f"| Difficulty: {question['difficulty']} "
            f"| Marks: {question['marks']}"
        )


        content.append(
            Paragraph(
                details,
                normal_style
            )
        )


        content.append(
            Spacer(
                1,
                12
            )
        )


    # ----------------------------------------
    # FOOTER TEXT
    # ----------------------------------------

    content.append(
        Spacer(
            1,
            15
        )
    )


    content.append(
        Paragraph(
            "Generated by ExamForge — "
            "DAA Algorithm-Based Question Paper Generator",
            subtitle_style
        )
    )


    # ----------------------------------------
    # BUILD PDF
    # ----------------------------------------

    document.build(
        content
    )