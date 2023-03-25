
from dataclasses import dataclass
from typing import List

import subprocess

from enum import Enum

class InstanceType(Enum):
    SHARED = 'shared'
    DEDICATED = 'dedicated'
    COMPUTE_OPTIMIZED = 'compute_optimized'
    HIGH_FREQUENCY = 'high_frequency'
    BAREMETAL = 'baremetal'
    
class TerrainType(Enum):
    VANILLA = 'vanilla'
    RUN = 'run'

@dataclass
class ResourceAllocationRequest:
    """ Represents the request to allocate resources to a server. """
    # A tracking id for the request
    id: str
    # The amount of memory to allocate in MiB
    memoryInMib: int
    # The amount of cpus to allocate
    cpus: int
    # The type of instance to allocate
    instance_type: InstanceType
    
@dataclass
class GameConfig:
    """ A class to hold UHC match game config. """
    world_seed: str
    terrain_generation: TerrainType
    game_host: str # ideally a UUID
    scenarios: List[str]
    nether: bool
    end: bool
    

@dataclass
class ServerCreationRequest:
    # The name of the docker image to be used in the deployment
    container_image: str
    resources: ResourceAllocationRequest
    
    
@dataclass
class ServerCreationResponse:
    """ Represents the response to a server creation request. """
    # A tracking id for the request
    id: str
    # The name of the server
    name: str
    # The ip address of the server
    ip_address: str
    # The port of the server
    port: int
    # The game config of the server
    game_config: GameConfig
    

# Post request
def create_infraestructure(req: ServerCreationRequest) -> ServerCreationResponse:
    """ Deploys new infraestructure from provided template."""
    # declare variables
    vm_name = generate_unique_match_game(req)
    
    
    # Run a bash command to terraform deploy
    terraform_cmd = ['terraform', 'apply', '-var', 'vm_name=my-vm', '-var', 'region=nrt', '-var', 'plan=vc2-1c-1gb', '-var', 'os_id=387']

    # Run the Terraform command
    result = subprocess.run(terraform_cmd, capture_output=True)

    # Print the output of the Terraform command
    print(result.stdout.decode())
    
def generate_unique_match_game(user_creation_request: ServerCreationRequest) -> str:
    """ Generates a unique match game name. """
    return '1234-1234-1234-1234'
