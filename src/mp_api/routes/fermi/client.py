from mp_api.core.client import BaseRester
from mp_api.routes.fermi.models import FermiDoc

from collections import defaultdict
from typing import Optional, List
import warnings


class FermiRester(BaseRester):

    suffix = "fermi"
    document_model = FermiDoc  # type: ignore
