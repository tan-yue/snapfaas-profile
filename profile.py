"""Ubuntu 16.04; kernel 4.15"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node node
node = request.RawPC('node')
node.disk_image = 'urn:publicid:IDN+clemson.cloudlab.us+image+praxis-PG0:firecracker'
node.hardware_type = 'c220g5'
bs = node.Blockstore("bs", "/mydata")
bs.size = "50GB"

# Print the generated rspec
pc.printRequestRSpec(request)