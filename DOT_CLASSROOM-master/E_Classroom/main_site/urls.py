
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/', views.login_page, name='login'),
    path('login/forget-password', views.forget_password, name='login'),
    path('student-login-url/forget-password', views.forget_password, name='login'),
    path( 'register_teacher/forget-password', views.forget_password, name='_login_'),
    path('login/submit-email', views.submit_email, name='login'),
    path('student-login-url', views.student_login, name='student_login'),
    path('student-login-url/', views.student_login, name='student_login'),
    path('/student-login-url/', views.student_login, name='student_login'),
    path('teacher-login-url', views.teacher_login, name='teacher_login'),
    path('teacher-registration-url',views.teacher_registration, name='teacher_registration'),
    path('send_otp',views.send_otp_pre_page,name='send_otp'),
    path('verify_otp',views.verify,name='verify'),
    path('register_teacher/',views.register_teacher,name='register'),
    path('explore-url',views.explore_url,name='explore'),
    path('explore', views.explore, name='rexplore'),

    path('delete-url',views.handle_delete_request,name='delete'),
    path('create_user',views.create_user,name='create_user'),
    path('teacher-create', views.teacher_create, name='teacher-create'),
    path('create_classroom',views.create_classroom,name='create_classroom'),
    path('create_class',views.create_class,name='create_class'),
    path('Login_page',views.login_page,name='Login_page'),
    path('student-login-url/Login_page', views.login_page, name='Login_page'),
    path('student-login-url/see-document',views.see_document , name='see-document'),
    path('see-document', views.see_document, name='see-document'),
    path('student-login-url/veiw-document', views.view_document, name='view-document'),
    path('veiw-document', views.view_document, name='view-document'),
    path('take_test',views.take_test,name='take_test'),
    path('upload_file',views.upload_file,name='upload_file'),
    path('give_data_to_tab',views.give_data_to_tab,name='give_data_to_tab'),
    path('give_data_to_tab1',views.give_data_to_tab1,name='give_data_to_tab1'),
    path('student-login-url/take_test_student',views.take_test_student,name='take_test_student'),
    path('take_test_student', views.take_test_student, name='take_test_student'),
    path('your-profile-photo/',views.your_profile_photo,name='profile_photo'),
    path('view_answers',views.view_answers,name='view_answers'),
    path('next_page',views.next_page,name='next_page'),
    path('next_page1',views.next_page1,name='next_page1'),
    path('filter_data',views.filter_data,name='filter_data'),
    path('filter_data1', views.filter_data1, name='filter_data1'),
    path('student-login-url/get_q',views.get_q,name='get_q'),
    path('answers',views.answers,name='answers'),
    path('give_marks',views.give_marks,name='give_marks'),
    path('submitted_answers',views.submitted_answers,name='submitted_answers'),
    path('alternate',views.alternate,name='alternate'),
    path('student-login-url/alternate', views.alternate, name='alternate'),
    path('my_url',views.my_url,name='my_url'),


    path('student-login-url/my_url', views.my_url, name='my_url'),
    path('run_py',views.run_py,name='run_py'),

    path('student-login-url/run_py', views.run_py, name='run_py'),

               path('run_sql', views.run_sql, name='run_sql'),

    path('student-login-url/run_sql', views.run_sql, name='run_sql'),
    path('run_R', views.run_R, name='run_R'),
    path('student-login-url/run_R',views.run_R,name='run_R'),
    path('new_alternate_question_py',views.new_alternate_question,name='new_alternate_question_py'),


    path( 'student-login-url/new_alternate_question_py', views.new_alternate_question, name='new_alternate_question_py'),

])
