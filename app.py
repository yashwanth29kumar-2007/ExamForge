from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file
)

from database.database import get_connection
from services.generator import generate_paper
from services.pdf_generator import generate_pdf

import os


# ============================================================
# FLASK APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# GET ALL QUESTIONS
# ============================================================

def get_questions():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM questions"
    )

    questions = cursor.fetchall()

    connection.close()

    return questions


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/")
def home():

    questions = get_questions()

    return render_template(
        "dashboard.html",
        questions=questions
    )


# ============================================================
# QUESTION BANK
# ============================================================

@app.route("/questions")
def questions():

    unit = request.args.get(
        "unit",
        ""
    )

    difficulty = request.args.get(
        "difficulty",
        ""
    )

    topic = request.args.get(
        "topic",
        ""
    )

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        SELECT *
        FROM questions
        WHERE 1=1
    """

    parameters = []


    # --------------------------------------------------------
    # UNIT FILTER
    # --------------------------------------------------------

    if unit:

        query += """
            AND unit = ?
        """

        parameters.append(
            int(unit)
        )


    # --------------------------------------------------------
    # DIFFICULTY FILTER
    # --------------------------------------------------------

    if difficulty:

        query += """
            AND difficulty = ?
        """

        parameters.append(
            difficulty
        )


    # --------------------------------------------------------
    # TOPIC FILTER
    # --------------------------------------------------------

    if topic:

        query += """
            AND topic LIKE ?
        """

        parameters.append(
            "%" + topic + "%"
        )


    # --------------------------------------------------------
    # ORDER
    # --------------------------------------------------------

    query += """
        ORDER BY unit, id
    """


    cursor.execute(
        query,
        parameters
    )

    filtered_questions = cursor.fetchall()

    connection.close()


    return render_template(
        "questions.html",
        questions=filtered_questions,
        selected_unit=unit,
        selected_difficulty=difficulty,
        selected_topic=topic
    )


# ============================================================
# ADD QUESTION
# ============================================================

@app.route(
    "/questions/add",
    methods=["GET", "POST"]
)
def add_question():

    if request.method == "POST":

        question = request.form["question"]

        subject = request.form["subject"]

        unit = int(
            request.form["unit"]
        )

        topic = request.form["topic"]

        difficulty = request.form["difficulty"]

        marks = int(
            request.form["marks"]
        )

        priority = int(
            request.form["priority"]
        )


        connection = get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO questions
            (
                question,
                subject,
                unit,
                topic,
                difficulty,
                marks,
                priority
            )

            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                question,
                subject,
                unit,
                topic,
                difficulty,
                marks,
                priority
            )
        )


        connection.commit()

        connection.close()


        return redirect(
            url_for("questions")
        )


    return render_template(
        "add_question.html"
    )


# ============================================================
# GENERATE QUESTION PAPER
# ============================================================

@app.route(
    "/generate",
    methods=["GET", "POST"]
)
def generate():

    # ========================================================
    # SHOW GENERATE PAGE
    # ========================================================

    if request.method == "GET":

        return render_template(
            "generate.html"
        )


    # ========================================================
    # EXAMINATION DETAILS
    # ========================================================

    college_name = request.form.get(
        "college_name",
        ""
    ).strip()


    subject_name = request.form.get(
        "subject_name",
        "Design and Analysis of Algorithms"
    ).strip()


    subject_code = request.form.get(
        "subject_code",
        ""
    ).strip()


    semester = request.form.get(
        "semester",
        ""
    ).strip()


    exam_title = request.form.get(
        "exam_title",
        "End Semester Examination"
    ).strip()


    duration = request.form.get(
        "duration",
        "3 Hours"
    ).strip()


    # ========================================================
    # TARGET TOTAL MARKS
    # ========================================================

    try:

        target_marks = int(
            request.form.get(
                "target_marks",
                30
            )
        )

    except ValueError:

        target_marks = 30


    # ========================================================
    # QUESTION COUNTS
    # ========================================================

    try:

        easy_count = int(
            request.form.get(
                "easy_count",
                3
            )
        )

        medium_count = int(
            request.form.get(
                "medium_count",
                3
            )
        )

        hard_count = int(
            request.form.get(
                "hard_count",
                2
            )
        )

    except ValueError:

        easy_count = 3

        medium_count = 3

        hard_count = 2


    # ========================================================
    # SAFETY CHECK
    # ========================================================

    easy_count = max(
        0,
        min(easy_count, 20)
    )


    medium_count = max(
        0,
        min(medium_count, 20)
    )


    hard_count = max(
        0,
        min(hard_count, 20)
    )


    # ========================================================
    # CALCULATE SELECTED MARKS
    #
    # Easy   = 2 marks
    # Medium = 4 marks
    # Hard   = 6 marks
    # ========================================================

    selected_marks = (
        (easy_count * 2)
        +
        (medium_count * 4)
        +
        (hard_count * 6)
    )


    # ========================================================
    # CHECK TARGET MARKS
    # ========================================================

    if selected_marks != target_marks:

        paper = {

            "success": False,

            "method":
                "Customized College Pattern",

            "questions": [],

            "total_marks":
                selected_marks,

            "target_marks":
                target_marks,

            "error": (
                f"Target is {target_marks} marks, "
                f"but the selected questions total "
                f"{selected_marks} marks. "
                f"Please adjust Easy, Medium and "
                f"Hard question counts."
            ),

            "sorting_trace": [],

            "greedy_trace": [],

            "backtracking_trace": [],

            "college_name":
                college_name,

            "subject_name":
                subject_name,

            "subject_code":
                subject_code,

            "semester":
                semester,

            "exam_title":
                exam_title,

            "duration":
                duration,

            "easy_count":
                easy_count,

            "medium_count":
                medium_count,

            "hard_count":
                hard_count,

            "easy_marks":
                2,

            "medium_marks":
                4,

            "hard_marks":
                6,

            "easy_type":
                "Very Short",

            "medium_type":
                "Short",

            "hard_type":
                "Long"
        }


        return render_template(
            "result.html",
            paper=paper
        )


    # ========================================================
    # GET QUESTIONS FROM DATABASE
    # ========================================================

    questions = get_questions()


    # ========================================================
    # GENERATE QUESTION PAPER
    # ========================================================

    paper = generate_paper(
        questions,
        target_marks,
        easy_count,
        medium_count,
        hard_count
    )


    # ========================================================
    # ADD EXAM DETAILS TO PAPER
    # ========================================================

    paper["college_name"] = college_name

    paper["subject_name"] = subject_name

    paper["subject_code"] = subject_code

    paper["semester"] = semester

    paper["exam_title"] = exam_title

    paper["duration"] = duration


    # ========================================================
    # QUESTION PATTERN INFORMATION
    # ========================================================

    paper["easy_count"] = easy_count

    paper["medium_count"] = medium_count

    paper["hard_count"] = hard_count

    paper["target_marks"] = target_marks

    paper["easy_marks"] = 2

    paper["medium_marks"] = 4

    paper["hard_marks"] = 6

    paper["easy_type"] = "Very Short"

    paper["medium_type"] = "Short"

    paper["hard_type"] = "Long"


    # ========================================================
    # SAVE HISTORY ONLY IF SUCCESSFUL
    # ========================================================

    if paper["success"]:

        connection = get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO paper_history
            (
                total_marks,
                easy_count,
                medium_count,
                hard_count,
                method,
                question_count
            )

            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                paper["total_marks"],
                easy_count,
                medium_count,
                hard_count,
                paper["method"],
                len(paper["questions"])
            )
        )


        connection.commit()

        connection.close()


    # ========================================================
    # SHOW RESULT
    # ========================================================

    return render_template(
        "result.html",
        paper=paper
    )


# ============================================================
# DOWNLOAD PDF
# ============================================================

@app.route(
    "/download-pdf",
    methods=["POST"]
)
def download_pdf():

    # ========================================================
    # TARGET MARKS
    # ========================================================

    try:

        target_marks = int(
            request.form.get(
                "target_marks",
                30
            )
        )

    except ValueError:

        target_marks = 30


    # ========================================================
    # QUESTION COUNTS
    # ========================================================

    try:

        easy_count = int(
            request.form.get(
                "easy_count",
                3
            )
        )

        medium_count = int(
            request.form.get(
                "medium_count",
                3
            )
        )

        hard_count = int(
            request.form.get(
                "hard_count",
                2
            )
        )

    except ValueError:

        return "Invalid question count."


    # ========================================================
    # EXAMINATION DETAILS
    # ========================================================

    college_name = request.form.get(
        "college_name",
        "College / University"
    )


    subject_name = request.form.get(
        "subject_name",
        "Design and Analysis of Algorithms"
    )


    subject_code = request.form.get(
        "subject_code",
        ""
    )


    semester = request.form.get(
        "semester",
        ""
    )


    exam_title = request.form.get(
        "exam_title",
        "End Semester Examination"
    )


    duration = request.form.get(
        "duration",
        "3 Hours"
    )


    # ========================================================
    # VALIDATE TARGET
    # ========================================================

    selected_marks = (
        (easy_count * 2)
        +
        (medium_count * 4)
        +
        (hard_count * 6)
    )


    if selected_marks != target_marks:

        return (
            f"Cannot create PDF. "
            f"Target is {target_marks} marks, "
            f"but selected questions total "
            f"{selected_marks} marks."
        )


    # ========================================================
    # GET QUESTIONS
    # ========================================================

    questions = get_questions()


    # ========================================================
    # GENERATE PAPER
    # ========================================================

    paper = generate_paper(
        questions,
        target_marks,
        easy_count,
        medium_count,
        hard_count
    )


    # ========================================================
    # CHECK GENERATION
    # ========================================================

    if not paper["success"]:

        return (
            "Unable to generate PDF paper. "
            + paper.get(
                "error",
                "Unknown error."
            )
        )


    # ========================================================
    # ADD EXAM DETAILS
    # ========================================================

    paper["college_name"] = college_name

    paper["subject_name"] = subject_name

    paper["subject_code"] = subject_code

    paper["semester"] = semester

    paper["exam_title"] = exam_title

    paper["duration"] = duration

    paper["target_marks"] = target_marks

    paper["easy_count"] = easy_count

    paper["medium_count"] = medium_count

    paper["hard_count"] = hard_count


    # ========================================================
    # CREATE GENERATED PAPERS FOLDER
    # ========================================================

    pdf_folder = os.path.join(
        app.root_path,
        "generated_papers"
    )


    os.makedirs(
        pdf_folder,
        exist_ok=True
    )


    # ========================================================
    # PDF PATH
    # ========================================================

    pdf_path = os.path.join(
        pdf_folder,
        "ExamForge_Question_Paper.pdf"
    )


    # ========================================================
    # GENERATE PDF
    # ========================================================

    generate_pdf(
        paper,
        pdf_path
    )


    # ========================================================
    # SEND PDF
    # ========================================================

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name="ExamForge_Question_Paper.pdf"
    )


# ============================================================
# PAPER HISTORY
# ============================================================

@app.route("/history")
def history():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM paper_history
        ORDER BY id DESC
        """
    )


    history_records = cursor.fetchall()

    connection.close()


    return render_template(
        "history.html",
        history=history_records
    )


