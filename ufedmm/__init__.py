"""
AFED for OpenMM
Unified Free Energy Dynamics with OpenMM

"""


from ._version import get_versions
from .ufedmm import CollectiveVariable, UnifiedFreeEnergyDynamics  # noqa: F401, F403
from .integrators import CustomIntegrator, GeodesicBAOABIntegrator  # noqa: F401, F403
from .output import MultipleFiles, StateDataReporter  # noqa: F401, F403
from .testmodels import AlanineDipeptideModel  # noqa: F401, F403

# Handle versioneer:
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
