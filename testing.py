# # import json
# # import boto3

# # client = boto3.client('pricing')
# # Pricing.Client.list_price_lists(**kwargs)
# # def lambda_handler(event, context):
# #     account_id = event.get('queryStringParameters', {}).get('accountId')
# #     region = event.get('queryStringParameters', {}).get('region', 'us-east-1')  # Default to 'us-east-1' if not provided
# #     instance_family = event.get('queryStringParameters', {}).get('productFamily')  # Instance family like 'c5'

# #     # print('event',event)

# #     # Validate input parameters
# #     if not account_id:
# #         return {
# #             'statusCode': 400,
# #             'body': json.dumps({'error': "accountId query parameter is required"})
# #         }
    
# #     if not instance_family:
# #         return {
# #             'statusCode': 400,
# #             'body': json.dumps({'error': "instanceFamily query parameter is required"})
# #         }

# #     # Initialize Pricing client (always 'us-east-1' for pricing API)
# #     pricing_client = boto3.client('pricing', region_name='us-east-1')

# #     try:
# #         # Query the Pricing API to get EC2 instance pricing for a specific instance family
# #         response = pricing_client.get_products(
# #             ServiceCode='AmazonEC2',
# #             Filters=[
# #                 {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_family},
# #                 {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
# #                 {'Type': 'TERM_MATCH', 'Field': 'productFamily', 'Value': 'Compute Instance'}
# #             ],
# #             MaxResults=10
# #         )
# #         print('responses',response)
# #         # Process the pricing data to extract necessary information
# #         instance_pricing = []
# #         for price_item in response.get('PriceList', []):
# #             product_data = json.loads(price_item)['product']['attributes']
# #             price_dimensions = list(json.loads(price_item)['terms']['OnDemand'].values())[0]['priceDimensions']
# #             price = list(price_dimensions.values())[0]['pricePerUnit']['USD']
# #             print(product_data)
# #             instance_pricing.append({
# #                 'InstanceName': product_data.get('instanceType', 'Unknown'),
# #                 'vCPUs': product_data.get('vcpu', 'Unknown'),
# #                 'Memory': product_data.get('memory', 'Unknown'),
# #                 'NetworkPerformance': product_data.get('networkPerformance', 'Unknown'),
# #                 'Storage': product_data.get('storage', 'Unknown'),
# #                 'OnDemandHourlyCost': price,
# #                 'CurrentGeneration': product_data.get('currentGeneration', 'Unknown'),
# #                 'PotentialEffectiveHourlyCost (Savings %)': 'N/A'  # Placeholder
# #             })

# #         # Return the filtered pricing details as JSON
# #         return {
# #             'statusCode': 200,
# #             'body': json.dumps(instance_pricing)
# #         }

# #     except Exception as e:
# #         # Return error response
# #         return {
# #             'statusCode': 500,
# #             'body': json.dumps({'error': 'Failed to fetch EC2 pricing', 'details': str(e)})
# #         }
# # # import json
# # # import boto3

# # # def lambda_handler(event, context):
# # #     # Log the incoming event
# # #     print("Event received:", json.dumps(event))

# # #     # Extract query parameters
# # #     account_id = event.get('queryStringParameters', {}).get('accountId')
# # #     region = event.get('queryStringParameters', {}).get('region', 'us-east-1')  # Default to 'us-east-1' if not provided
# # #     instance_family = event.get('queryStringParameters', {}).get('instanceFamily')  # Instance family like 'c5'

# # #     # Validate input parameters
# # #     if not account_id:
# # #         return {
# # #             'statusCode': 400,
# # #             'body': json.dumps({'error': "accountId query parameter is required"})
# # #         }
    
# # #     if not instance_family:
# # #         return {
# # #             'statusCode': 400,
# # #             'body': json.dumps({'error': "instanceFamily query parameter is required"})
# # #         }

# # #     # Initialize Pricing client (always 'us-east-1' for pricing API)
# # #     pricing_client = boto3.client('pricing', region_name='us-east-1')

# # #     try:
# # #         # Query the Pricing API to get EC2 instance pricing for a specific instance family
# # #         response = pricing_client.get_products(
# # #             ServiceCode='AmazonEC2',
# # #             Filters=[
# # #                 {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_family},
# # #                 {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
# # #                 {'Type': 'TERM_MATCH', 'Field': 'productFamily', 'Value': 'Compute Instance'}
# # #             ],
# # #             MaxResults=10
# # #         )
# # #         print(response)

