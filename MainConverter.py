import MetricToImperialConvert
import ImperialToMetricConvert

'''This is main fail for converter'''
while True:
    
    try:
        conversion = int(input('''
        What do you want to convert:\n
        1. Metric units to imperail units convertion\n
        2. Imperila units to metric units convertion\n
        3. Quit
        Enter option number...'''))
    
        if conversion == 1:

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

                        with True:

                            try:
                                conversion_to_unit = int(input('''
                                Do you want to convert milimeters to:
                                1. Inchs
                                2. Foots
                                3. Yards
                                4. Miels
                                5. Return to preciosu menu
                                Enter option number...'''))

                                if conversion_to_unit == 1:
                                    pass

                                elif conversion_to_unit == 2:
                                    pass

                                elif conversion_to_unit == 3:
                                    pass

                                elif conversion_to_unit == 4:
                                    pass

                                elif conversion_to_unit == 5:
                                    break

                                else:
                                    print('Enter correct number\n')
                            
                            except ValueError:
                                print('Entered value need to be integral number\n')


                    elif unit_to_convert == 2:

                        with True:
                            
                            try:
                                conversion_to_unit = int(input('''
                                Do you want to convert centimeters to:
                                1. Inchs
                                2. Foots
                                3. Yards
                                4. Miels
                                5. Return to preciosu menu
                                Enter option number...'''))

                                if conversion_to_unit == 1:
                                    pass

                                elif conversion_to_unit == 2:
                                    pass

                                elif conversion_to_unit == 3:
                                    pass

                                elif conversion_to_unit == 4:
                                    pass

                                elif conversion_to_unit == 5:
                                    break

                                else:
                                    print('Enter correct number\n')

                            except ValueError:
                                print('Entered value need to be integral number\n')

                    elif unit_to_convert == 3:

                        with True:
                            
                            try:
                                conversion_to_unit = int(input('''
                                Do you want to convert meters to:
                                1. Inchs
                                2. Foots
                                3. Yards
                                4. Miels
                                5. Return to preciosu menu
                                Enter option number...'''))
                            
                                if conversion_to_unit == 1:
                                    pass

                                elif conversion_to_unit == 2:
                                    pass

                                elif conversion_to_unit == 3:
                                    pass

                                elif conversion_to_unit == 4:
                                    pass

                                elif conversion_to_unit == 5:
                                    break

                                else:
                                    print('Enter correct number\n')

                            except ValueError:
                                print('Entered value need to be integral number\n')

                    elif unit_to_convert == 4:

                        with True:
                            
                            try:
                                conversion_to_unit = int(input('''
                                Do you want to convert kilimeters to:
                                1. Inchs
                                2. Foots
                                3. Yards
                                4. Miels
                                5. Return to preciosu menu
                                Enter option number...'''))

                                if conversion_to_unit == 1:
                                    pass

                                elif conversion_to_unit == 2:
                                    pass

                                elif conversion_to_unit == 3:
                                    pass

                                elif conversion_to_unit == 4:
                                    pass

                                elif conversion_to_unit == 5:
                                    break

                                else:
                                    print('Enter correct number\n')

                            except ValueError:
                                print('Entered value need to be integral number\n')

                    elif unit_to_convert ==5:
                        break

                    else:
                        print('Enter correct number\n')

                except ValueError:
                    print('Entered value need to be integral number\n')


        elif conversion == 2:
            try:
                unit_to_convert = int(input('''
                What unit do you want to convert:
                1. Inchs
                2. Foots
                3. Yards
                4. Mails
                5. Return to previous menu
                Enter option number...'''))

                if unit_to_convert == 1:
                    
                    with True:
                            
                            try:
                                conversion_to_unit = int(input('''
                                Do you want to convert Inchs to:
                                1. Milimeters
                                2. Centimeters
                                3. Meters
                                4. Kilometers
                                5. Return to preciosu menu
                                Enter option number...'''))

                                if conversion_to_unit == 1:
                                    pass

                                elif conversion_to_unit == 2:
                                    pass

                                elif conversion_to_unit == 3:
                                    pass

                                elif conversion_to_unit == 4:
                                    pass

                                elif conversion_to_unit == 5:
                                    break

                                else:
                                    print('Enter correct number\n')

                            except ValueError:
                                print('Entered value need to be integral number\n')

                elif unit_to_convert == 2:
                    
                    with True:
                            
                            try:
                                conversion_to_unit = int(input('''
                                Do you want to convert Foots to:
                                1. Milimeters
                                2. Centimeters
                                3. Meters
                                4. Kilometers
                                5. Return to preciosu menu
                                Enter option number...'''))

                                if conversion_to_unit == 1:
                                    pass

                                elif conversion_to_unit == 2:
                                    pass

                                elif conversion_to_unit == 3:
                                    pass

                                elif conversion_to_unit == 4:
                                    pass

                                elif conversion_to_unit == 5:
                                    break

                                else:
                                    print('Enter correct number\n')

                            except ValueError:
                                print('Entered value need to be integral number\n')

                elif unit_to_convert == 3:
                    
                    with True:
                            
                            try:
                                conversion_to_unit = int(input('''
                                Do you want to convert Yards to:
                                1. Milimeters
                                2. Centimeters
                                3. Meters
                                4. Kilometers
                                5. Return to preciosu menu
                                Enter option number...'''))

                                if conversion_to_unit == 1:
                                    pass

                                elif conversion_to_unit == 2:
                                    pass

                                elif conversion_to_unit == 3:
                                    pass

                                elif conversion_to_unit == 4:
                                    pass

                                elif conversion_to_unit == 5:
                                    break

                                else:
                                    print('Enter correct number\n')

                            except ValueError:
                                print('Entered value need to be integral number\n')

                elif unit_to_convert == 4:
                    
                    with True:
                            
                            try:
                                conversion_to_unit = int(input('''
                                Do you want to convert Mails to:
                                1. Milimeters
                                2. Centimeters
                                3. Meters
                                4. Kilometers
                                5. Return to preciosu menu
                                Enter option number...'''))

                                if conversion_to_unit == 1:
                                    pass

                                elif conversion_to_unit == 2:
                                    pass

                                elif conversion_to_unit == 3:
                                    pass

                                elif conversion_to_unit == 4:
                                    pass

                                elif conversion_to_unit == 5:
                                    break

                                else:
                                    print('Enter correct number\n')

                            except ValueError:
                                print('Entered value need to be integral number\n')

                elif unit_to_convert ==5:
                    break

                else:
                    print('Enter correct number\n')

            except ValueError:
                print('Entered value need to be integral number\n')


        elif conversion == 3:
            break


        else:
            print('Enter correct number\n')
    
    except ValueError:
        print('Entered value need to be integral number\n')