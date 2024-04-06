import random
import io
import sys
from django.http import HttpRequest
from PIL import Image
import json
from io import BytesIO
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from django.templatetags.static import static
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import pandas as pd
import os

from django.http import JsonResponse
import base64
def index(request):
    return render(request,"main_site/first_page.html",{})

def login_page(request):
    return render(request, 'main_site/second_page.html',{})

def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        roll_number = request.POST.get('roll_number')
        #########################################################################
        ###   Check if the students email is present in the table and then     ##
        ###   check whether the email and  the roll number is same             ##
        #########################################################################
        print("Student Email:", email)
        print("Student Roll Number:", roll_number)
        data = {
            'Class Name': ['BSC22DS', 'BSC22DS', 'BSC22DS'],
            'Subject Name': ['Data Warehouse and Data Management', 'Internet of things', 'Deep Learning']
        }

        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Convert DataFrame to HTML table
        html_table = df.to_html(index=False)
        return render(request, 'main_site/ninthpage.html', {"email":email,"roll_number":roll_number, "class_data": html_table})


def teacher_login(request):
    if request.method == 'POST':



        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Teacher Username:", username)
        print("Teacher Password:", password)

        # Get the teacher's email from wherever it's coming from
        email =username # Example email, replace with actual email

        #########################################################################
        ########   Here we check if the username password is same or not  #######
        #########################################################################
        ##############################################################################################
        ########   also need to find all classes of the teacher and convert them to html table #######
        ##############################################################################################

        data = {
            'Class Name': ['BSC22DS', 'BSC23DS', 'PG22DS-Jan'],
            'Subject Name': ['Data Warehouse and Data  Management ', 'SQL', 'Introduction to Operating System']
        }

        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Convert DataFrame to HTML table
        html_table = df.to_html(index=False)

        # Render the template with data
        return render(request, "main_site/sixth_page.html", {"email": email, "class_data": html_table})

def forget_password(request):
    return render(request,"main_site/forget_password_page.html",{})

def submit_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print("Email:", email)
        return render(request, 'main_site/second_page.html', {})


def teacher_registration(request):
    return render(request,"main_site/third_page.html",{})

def send_otp_pre_page(request):
    if request.method == 'POST':
        email = request.POST.get('name')
        return render(request, "main_site/forth_page.html", {'email': email})



def verify(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        entered_otp = request.POST.get('digit1') + request.POST.get('digit2') + request.POST.get(
            'digit3') + request.POST.get('digit4')

        #########################################################################
        ########   Here we check if the entered otp i correct or not   ##########
        #########################################################################
        print(f'The entered otp is - {entered_otp} ')
        print(f'entered email is - {email}')
        return render(request, "main_site/fifth_page.html", {'email': email})


def register_teacher(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'email-{email}')
        print(f'username-{username}')
        print(f'password-{password}')
        #########################################################################
        ########   Here we create new teacher users                    ##########
        #########################################################################
        return render(request, "main_site/second_page.html", {'email': email})


@csrf_exempt
def handle_delete_request(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        email = data.get('email')
        row_data = data.getlist('data[]')
        print("Email:", email)
        print("Row data:", row_data)
        data = {
            'Class Name': ['Class x', 'Class y', 'Class z'],
            'Subject Name': ['physics', 'chem', 'Bio']
        }

        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Convert DataFrame to HTML table
        html_table = df.to_html(index=False)

        # Render the template with data
        return render(request, "main_site/sixth_page.html", {"email": email, "class_data": html_table})

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})

