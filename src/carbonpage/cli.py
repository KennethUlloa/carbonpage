import argparse

def main():
    import importlib
    import sys
    import os

    sys.path.append(os.getcwd())
    
    parser = argparse.ArgumentParser(description='Project template tool')
    parser.add_argument('template', help='Template to use')
    parser.add_argument('--settings','-s', help='Settings module', default='carbon_settings')

    args = parser.parse_args()
    
    settings = importlib.import_module(args.settings)
    template = settings.TEMPLATES.get(args.template)
    if not template:
        print(f"Template {args.template} not found")
        return
    
    from carbonpage.templates import CarbonTemplate

    if isinstance(template, dict):
        template = CarbonTemplate(**template)

    if isinstance(template, CarbonTemplate):
        template.render()
        print("Done")
    else:
        print(f"Template {args.template} is not a valid template")
        return

if __name__ == "__main__":
    main()

