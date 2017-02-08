from sqlwhat.test_exercise import test_exercise as te

def test_pass():
    result = [['id', 'name'], [1, 'greg']]
    sct_payload = te(
        sct = "Ex().check_result()",
        student_code = "SELECT * FROM company",
        solution_code = "SELECT * FROM company",
        pre_exercise_code = "",
        student_conn = None,
        solution_conn = None,
        student_result = result,
        solution_result = result,
        ex_type="NormalExercise",
        error=[]
        )

    assert sct_payload.get('correct') is True

def test_fail():
    sol_result = [['id', 'name'], [1, 'greg']]
    stu_result = [['id', 'name']]
    sct_payload = te(
        sct = "Ex().check_result()",
        student_code = "SELECT * FROM company",
        solution_code = "SELECT * FROM company",
        pre_exercise_code = "",
        student_conn = None,
        solution_conn = None,
        student_result = stu_result,
        solution_result = sol_result,
        ex_type="NormalExercise",
        error=[]
        )

    assert sct_payload.get('correct') is False
