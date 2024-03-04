
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


# def record_current_answer(answer, current_question_id, session):
#     '''
#     Validates and stores the answer for the current question to django session.
#     '''
#     return True, ""

def record_current_answer(answer, current_question_id, session):
    '''
    Validates and stores the answer for the current question to django session.
    '''
    # Check if the answer is empty or None
    if not answer:
        return False, "Please provide an answer."

    # You can implement additional validation logic based on your requirements

    # Store the answer in the session
    if "user_answers" not in session:
        session["user_answers"] = {}

    session["user_answers"][current_question_id] = answer
    session.save()

    return True, ""


# def get_next_question(current_question_id):
#     '''
#     Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
#     '''

#     return "dummy question", -1




def get_next_question(current_question_id):
    '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''

    # Assuming PYTHON_QUESTION_LIST is a list of questions
    if current_question_id < len(PYTHON_QUESTION_LIST) - 1:
        next_question_id = current_question_id + 1
        return PYTHON_QUESTION_LIST[next_question_id], next_question_id
    else:
        return None, -1
    

def generate_final_response(session):
    '''
    Creates a final result message including a score based on the answers
    by the user for questions in the PYTHON_QUESTION_LIST.
    '''

    # Assuming you have a scoring mechanism based on user answers
    score = calculate_score(session.get("answers", {}))
    
    return f"Thank you for answering the questions. Your score is {score}."

def calculate_score(answers):
    '''
    Example scoring mechanism based on the user's answers.
    You can customize this based on your requirements.
    '''

    score = 0
    for question_id, answer in answers.items():
        # Add scoring logic based on answers
        # For example, if the answer is correct, increment the score
        if answer == PYTHON_QUESTION_LIST[question_id]["correct_answer"]:
            score += 1

    return score









# def generate_final_response(session):
#     '''
#     Creates a final result message including a score based on the answers
#     by the user for questions in the PYTHON_QUESTION_LIST.
#     '''

#     return "dummy result"
