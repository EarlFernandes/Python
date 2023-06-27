def send_email(num_visits, visits_email):
    if num_visits == 3 and visits_email == 5:
        print ("Not enough visits")
    elif num_visits==5 and visits_email==5:
        print ("Send email.")