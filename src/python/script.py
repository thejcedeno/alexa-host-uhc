
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
    game_host: str  # ideally a UUID
    scenarios: List[str]
    nether: bool
    end: bool


@dataclass
class Requestor:
    """ Represents the requestor of a server creation request. """
    # A uniqu id for the requestor
    id: str
    # The name of the requestor
    name: str
    # The email of the requestor
    email: str


@dataclass
class ServerCreationRequest:
    # The name of the docker image to be used in the deployment
    container_image: str
    resources: ResourceAllocationRequest
    requestor: Requestor


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
    region = get_region(req)
    plan = get_optimal_plan(req)

    # Run a bash command to terraform deploy
    terraform_cmd = ['terraform', 'apply', '-var',
                     f'vm_name={vm_name}', '-var', f'region={region}', '-var', f'plan={plan}', '-var', 'os_id=387']
    
    print(f'Running command: {terraform_cmd}')

    # Run the Terraform command
    result = subprocess.run(terraform_cmd, capture_output=True)

    # Print the output of the Terraform command
    print(result.stdout.decode())


def generate_unique_match_game(user_creation_request: ServerCreationRequest) -> str:
    """ Generates a unique match game name. """
    return '1234-1234-1234-1234'


def get_region(req: ServerCreationRequest) -> str:
    """ Gets the region of the server. """
    return 'nrt'


def get_optimal_plan(req: ServerCreationRequest) -> str:
    """ Gets the optimal plan for the server. """
    return 'vc2-1c-1gb'


create_infraestructure(ServerCreationRequest("doesn't matter now lol xd.", ResourceAllocationRequest('e085d739-25e3-4990-a2ec-98e84f5e03d9',
                       1024, 1, InstanceType.SHARED), Requestor('5de6e184-af8d-498a-bbde-055e50653316', 'jcedeno', 'jcedeno@jcedeno.us')))
