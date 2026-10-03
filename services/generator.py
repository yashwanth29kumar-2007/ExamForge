from algorithms.sorting import sorting_trace
from algorithms.greedy import greedy_trace
from algorithms.backtracking import backtracking_trace


# ============================================================
# SELECT QUESTIONS ACCORDING TO USER'S REQUIREMENT
# ============================================================

def select_questions_for_pattern(
    questions,
    easy_count,
    medium_count,
    hard_count
):
    """
    Select questions according to the customized
    college examination pattern.

    Easy   -> 2 marks
    Medium -> 4 marks
    Hard   -> 6 marks
    """

    # --------------------------------------------------------
    # SEPARATE QUESTIONS BY DIFFICULTY AND MARKS
    # --------------------------------------------------------

    easy_questions = [
        q for q in questions
        if q["difficulty"] == "Easy"
        and q["marks"] == 2
    ]

    medium_questions = [
        q for q in questions
        if q["difficulty"] == "Medium"
        and q["marks"] == 4
    ]

    hard_questions = [
        q for q in questions
        if q["difficulty"] == "Hard"
        and q["marks"] == 6
    ]


    # --------------------------------------------------------
    # SORT BY PRIORITY
    # --------------------------------------------------------

    easy_questions.sort(
        key=lambda q: q["priority"],
        reverse=True
    )

    medium_questions.sort(
        key=lambda q: q["priority"],
        reverse=True
    )

    hard_questions.sort(
        key=lambda q: q["priority"],
        reverse=True
    )


    # --------------------------------------------------------
    # CHECK EASY QUESTIONS
    # --------------------------------------------------------

    if len(easy_questions) < easy_count:

        return {
            "success": False,
            "message": (
                f"Not enough Easy questions. "
                f"Required: {easy_count}, "
                f"Available: {len(easy_questions)}"
            ),
            "questions": []
        }


    # --------------------------------------------------------
    # CHECK MEDIUM QUESTIONS
    # --------------------------------------------------------

    if len(medium_questions) < medium_count:

        return {
            "success": False,
            "message": (
                f"Not enough Medium questions. "
                f"Required: {medium_count}, "
                f"Available: {len(medium_questions)}"
            ),
            "questions": []
        }


    # --------------------------------------------------------
    # CHECK HARD QUESTIONS
    # --------------------------------------------------------

    if len(hard_questions) < hard_count:

        return {
            "success": False,
            "message": (
                f"Not enough Hard questions. "
                f"Required: {hard_count}, "
                f"Available: {len(hard_questions)}"
            ),
            "questions": []
        }


    # --------------------------------------------------------
    # SELECT REQUIRED QUESTIONS
    # --------------------------------------------------------

    selected_questions = []

    selected_questions.extend(
        easy_questions[:easy_count]
    )

    selected_questions.extend(
        medium_questions[:medium_count]
    )

    selected_questions.extend(
        hard_questions[:hard_count]
    )


    # --------------------------------------------------------
    # SUCCESS
    # --------------------------------------------------------

    return {
        "success": True,
        "message": "Questions selected successfully.",
        "questions": selected_questions
    }


# ============================================================
# GENERATE PAPER
# ============================================================

def generate_paper(
    questions,
    target_marks,
    easy_count=3,
    medium_count=3,
    hard_count=2
):

    # --------------------------------------------------------
    # STEP 1 — SORTING
    # --------------------------------------------------------

    sorted_questions, sorting_steps = sorting_trace(
        questions
    )


    # --------------------------------------------------------
    # STEP 2 — CUSTOM PATTERN SELECTION
    # --------------------------------------------------------

    selection_result = select_questions_for_pattern(
        sorted_questions,
        easy_count,
        medium_count,
        hard_count
    )


    # --------------------------------------------------------
    # IF SELECTION FAILED
    # --------------------------------------------------------

    if not selection_result["success"]:

        return {
            "success": False,

            "method":
                "Customized College Pattern",

            "questions": [],

            "total_marks": 0,

            "error":
                selection_result["message"],

            "sorting_trace":
                sorting_steps,

            "greedy_trace": [],

            "backtracking_trace": []
        }


    # --------------------------------------------------------
    # GET SELECTED QUESTIONS
    # --------------------------------------------------------

    selected_questions = (
        selection_result["questions"]
    )


    # --------------------------------------------------------
    # STEP 3 — CALCULATE TOTAL MARKS
    # --------------------------------------------------------

    total_marks = sum(
        question["marks"]
        for question in selected_questions
    )


    # --------------------------------------------------------
    # STEP 4 — GREEDY ALGORITHM TRACE
    # --------------------------------------------------------

    _, _, greedy_steps = greedy_trace(
        sorted_questions,
        target_marks
    )


    # --------------------------------------------------------
    # STEP 5 — VERIFY TOTAL MARKS
    # --------------------------------------------------------

    if total_marks != target_marks:

        return {
            "success": False,

            "method":
                "Customized College Pattern",

            "questions": [],

            "total_marks":
                total_marks,

            "error": (
                "Calculated marks do not match "
                "the requested pattern."
            ),

            "sorting_trace":
                sorting_steps,

            "greedy_trace":
                greedy_steps,

            "backtracking_trace": []
        }


    # --------------------------------------------------------
    # STEP 6 — SUCCESS
    # --------------------------------------------------------

    return {
        "success": True,

        "method":
            "Greedy + Customized College Pattern",

        "questions":
            selected_questions,

        "total_marks":
            total_marks,

        "error":
            "",

        "sorting_trace":
            sorting_steps,

        "greedy_trace":
            greedy_steps,

        "backtracking_trace":
            []
    }