# # #         # Log the API response
# # #         print("API response:", json.dumps(response, indent=2))

# # #         # Process the pricing data to extract necessary information
# # #         instance_pricing = []
# # #         if 'PriceList' in response and response['PriceList']:
# # #             for price_item in response['PriceList']:
# # #                 product_data = json.loads(price_item)['product']['attributes']
# # #                 price_dimensions = list(json.loads(price_item)['terms']['OnDemand'].values())[0]['priceDimensions']
# # #                 price = list(price_dimensions.values())[0]['pricePerUnit']['USD']

# # #                 instance_pricing.append({
# # #                     'InstanceName': product_data.get('instanceType', 'Unknown'),
# # #                     'vCPUs': product_data.get('vcpu', 'Unknown'),
# # #                     'Memory': product_data.get('memory', 'Unknown'),
# # #                     'NetworkPerformance': product_data.get('networkPerformance', 'Unknown'),
# # #                     'Storage': product_data.get('storage', 'Unknown'),
# # #                     'OnDemandHourlyCost': price,
# # #                     'CurrentGeneration': product_data.get('currentGeneration', 'Unknown'),
# # #                     'PotentialEffectiveHourlyCost (Savings %)': 'N/A'  # Placeholder
# # #                 })
# # #         else:
# # #             # Log if no pricing data is found
# # #             print("No pricing data found for the specified instance family")
# # #             return {
# # #                 'statusCode': 404,
# # #                 'body': json.dumps({'error': 'No pricing data found for the specified instance family'})
# # #             }
# # #         print(instance_pricing)
# # #         # Log the processed pricing data
# # #         print("Processed pricing data:", json.dumps(instance_pricing, indent=2))

# # #         # Return the filtered pricing details as JSON
# # #         return {
# # #             'statusCode': 200,
# # #             'body': json.dumps(instance_pricing)
# # #         }

# # #     except Exception as e:
# # #         # Log the error and return error response
# # #         print("Error fetching EC2 pricing:", str(e))
# # #         return {
# # #             'statusCode': 500,
# # #             'body': json.dumps({'error': 'Failed to fetch EC2 pricing', 'details': str(e)})
# # #         }



# import json
# import boto3

# def lambda_handler(event, context):
#     account_id = event.get('queryStringParameters', {}).get('accountId')
#     region = event.get('queryStringParameters', {}).get('region', 'us-east-1')  # Default to 'us-east-1' if not provided
#     instance_family = event.get('queryStringParameters', {}).get('productFamily')  # Instance family like 'c5'

#     # Validate input parameters
#     if not account_id:
#         return {
#             'statusCode': 400,
#             'body': json.dumps({'error': "accountId query parameter is required"})
#         }
    
#     if not instance_family:
#         return {
#             'statusCode': 400,
#             'body': json.dumps({'error': "instanceFamily query parameter is required"})
#         }

#     # Initialize Pricing client (always 'us-east-1' for pricing API)
#     pricing_client = boto3.client('pricing', region_name='us-east-1')

#     try:
#         # Query the Pricing API to get EC2 instance pricing for a specific instance family
#         response = pricing_client.get_products(
#             ServiceCode='AmazonEC2',
#             Filters=[
#                 {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_family},
#                 {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
#                 {'Type': 'TERM_MATCH', 'Field': 'productFamily', 'Value': 'Compute Instance'}
#             ],
#             MaxResults=10
#         )

#         # Process the pricing data to extract necessary information
#         instance_pricing = []
#         price_list = response.get('PriceList', [])
        
#         if not price_list:
#             return {
#                 'statusCode': 404,
#                 'body': json.dumps({'error': 'No pricing data found for the specified instance family'})
#             }

#         for price_item in price_list:
#             product_data = json.loads(price_item).get('product', {}).get('attributes', {})
#             terms = json.loads(price_item).get('terms', {})
#             on_demand_terms = terms.get('OnDemand', {})
            
#             if not on_demand_terms:
#                 continue
            
#             price_dimensions = list(on_demand_terms.values())[0].get('priceDimensions', {})
#             if not price_dimensions:
#                 continue
            
#             price = list(price_dimensions.values())[0].get('pricePerUnit', {}).get('USD', 'N/A')

