from jdc_utils.core_measures import schemas
import pandas as pd
from collections import OrderedDict

modules = ["Record and linkage", "PROMIS 29+2/ PROPr"]
timepoint_fields = [
    dict(OrderedDict(field))
    for field in schemas.timepoints["fields"]
    if field["module"] in modules
]

excluded_names = ["quarter_enrolled"]
baseline_fields = [
    dict(OrderedDict(field))
    for field in schemas.baseline["fields"]
    if not field["name"] in excluded_names
]