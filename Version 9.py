rounds = 0

bucket = 0
combination = 0
bucket_list = [1,2,3,4,5,6,7,8]
combination_list = [1,2,3,4,5]

line_array = []
line_number = 0
#line_number represents which line we draw our inputs from the text file

#create arrays A, B, and C to record/output inputs more easily
A=[]
B=[]
C=[]
Performance=[]
KPerformance=[]

print("Hello! Welcome to the Game.\nLet's start by entering your personal code given to you by a researcher.")
#NEED TO PUT ANY 5 CHARACTERS TO GO FURTHER
personal_code=raw_input()

while len(personal_code)!=5:
    print("Your personal code should be 5 characters long. Please enter your personal code again.")
    personal_code=raw_input()
    
print("\nThank you! Please read the rules of the game. When you are done reading, please enter your game code and press enter to start playing.")
#1050 SHOULD BE ENTERED TO GO FURTHER]
treatment_condition=raw_input()
    
if int(treatment_condition)==1050:
    #output to a text file
    with open("%s_output.txt"%personal_code, "w") as output:
        output.write("Players_ID    Game_Code	Rounds	Bucket  Combination Steps	Decision_1	Decision_2	Decision_3	Performance\n")
        
    #Loop through 6 rounds
    i=1
    
    while i < 8:
        if i<7:
            print("\nNow get ready to play your round %d! Good luck!"%i)
            def Rounds(r):
                rounds = r
                
                #randomly select a bucket
                import random
                bucket = random.choice(bucket_list)
                bucket_list.remove(bucket)
                
                #randomly select a combination within the bucket
                combination = random.choice(combination_list)
                
                line_number = (bucket-1)*5 + combination + 1
                
                line = open("Input.txt", "r").readlines()[line_number-1]
                line_array = line.split("\t")
                
                
                A.append(int(line_array[5]))
                B.append(int(line_array[6]))
                C.append(int(line_array[7]))
                a1=int(line_array[8])
                a2=int(line_array[9])
                a3=int(line_array[10])
                
                step = 0
                
                #base case before input
                #record the base case values in the arrays
                Performance.append(30000-(a1-A[step])*(a1-A[step])-(a2-B[step])*(a2-B[step])-(a3-C[step])*(a3-C[step]))
                
                #print the base case
                print("\nYour values in set "+str(step)+" is ["+str(A[step])+";"+str(B[step])+";"+str(C[step])+"] that corresponds to the performance value of "+str(Performance[step]))
                print('\n---------------------------------------------------------------------------------')
                print('|\tStep\t|\tA\t|\tB\t|\tC\t|  Performance  |')
                print('---------------------------------------------------------------------------------')
                step0_row='|\t'+str(step)+'\t|\t'+str(A[step])+'\t|\t'+str(B[step])+'\t|\t'+str(C[step])+'\t|\t'+str(Performance[step])+'\t|'
                print(step0_row)
                print('---------------------------------------------------------------------------------')
                print("\nPlease enter your choice of decision variables A,B, and C in the following format: A,B,C. All three decision variables should be within the range of 0-99.")
                print('For example, your input may be: 1,1,1. Please note that values are separated by commas.')   
                
                with open("%s_output.txt"%personal_code, "a") as output:
                    output.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n" % (personal_code,treatment_condition,rounds,bucket,combination,step,A[step],B[step],C[step],Performance[step]))
                    
                    
                #use the while statement to easily print values in privious steps 
                while step<20:
                    
                    #increase the index to go back to the beginning of the while loop
                    step += 1
                    
                    #for following steps
                    #define the function for easier calling in try/except statements
                    def performance():
                        
                        #for each step
                        step_input=raw_input()
                        step_dvalues=step_input.split(',')
                        
                        d1 = int(step_dvalues[0])
                        d2 = int(step_dvalues[1])
                        d3 = int(step_dvalues[2])
                        
                        #limit the decision variables to a range of 0-99
                        if d1<100 and d1>=0 and d2<100 and d2>=0 and d3<100 and d3>=0:
                            
                            #record the values in the corresponding arrays
                            A.append(d1)
                            B.append(d2)
                            C.append(d3)
                            Performance.append(30000-(a1-A[step])*(a1-A[step])-(a2-B[step])*(a2-B[step])-(a3-C[step])*(a3-C[step]))
                             
                            #print the header of performance
                            print("\nYour values in set "+str(step)+" is ["+str(A[step])+";"+str(B[step])+";"+str(C[step])+"] that corresponds to the performance value of "+str(Performance[step]))
                            print('\n---------------------------------------------------------------------------------')
                            print('|\tStep\t|\tA\t|\tB\t|\tC\t|  Performance  |')
                            print('---------------------------------------------------------------------------------')
                       
                            #use this while loop to print all steps and results
                            i=0
                            while i<=step:
                                step_row='|\t'+str(i)+'\t|\t'+str(A[i])+'\t|\t'+str(B[i])+'\t|\t'+str(C[i])+'\t|\t'+str(Performance[i])+'\t|'
                                print(step_row)
                                print('---------------------------------------------------------------------------------')
                                i += 1
                            if step < 19 and Performance[step] != 30000:
                                print("\nPlease enter your next set of decision variables")
                            elif step == 19:
                                print("\nNOW IT IS TIME TO PUT IN YOUR LAST SET VALUES. CHOOSE WISELY.\n")
                            
                        else:
                            print "Oops!  You entered values out of range (0,99).  Please try again..."
                            performance()
                           
                    #handle the Exception errors and use the defined function to loop if errors occur continuously
                    def handleRepeatingExceptionErrors():
                        global A,B,C
                        try:
                            performance()
                            
                            with open("%s_output.txt"%personal_code, "a") as output:
                                output.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n" % (personal_code,treatment_condition,rounds,bucket,combination,step,A[step],B[step],C[step],Performance[step]))
                                
                        #handle ValueError (occurs when inputs don't match the required integer type for variables)
                        except ValueError:
                            print "Oops!  These were not valid numbers.  Please try again..."
                            
                            #Prevent the program from adding values in the wrong input(added to index of array length)
                            arraylength = min(len(A),len(B),len(C))
                            A = A[:arraylength]
                            B = B[:arraylength]
                            C = C[:arraylength]
                        
                            #loops back for the correct inputs if error occurs
                            handleRepeatingExceptionErrors()
                            
                        #handles IndexError (occurs when inputs are less than 3 as expected)
                        except IndexError:
                            print "Oops!  You entered less than 3 numbers.  Please try again..."
                            
                            #Prevent the program from adding values in the wrong input(added to index of array length)
                            arraylength = min(len(A),len(B),len(C))
                            A = A[:arraylength]
                            B = B[:arraylength]
                            C = C[:arraylength]
                            
                            #loops back for the correct inputs if error occurs
                            handleRepeatingExceptionErrors()
                
                    #call the function        
                    handleRepeatingExceptionErrors()
                    
                    if Performance[step] == 30000:
                        print "Congratulations! You have reached 30,000 in this round."
                        step = 20
            
            Rounds(i)
            
            if i < 6:
                print("Are you ready for the next round? y/n")
                ready=raw_input()

                while ready!= "y":
                    print("Are you ready for the next round? y/n")
                    ready=raw_input()
                    
            #Clear the arrays for next round
            A=[]
            B=[]
            C=[]
            Performance=[]
            
            i += 1
            
        elif i == 7:
            print("Thank you! Now you have finished the game. Please call for a researcher to record your results and complete the game.")
            k=raw_input()
            while "the end" not in k:
                print "Please enter code to finish the program"
                k=raw_input()
            i += 1
    