#             instance_pricing.append({
#                 'InstanceName': product_data.get('instanceType', 'Unknown'),
#                 'vCPUs': product_data.get('vcpu', 'Unknown'),
#                 'Memory': product_data.get('memory', 'Unknown'),
#                 'NetworkPerformance': product_data.get('networkPerformance', 'Unknown'),
#                 'Storage': product_data.get('storage', 'Unknown'),
#                 'OnDemandHourlyCost': price,
#                 'CurrentGeneration': product_data.get('currentGeneration', 'Unknown'),
#                 'PotentialEffectiveHourlyCost (Savings %)': 'N/A'  # Placeholder
#             })
#         print(instance_pricing)
#         # Return the filtered pricing details as JSON
#         return {
#             'statusCode': 200,
#             'body': json.dumps(instance_pricing)
#         }

#     except Exception as e:
#         # Return error response
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'error': 'Failed to fetch EC2 pricing', 'details': str(e)})
#         }


# import boto3
# import json

# def lambda_handler(event, context):
#     # Extract instance type from query parameters
#     instance_type = event['queryStringParameters']['instanceType']
    
#     # Initialize the Pricing client
#     client = boto3.client('pricing', region_name='us-east-1')

#     # Query the AWS Pricing API for the given instance type
#     response = client.get_products(
#         ServiceCode='AmazonEC2',
#         Filters=[
#             {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
#             {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
#             {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
#             {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
#             {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
#         ],
#         MaxResults=10
#     )
    
#     # Process and extract the price details
#     price_per_hour = None
#     for price_item in response['PriceList']:
#         price_item_json = json.loads(price_item)
#         on_demand_details = price_item_json['terms']['OnDemand']
#         for key, value in on_demand_details.items():
#             price_dimensions = value['priceDimensions']
#             for pd_key, pd_value in price_dimensions.items():
#                 price_per_hour = pd_value['pricePerUnit']['USD']
#                 break
#         if price_per_hour:
#             break

#     # Return the price or an error message if not found
#     if price_per_hour:
#         return {
#             'statusCode': 200,
#             'body': json.dumps({
#                 'instanceType': instance_type,
#                 'pricePerHour': price_per_hour
#             })
#         }
#     else:
#         return {
#             'statusCode': 404,
#             'body': json.dumps({'error': 'Price information not found'})
#         }

# import boto3
# import json

# def lambda_handler(event, context):
#     # Extract instance type from query parameters
#     instance_type = event['queryStringParameters']['instanceType']
    
#     # Initialize the Pricing client
#     client = boto3.client('pricing', region_name='us-east-1')

#     # Query the AWS Pricing API for the given instance type
#     response = client.get_products(
#         ServiceCode='AmazonEC2',
#         Filters=[
#             {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
#             {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
#             {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
#             {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
#             {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
#         ],
#         MaxResults=10
#     )
    
#     # Initialize the details to be fetched
#     price_per_hour = None
#     vcpus = None
#     memory = None
#     network_performance = None
#     storage = None
#     current_generation = None
#     potential_savings = None
    
#     # Process and extract the price and other details
#     for price_item in response['PriceList']:
#         price_item_json = json.loads(price_item)
        
#         # Extract attributes
#         attributes = price_item_json['product']['attributes']
#         vcpus = attributes.get('vcpu')
#         memory = attributes.get('memory')
#         network_performance = attributes.get('networkPerformance')
#         storage = attributes.get('storage')
#         current_generation = attributes.get('currentGeneration')
        
#         # Extract on-demand price
#         on_demand_details = price_item_json['terms']['OnDemand']
#         for key, value in on_demand_details.items():
#             price_dimensions = value['priceDimensions']
#             for pd_key, pd_value in price_dimensions.items():
#                 price_per_hour = pd_value['pricePerUnit']['USD']
#                 break
        
#         # Extract potential savings (if applicable)
#         if 'PotentialSavings' in price_item_json:
#             potential_savings = price_item_json['PotentialSavings']
        
#         # Break if price is found
#         if price_per_hour:
#             break

#     # Return the details or an error message if not found
#     if price_per_hour:
#         return {
#             'statusCode': 200,
#             'body': json.dumps({
#                 'instanceType': instance_type,
#                 'pricePerHour': price_per_hour,
#                 'vCPUs': vcpus,
#                 'memory': memory,
#                 'networkPerformance': network_performance,
#                 'storage': storage,
#                 'currentGeneration': current_generation,
#                 'potentialSavings': potential_savings
#             })
#         }
#     else:
#         return {
#             'statusCode': 404,
#             'body': json.dumps({'error': 'Price information not found'})
#         }

# import boto3
# import json

