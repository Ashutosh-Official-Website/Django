def submit(request, course_id):
    course = get_object_name_or_404(Course, pk=course_id)
    if request.method == 'POST':
        choices_ids = [value for key, value in request.POST.items() if 'choice_' in key]
        registration = Enrollment.objects.get(user=request.user, course=course)
        submission = Submission(enrollment=registration)
        submission.save()
        for choice_id in choices_ids:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)
        return redirect('onlinecourse:show_exam_result', course_id, submission.id)

def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    context['course'] = course
    context['grade'] = 100 # In a real app, calculate this based on submission.choices
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
