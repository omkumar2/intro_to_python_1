
def filter_students(data: dict, criteria: str) -> set:
    '''
    Takes a dictionary where keys are student names and values are lists of scores, filters names based on the given criteria
     - "excellent" - average score >= 85.
     - "good" - average score >= 50 and < 85.
     - "all_pass" - all scores >= 50.
     - "balanced" - difference between min and max is <= 10.
   
    Args:
        scores(dict)  : keys are student names and values are lists of scores

    Returns:
        set: Set of roll numbers matching the criteria
    '''
    
    # for key in data:
    #     if criteria >= 85:
    #         return "excellent"
    #     elif criteria >= 50 and criteria < 85:
    #         return "good"
    #     elif criteria >= 50:
    #         return "all_pass"
    #     elif criteria <= 10:
    #         return "balanced"
        
    # return filter_students(key,end ='')
        
        
        
    filtered_students = set()

    for student, scores in data.items():
        avg_score = sum(scores) / len(scores)
        min_score = min(scores)
        max_score = max(scores)

        if criteria == "excellent" and avg_score >= 85:
            filtered_students.add(student)
        elif criteria == "good" and 50 <= avg_score < 85:
            filtered_students.add(student)
        elif criteria == "all_pass" and all(score >= 50 for score in scores):
            filtered_students.add(student)
        elif criteria == "balanced" and (max_score - min_score) <= 10:
            filtered_students.add(student)

    return filtered_students


    result = set()
    
    for student, scores in data.items():
        if not scores:  # Handle empty score lists
            continue
            
        avg_score = sum(scores) / len(scores)
        min_score = min(scores)
        max_score = max(scores)
        
        if criteria == "excellent" and avg_score >= 85:
            result.add(student)
        elif criteria == "good" and 50 <= avg_score < 85:
            result.add(student)
        elif criteria == "all_pass" and all(score >= 50 for score in scores):
            result.add(student)
        elif criteria == "balanced" and (max_score - min_score) <= 10:
            result.add(student)
            
    return result


