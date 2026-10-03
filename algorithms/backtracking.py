def backtrack_questions(
    questions,
    target_marks,
    selected=None,
    start_index=0
):
    """
    Backtracking algorithm for selecting questions.

    Tries different combinations of questions until
    the target marks are reached exactly.
    """

    if selected is None:
        selected = []

    current_marks = sum(
        question["marks"]
        for question in selected
    )

    if current_marks == target_marks:
        return selected.copy()

    if current_marks > target_marks:
        return None

    for i in range(start_index, len(questions)):

        question = questions[i]

        selected.append(question)

        result = backtrack_questions(
            questions,
            target_marks,
            selected,
            i + 1
        )

        if result is not None:
            return result

        selected.pop()

    return None


def backtracking_trace(
    questions,
    target_marks,
    selected=None,
    start_index=0,
    trace=None
):
    """
    Backtracking algorithm with execution trace.
    """

    if selected is None:
        selected = []

    if trace is None:
        trace = []

    current_marks = sum(
        question["marks"]
        for question in selected
    )

    # Target reached
    if current_marks == target_marks:

        trace.append({
            "step": len(trace) + 1,
            "action": "Target reached",
            "details": (
                f"Current total: {current_marks} marks."
            )
        })

        return selected.copy(), trace

    # Target exceeded
    if current_marks > target_marks:

        trace.append({
            "step": len(trace) + 1,
            "action": "Backtrack",
            "details": (
                f"Current total {current_marks} exceeds "
                f"target {target_marks}."
            )
        })

        return None, trace

    # Try remaining questions
    for i in range(
        start_index,
        len(questions)
    ):

        question = questions[i]

        trace.append({
            "step": len(trace) + 1,
            "action": "Try question",
            "details": (
                f"{question['question']} "
                f"| Marks: {question['marks']} "
                f"| Current total before selection: "
                f"{current_marks}"
            )
        })

        selected.append(question)

        result, trace = backtracking_trace(
            questions,
            target_marks,
            selected,
            i + 1,
            trace
        )

        if result is not None:

            return result, trace

        selected.pop()

        trace.append({
            "step": len(trace) + 1,
            "action": "Remove question",
            "details": (
                f"Removed: {question['question']}"
            )
        })

    return None, trace