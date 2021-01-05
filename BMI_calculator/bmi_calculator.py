'''
BMI 지수를 계산하는 계산기입니다.
BMI 지수는 체중(kg)과 신장(cm)으로, 다음과 같이 계산됩니다:

BMI = 체중 / (신장 *)
'''
def func_BMI():
    weight = float(input("Enter the Weight(kg): "))
    height_m = float(input("Enter the Height(cm): "))
    height_cm = height_m*(1/100)
    return weight,height_cm

weight, height_cm = func_BMI()

BMI = weight / (height_cm * height_cm)

print(BMI)