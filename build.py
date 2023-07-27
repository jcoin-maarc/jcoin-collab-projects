from jdc_utils.core_measures import schemas
import pandas as pd
from collections import OrderedDict
import yaml
import json
from pathlib import Path

# get promis time points schema (only with derived variables) from dictionary
promis_schema = yaml.safe_load(Path("schemas/dictionary/promis.yaml").read_text())
promis_modules = ["Record and linkage", "PROMIS 29+2/ PROPr"]
promis_schema["fields"] = [
    dict(OrderedDict(field))
    for field in schemas.timepoints["fields"]
    if field["module"] in promis_modules
] + promis_schema["fields"]


# baseline schema
baseline_schema = dict(schemas.baseline)
baseline_modules = ["Record and linkage","Demographics"]
excluded_names = ["quarter_enrolled"]
baseline_schema["fields"] = [
    dict(OrderedDict(field))
    for field in schemas.baseline["fields"]
    if not field["name"] in excluded_names 
        and field["module"] in baseline_modules
]

# write to json
Path("schemas/promis").mkdir(exist_ok=True)
Path("schemas/promis/timepoints_promis.json").write_text(json.dumps(promis_schema,indent=2))
Path("schemas/promis/baseline.json").write_text(json.dumps(baseline_schema,indent=2))