# def lambda_handler(event, context):
#     # Extract instance types from query parameters (comma-separated values)
#     instance_types = event['queryStringParameters']['instanceType'].split(',')

#     # Initialize the Pricing client
#     client = boto3.client('pricing', region_name='us-east-1')

#     # Initialize a list to store pricing details for all instance types
#     pricing_details = []

#     # Iterate over each instance type and get pricing details
#     for instance_type in instance_types:
#         # Query the AWS Pricing API for the given instance type
#         response = client.get_products(
#             ServiceCode='AmazonEC2',
#             Filters=[
#                 {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type.strip()},
#                 {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
#                 {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
#                 {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
#                 {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
#             ],
#             MaxResults=10
#         )

#         # Initialize the details to be fetched
#         price_per_hour = None
#         vcpus = None
#         memory = None
#         network_performance = None
#         storage = None
#         current_generation = None
#         potential_savings = None

#         # Process and extract the price and other details
#         for price_item in response['PriceList']:
#             price_item_json = json.loads(price_item)
            
#             # Extract attributes
#             attributes = price_item_json['product']['attributes']
#             vcpus = attributes.get('vcpu')
#             memory = attributes.get('memory')
#             network_performance = attributes.get('networkPerformance')
#             storage = attributes.get('storage')
#             current_generation = attributes.get('currentGeneration')
            
#             # Extract on-demand price
#             on_demand_details = price_item_json['terms']['OnDemand']
#             for key, value in on_demand_details.items():
#                 price_dimensions = value['priceDimensions']
#                 for pd_key, pd_value in price_dimensions.items():
#                     price_per_hour = pd_value['pricePerUnit']['USD']
#                     break
            
#             # Extract potential savings (if applicable)
#             if 'PotentialSavings' in price_item_json:
#                 potential_savings = price_item_json['PotentialSavings']
            
#             # Break if price is found
#             if price_per_hour:
#                 break

#         # Add details to the list of pricing details
#         pricing_details.append({
#             'instanceType': instance_type,
#             'pricePerHour': price_per_hour,
#             'vCPUs': vcpus,
#             'memory': memory,
#             'networkPerformance': network_performance,
#             'storage': storage,
#             'currentGeneration': current_generation,
#             'potentialSavings': potential_savings
#         })

#     # Return the pricing details for all instance types
#     return {
#         'statusCode': 200,
#         'body': json.dumps(pricing_details)
#     }



#working code for specific instances
# import boto3
# import json

# def lambda_handler(event, context):
#     # Extract instance types from query parameters (comma-separated values)
#     instance_types = event['queryStringParameters']['instanceType'].split(',')

#     # Initialize the Pricing client
#     client = boto3.client('pricing', region_name='us-east-1')

#     # Initialize a list to store pricing details for all instance types
#     pricing_details = []

#     # Iterate over each instance type and get pricing details
#     for instance_type in instance_types:
#         # Query the AWS Pricing API for the given instance type
#         response = client.get_products(
#             ServiceCode='AmazonEC2',
#             Filters=[
#                 {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type.strip()},
#                 {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
#                 {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
#                 {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
#                 {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
#             ],
#             MaxResults=10
#         )

#         # Initialize the details to be fetched
#         price_per_hour = None
#         vcpus = None
#         memory = None
#         network_performance = None
#         storage = None
#         current_generation = None
#         potential_savings = None

#         # Process and extract the price and other details
#         for price_item in response['PriceList']:
#             price_item_json = json.loads(price_item)
            
#             # Extract attributes
#             attributes = price_item_json['product']['attributes']
#             vcpus = attributes.get('vcpu')
#             memory = attributes.get('memory')
#             network_performance = attributes.get('networkPerformance')
#             storage = attributes.get('storage')
#             current_generation = attributes.get('currentGeneration')
            
#             # # Extract on-demand price
#             # on_demand_details = price_item_json['terms']['OnDemand']
#             # for key, value in on_demand_details.items():
#             #     price_dimensions = value['priceDimensions']
#             #     for pd_key, pd_value in price_dimensions.items():
#             #         price_per_hour = pd_value['pricePerUnit']['USD']
#             #         break
            
#             # potential_savings = attributes.get('Potential Effective Hourly Cost (Savings %)')
                
            
#             # # Break if price is found
#             # if price_per_hour:
#             #     break

#             on_demand_details = price_item_json['terms']['OnDemand']
#             for key, value in on_demand_details.items():
#                 price_dimensions = value['priceDimensions']
#                 for pd_key, pd_value in price_dimensions.items():
#                     price_per_hour = pd_value['pricePerUnit']['USD']
#                     break
            
