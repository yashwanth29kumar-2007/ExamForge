import sqlite3


DATABASE_NAME = "database/examforge.db"


questions = [

    # =========================================================
    # UNIT 1 - INTRODUCTION / ANALYSIS
    # =========================================================

    (
        "Explain the concept of time complexity with examples.",
        "Design and Analysis of Algorithms",
        1,
        "Algorithm Analysis",
        "Easy",
        5,
        8
    ),

    (
        "Explain Big O, Big Omega and Big Theta notations.",
        "Design and Analysis of Algorithms",
        1,
        "Asymptotic Analysis",
        "Medium",
        10,
        9
    ),

    (
        "Analyze the time complexity of a nested loop algorithm.",
        "Design and Analysis of Algorithms",
        1,
        "Complexity Analysis",
        "Medium",
        10,
        8
    ),

    (
        "Compare best case, average case and worst case complexity.",
        "Design and Analysis of Algorithms",
        1,
        "Complexity Analysis",
        "Easy",
        5,
        7
    ),


    # =========================================================
    # UNIT 2 - SORTING AND SEARCHING
    # =========================================================

    (
        "Explain Bubble Sort with an example.",
        "Design and Analysis of Algorithms",
        2,
        "Sorting",
        "Easy",
        5,
        6
    ),

    (
        "Explain Merge Sort and analyze its time complexity.",
        "Design and Analysis of Algorithms",
        2,
        "Sorting",
        "Medium",
        10,
        10
    ),

    (
        "Explain Quick Sort and its partitioning technique.",
        "Design and Analysis of Algorithms",
        2,
        "Sorting",
        "Medium",
        10,
        9
    ),

    (
        "Compare Merge Sort and Quick Sort.",
        "Design and Analysis of Algorithms",
        2,
        "Sorting",
        "Hard",
        10,
        10
    ),

    (
        "Explain Binary Search with an example.",
        "Design and Analysis of Algorithms",
        2,
        "Searching",
        "Easy",
        5,
        7
    ),

    (
        "Compare Linear Search and Binary Search.",
        "Design and Analysis of Algorithms",
        2,
        "Searching",
        "Medium",
        5,
        8
    ),


    # =========================================================
    # UNIT 3 - GREEDY ALGORITHMS
    # =========================================================

    (
        "Explain the Greedy method and its characteristics.",
        "Design and Analysis of Algorithms",
        3,
        "Greedy Algorithms",
        "Easy",
        5,
        8
    ),

    (
        "Explain the Activity Selection Problem using a Greedy approach.",
        "Design and Analysis of Algorithms",
        3,
        "Activity Selection",
        "Medium",
        10,
        10
    ),

    (
        "Solve the Fractional Knapsack Problem using Greedy strategy.",
        "Design and Analysis of Algorithms",
        3,
        "Knapsack",
        "Medium",
        10,
        10
    ),

    (
        "Explain Huffman Coding algorithm with an example.",
        "Design and Analysis of Algorithms",
        3,
        "Huffman Coding",
        "Hard",
        10,
        9
    ),

    (
        "Explain the Job Sequencing with Deadlines problem.",
        "Design and Analysis of Algorithms",
        3,
        "Job Sequencing",
        "Hard",
        10,
        9
    ),


    # =========================================================
    # UNIT 4 - DYNAMIC PROGRAMMING
    # =========================================================

    (
        "Explain the basic concept of Dynamic Programming.",
        "Design and Analysis of Algorithms",
        4,
        "Dynamic Programming",
        "Easy",
        5,
        7
    ),

    (
        "Explain the 0/1 Knapsack problem using Dynamic Programming.",
        "Design and Analysis of Algorithms",
        4,
        "Knapsack",
        "Hard",
        10,
        10
    ),

    (
        "Explain the Longest Common Subsequence problem.",
        "Design and Analysis of Algorithms",
        4,
        "LCS",
        "Medium",
        10,
        9
    ),

    (
        "Explain Matrix Chain Multiplication using Dynamic Programming.",
        "Design and Analysis of Algorithms",
        4,
        "Matrix Chain Multiplication",
        "Hard",
        10,
        10
    ),


    # =========================================================
    # UNIT 5 - GRAPH ALGORITHMS
    # =========================================================

    (
        "Explain Breadth First Search with an example.",
        "Design and Analysis of Algorithms",
        5,
        "Graph Traversal",
        "Easy",
        5,
        8
    ),

    (
        "Explain Depth First Search with an example.",
        "Design and Analysis of Algorithms",
        5,
        "Graph Traversal",
        "Easy",
        5,
        8
    ),

    (
        "Compare BFS and DFS algorithms.",
        "Design and Analysis of Algorithms",
        5,
        "Graph Traversal",
        "Medium",
        10,
        9
    ),

    (
        "Explain Dijkstra's Shortest Path algorithm.",
        "Design and Analysis of Algorithms",
        5,
        "Shortest Path",
        "Hard",
        10,
        10
    ),

    (
        "Explain Kruskal's Minimum Spanning Tree algorithm.",
        "Design and Analysis of Algorithms",
        5,
        "Minimum Spanning Tree",
        "Hard",
        10,
        10
    ),


    # =========================================================
    # UNIT 5 - BACKTRACKING
    # =========================================================

    (
        "Explain the Backtracking technique.",
        "Design and Analysis of Algorithms",
        5,
        "Backtracking",
        "Easy",
        5,
        8
    ),

    (
        "Explain the N-Queens problem using Backtracking.",
        "Design and Analysis of Algorithms",
        5,
        "N-Queens",
        "Hard",
        10,
        10
    ),

    (
        "Explain the Graph Coloring problem using Backtracking.",
        "Design and Analysis of Algorithms",
        5,
        "Graph Coloring",
        "Hard",
        10,
        9
    ),

    (
        "Explain the Hamiltonian Cycle problem using Backtracking.",
        "Design and Analysis of Algorithms",
        5,
        "Hamiltonian Cycle",
        "Hard",
        10,
        9
    ),


    # =========================================================
    # COLLEGE 30-MARK PATTERN
    #
    # VERY SHORT -> EASY   -> 3 x 2 = 6
    # SHORT       -> MEDIUM -> 3 x 4 = 12
    # LONG        -> HARD   -> 2 x 6 = 12
    #
    # TOTAL = 30 MARKS
    # =========================================================


    # =========================================================
    # EASY - 2 MARKS
    # =========================================================

    (
        "What is an algorithm?",
        "Design and Analysis of Algorithms",
        1,
        "Introduction to Algorithms",
        "Easy",
        2,
        10
    ),

    (
        "Define time complexity.",
        "Design and Analysis of Algorithms",
        1,
        "Complexity Analysis",
        "Easy",
        2,
        9
    ),

    (
        "What is Big O notation?",
        "Design and Analysis of Algorithms",
        1,
        "Asymptotic Analysis",
        "Easy",
        2,
        8
    ),


    # =========================================================
    # MEDIUM - 4 MARKS
    # =========================================================

    (
        "Explain Binary Search with an example.",
        "Design and Analysis of Algorithms",
        2,
        "Searching",
        "Medium",
        4,
        10
    ),

    (
        "Explain Merge Sort with an example.",
        "Design and Analysis of Algorithms",
        2,
        "Sorting",
        "Medium",
        4,
        9
    ),

    (
        "Explain the Greedy method with an example.",
        "Design and Analysis of Algorithms",
        3,
        "Greedy Algorithms",
        "Medium",
        4,
        8
    ),

    (
        "Explain the Activity Selection Problem using the Greedy method.",
        "Design and Analysis of Algorithms",
        3,
        "Activity Selection",
        "Medium",
        4,
        7
    ),


    # =========================================================
    # HARD - 6 MARKS
    # =========================================================

    (
        "Analyze the 0/1 Knapsack problem using a Dynamic Programming table.",
        "Design and Analysis of Algorithms",
        4,
        "Dynamic Programming",
        "Hard",
        6,
        10
    ),

    (
        "Demonstrate the N-Queens problem using the Backtracking approach.",
        "Design and Analysis of Algorithms",
        5,
        "Backtracking",
        "Hard",
        6,
        9
    ),

    (
        "Explain Dijkstra's algorithm and its working with an example.",
        "Design and Analysis of Algorithms",
        5,
        "Shortest Path",
        "Hard",
        6,
        8
    )

]


# =========================================================
# INSERT QUESTIONS
# =========================================================

def insert_questions():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()

    added_count = 0
    skipped_count = 0

    for question in questions:

        question_text = question[0]

        # -------------------------------------------------
        # CHECK WHETHER QUESTION ALREADY EXISTS
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT id
            FROM questions
            WHERE question = ?
            """,
            (question_text,)
        )

        existing_question = cursor.fetchone()

        if existing_question:

            skipped_count += 1

            continue

        # -------------------------------------------------
        # INSERT QUESTION
        # -------------------------------------------------

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
            question
        )

        added_count += 1

    connection.commit()

    connection.close()

    print()
    print("==============================================")
    print("       EXAMFORGE DATABASE UPDATE")
    print("==============================================")
    print()

    print(
        f"Questions added   : {added_count}"
    )

    print(
        f"Questions skipped : {skipped_count}"
    )

    print(
        f"Total in seed list: {len(questions)}"
    )

    print()

    print(
        "Database update completed successfully!"
    )

    print(
        "=============================================="
    )


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":

    insert_questions()