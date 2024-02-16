questions = [
    ["Which of the following is NOT a programming language?", "Python", "HTML", "MySQL", "JPEG", 4],
    ["What does CPU stand for in computing jargon?", " Computer Processing Unit", "Central Processing Unit", "Computer Programming Unit", " Central Programming Unit", 1],
    ["Which of the following is an example of secondary storage device?", "RAM", "SSD", "CPU", "GPU", 1],
    ["What does HTML stand for in web development?", "Hyper Text Markup Language", "High Tech Multi Language", "Hyperlink Text Manipulation Language", "Home Tool Markup Language", 1],
    ["What is the purpose of a firewall in computer networking?", "To protect against physical damage", "To prevent unauthorized access to or from a private network", "To improve internet speed", "To enhance graphics rendering", 2],
    ["What is the full form of SSD in computer hardware?", "Solid State Drive", "Software System Directory", "Sequential System Development", "System Software Deployment", 1],
    ["Which programming language is often used for web development?", "Python", "Java", "C++", "JavaScript", 4],
    ["What is the function of an operating system?", "To control hardware resources", "To develop software applications", "To design computer networks", "To write code for websites", 1],
    ["What is the binary equivalent of the decimal number 10?", "1010", "1100", "1001", "1110", 1],
    ["What is the main purpose of a database management system (DBMS)?", "To manage and organize data", "To design graphics", "To create websites", "To write programs", 1],
    ["Which component of a computer is responsible for temporarily storing data?", "RAM", "CPU", "SSD", "GPU", 1],
    ["What does GPU stand for in computing?", "Graphics Processing Unit", "General Processing Unit", "Graphical Performance Utility", "Graphical Power Unit", 1],
    ["What programming language is often used for scientific computing and data analysis?", "Python", "C#", "Ruby", "Swift", 1],
    ["What does DNS stand for in the context of computer networks?", "Domain Name System", "Dynamic Network System", "Data Network Security", "Digital Network Service", 1],
    ["What is the purpose of a compiler in programming?", "To translate high-level programming languages to machine code", "To manage databases", "To create graphical user interfaces", "To optimize internet speed", 1],
    ["Which of the following is NOT an example of a web browser?", "Google Chrome", "Firefox", "Microsoft Word", "Safari", 3]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0

for i in range(0,len(questions)):
    question = questions[i]
    print(f"\t Question for Rs.{levels[i]}")
    print(f"Question : {question[0]}")
    print(f"a. {question[1]}               b.{question[2]} ")
    print(f"c. {question[3]}               d.{question[4]} ")
    reply = int(input("Enter the answer between (1-4) "))
    if reply == question[-1]:
        print(f"Correct answer! You have won Rs.{levels[i]}")
        money = levels[i]
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer.")
        break
print("Your take home money is {money}")