def explore_url(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        email = data.get('email')
        row_data = data.getlist('data[]')
        print("Email:", email)
        print("Row data:", row_data)
        teacher_class=row_data[0]
        teacher_sub=row_data[1]

        return render(request, "main_site/seventh_page.html", {"email": email, "teacher_class":teacher_class,"teacher_sub":teacher_sub})


def view_answers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('This is request- ',data)
        # Extract data sent in the request
        email = data.get('email')
        roll_no = data.get('roll_no')
        attentionScore = data.get('attentionScore')
        watchtime= data.get('watchTime')
        document_name= data.get('document_name')
        upload_time= data.get('upload_time')
        upload_date= data.get('upload_date')
        attempt_time= data.get('attempt_time')
        attempt_date= data.get('attempt_date')
        row_data = data.get('rowData')
        teacher_class=data.get('teacher_class')
        teacher_sub=data.get('teacher_sub')
        redirect_url = 'next_page'

        response_data = {
            'email': email,
            'teacher_class': teacher_class,
            'teacher_sub': teacher_sub,
            'row_data': row_data,
            'redirectUrl': redirect_url,
            'roll_no':roll_no,
        'attentionScore':attentionScore,
        'watchtime':watchtime,
        'document_name':document_name,
        'upload_time':upload_time,
        'upload_date':upload_date,
        'attempt_time':attempt_time,
        'attempt_date':attempt_date,
        }
        return JsonResponse(response_data)


def next_page1(request:HttpRequest):
    email = request.GET.get('email')
    teacher_class = request.GET.get('teacher_class')
    teacher_sub = request.GET.get('teacher_sub')
    row_data = request.GET.get('row_data').split(',')  # Splitting row_data into a list
    document_name = row_data[0]
    AVG_watchtime = row_data[1]
    AVG_attention_score = row_data[2]
    AVGstudent_watch_time = row_data[3]
    doc_name = row_data[4]
    doc_upload_time = row_data[5]
    doc_upload_date = row_data[6]
    print(row_data,'Hare krishna')
    barData={
        'OLTP':{
            'Applications of OLTP':75,
            'OLTP Methods':25,
        },
        'OLAP':
            {
                'Applications of OLAP':35,
            'OLAP Methods':5,
            }
    }
    return render(request, "main_site/fifteenth_page.html", {"email": email, "teacher_class": teacher_class,
                                                         'teacher_sub':teacher_sub,
                                                          'document_name':document_name,
                                                           'AVG_watchtime':AVG_watchtime,
                                                        'AVG_attention_score':AVG_attention_score,
                                                        'AVGstudent_watch_time':AVGstudent_watch_time,
                                                           'doc_name':doc_name,
                                                             'doc_upload_time':doc_upload_time,
                                                             'doc_upload_date':doc_upload_date,
                                                             'barData':barData
                                                         })


def next_page(request: HttpRequest):
    # Extracting parameters from the request
    email = request.GET.get('email')
    teacher_class = request.GET.get('teacher_class')
    teacher_sub = request.GET.get('teacher_sub')
    row_data = request.GET.get('row_data').split(',')  # Splitting row_data into a list
    print(type(row_data))  # This will show you the type of row_data, it should be a list

    # Extracting individual data from row_data
    student_email = row_data[0]
    student_roll_number = row_data[1]
    student_attention_score = row_data[2]
    student_watch_time = row_data[3]
    doc_name = row_data[4]
    doc_upload_time = row_data[5]
    doc_upload_date = row_data[6]
    student_attempt_time = row_data[7]
    student_attempt_date = row_data[8]

    questions = {
        'What is data warehouse?': ["Dataware house is a large collection of Data for analytical and transactional purpose in an organization",1,3],
        "What is clustering in OLAP": ["It is a method of Aggregating Data in a DATA WAREHOUSE for analytical purposes.",1,5],
        "what is OLAP": ["OLAP is online analytical processing",1,5]
    }

    return render(request, "main_site/fourteenth_page.html", {
        "email": email,
        "teacher_class": teacher_class,
        "teacher_sub": teacher_sub,
        "row_data": row_data,
        'student_email': student_email,
        'student_roll_number': student_roll_number,
        'student_attention_score': student_attention_score,
        'student_watch_time': student_watch_time,
        'doc_name': doc_name,
        'doc_upload_time': doc_upload_time,
        'doc_upload_date': doc_upload_date,
        'student_attempt_time': student_attempt_time,
        'student_attempt_date': student_attempt_date,
        'questions': questions,
    })


def create_user(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        df = pd.read_excel(uploaded_file)
        print(df)
        return HttpResponse('Hare Krishna Prabhu')

def teacher_create(request):
        print(request)
        email = request.GET.get('email', '')
        teacher_class = request.GET.get('teacher_class', '')
        teacher_subject = request.GET.get('teacher_subject', '')
        print('email: ',email)
        data = {
            'Class Name': ['Hare Krishna', 'Class y', 'Class z'],
            'Subject Name': ['Jai Shree Krishna', 'chem', 'Bio']
        }

        df = pd.DataFrame(data)

        html_table = df.to_html(index=False)

        return render(request, "main_site/sixth_page.html", {"email": email, "class_data": html_table})



def create_classroom(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        return render(request, "main_site/eighth_page.html", {"email": email})
def create_class(request):
    if request.method == 'POST':
        # Get the values from the form
        email = request.POST.get('email', '')
        class_name = request.POST.get('className', '')
        subject_name = request.POST.get('subjectName', '')

        # Print the values (you can replace print with any desired action)
        print("Class Name:", class_name)
        print("Subject Name:", subject_name)
        # Sample data for demonstration
        data = {
            'Class Name': ['Hare Krishna', 'Jai shree Ram', 'Class z'],
            'Subject Name': ['Jai Shree Krishna', 'Jai Ayodhya Dham', 'Bio']
        }

        df = pd.DataFrame(data)

        html_table = df.to_html(index=False)
        # You can also return an HTTP response
        return render(request, "main_site/sixth_page.html", {"email": email, "class_data": html_table})


def see_document(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        row_data = request.POST.getlist('data[]')
        print("Email:", email)
        print("Row data:", row_data)
        subject=row_data[0]
        classroom=row_data[1]

        data = {
            'name': ['deep learning introduction', 'statistics', 'Class z'],
            'document': ['attention_is_all_you_need.pdf', 'Normalization Lecture-1', 'Bio']
        }
        df = pd.DataFrame(data)
        image_filename = "yash.jpeg"
        image_path = f"profile_photos/{image_filename}"
        TEXT= "Leading the class with the highest attention score for uploaded study materials and outstanding performance in mock tests."
        html_table = df.to_html(index=False)
        student_email='yashpadale108@gmail.com'
        text=f'{student_email}'


        data = [
            {"image_path": "profile_photos/yash.jpeg", "text": "Yash"},
            {"image_path": "profile_photos/ritesh.jpeg", "text": "ritesh"},
            {"image_path": "profile_photos/krishna.jpeg", "text": "krishna"},

            # Add more data as needed
        ]
        return render(request, "main_site/tenth_page.html", {"email": email,
        "classroom":classroom,"subject":subject, "class_data": html_table,
        'image_path':image_path,'TEXT':TEXT,'text':text, 'data': data})



def view_document(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        row_data = request.POST.getlist('data[]')
        fs = FileSystemStorage()
        print('Hare KRishna Prabhu', row_data)
        if row_data[1]=='attention_is_all_you_need.pdf':
            filename = "C:staticfiles/pdf/attention_is_all_you_need.pdf"
            with fs.open(filename) as pdf:
                pdf_content = base64.b64encode(pdf.read()).decode('utf-8')
            return render(request, "main_site/eleventh_page.html", {"email": email,"filename":filename, "pdf_content": pdf_content})
        else:
            video_path="C:staticfiles/videos/v4.mp4"
            with open(video_path, 'rb') as f:
                video = base64.b64encode(f.read()).decode('utf-8')
            return render(request, "main_site/twelth_page.html", {"email": email, "video": video})




def upload_file(request):
    if request.method == 'POST':
        # Get the uploaded files
        uploaded_files = request.FILES.getlist('file')

        # Print the file names
        for uploaded_file in uploaded_files:
            print("Uploaded File Name:", uploaded_file.name)

        # Get the email, teacherClass, teacherSubject, and selectedDate from the request
        email = request.POST.get('email')
        teacher_class = request.POST.get('teacherClass')
        teacher_sub = request.POST.get('teacherSubject')
        selected_date = request.POST.get('selectedDate')
        question = request.POST.get('question')

        # Get the marker count values
        one_marker_count = request.POST.get('oneMarkerCount')
        two_marker_count = request.POST.get('twoMarkerCount')
        three_marker_count = request.POST.get('threeMarkerCount')
        five_marker_count = request.POST.get('fiveMarkerCount')

        # Print the email, teacherClass, teacherSubject, selectedDate, and marker counts
        print("Email:", email)
        print("Class:", teacher_class)
        print("Subject:", teacher_sub)
        print("Date:", selected_date)
        print("question",question)
        print("Number of One Markers:", one_marker_count)
        print("Number of Two Markers:", two_marker_count)
        print("Number of Three Markers:", three_marker_count)
        print("Number of Five Markers:", five_marker_count)

        # Add your logic to process the uploaded files and marker count values

        # Return a response
        return HttpResponse("Files uploaded successfully!")
    else:
        return HttpResponse("Only POST requests are allowed.")


def give_data_to_tab(request):
    # Get the tab name, email, teacher_class, and teacher_sub from the request
    tab_name = request.GET.get('tab')
    email = request.GET.get('email')
    teacher_class = request.GET.get('teacher_class')
    teacher_sub = request.GET.get('teacher_sub')

    # Print the received data
    print("Tab Name:", tab_name)
    print("Email:", email)
    print("Teacher Class:", teacher_class)
    print("Teacher Subject:", teacher_sub)

    # Add your logic here to process the received data

    # Return a response
    if tab_name=='Tab2':
        data = {
            'document_name': ['deep learning introduction', 'statistics', 'Class z'],
            'Avg watch time of students': ['25 hrs', '10 hrs', '15 hrs'],
            'Attention Score':[1,2,3],
            'Test result':[10,20000,30],
            'upload_time':['10:30','12:00','1:00'],
            'upload_date':['12/12/2012','11/11/2025','9/9/2009']

        }
        df = pd.DataFrame(data)

        html_table = df.to_html(index=False)
        return HttpResponse(html_table, content_type='text/html')
    if tab_name == 'Tab3':
        data = {
            'email': ['yash', 'krishna', 'ritesh'],
            'roll_number': [114, 57, 87],
            'attention_score': [10, 15, 17],
            'watch time': [19, 25, 37],
            'document_name': ['attention_is_all_you_need.pdf', 'xyz.mp4', 'v1.mp4'],
            'upload_time': ['10:30', '12:00', '1:00'],
            'upload_date': ['12/12/2012', '11/11/2025', '9/9/2009'],
            'attempt_time': ['10:30', '12:00', '1:00'],
            'attempt_date': ['12/12/2012', '11/11/2025', '9/9/2009']
        }

        df = pd.DataFrame(data)

        html_table = df.to_html(index=False, escape=False)
        return HttpResponse(html_table, content_type='text/html')
    if tab_name == 'Tab4':
        data = {
            'email': ['yash', 'krishna', 'rakesh'],
            'roll_number': [114, 57, 87],
            'attention_score': [10, 15, 17],
            'watch time': [19, 25, 37],
            'document_name': ['attention_is_all_you_need.pdf', 'xyz.mp4', 'v1.mp4'],
            'upload_time': ['10:30', '12:00', '1:00'],
            'upload_date': ['12/12/2012', '11/11/2025', '9/9/2009'],
            'attempt_time': ['10:30', '12:00', '1:00'],
            'attempt_date': ['12/12/2012', '11/11/2025', '9/9/2009']
        }

        df = pd.DataFrame(data)

        html_table = df.to_html(index=False, escape=False)
        return HttpResponse(html_table, content_type='text/html')

def give_data_to_tab1(request):
    if request.method == 'GET':
        tab_name = request.GET.get('tab', '')
        email = request.GET.get('email', '')
        roll_number = request.GET.get('roll_number', '')
        print(f'tab_name- {tab_name}')
        print(f'email- {email}')
        print(f'roll_number- {roll_number}')
        if tab_name == 'Tab2':
            data = {
                'document_name': ['deep learning introduction', 'statistics', 'Class z'],
                'teacher_name': ['xyz', 'abc', 'defz'],
            'submission_date': ['12/12/2012', '11/11/2025', '9/9/2009']


            }
            df = pd.DataFrame(data)

            html_table = df.to_html(index=False)
            return HttpResponse(html_table, content_type='text/html')
        if tab_name == 'Tab3':

            image = static("C:/Users/Yash/Downloads/DOT_CLASSROOM-master/DOT_CLASSROOM-master/E_Classroom/main_site/static/profile_photos/yash.jpeg")
            Average_score=10

            data = f"""        
<div class="card">
    <div class="content">
        <img src="{image}" alt="Image" class="image circular">
        <button onclick="changePhoto()">Change Photo</button> <!-- Add this button for changing the photo -->
        <input type="file" id="fileInput_image" style="display: none;" accept="image/*"> <!-- Hidden file input element -->
    </div>
    <div>
        <div class="text">
            <h1>Email ID - <span id="emailValue">{ email }</span></h1> 
            <h1>roll_number - {roll_number}</h1> 
            <h1>Average score- {Average_score}</h1> 
            <h1>Average watch time- {Average_score}</h1> 
        </div>  
    </div>
</div>
            """
            return HttpResponse(data, content_type='text/html')




def your_profile_photo(request):
    if request.method == 'POST':
        # Get the uploaded file and email from the request
        uploaded_file = request.FILES.get('file')
        email = request.POST.get('email')

        save_dir = "C:/Users/Yash/Downloads/DOT_CLASSROOM-master/DOT_CLASSROOM-master/E_Classroom/main_site/static/profile_photos"

        if uploaded_file:
            file_name = uploaded_file.name
            file_path = os.path.join(save_dir, file_name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Print email and file name
            print(f'Email: {email}')
            print(f'File Name: {file_name}')

            image_url = f"/static/profile_photos/{file_name}"  # Assuming the file will be served from this URL
            return JsonResponse({'image_url': image_url, 'save_path': save_dir}, status=200)
        else:
            return JsonResponse({'error': 'No file provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)







def filter_data(request):
    if request.method == 'GET':
        print(request)
        # Retrieve the search query and hidden input values from the request
        email = request.GET.get('email')
        teacher_class = request.GET.get('teacher_class')
        teacher_sub = request.GET.get('teacher_sub')
        search_value = request.GET.get('search')
        print('search_value-',search_value)
        # Perform search operation based on the search query and other parameters
        # This is where you would implement your search logic
        # For example, you might query your database based on the search query and return the results

        # For demonstration purposes, let's assume you have some search results
        data = {
            'email': ['John', 'Alice', 'Bob'],
            'roll_number': [101, 202, 303],
            'attention_score': [20, 25, 30],
            'watch time': [30, 40, 50],
            'document_name': ['document1.pdf', 'document2.pdf', 'document3.pdf'],
            'upload_time': ['9:00', '10:30', '11:45'],
            'upload_date': ['01/05/2023', '02/10/2023', '03/15/2023'],
            'attempt_time': ['9:30', '11:00', '12:15'],
            'attempt_date': ['01/05/2023', '02/10/2023', '03/15/2023']
        }

        df = pd.DataFrame(data)

        html_table = df.to_html(index=False, escape=False)
        return HttpResponse(html_table, content_type='text/html')
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid request method'})


def filter_data1(request):
    if request.method == 'GET':
        print(request)
        # Retrieve the search query and hidden input values from the request
        email = request.GET.get('email')
        teacher_class = request.GET.get('teacher_class')
        teacher_sub = request.GET.get('teacher_sub')
        search_value = request.GET.get('search')
        print('search_value-',search_value)
        print('HARE KRISHNA')

        # For demonstration purposes, let's assume you have some search results
        data = {
            'email': ['Alice', 'Bob', 'Charlie'],
            'roll_number': [101, 102, 103],
            'attention_score': [20, 25, 30],
            'watch time': [30, 35, 40],
            'document_name': ['abc.pdf', 'def.mp4', 'ghi.mp4'],
            'upload_time': ['10:30', '12:00', '1:00'],
            'upload_date': ['12/12/2021', '11/11/2022', '10/10/2023'],
            'attempt_time': ['10:30', '12:00', '1:00'],
            'attempt_date': ['12/12/2021', '11/11/2022', '10/10/2023']
        }

        df = pd.DataFrame(data)

        html_table = df.to_html(index=False, escape=False)
        return HttpResponse(html_table, content_type='text/html')
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid request method'})


def get_q(request):
    email = request.POST.get('email')
    print(request)
    document_name = request.POST.get('documentName')
    teacher_name = request.POST.get('teacherName')
    number_of_questions = request.POST.get('numberOfQuestions')
    print(email,document_name,teacher_name, number_of_questions)
    questions = {
        'OLTP': {
            '1': {
                'question': 'What does OLTP stand for?',
            },
            '3': {
                'question': 'What is the primary purpose of OLTP systems?',
            },
            '5': {
                'question': 'Give an example of an OLTP application.',
            }
        },
        'OLAP': {
            '1': {
                'question': 'What does OLAP stand for?',
            },
            '3': {
                'question': 'What is the primary purpose of OLAP systems?',
            },
            '5': {
                'question': 'Give an example of an OLAP tool.',
            }
        }
    }

    return JsonResponse({'status': 'success','questions':questions})





def take_test(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        filename = request.POST.get('filename')
        print('This is email->')
        print("Email:", email)
        print('This is filename->')
        print("Filename:", filename)
        return HttpResponse(f'{email}- {filename}- Hare Krishna')


def answers(request):
    if request.method == 'POST':
        # Assuming the data is sent as JSON in the request body
        data = request.POST.get('dataToSubmit')
        # Handle the data as needed
        # For example, you can save it to the database or perform any other operations
        print(data)
        print(data)
        print(data)

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Data received successfully'})
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'}, status=405)


def give_marks(request):
    if request.method == 'POST':
        # Extract query parameters from the request
        data = json.loads(request.body)
        print('This is data ->', data)
        email = data['email']
        teacher_class = data['teacherClass']
        teacher_sub = data['teacherSub']
        redirect_url = 'explore'  # Replace with your desired redirect URL
        additional_data = {'email': email, 'teacher_class': teacher_class,
                           'teacher_sub': teacher_sub}  # Additional data to be sent
        return JsonResponse(
            {'message': 'Data received successfully', 'redirect_url': redirect_url, 'additional_data': additional_data})
    else:
        # Return a method not allowed response for other request methods
        return HttpResponse(status=405)


def explore(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        teacher_class = request.GET.get('teacher_class')
        teacher_sub = request.GET.get('teacher_sub')
        return render(request, "main_site/seventh_page.html", {"email": email, "teacher_class": teacher_class, "teacher_sub": teacher_sub})
    else:
        return HttpResponse(status=405)


def take_test_student(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        data = request.POST.getlist('data[]')
        document_name = data[0]
        teacher_name = data[1]
        roll_number = request.POST.get('roll_number')  # Retrieving roll number from the POST data
        print('This is email->')
        print("Email:", email)
        print('This is data->')
        print("Data:", data)
        print('Hare Krishna')
        print(roll_number)
        questions = [
            {'category': 'OLTP', 'question': 'HOW TO create a database', 'type': 'sql'},

            {'category': 'OLTP', 'question': 'HOW TO create a variable in R', 'type': 'R'},
            {'category': 'OLTP', 'question': 'HOW TO IMPORT NUMPY','type':'py'},
            {'category': 'OLTP', 'question': 'how to print random number using numpy','type':'py'},
            {'category': 'OLTP', 'question': 'how to create a list of random numbers using numpy','type':'py'},
            {'category': 'OLAP', 'question': 'OLAP stands for Online ___ processing','type':'Fill in the Blanks'},
            {'category': 'OLTP', 'question': 'Python is interpreted language . True or false', 'type': 'T/F'},
            {'category': 'OLAP', 'question': 'What is the primary purpose of OLAP systems?','type':'normal'},
            {'category': 'OLAP', 'question': 'Give an example of an OLAP tool.','type':'normal'},
            {'category': 'OLAP', 'question': 'What is the difference between machine learning and deep learning?.', 'type': 'difference','header1':' machine learning ','header2':'deep learning'}
        ]

        return render(request, "main_site/alter_13.html", {
            "email": email,
            "roll_number":roll_number,
            "document_name": document_name,
            "teacher_name": teacher_name,
            "questions": questions
        })

def submitted_answers(request):
    if request.method == 'POST':
        # Retrieve the raw JSON data from the request body
        data = json.loads(request.body.decode('utf-8'))

        # Process the data as needed
        print(data)

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Answers submitted successfully.'})
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

def alternate(request):
    if request.method == 'POST':
        # Assuming the data is sent as JSON in the request body
        try:
            received_data = json.loads(request.body.decode('utf-8'))
            email = received_data.get('email')
            document_name = received_data.get('documentName')
            teacher_name = received_data.get('teacherName')
            category = received_data.get('category')

            # Print the received values
            print("Email:", email)
            print("Document Name:", document_name)
            print("Teacher Name:", teacher_name)
            print("Category:", category)

            # Dummy data for demonstration, replace this with your logic to get a new question
            questions = [
                "What is deep learning?",
                "What is the difference between machine learning and deep learning?",
                "What is the name of the test to decide if a computer program is AI or not?",
                "What are the different types of artificial neural networks?",
                "Explain the concept of backpropagation in neural networks.",
                "What are some popular deep learning frameworks?",
                "How does convolutional neural network (CNN) work?",
                "What is recurrent neural network (RNN) and where is it used?",
                "What are some applications of deep learning in computer vision?",
                "What are the challenges faced in training deep learning models?",
                "Explain the concept of overfitting in machine learning.",
                "What is reinforcement learning and how does it work?",
                "What is natural language processing (NLP) and its applications in AI?",
                "Discuss the role of GPUs in accelerating deep learning computations.",
                "What is transfer learning and how is it useful in deep learning?",
                "How do you evaluate the performance of a machine learning model?",
                "Explain the bias-variance tradeoff in machine learning.",
                "What is unsupervised learning and provide examples.",
                "Discuss the ethical implications of AI and machine learning.",
                "What are some limitations of deep learning models?",
                "What is generative adversarial network (GAN) and how does it work?",
                "Explain the concept of regularization in machine learning.",
                "How does attention mechanism work in deep learning models?",
                "What is the role of activation functions in neural networks?",
                "Discuss the importance of data preprocessing in machine learning.",
                "What is the difference between supervised and unsupervised learning?",
                "Explain the concept of dropout regularization in deep learning.",
                "What are some common optimization algorithms used in training neural networks?",
                "How do you handle imbalanced datasets in machine learning?",
                "What are some challenges faced in deploying machine learning models in production?",
                "Discuss the tradeoffs between model complexity and interpretability.",
                "What is the curse of dimensionality and how does it affect machine learning?",
                "What is the role of hyperparameters in machine learning models?",
                "Explain the concept of ensemble learning and its advantages.",
                "What is the role of activation functions in neural networks?",
                "Discuss the concept of feature engineering in machine learning.",
                "How do you handle missing data in machine learning datasets?",
                "What are some techniques for reducing model overfitting?",
                "Discuss the role of cross-validation in model evaluation.",
                "What are some common evaluation metrics used in classification tasks?",
                "Explain the concept of precision and recall in classification.",
                "What is the difference between L1 and L2 regularization?",
                "How do you choose the number of layers and neurons in a neural network?",
                "What is the difference between batch gradient descent and stochastic gradient descent?",
                "Discuss the role of learning rate in training neural networks.",
                "What is the role of normalization techniques in machine learning?",
                "How do you handle categorical variables in machine learning models?",
                "Discuss the bias-variance tradeoff in the context of model selection.",
                "What are some techniques for dimensionality reduction in machine learning?",
                "Explain the concept of feature scaling and its importance.",
                "What are some common preprocessing techniques for text data in NLP?",
                "Discuss the challenges faced in handling time-series data in machine learning.",
                "What are some strategies for handling imbalanced classes in classification tasks?",
                "Explain the concept of kernel methods and provide examples.",
                "What is the role of early stopping in training deep learning models?",
                "How do you interpret the coefficients of a linear regression model?",
                "Discuss the concept of bagging and boosting in ensemble learning.",
                "What are some advantages of using decision trees in machine learning?",
                "How do you handle multicollinearity in regression analysis?",
                "Explain the concept of k-fold cross-validation and its benefits.",
                "What is the role of feature selection in machine learning?",
                "Discuss the concept of grid search and its use in hyperparameter tuning.",
                "What are some techniques for handling outliers in machine learning datasets?",
                "How do you handle non-linear relationships in regression analysis?",
                "Explain the concept of one-hot encoding and its use in categorical data preprocessing.",
                "What are some common distance metrics used in clustering algorithms?",
                "Discuss the concept of silhouette score and its use in evaluating clustering results.",
                "What is the difference between classification and regression?",
                "Explain the bias-variance tradeoff in the context of model complexity.",
                "Discuss the concept of gradient boosting and its advantages.",
                "What are some techniques for dealing with noisy data in machine learning?",
                "How do you choose the appropriate algorithm for a machine learning problem?",
                "Explain the concept of cross-entropy loss and its use in training neural networks.",
                "Discuss the concept of information gain in decision tree learning.",
                "What are some challenges faced in training deep learning models on large datasets?"]
            new_question = random.choice(questions)

            # Return a JSON response with acknowledgment, new question, and category
            return JsonResponse({'message': 'Data received successfully.', 'question': new_question, 'category': category})
        except json.JSONDecodeError as e:
            # Return an error response if the JSON data is not valid
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def my_url(request):
    if request.method == 'POST':
        # Assuming the POST data contains the user responses in a JSON format
        try:
            post_data = json.loads(request.body.decode('utf-8'))
            user_responses = post_data.get('userResponses', None)
            if user_responses:
                print("_userResponses_:", user_responses)
                # You can also process the user responses further as needed
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'User responses not found in POST data'})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format in POST data'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})



def run_py(request):
    if request.method == 'POST':
        try:
            # Load the JSON data from the request body
            data = json.loads(request.body)
            answer_input = data.get('answerInput', None)
            if answer_input:
                # Print the answerInput
                print("Answer Input:", answer_input)

                # Perform any necessary processing here
                output = io.StringIO()
                sys.stdout = output

                # Execute the code
                exec(answer_input)

                # Reset stdout
                sys.stdout = sys.__stdout__

                # Get the output as a string
                output_str = output.getvalue()

                # Return a JSON response with the output
                return JsonResponse({'output': output_str})
            else:
                return JsonResponse({'error': 'Answer input not found in the request'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data in request body'})
        except Exception as e:
            # Return the error message in the response
            return JsonResponse({'output': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})


import json
import pandas as pd
from django.http import JsonResponse
from django.db import connections

def run_sql(request):
    if request.method == 'POST':
        try:
            # Load the JSON data from the request body
            data = json.loads(request.body)
            answer_input = data.get('answerInput', None)
            if answer_input:
                # Specify the database alias
                database_alias = 'sql'  # Change this to your desired database alias

                # Drop all tables in the database
                drop_all_tables(database_alias)

                # Initialize a list to store results
                all_results = []

                # Execute each SQL statement separately
                with connections[database_alias].cursor() as cursor:
                    # Split the input into separate SQL statements
                    sql_statements = answer_input.split(';')

                    for sql_statement in sql_statements:
                        if sql_statement.strip():  # Check if the statement is not empty
                            print("Executing SQL statement:", sql_statement)
                            cursor.execute(sql_statement)
                            # Fetch all results for each statement
                            results = cursor.fetchall()
                            all_results.append(results)

                # Convert results to a list of Pandas DataFrames
                dfs = [pd.DataFrame(results) for results in all_results]

                # Convert DataFrames to HTML tables
                html_tables = [df.to_html(index=False, header=False) for df in dfs]

                # Return a JSON response with the HTML tables
                return JsonResponse({'output': html_tables})
            else:
                return JsonResponse({'output': 'Answer input not found in the request'})
        except json.JSONDecodeError:
            return JsonResponse({'output': 'Invalid JSON data in request body'})
        except Exception as e:
            # Return the error message in the response
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'output': 'Invalid request method'})

def drop_all_tables(database_alias):
    try:
        # Get a cursor for the specified database alias
        with connections[database_alias].cursor() as cursor:
            # Disable foreign key constraints
            cursor.execute("PRAGMA foreign_keys = OFF")

            # Get a list of all tables in the database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            tables = cursor.fetchall()

            # Drop each table in the list
            for table in tables:
                table_name = table[0]
                cursor.execute(f"DROP TABLE IF EXISTS {table_name};")

            # Re-enable foreign key constraints
            cursor.execute("PRAGMA foreign_keys = ON")
    except Exception as e:
        print(f"Error dropping tables: {str(e)}")



import rpy2.robjects as robjects
from django.http import JsonResponse
import json

import rpy2.robjects as robjects

def evaluate_r_code(r_code):
    try:
        # Evaluate the R code
        r = robjects.r(r_code)
        # Return the result as a string
        return (r[0])
    except Exception as e:
        # If there's an error, return the error message as a string
        return (e)

def run_R(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            answer_input = data.get('answerInput', None)
            if answer_input:
                print("Answer Input:", answer_input)
                output = evaluate_r_code(answer_input)
                return JsonResponse({'single': output})
            else:
                return JsonResponse({'error': 'Answer input not found in the request'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data in request body'})
        except Exception as e:
            # Return the error message in the response
            return JsonResponse({'output': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})



def new_alternate_question(request):
    if request.method == 'POST':
        # Assuming the request body contains JSON data
        json_data = json.loads(request.body)

        # Print the parsed JSON data
        print("Parsed JSON data:", json_data)

        # Access specific fields from the JSON data
        email = json_data.get('email')
        roll_number = json_data.get('roll_number')
        text = json_data.get('text')
        questionType=json_data.get('questionType')
        print(questionType)
        # Print specific fields
        print("Email:", email)
        print("Roll number:", roll_number)
        print("Text:", text)

        # Do something with the data

        return JsonResponse({'question': "Who is supreme personality of godhead"})  # Return a JSON response if needed

    # Handle other HTTP methods or return an error response if needed
