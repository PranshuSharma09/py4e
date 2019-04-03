while True:
    score = input("score: ")
    try:
        score = float(score)
        def grade(score):
            if score > 1.0:
                quit()
            if score >= 0.9:
                return 'A'
            elif score >= 0.8:
                return 'B'
            elif score >= 0.7:
                return'C'
            elif score >= 0.6:
                return 'D'
            elif score < 0.6:
                return 'F'
        print (grade(score))
        break
    except:
        print("bad score")