#                 # Extract potential savings (if applicable)
#                 attributes = price_item_json.get('product', {}).get('attributes', {})
#                 potential_savings = attributes.get('PotentialEffectiveHourlyCost')
                
#                 # Break if price is found
#                 if price_per_hour:
#                     break


#         # Add details to the list of pricing details
#         pricing_details.append({
#             'instanceType': instance_type,
#             'pricePerHour': price_per_hour,
#             'vCPUs': vcpus,
#             'memory': memory,
#             'networkPerformance': network_performance,
#             'storage': storage,
#             'currentGeneration': current_generation,
#             'PotentialEffectiveHourlyCost': potential_savings
#         })

#     # Return the pricing details for all instance types
#     return {
#         'statusCode': 200,
#         'body': json.dumps(pricing_details)
#     }


# import boto3
# import json

# def lambda_handler(event, context):
#     # Extract instance type prefixes from query parameters (comma-separated values)
#     prefixes = event['queryStringParameters']['instanceType'].split(',')
    
#     # Initialize the Pricing client
#     client = boto3.client('pricing', region_name='us-east-1')
    
#     # Initialize a list to store all filtered instance types
#     instance_types = set()
    
#     # Fetch all instance types (limit number of results to avoid long execution)
#     paginator = client.get_paginator('get_products')
#     for page in paginator.paginate(
#         ServiceCode='AmazonEC2',
#         Filters=[{'Type': 'TERM_MATCH', 'Field': 'serviceCode', 'Value': 'AmazonEC2'}],
#         MaxResults=50  # Adjust based on your needs
#     ):
#         for product in page['PriceList']:
#             product_json = json.loads(product)
#             attributes = product_json['product']['attributes']
#             instance_type = attributes.get('instanceType')
#             if instance_type:
#                 for prefix in prefixes:
#                     if instance_type.startswith(prefix):
#                         instance_types.add(instance_type)
#                         break
    
#     # Initialize a list to store pricing details
#     pricing_details = []

#     # Iterate over each instance type and get pricing details
#     for instance_type in instance_types:
#         # Query the AWS Pricing API for the given instance type
#         response = client.get_products(
#             ServiceCode='AmazonEC2',
#             Filters=[
#                 {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type.strip()},
#                 {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
#                 {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
#                 {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
#                 {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
#             ],
#             MaxResults=10
#         )

#         # Initialize the details to be fetched
#         price_per_hour = None
#         vcpus = None
#         memory = None
#         network_performance = None
#         storage = None
#         current_generation = None
#         potential_savings = None

#         # Process and extract the price and other details
#         for price_item in response['PriceList']:
#             price_item_json = json.loads(price_item)
            
#             # Extract attributes
#             attributes = price_item_json['product']['attributes']
#             vcpus = attributes.get('vcpu')
#             memory = attributes.get('memory')
#             network_performance = attributes.get('networkPerformance')
#             storage = attributes.get('storage')
#             current_generation = attributes.get('currentGeneration')
            
#             # Extract on-demand price
#             on_demand_details = price_item_json['terms']['OnDemand']
#             for key, value in on_demand_details.items():
#                 price_dimensions = value['priceDimensions']
#                 for pd_key, pd_value in price_dimensions.items():
#                     price_per_hour = pd_value['pricePerUnit']['USD']
#                     break
            
#                 # Extract potential savings (if applicable)
#                 potential_savings = attributes.get('PotentialEffectiveHourlyCost')
                
#                 # Break if price is found
#                 if price_per_hour:
#                     break

#         # Add details to the list of pricing details
#         pricing_details.append({
#             'instanceType': instance_type,
#             'pricePerHour': price_per_hour,
#             'vCPUs': vcpus,
#             'memory': memory,
#             'networkPerformance': network_performance,
#             'storage': storage,
#             'currentGeneration': current_generation,
#             'PotentialEffectiveHourlyCost': potential_savings
#         })

#     # Return the pricing details for all instance types
#     return {
#         'statusCode': 200,
#         'body': json.dumps(pricing_details)
#     }




# import boto3
# import json

# def lambda_handler(event, context):
#     # Extract instance types from query parameters (comma-separated values)
#     instance_types = event['queryStringParameters']['instanceType'].split(',')

#     # Initialize the Pricing client
#     client = boto3.client('pricing', region_name='us-east-1')

