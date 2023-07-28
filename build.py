from jdc_utils.core_measures import schemas,encodings
from dataforge.frictionless import encode_table
import pandas as pd
from frictionless import Resource
from collections import OrderedDict
import yaml
import json
from pathlib import Path

# promis time points schema (only with derived variables) from dictionary
promis_schema = yaml.safe_load(Path("schemas/dictionary/promis.yaml").read_text())
# promis_modules = ["Record and linkage", "PROMIS"]
# timepoints_url = ("https://raw.githubusercontent.com/jcoin-maarc/"
#     "jdc-utilities/mbkranz/derived-measures/data/core-measures-test/"
#     "data/timepoints.csv")
# encoded_schema = (
#     Resource(data=timepoints_url,schema=schemas.timepoints)
#     .transform(steps=[encode_table(encodings=encodings.fields)])
# ).schema


# promis_schema["fields"] = [
#     dict(OrderedDict(field))
#     for field in encoded_schema["fields"]
#     if field["module"] in promis_modules
# ] + promis_schema["fields"]


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

# cols = {
#         "PROMIS - Pain intensity":["pain_intensity"], # not used in calcs
#         "PROMIS - Anxiety":[
#             "past_week_fearful",
#             "past_week_anxiety",
#             "past_week_worried",
#             "past_week_uneasy",
#         ],
#         "PROMIS - Social Roles and Activities":[
#             "trouble_with_leisure",
#             "trouble_with_family",
#             "trouble_with_work",
#             "trouble_with_activities",
#         ],
#         "PROMIS - Cognitive":["can_concentrate", "can_remember"],
#         "PROMIS - Depression":[
#             "past_week_worthless",
#             "past_week_helpless",
#             "past_week_depressed",
#             "past_week_hopeless",
#         ],
#         "PROMIS - Fatigue":[
#             "past_week_fatigued",
#             "past_week_tired",
#             "past_week_rundown",
#             "fatigue_level",
#         ],
#         "PROMIS - Pain interference":[
#             "pain_daily_activity",
#             "pain_work_around_house",
#             "pain_social_activity",
#             "pain_household_chores",
#         ],
#         "PROMIS - Physical Activity":[
#             "difficulty_chores",
#             "difficulty_stairs",
#             "difficulty_walking",
#             "difficulty_traveling",
#         ],
#         "PROMIS - Sleep difficulty":[
#             "sleep_quality",
#             "sleep_refreshing",
#             "sleep_problems",
#             "sleep_difficulty",
#         ]
# }

# df = pd.DataFrame(json.loads(Path("test.json").read_text())).set_index("name")

# for module,colnames in cols.items():
#     df.loc[colnames,"module"] = module
