def driver_names_passed_at_least(drivers_list, num_of_tests):
    passed_drivers_names = []
    for driver in drivers_list:
        if driver.tests < num_of_tests:
            passed_drivers_names.append(driver.name)
    return passed_drivers_names
