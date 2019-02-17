from django.shortcuts import render

#问题汇总图表
def problem_chart(request):
    #按单位和时间统计问题数量
    return render(request, 'manage_problem/problem_chart.html')

