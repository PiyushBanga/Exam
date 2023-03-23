import csv


def create_options_csv():

    header = ["Question", "Option A", "Option B",
              "Option C", "Option D"]
    data = [
        ["Who is the second fastest batsman to reach 25 hundreds in Tests ?",
            "[Sachin Tendulkar]","Alastair Cook","Virat Kohli","Steve Smith"],
        ["What is the capital of France?","London",
            "[Paris]", "Berlin", "Madrid"],
        ["Who painted the famous Mona Lisa portrait?", "Michelangelo",
            "Leonardo da Vinci", "[Vincent van Gogh]", "Pablo Picasso"],
        ["What is the largest planet in our solar system?",
            "Venus", "Jupiter", "Mars", "[Saturn]"],
        ["What is the capital of India?", "[Delhi]",
            "Mumbai", "Bangalore", "New Delhi"],]

    with open("mcq_questions.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


def select_method():
    select = int(input("""Chosse what you want to do:
[1] LOGIN
[2] SIGN UP
"""))
    if select == 1:
        login()
    elif select == 2:
        sign_up()
    else:
        print('Choose a valid operation')


def login():
    username = str(input('username: '))
    password = str(input('Password: '))

    with open('user_details.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        found_user = False
        for row in csv_reader:
            if row['username'] == username:
                found_user = True
                if row['password'] == password:
                    print("Login successful!")
                    print("Welcome to the exam!")
                    take_exam('mcq_questions.csv')
                    return
                else:
                    while True:
                        password = input("Wrong Password. Please enter correct password: ")
                        if row['password'] == password:
                            print("Login successful!")
                            print("Welcome to the exam!")
                            take_exam('mcq_questions.csv')
                            return
                        else:
                            continue
        if not found_user:
            print("Username not found. Please ask administrator for registration.")
            print('Do you want to sign up? [Yes/No]')
            start_over = str(input())
            if 'y' in start_over:
                sign_up()
            else:
                print('See you next time!')
                exit(0)



def sign_up():
    username = str(input('Username: '))
    password = str(input('Password: '))
    with open('user_details.csv', mode='a', newline='') as csv_file:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({'username': username, 'password': password})

    print("Signup successful!")
    print('Do you want to log in? [Yes/No]')
    start_over = str(input())
    if 'y' in start_over:
        login()
    else:
        print('See you next time!')
        exit(0)



def take_exam(file_name):
    with open("mcq_questions.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        score = 0
        total_questions = 0
        for row in reader:
            print(row[0])
            for i in range(1, 5):
                option = row[i]
                if option.startswith("[") and option.endswith("]"):
                    option = option[1:-1]
                print(f"{chr(64 + i)}. {option}")
            answer = input("Enter your answer (A/B/C/D): ")
            correct_option = None
            for i in range(1, 5):
                if row[i].startswith("[") and row[i].endswith("]"):
                    correct_option = chr(64 + i)
                    break
            if answer.upper() == correct_option:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
            total_questions += 1
            print()
    print(f"You scored {score}/{total_questions} ({(score/total_questions)*100:.2f}%).")
    percentage_score = score / total_questions * 100
    if percentage_score >= 50:
        result_message = 'Congratulations, you passed!'
    else:
        result_message = 'Sorry, you failed.'
    print(f'\nYour result: {percentage_score }% {result_message}')


select_method()
