import boto3
from os.path import dirname

session = boto3.Session(region_name='ap-southeast-2')

cfnclient = session.client('cloudformation')

script_dir = dirname(__file__)
print(script_dir)

stack = ''
with open(f"{script_dir}/stack.yml", 'r') as fd:
    stack = fd.read()

print(stack)

params: [
    {
        'ParameterKey': 'test',
        'ParameterValue': 'test'
    }
]

#cfnclient.create_stack(StackName='sinatra', TemplateBody=stack, Parameters=params)

cfnclient.describe_stacks()