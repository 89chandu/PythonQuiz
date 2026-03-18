import streamlit as st

st.title("Simple Quiz App")

score = 0

questions = [

    {
        "question":"What is the capital of india ?",
        "options":["Mumbai","Delhi","Kolkata","Chennai"],
        "answer":"Delhi"
    },
      {
        "question":"Which language is used for AI ?",
        "options":["Java","C++","Python","Javascript"],
        "answer":"Python"
    },
      {
        "question":"Techno Skill Kaha hai ?",
        "options":["Balaghat","Bhopal","Dharti","Mars"],
        "answer":"Mars"
    }

]

user_answers = []

for i, q in enumerate(questions):
    st.subheader(q["question"])

    option = st.radio("Choose an option",
                      q["options"],
                      key=q["question"]
                      )
    
    user_answers.append(option)

    if st.button("Submit:Quiz", key=f"submit_{i}"):

        for i in range(len(questions)):
            if user_answers[i] == questions[i]["answer"]:
                score = score + 1

        st.success(f"your score : {score}/{len(questions)}")
