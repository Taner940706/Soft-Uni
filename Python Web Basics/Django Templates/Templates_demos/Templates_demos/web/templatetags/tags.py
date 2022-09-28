from django.template import Library

from Templates_demos.web.views import Student

register = Library()


@register.simple_tag(name='student_info')
def student_info(student: Student):
    return f'Hello, my name is {student.name} and Im {student.age} year old!!!'


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'urls': args,
    }

    return context