#     # Initialize a list to store pricing details for all instance types
#     pricing_details = []

#     # Iterate over each instance type and get pricing details
#     for instance_type in instance_types:
#         # Query the AWS Pricing API for the given instance type
#         response = client.get_products(
#             ServiceCode='AmazonEC2',
#             Filters=[
#                 {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type.strip()},
#                 {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
#                 {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
#                 {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
#                 {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
#             ],
#             MaxResults=10
#         )

#         # Initialize the details to be fetched
#         price_per_hour = None
#         vcpus = None
#         memory = None
#         network_performance = None
#         storage = None
#         current_generation = None
#         potential_savings = None

#         # Process and extract the price and other details
#         for price_item in response['PriceList']:
#             price_item_json = json.loads(price_item)
            
#             # Extract attributes
#             attributes = price_item_json['product']['attributes']
#             vcpus = attributes.get('vcpu')
#             memory = attributes.get('memory')
#             network_performance = attributes.get('networkPerformance')
#             storage = attributes.get('storage')
#             current_generation = attributes.get('currentGeneration')
            
#             # Extract on-demand price
#             on_demand_details = price_item_json['terms']['OnDemand']
#             for key, value in on_demand_details.items():
#                 price_dimensions = value['priceDimensions']
#                 for pd_key, pd_value in price_dimensions.items():
#                     price_per_hour = pd_value['pricePerUnit'].get('USD', None)
#                     break
            
#             # Extract potential savings (if applicable)
#             potential_savings = attributes.get('PotentialEffectiveHourlyCost')
                
#             # Break if price is found
#             if price_per_hour:
#                 break

#         # Add details to the list of pricing details
#         pricing_details.append({
#             'instanceType': instance_type,
#             'pricePerHour': price_per_hour,
#             'vCPUs': vcpus,
#             'memory': memory,
#             'networkPerformance': network_performance,
#             'storage': storage,
#             'currentGeneration': current_generation,
#             'PotentialEffectiveHourlyCost': potential_savings
#         })

#     # Return the pricing details for all instance types
#     return {
#         'statusCode': 200,
#         'body': json.dumps(pricing_details)
#     }


#req satisfied partially
# import boto3
# import json

# def lambda_handler(event, context):
#     # Extract instance families from query parameters (comma-separated values)
#     instance_families = event['queryStringParameters']['instanceType'].split(',')

#     # Initialize the Pricing client
#     client = boto3.client('pricing', region_name='us-east-1')

#     # Initialize a list to store pricing details for all instances in the families
#     pricing_details = []

#     # Query the AWS Pricing API for all EC2 instances
#     response = client.get_products(
#         ServiceCode='AmazonEC2',
#         Filters=[
#             {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
#             {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
#             {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
#             {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
#         ],
#         MaxResults=100  # Fetch more if needed
#     )

#     # Process and extract the price and other details
#     for price_item in response['PriceList']:
#         price_item_json = json.loads(price_item)
        
#         # Extract attributes
#         attributes = price_item_json['product']['attributes']
#         instance_type = attributes.get('instanceType')

#         # Check if the instance type belongs to one of the provided families
#         if any(instance_type.startswith(family.strip()) for family in instance_families):
#             vcpus = attributes.get('vcpu')
#             memory = attributes.get('memory')
#             network_performance = attributes.get('networkPerformance')
#             storage = attributes.get('storage')
#             current_generation = attributes.get('currentGeneration')

#             # Extract on-demand price
#             price_per_hour = None
#             on_demand_details = price_item_json['terms']['OnDemand']
#             for key, value in on_demand_details.items():
#                 price_dimensions = value['priceDimensions']
#                 for pd_key, pd_value in price_dimensions.items():
#                     price_per_hour = pd_value['pricePerUnit'].get('USD', None)
#                     break

#             # Extract potential savings (if applicable)
#             potential_savings = attributes.get('PotentialEffectiveHourlyCost')

#             # Add details to the list of pricing details
#             pricing_details.append({
#                 'instanceType': instance_type,
#                 'pricePerHour': price_per_hour,
#                 'vCPUs': vcpus,
#                 'memory': memory,
#                 'networkPerformance': network_performance,
#                 'storage': storage,
#                 'currentGeneration': current_generation,
#                 'PotentialEffectiveHourlyCost': potential_savings
#             })

#     # Return the pricing details for all instance types in the families
#     return {
#         'statusCode': 200,
#         'body': json.dumps(pricing_details)
#     }