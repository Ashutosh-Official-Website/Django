def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    context['course'] = course
    
    total_score = 0
    # Calculate score using the model method
    for question in course.question_set.all():
        selected_ids = submission.choices.filter(question=question).values_list('id', flat=True)
        if question.is_get_score(selected_ids):
            total_score += question.grade
            
    context['grade'] = total_score
    context['submission'] = submission
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
