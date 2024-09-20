#all req staisfied
import boto3
import json

def lambda_handler(event, context):
    # Extract instance families from query parameters (comma-separated values)
    instance_families = event['queryStringParameters']['instanceType'].split(',')

    # Initialize the Pricing client
    client = boto3.client('pricing', region_name='us-east-1')

    # Initialize a list to store pricing details for all instances in the families
    pricing_details = []
    next_token = None

    # Pagination loop to ensure all results are fetched
    while True:
        # Query the AWS Pricing API for all EC2 instances (with pagination handling)
        if next_token:
            response = client.get_products(
                ServiceCode='AmazonEC2',
                Filters=[
                    {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
                    {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
                    {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
                    {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
                ],
                MaxResults=100,
                NextToken=next_token
            )
        else:
            response = client.get_products(
                ServiceCode='AmazonEC2',
                Filters=[
                    {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'},
                    {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
                    {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
                    {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
                ],
                MaxResults=100
            )
        
        # Process and extract the price and other details
        for price_item in response['PriceList']:
            price_item_json = json.loads(price_item)
            
            # Extract attributes
            attributes = price_item_json['product']['attributes']
            instance_type = attributes.get('instanceType')

            # Check if the instance type belongs to one of the provided families
            if any(instance_type.startswith(family.strip()) for family in instance_families):
                vcpus = attributes.get('vcpu')
                memory = attributes.get('memory')
                network_performance = attributes.get('networkPerformance')
                storage = attributes.get('storage')
                current_generation = attributes.get('currentGeneration')

                # Extract on-demand price
                price_per_hour = None
                on_demand_details = price_item_json['terms']['OnDemand']
                for key, value in on_demand_details.items():
                    price_dimensions = value['priceDimensions']
                    for pd_key, pd_value in price_dimensions.items():
                        price_per_hour = pd_value['pricePerUnit'].get('USD', None)
                        break

                # Extract potential savings (if applicable)
                potential_savings = attributes.get('PotentialEffectiveHourlyCost')

                # Add details to the list of pricing details
                pricing_details.append({
                    'instanceType': instance_type,
                    'pricePerHour': price_per_hour,
                    'vCPUs': vcpus,
                    'memory': memory,
                    'networkPerformance': network_performance,
                    'storage': storage,
                    'currentGeneration': current_generation,
                    'PotentialEffectiveHourlyCost': potential_savings
                })

        # Handle pagination
        next_token = response.get('NextToken')
        if not next_token:
            break

    # Return the pricing details for all instance types in the families
    return {
        'statusCode': 200,
        'body': json.dumps(pricing_details)
    }
