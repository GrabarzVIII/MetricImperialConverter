import MetricToImperialConvert
import ImperialToMetricConvert

'''This is main fail for converter'''
while True:
    
    try:
        conversion_to = int(input('''
        What do you want to convert:\n
        1. Metric units to imperail units convertion\n
        2. Imperila units to metric units convertion\n
        3. Quit
        Enter option number...'''))
    
        if conversion_to == 1:

            while True:
                
                try:
                    unit_to_convert = int(input('''
                    What unit do you want to convert:
                    1. Milimeters
                    2. Centimeters
                    3. Meters
                    4. Kilometers
                    5. Return to previous menu
                    Enter option number...'''))

                    if unit_to_convert == 1:
                        pass

                    elif unit_to_convert == 2:
                        pass

                    elif unit_to_convert == 3:
                        pass

                    elif unit_to_convert == 4:
                        pass

                    elif unit_to_convert ==5:
                        break

                    else:
                        print('Enter correct number\n')

                except ValueError:
                    print('Entered value need to be integral number\n')


        elif conversion_to == 2:
            pass


        elif conversion_to == 3:
            break


        else:
            print('Enter correct number\n')
    
    except ValueError:
        print('Entered value need to be integral number\n')