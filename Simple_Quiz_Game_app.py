import streamlit as st

st.title("Simple Quiz Game")

questions = [
    "What is the name of your college?",
    "Which programming language are you learning?",
    "How many days are there in a week?",
    "Which device is used to type text into a computer?",
    "What does CPU stand for?"
]

options = [
    ["NCIT College", "Oxford College", "Cosmos College", "City College"],
    ["PHP", "Java", "C++", "python"],
    ["5", "6", "7", "8"],
    ["Monitor", "Keyboard", "Speaker", "Printer"],
    [
        "Central Processing Unit",
        "Computer Personal Unit",
        "Central Program Unit",
        "Computer Processing Unit"
    ]
]

answers = [
    "Cosmos College",
    "Python",
    "7",
    "Keyboard",
    "Central Processing Unit"
]

if "question" not in st.session_state:
    st.session_state.question = 0
    st.session_state.score = 0

if st.session_state.question < 5:

    number = st.session_state.question

    st.write("Question", number + 1)
    st.write(questions[number])

    answer = st.radio(
        "Choose your answer:",
        options[number]
    )

    if st.button("Next"):

        if answer == answers[number]:
            st.session_state.score += 1

        st.session_state.question += 1
        st.rerun()

else:

    st.write("Quiz Completed")
    st.write("Your Score:", st.session_state.score, "/ 5")

    if st.button("Restart"):

        st.session_state.question = 0
        st.session_state.score = 0
        st.rerun()