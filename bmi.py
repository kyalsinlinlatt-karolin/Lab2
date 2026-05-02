def calculate_bmi(height, weight):
    print("Height = " +str(height) + " m")
    print("Weight = " +str(weight) + " kg")

    bmi = weight/(height*height)

    print("BMI is " +str(round(bmi,2)))
    # (or) --> print(f"BMI is {bmi:.2f}")

    if bmi<18.5:                                    #no need round bracket, different from C++
        print ("The user is Under Weight.")
    elif bmi <=25.0:
        print ("The user is Normal Weight.")
    else:
        print ("The suer is Over Weight.")
    
calculate_bmi(weight=57, height=1.73)
