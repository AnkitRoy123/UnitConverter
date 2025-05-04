units = ["Temperature Converter",
         "Length Converter",
         "Weight Converter",
         "Digital Storage Converter"]

print()
print("____________Unit Converter____________")
while True:
    print("\nType the number of the unit you want to convert.")
    print("\nType 1 to temperature converter, 2 to length converter, 3 to weight converter, 4 to digital storage converter.")
    print("Type 0 to exit.")
    choice = input("\nEnter your choice: ")

    if choice == "0":
        print("You are exited!!")
        print("Thanks for using our Unit Converter!")
        break

# Temperature unit converter
    elif choice == "1":
        print("\nType 0 to exit,  1 to Celsius to Fahrenheit, 2 to Fahrenheit to Celsius convert.")
        cois = input("\nEnter your choice: ")
        
        if cois == "1":
            try:
                c = float(input("Enter the temperature in Celsius: "))
                f = (c * 9/5) + 32
                print(f"{c} Celsius = {f} Fahrenheit")
            except ValueError:
                print("Please enter a number.")

        elif cois == "2":
            try:
                f = float(input("Enter the temperature in Fahrenheit: "))
                c = (f - 32) * 5/9
                print(f"{f} Fahrenheit = {c} Celsius")
            except ValueError:
                print("Please enter a number.")
        elif cois == "0":
            break
        else:
            print("Invalid choice.")
# Length unit converter
    elif choice == "2":
       print()
       conversation_avalible = [
          (1, "Meters", "Kilometer") ,
          (2, "Kilometer", "Meters"),
          (3, "Kilometer", "Mile"),
          (4, "Mile", "Kilometer"),
          (5, "Mile", "Meters"),
          (6, "Meters", "Centimeter"),
          (7, "Centimeter", "Meters"),
          (8, "Centimeter", "Millimeter"),
          (9, "Millimeter", "Centimeter"),
          (10, "Centimeter", "Inch"),
          (11, "Inch", "Meters"),
          (12, "Inch", "Centimeter"),
        ]
       print("Conversation avalible: ")
       for number, from_unit, to_unit in conversation_avalible:
          print(f"{number}.{from_unit} => {to_unit}")
       print()
       conversation = input("Enter the number of the conversation you want to perform: ")
       try:         
         conversation = int(conversation)
         conversation_index = int(conversation) - 1
         number, from_unit, to_unit = conversation_avalible[conversation_index]
         print()
         from_value = float(input(f"Enter the value in {from_unit}: "))

         if number == 1 and from_unit == "Meters" and to_unit == "Kilometer":
                to_value = from_value / 1000
                print(f"{from_value} {from_unit} = {to_value} {to_unit}") 
         elif number == 2 and from_unit == "Kilometer" and to_unit == "Meters":
                to_value = from_value * 1000
                print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 3 and from_unit == "Kilometer" and to_unit == "Mile":
                to_value = from_value / 1.5
                print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 4 and from_unit == "Mile" and to_unit == "Kilometer":
              to_value = from_value * 1.5
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")
           
         elif number == 5 and from_unit == "Mile" and to_unit == "Meters":
          to_value = from_value * 1500
          print(f"{from_value} {from_unit} = {to_value} {to_unit}")

         elif number == 6 and from_unit == "Meters" and to_unit == "Centimeter":
              to_value = from_value * 100
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 7 and from_unit == "Centimeter" and to_unit == "Meters":
              to_value = from_value * 0.01
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 8 and from_unit == "Centimeter" and to_unit == "Millimeter":
              to_value = from_value * 10
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 9 and from_unit == "Millimeter" and to_unit == "Centimeter":
              to_value = from_value * 0.1
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 10 and from_unit == "Centimeter" and to_unit == "Inch":
              to_value = from_value * 0.393701          
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")  
         elif number == 11 and from_unit == "Inch" and to_unit == "Meters":
              to_value = from_value * 0.0254   
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 12 and from_unit == "Inch" and to_unit == "Centimeter":
              to_value = from_value * 2.54
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")        
         else:
              print("Invalid input!!")              
       except ValueError:
              print("Please enter a number.")        
       except IndexError:
            print("Invalid input!!")    