if int(treatment_condition)==2140:
    #output to a text file
    with open("%s_output.txt"%personal_code, "w") as output:
        output.write("Players_ID    Game_Code	Rounds	Bucket  Combination Steps	Decision_1	Decision_2	Decision_3	Performance Kasper_Performance\n")
    
    #Loop through 6 rounds
    i=1
    
    while i < 8:
        if i<7:
            print("\nNow get ready to play your round %d! Good luck!"%i)
            def RoundsK(r):
                rounds = r
                
                #randomly select a bucket
                import random
                bucket = random.choice(bucket_list)
                bucket_list.remove(bucket)
                
                #randomly select a combination within the bucket
                combination = random.choice(combination_list)
                
                line_number = (bucket-1)*5 + combination + 1
                
                line = open("Input.txt", "r").readlines()[line_number-1]
                line_array = line.split("\t")
                
                
                A.append(int(line_array[5]))
                B.append(int(line_array[6]))
                C.append(int(line_array[7]))
                a1=int(line_array[8])
                a2=int(line_array[9])
                a3=int(line_array[10])
                
                step = 0
                
                #base case before input
                #record the base case values in the arrays
                Performance.append(30000-(a1-A[step])*(a1-A[step])-(a2-B[step])*(a2-B[step])-(a3-C[step])*(a3-C[step]))
                
                KPerformance.append(Performance[step])
                
                #print the base case
                print("\nYour values in set "+str(step)+" is ["+str(A[step])+";"+str(B[step])+";"+str(C[step])+"] that corresponds to the performance value of "+str(Performance[step])+", Kasper's performance value is "+str(KPerformance[step]))
                print('\n---------------------------------------------------------------------------------------------------------')
                print('|\tStep\t|\tA\t|\tB\t|\tC\t|  Performance  | Kasper_Performance\t|')
                print('---------------------------------------------------------------------------------------------------------')
                step0_row='|\t'+str(step)+'\t|\t'+str(A[step])+'\t|\t'+str(B[step])+'\t|\t'+str(C[step])+'\t|\t'+str(Performance[step])+'\t|\t'+str(KPerformance[step])+'\t\t|'
                print(step0_row)
                print('---------------------------------------------------------------------------------------------------------')
                print("\nPlease enter your choice of decision variables A,B, and C in the following format: A,B,C. All three decision variables should be within the range of 0-99.")
                print('For example, your input may be: 1,1,1. Please note that values are separated by commas.')   
                
                with open("%s_output.txt"%personal_code, "a") as output:
                    output.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n" % (personal_code,treatment_condition,rounds,bucket,combination,step,A[step],B[step],C[step],Performance[step],KPerformance[step]))
                    
                    
                #use the while statement to easily print values in privious steps 
                while step<20:
                    
                    #increase the index to go back to the beginning of the while loop
                    step += 1
                    
                    #for following steps
                    #define the function for easier calling in try/except statements
                    def performance():
                        
                        #for each step
                        step_input=raw_input()
                        step_dvalues=step_input.split(',')
                        
                        d1 = int(step_dvalues[0])
                        d2 = int(step_dvalues[1])
                        d3 = int(step_dvalues[2])
                        
                        #limit the decision variables to a range of 0-99
                        if d1<100 and d1>=0 and d2<100 and d2>=0 and d3<100 and d3>=0:
                            
                            #record the values in the corresponding arrays
                            A.append(d1)
                            B.append(d2)
                            C.append(d3)
                            Performance.append(30000-(a1-A[step])*(a1-A[step])-(a2-B[step])*(a2-B[step])-(a3-C[step])*(a3-C[step]))
                            
                            KPerformance.append(Performance[step]+random.randint(-100,100))
                            while KPerformance[step]>=30000:
                                KPerformance[step]=Performance[step]+random.randint(-100,100)
                                
                            #print the header of performance
                            print("\nYour values in set "+str(step)+" is ["+str(A[step])+";"+str(B[step])+";"+str(C[step])+"] that corresponds to the performance value of "+str(Performance[step])+", Kasper's performance value is "+str(KPerformance[step]))
                            print('\n---------------------------------------------------------------------------------------------------------')
                            print('|\tStep\t|\tA\t|\tB\t|\tC\t|  Performance  | Kasper_Performance\t|')
                            print('---------------------------------------------------------------------------------------------------------')
                       
                            #use this while loop to print all steps and results
                            i=0
                            while i<=step:
                                step_row='|\t'+str(i)+'\t|\t'+str(A[i])+'\t|\t'+str(B[i])+'\t|\t'+str(C[i])+'\t|\t'+str(Performance[i])+'\t|\t'+str(KPerformance[i])+'\t\t|'
                                print(step_row)
                                print('---------------------------------------------------------------------------------------------------------')
                                i += 1
                            if step < 19 and Performance[step] != 30000:
                                print("\nPlease enter your next set of decision variables")
                            elif step == 19:
                                print("\nNOW IT IS TIME TO PUT IN YOUR LAST SET VALUES. CHOOSE WISELY.\n")
                            
                        else:
                            print "Oops!  You entered values out of range (0,99).  Please try again..."
                            performance()
                           
                    #handle the Exception errors and use the defined function to loop if errors occur continuously
                    def handleRepeatingExceptionErrors():
                        global A,B,C
                        try:
                            performance()
                            
                            with open("%s_output.txt"%personal_code, "a") as output:
                                output.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n" % (personal_code,treatment_condition,rounds,bucket,combination,step,A[step],B[step],C[step],Performance[step],KPerformance[step]))
                                
                        #handle ValueError (occurs when inputs don't match the required integer type for variables)
                        except ValueError:
                            print "Oops!  These were not valid numbers.  Please try again..."
                            
                            #Prevent the program from adding values in the wrong input(added to index of array length)
                            arraylength = min(len(A),len(B),len(C))
                            A = A[:arraylength]
                            B = B[:arraylength]
                            C = C[:arraylength]
                        
                            #loops back for the correct inputs if error occurs
                            handleRepeatingExceptionErrors()
                            
                        #handles IndexError (occurs when inputs are less than 3 as expected)
                        except IndexError:
                            print "Oops!  You entered less than 3 numbers.  Please try again..."
                            
                            #Prevent the program from adding values in the wrong input(added to index of array length)
                            arraylength = min(len(A),len(B),len(C))
                            A = A[:arraylength]
                            B = B[:arraylength]
                            C = C[:arraylength]
                            
                            #loops back for the correct inputs if error occurs
                            handleRepeatingExceptionErrors()
                
                    #call the function        
                    handleRepeatingExceptionErrors()
                    
                    if Performance[step] == 30000:
                        print "Congratulations! You have reached 30,000 in this round."
                        step = 20
            
            RoundsK(i)
            
            if i < 6:
                print("Are you ready for the next round? y/n")
                ready=raw_input()

                while ready!= "y":
                    print("Are you ready for the next round? y/n")
                    ready=raw_input()
                    
            #Clear the arrays for next round
            A=[]
            B=[]
            C=[]
            Performance=[]
            KPerformance=[]
            
            i += 1
            
        elif i == 7:
            print("Thank you! Now you have finished the game. Please call for a researcher to record your results and complete the game.")
            k=raw_input()
            while "the end" not in k:
                print "Please enter code to finish the program"
                k=raw_input()
            i += 1

            
        
            
        
            
