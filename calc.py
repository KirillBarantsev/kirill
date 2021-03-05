str_input = input("Vvedite pervoe chislo: ")
chisloodin = float(str_input)

operation = input ("+ / * - ^ ")
str_input2 = input("Vvedite vtoroe chislo: ")
chislodva = float(str_input2)

if operation == "+":
	result = chisloodin + chislodva
elif operation == "/":
         if chislodva != 0:
                 result = chisloodin / chislodva
         else:
               result = "na nol' delit' nel'zya"       
elif operation == "*":
        result = chisloodin * chislodva
elif operation == "-":
	 result = chisloodin - chislodva
elif operation == "^":
        result = chisloodin ** chislodva

print("Result: " + str(result))
input("Нажмите Enter для выхода.")