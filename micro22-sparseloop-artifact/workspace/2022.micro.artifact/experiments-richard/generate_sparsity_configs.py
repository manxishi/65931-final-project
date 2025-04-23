import yaml
import os

# Base configuration
base_config = {
    'problem': {
        'shape': {
            'name': '1DCONV',
            'dimensions': ['R', 'E', 'C', 'M', 'N'],
            'coefficients': [
                {'name': 'Wstride', 'default': 1},
                {'name': 'Wdilation', 'default': 1}
            ],
            'data-spaces': [
                {
                    'name': 'Weights',
                    'projection': [
                        [['M']],
                        [['C']],
                        [['R']]
                    ]
                },
                {
                    'name': 'Inputs',
                    'projection': [
                        [['N']],
                        [['C']],
                        [['R', 'Wdilation'], ['E', 'Wstride']]
                    ]
                },
                {
                    'name': 'Outputs',
                    'projection': [
                        [['N']],
                        [['M']],
                        [['E']]
                    ],
                    'read-write': True
                }
            ]
        },
        'instance': {
            'M': 64,
            'E': 32,
            'R': 1,
            'N': 1,
            'C': 64,
            'densities': {
                'Inputs': {
                    'distribution': 'hypergeometric',
                    'density': 1.0
                },
                'Weights': {
                    'distribution': 'hypergeometric',
                    'density': 1.0
                }
            }
        }
    }
}

# Create output directory
output_dir = 'sparsity_testing'
os.makedirs(output_dir, exist_ok=True)

# Density values to test
density_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Generate configs for different density combinations
for input_density in density_values:
    for weight_density in density_values:
        config = base_config.copy()
        config['problem']['instance']['densities']['Inputs']['density'] = input_density
        config['problem']['instance']['densities']['Weights']['density'] = weight_density
        
        # Create filename based on densities
        filename = f'1dconv_input{input_density}_weight{weight_density}.yaml'
        filepath = os.path.join(output_dir, filename)
        
        # Write to file
        with open(filepath, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print(f"Generated {len(density_values) * len(density_values)} configuration files in {output_dir}") 