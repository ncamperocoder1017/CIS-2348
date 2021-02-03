# Nicolas Campero
# 1856853

# dictionary associates services with costs
services = {
    'Oil change': 35,
    'Tire shine': 20,
    'Car wash': 25,
    'Cranberry scent': 3
}

# output services and cost
print("Davy's auto shop services")
print('Oil change -- ${}'.format(services['Oil change']))
print('Tire shine -- ${}'.format(services['Tire shine']))
print('Car wash -- ${}'.format(services['Car wash']))
print('Cranberry scent cost ${}'.format(services['Cranberry scent']), end='')
print('\n')

# ask user for services needed
print('Select first service:')
service = str(input())
print('Select second service:')
service2 = str(input())
service1_cost = 0
service2_cost = 0

# assign cost to service
if service == '-':
    service1_cost = 0
    service2_cost = services[service2]
elif service2 == '-':
    service2_cost = 0
    service1_cost = services[service]
else:
    service1_cost = services[service]
    service2_cost = services[service2]

total_cost = service1_cost + service2_cost

# conditionals determine output. If any service is a dash, cost is 0. Print total cost.
if service == '-':
    print("\nDavy's auto shop invoice", '\n')
    print('Service 1: No service')
    print('Service 2: {}, ${}'.format(service2, services[service2]), end='')
    print('\n')
    print('Total: ${}'.format(total_cost))
elif service2 == '-':
    print("\nDavy's auto shop invoice", '\n')
    print('Service 1: {}, ${}'.format(service, services[service]))
    print('Service 2: No service', end='')
    print('\n')
    print('Total: ${}'.format(total_cost))
else:
    print("\nDavy's auto shop invoice", '\n')
    print('Service 1: {}, ${}'.format(service, services[service]))
    print('Service 2: {}, ${}'.format(service2, services[service2]), end='')
    print('\n')
    print('Total: ${}'.format(total_cost))