# Weight unit converter 
    elif choice == "3":
        weight_conversions = [
           (1, "Kilogram" ,"Gram"),
           (2, "Gram" ,"Kilogram"),
           (3, "Quintal", "Kilogram"),
           (4, "Kilogram", "Quintal"),
           (5, "Tonne", "Kilogram"),
           (6, "Kilogram", "Tonne"),
           (7, "Kilogram", "Pound"),
           (8, "Pound", "Kilogram"),
           (9, "Gram", "Milligram"),
           (10, "Milligram", "Microgram")
        ]
        for number, from_unit, to_unit in weight_conversions:
          print(f"{number}.{from_unit} => {to_unit}")
        conversation = input("Enter the number of the conversation you want to perform: ")
        try:         
         conversation = int(conversation)
         conversation_index = int(conversation) - 1
         number, from_unit, to_unit = weight_conversions[conversation_index]
         from_value = float(input(f"Enter the value in {from_unit}: "))
         print() 
         if number == 3 and from_unit == "Quintal" and to_unit == "Kilogram":
          to_value = from_value * 100
          print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 4 and from_unit == "Kilogram" and to_unit == "Quintal":
          to_value = from_value / 100
          print(f"{from_value} {from_unit} = {to_value} {to_unit}") 
         elif ((number == 6 and from_unit == "Kilogram" and to_unit == "Tonne") or 
               (number == 2 and from_unit == "Gram" and to_unit == "Kilogram")):
            to_value = from_value / 1000
            print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 7 and from_unit == "Kilogram" and to_unit == "Pound":
          to_value = from_value * 2.205
          print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif number == 8 and from_unit == "Pound" and to_unit == "Kilogram":
          to_value = from_value / 2.205
          print(f"{from_value} {from_unit} = {to_value} {to_unit}")
         elif ((number == 9 and from_unit == "Gram" and to_unit == "Milligram") or 
           (number == 10 and from_unit == "Milligram" and to_unit == "Microgram") or
           (number == 5 and from_unit == "Tonne" and to_unit == "Kilogram") or 
            (number == 1 and from_unit == "Kilogram" and to_unit == "Gram")):
               to_value = from_value * 1000
               print(f"{from_value} {from_unit} = {to_value} {to_unit}")

         else:
          print("Invalid input!!")                 
        except ValueError:
              print("Please enter a number.")        
        except IndexError:
            print("Invalid input!!")  
# Digital Storage unit converter  
    elif choice == "4":
        storage_avalible = [
           (1, "B" ,"KB"),
           (2, "KB" ,"MB"),
           (3, "MB" ,"GB"),
           (4, "GB" ,"TB"),
           (5, "KB" ,"B"),
           (6, "MB" ,"KB"),
           (7, "GB" ,"MB"),
           (8, "TB" ,"GB")
         ]
        for number, from_unit, to_unit in storage_avalible:
          print(f"{number}.{from_unit} => {to_unit}")
        conversation = input("Enter the number of the conversation you want to perform: ")
        try:         
           conversation = int(conversation)
           conversation_index = int(conversation) - 1
           number, from_unit, to_unit = storage_avalible[conversation_index]
           from_value = float(input(f"Enter the value in {from_unit}: "))
           print()  
           if ((number == 1 and from_unit == "B" and to_unit == "KB") or 
                    (number == 2 and from_unit == "KB" and to_unit == "MB") or
                    (number == 3 and from_unit == "MB" and to_unit == "GB") or 
                    (number == 4 and from_unit == "GB" and to_unit == "TB")):
                to_value = from_value / 1024
                print(f"{from_value} {from_unit} = {to_value} {to_unit}") 
           elif ((number == 5 and from_unit == "KB" and to_unit == "B") or 
            (number == 6 and from_unit == "MB" and to_unit == "KB") or
            (number == 7 and from_unit == "GB" and to_unit == "MB") or 
            (number == 8 and from_unit == "TB" and to_unit == "GB")):     
              to_value = from_value * 1024 
              print(f"{from_value} {from_unit} = {to_value} {to_unit}")
        except ValueError:
            print("Please enter a number.")        
        except IndexError:
          print("Invalid input!!")     
    else:
      print("Invalid input!")