# ============================================================
# ALGORITHM TRACE
# ============================================================

@app.route("/trace")
def trace():

    # --------------------------------------------------------
    # GET QUESTION COUNTS
    # --------------------------------------------------------

    try:

        easy_count = int(
            request.args.get(
                "easy",
                3
            )
        )

        medium_count = int(
            request.args.get(
                "medium",
                3
            )
        )

        hard_count = int(
            request.args.get(
                "hard",
                2
            )
        )

    except ValueError:

        easy_count = 3

        medium_count = 3

        hard_count = 2


    # --------------------------------------------------------
    # CALCULATE TARGET
    # --------------------------------------------------------

    target_marks = (
        (easy_count * 2)
        +
        (medium_count * 4)
        +
        (hard_count * 6)
    )


    # --------------------------------------------------------
    # GET QUESTIONS
    # --------------------------------------------------------

    questions = get_questions()


    # --------------------------------------------------------
    # GENERATE PAPER
    # --------------------------------------------------------

    generated_paper = generate_paper(
        questions,
        target_marks,
        easy_count,
        medium_count,
        hard_count
    )


    # --------------------------------------------------------
    # PREPARE TRACE DATA
    # --------------------------------------------------------

    paper = {

        "target_marks":
            target_marks,

        "easy_count":
            easy_count,

        "medium_count":
            medium_count,

        "hard_count":
            hard_count,

        "total_marks":
            generated_paper["total_marks"],

        "method":
            generated_paper["method"],

        "questions":
            generated_paper["questions"],

        "sorting_trace":
            generated_paper["sorting_trace"],

        "greedy_trace":
            generated_paper["greedy_trace"],

        "backtracking_trace":
            generated_paper["backtracking_trace"]

    }


    # --------------------------------------------------------
    # SHOW TRACE PAGE
    # --------------------------------------------------------

    return render_template(
        "algorithm_trace.html",
        paper=paper
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )