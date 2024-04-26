"""the main module to run and get info about the test result of students, get average score and plot a bar chart"""
import requests
import numpy as np
import matplotlib.pyplot as plt 

def get_student_data(api_url):
    """Get student information from external API"""
    # call the external API to get student information
    response = requests.get(api_url)
    response_json = response.json()
    student_data = response_json["students"]

    # store student roll no and test scores in list and return them
    test_scores = []
    roll_no = []
    for student in student_data:
        test_scores.append(student["score"])
        roll_no.append(student["id"])
    
    return roll_no, test_scores

def plot_scores(roll_no, scores):
    # plot student scores in a bar chart
    plt.bar(roll_no, scores)
    plt.show()


if __name__ == "__main__":
    api_url = "https://mocki.io/v1/2cd777cf-d6a0-483e-982e-9e1184d1483b"  # created a dummy api for testing
    roll_no, test_scores = get_student_data(api_url)

    # calculate average score of the students
    avg_score = np.mean(test_scores)
    print("average score: ", avg_score)

    plot_scores(roll_no, test_scores)