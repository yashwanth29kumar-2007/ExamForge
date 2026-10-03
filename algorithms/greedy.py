# ============================================
# GREEDY ALGORITHM
# ============================================

def greedy_select(questions, target_marks):
    """
    Basic Greedy algorithm for selecting questions.

    Questions are assumed to already be sorted
    by priority and marks.
    """

    selected_questions = []
    total_marks = 0

    for question in questions:

        question_marks = question["marks"]

        if total_marks + question_marks <= target_marks:

            selected_questions.append(question)

            total_marks += question_marks

        if total_marks == target_marks:
            break

    return selected_questions, total_marks


# ============================================
# GREEDY TRACE
# ============================================

def greedy_trace(questions, target_marks):
    """
    Create a step-by-step trace of the Greedy algorithm.
    """

    selected_questions = []

    total_marks = 0

    trace = []

    trace.append({
        "step": 1,
        "action": "Greedy selection started",
        "details": (
            f"Target marks: {target_marks}"
        )
    })

    step = 2

    for question in questions:

        question_marks = question["marks"]

        # -----------------------------
        # SELECT QUESTION
        # -----------------------------

        if total_marks + question_marks <= target_marks:

            selected_questions.append(question)

            total_marks += question_marks

            trace.append({
                "step": step,
                "action": "Question selected",
                "details": (
                    f"{question['question']} "
                    f"| Difficulty: {question['difficulty']} "
                    f"| Marks: {question_marks} "
                    f"| Total: {total_marks}"
                )
            })

        # -----------------------------
        # SKIP QUESTION
        # -----------------------------

        else:

            trace.append({
                "step": step,
                "action": "Question skipped",
                "details": (
                    f"{question['question']} "
                    f"| Difficulty: {question['difficulty']} "
                    f"| Marks: {question_marks} "
                    f"| Would exceed target."
                )
            })

        step += 1

        if total_marks == target_marks:
            break

    # -----------------------------
    # COMPLETED
    # -----------------------------

    trace.append({
        "step": step,
        "action": "Greedy selection completed",
        "details": (
            f"Total marks selected: {total_marks}"
        )
    })

    return (
        selected_questions,
        total_marks,
        trace
    )


# ============================================
# DIFFICULTY-AWARE GREEDY
# ============================================

def greedy_select_with_difficulty(
    questions,
    target_marks,
    easy_count,
    medium_count,
    hard_count
):
    """
    Difficulty-aware Greedy algorithm.

    Requirements:
        Easy   -> required number
        Medium -> required number
        Hard   -> required number

    The algorithm first chooses the highest-mark
    questions from each required difficulty.

    Then it tries to fill the remaining marks.
    """

    selected_questions = []

    total_marks = 0

    # ========================================
    # DIFFICULTY REQUIREMENTS
    # ========================================

    requirements = {
        "Easy": easy_count,
        "Medium": medium_count,
        "Hard": hard_count
    }

    # ========================================
    # STEP 1
    # SELECT REQUIRED QUESTIONS
    # ========================================

    for difficulty in [
        "Easy",
        "Medium",
        "Hard"
    ]:

        required = requirements[difficulty]

        # Find questions of this difficulty
        difficulty_questions = [
            question
            for question in questions
            if question["difficulty"] == difficulty
        ]

        # ------------------------------------
        # Highest marks first
        # ------------------------------------

        difficulty_questions.sort(
            key=lambda question: (
                question["marks"],
                question["priority"]
            ),
            reverse=True
        )

        # ------------------------------------
        # Select required questions
        # ------------------------------------

        for question in difficulty_questions:

            if required <= 0:
                break

            if (
                total_marks
                + question["marks"]
                <= target_marks
            ):

                selected_questions.append(
                    question
                )

                total_marks += question["marks"]

                required -= 1

    # ========================================
    # STEP 2
    # FILL REMAINING MARKS
    # ========================================

    selected_ids = {
        question["id"]
        for question in selected_questions
    }

    remaining_questions = [
        question
        for question in questions
        if question["id"] not in selected_ids
    ]

    # Highest marks first
    remaining_questions.sort(
        key=lambda question: (
            question["marks"],
            question["priority"]
        ),
        reverse=True
    )

    # ----------------------------------------
    # Add extra questions if possible
    # ----------------------------------------

    for question in remaining_questions:

        if (
            total_marks
            + question["marks"]
            <= target_marks
        ):

            selected_questions.append(
                question
            )

            total_marks += question["marks"]

        if total_marks == target_marks:
            break

    # ========================================
    # STEP 3
    # CHECK DIFFICULTY COUNTS
    # ========================================

    easy_selected = sum(
        1
        for question in selected_questions
        if question["difficulty"] == "Easy"
    )

    medium_selected = sum(
        1
        for question in selected_questions
        if question["difficulty"] == "Medium"
    )

    hard_selected = sum(
        1
        for question in selected_questions
        if question["difficulty"] == "Hard"
    )

    # ========================================
    # FINAL VALIDATION
    # ========================================

    requirements_met = (
        easy_selected >= easy_count
        and
        medium_selected >= medium_count
        and
        hard_selected >= hard_count
        and
        total_marks == target_marks
    )

    return (
        selected_questions,
        total_marks,
        requirements_met
    )