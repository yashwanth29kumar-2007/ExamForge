def sort_questions(questions):
    """
    Sort questions based on priority.

    Higher priority questions come first.
    If priority is the same, higher marks come first.
    """

    sorted_questions = sorted(
        questions,
        key=lambda question: (
            question["priority"],
            question["marks"]
        ),
        reverse=True
    )

    return sorted_questions


def sorting_trace(questions):
    """
    Create a trace of the sorting process.
    """

    sorted_questions = sort_questions(questions)

    trace = []

    trace.append({
        "step": 1,
        "action": "Sorting started",
        "details": f"{len(questions)} questions received."
    })

    trace.append({
        "step": 2,
        "action": "Sorting criteria",
        "details": "Priority descending, then marks descending."
    })

    for index, question in enumerate(sorted_questions[:10], start=1):

        trace.append({
            "step": index + 2,
            "action": "Question positioned",
            "details": (
                f"{question['question']} "
                f"| Priority: {question['priority']} "
                f"| Marks: {question['marks']}"
            )
        })

    trace.append({
        "step": len(trace) + 1,
        "action": "Sorting completed",
        "details": "Questions are ready for selection."
    })

    return sorted_questions, trace