
# Before calling the API, replace filename and ensure sdk is installed: "pip install unstructured-client"
# See https://docs.unstructured.io/api-reference/api-services/sdk for more details

import unstructured_client
from unstructured_client.models import operations, shared

client = unstructured_client.UnstructuredClient(
    api_key_auth="RCDI0O10u4aXZvMLNnUiDg8yrSSMXI",
    server_url="https://api.unstructuredapp.io/general/v0/general",
)

filename = "/workspaces/gpt-researcher/docs/docs/gpt-researcher/tailored-research.md"
with open(filename, "rb") as f:
    data = f.read()

req = operations.PartitionRequest(
    partition_parameters=shared.PartitionParameters(
        files=shared.Files(
            content=data,
            file_name=filename,
        ),
        # --- Other partition parameters ---
        # Note: Defining 'strategy', 'chunking_strategy', and 'output_format'
        # parameters as strings is accepted, but will not pass strict type checking. It is
        # advised to use the defined enum classes as shown below.
        strategy=shared.Strategy.AUTO,  
        languages=['eng'],
        split_pdf_allow_failed=True
    ),
)

try:
    res = client.general.partition(request=req)
    print(res.elements[0])
except Exception as e:
    print(e)
