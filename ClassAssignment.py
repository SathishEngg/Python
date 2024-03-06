class multiplefunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        Lists=["Machine Learning", "Neural Networks", "Vision", "Robotics","Speech Processing", "Natural Language Processing"]
        for temp in Lists:
            print (temp)
            
    def oddEven():
        num=int(input("Enter a Number: "))
        if((num%2)==1):
            print("52452 is Odd Number")
            answer="52452 is Odd Number"
        else:
            print("52452 is Even Number")
            answer="52452 is Even Number"    
            
    def Elegible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if (age >= 21):
            print("ELIGIBLE")
            result="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            result="NOT ELIGIBLE"
            
    def Percentage():
        sub1=98
        print("The Subject1=", sub1)
        sub2=87
        print("The Subject2=", sub2)
        sub3=95
        print("The Subject3=", sub3)
        sub4=95
        print("The Subject4=", sub4)
        sub5=93
        print("The Subject5=", sub5)
        total_marks=sub1+sub2+sub3+sub4+sub5
        print("Total : ",total_marks) 
        total_subjects=5
        percentage = (total_marks / (100 * total_subjects)) * 100
        print("Percentage : ", percentage)       
        
    def triangle():
        height=32
        print("Height:",height)
        breadth=34
        print("Breadth:",breadth)
        area=(height*breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", area)

        height1=2
        print("Height1:",height1)
        height2=4
        print("Height2:",height2)
        breadth=4
        print("Breadth:",breadth)
        perimeter=height1+height2+breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", perimeter) 