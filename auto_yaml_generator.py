import yaml
import argparse
import re 

def process_yaml(path, output_path, **kwargs):

    with open(path, 'r') as file:
        template = file.read()

    for key, value in kwargs.items():
        pattern = r'\{' + key + r'\}'
        template = re.sub(pattern, str(value), template)


    with open(output_path, 'w') as file:
        file.write(template)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description ="Process SQL YAML")
    parser.add_argument("--template", required=True, help="Path to the template")
    parser.add_argument("--output", required=True)
    parser.add_argument("--category", required=True)
   #parser.add_argument("--FREQUENCY", required=True)
    parser.add_argument("--enabled", required=True)
    parser.add_argument("--test_folder", required=True)
    parser.add_argument("--production_folder", required=True)
    parser.add_argument("--hostname", required=True)
    parser.add_argument("--FREQUENCY", required=True)
    parser.add_argument("--port", required=True)
    parser.add_argument("--username", required=True)
    parser.add_argument("--name_prefix", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--program", required=False)

    args = parser.parse_args()

    process_yaml(
        args.template,
        args.output,
        category=args.category,
        FREQUENCY= args.FREQUENCY,
        enabled=args.enabled,
        test_folder=args.test_folder,
        production_folder= args.production_folder,
        hostname= args.hostname,
        port=args.port,
        username = args.username,
        name_prefix=args.name_prefix,
        format = args.format,
        #program =args.program
    )

    print(f"processed file generated to {args.output}")
