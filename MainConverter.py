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
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} mm')
                                    print(MetricToImperialConvert.MilimeterToInch(dimension), 'in')
                                    print('-'*40)

                                elif conversion_to_unit == 2:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} mm')
                                    print(MetricToImperialConvert.MilimeterToFoot(dimension), 'ft')
                                    print('-'*40)

                                elif conversion_to_unit == 3:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} mm')
                                    print(MetricToImperialConvert.MilimeterToYard(dimension), 'yd')
                                    print('-'*40)

                                elif conversion_to_unit == 4:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} mm')
                                    print(MetricToImperialConvert.MilimeterToMile(dimension), 'mile')
                                    print('-'*40)

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
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} cm')
                                    print(MetricToImperialConvert.CentimeterToInch(dimension), 'in')
                                    print('-'*40)

                                elif conversion_to_unit == 2:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} cm')
                                    print(MetricToImperialConvert.CentimeterToFoot(dimension), 'ft')
                                    print('-'*40)


                                elif conversion_to_unit == 3:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} cm')
                                    print(MetricToImperialConvert.CentimeterToYard(dimension), 'yd')
                                    print('-'*40)


                                elif conversion_to_unit == 4:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} cm')
                                    print(MetricToImperialConvert.CentimeterToMile(dimension), 'mile')
                                    print('-'*40)


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
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} m')
                                    print(MetricToImperialConvert.MeterToInch(dimension), 'in')
                                    print('-'*40)


                                elif conversion_to_unit == 2:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} m')
                                    print(MetricToImperialConvert.MeterToFoot(dimension), 'ft')
                                    print('-'*40)

                                elif conversion_to_unit == 3:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} m')
                                    print(MetricToImperialConvert.MeterToYard(dimension), 'yd')
                                    print('-'*40)

                                elif conversion_to_unit == 4:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} m')
                                    print(MetricToImperialConvert.MeterToMile(dimension), 'mile')
                                    print('-'*40)

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
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} km')
                                    print(MetricToImperialConvert.KilometerToInch(dimension), 'in')
                                    print('-'*40)

                                elif conversion_to_unit == 2:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} km')
                                    print(MetricToImperialConvert.KilometerToFoot(dimension), 'ft')
                                    print('-'*40)

                                elif conversion_to_unit == 3:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} km')
                                    print(MetricToImperialConvert.KilometerToYard(dimension), 'yd')
                                    print('-'*40)

                                elif conversion_to_unit == 4:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} km')
                                    print(MetricToImperialConvert.KilmeterToMile(dimension), 'mile')
                                    print('-'*40)

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
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} in')
                                    print(ImperialToMetricConvert.InchToMilimeter(dimension), 'mm')
                                    print('-'*40)

                                elif conversion_to_unit == 2:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} in')
                                    print(ImperialToMetricConvert.InchToCentimeter(dimension), 'cm')
                                    print('-'*40)

                                elif conversion_to_unit == 3:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} in')
                                    print(ImperialToMetricConvert.InchToMeter(dimension), 'm')
                                    print('-'*40)

                                elif conversion_to_unit == 4:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} in')
                                    print(ImperialToMetricConvert.InchToKilometer(dimension), 'km')
                                    print('-'*40)

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
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} ft')
                                    print(ImperialToMetricConvert.FootToMilimeter(dimension), 'mm')
                                    print('-'*40)

                                elif conversion_to_unit == 2:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} ft')
                                    print(ImperialToMetricConvert.FootToCentimeter(dimension), 'cm')
                                    print('-'*40)

                                elif conversion_to_unit == 3:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} ft')
                                    print(ImperialToMetricConvert.FootToMeter(dimension), 'm')
                                    print('-'*40)

                                elif conversion_to_unit == 4:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} ft')
                                    print(ImperialToMetricConvert.FootToKilometer(dimension), 'km')
                                    print('-'*40)

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
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} yd')
                                    print(ImperialToMetricConvert.YardToMilimeter(dimension), 'mm')
                                    print('-'*40)

                                elif conversion_to_unit == 2:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} yd')
                                    print(ImperialToMetricConvert.YardToCentimeter(dimension), 'cm')
                                    print('-'*40)

                                elif conversion_to_unit == 3:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} yd')
                                    print(ImperialToMetricConvert.YardToMeter(dimension), 'm')
                                    print('-'*40)

                                elif conversion_to_unit == 4:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} yd')
                                    print(ImperialToMetricConvert.YardToKilometer(dimension), 'km')
                                    print('-'*40)

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
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} mile')
                                    print(ImperialToMetricConvert.MileToMilimeter(dimension), 'mm')
                                    print('-'*40)

                                elif conversion_to_unit == 2:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} mile')
                                    print(ImperialToMetricConvert.MileToCentimeter(dimension), 'cm')
                                    print('-'*40)

                                elif conversion_to_unit == 3:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} mile')
                                    print(ImperialToMetricConvert.MileToMeter(dimension), 'm')
                                    print('-'*40)

                                elif conversion_to_unit == 4:
                                    dimension = float(input("Enter your dimension..."))
                                    print('-'*40)
                                    print(f'{dimension} mile')
                                    print(ImperialToMetricConvert.MileToKilometer(dimension), 'Km')
                                    print('-'*40)

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