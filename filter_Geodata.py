import json
from pathlib import Path

src = Path("NUTS_RG_20M_2024_4326.geojson")
dst = Path("IrelandGeo.json")

with src.open("r", encoding="utf-8") as f:
    nuts = json.load(f)

clean_features = []
for feat in nuts["features"]:
    props = feat.get("properties", {})
    if props.get("CNTR_CODE") == "IE" and props.get("LEVL_CODE") == 3:
        # strip unwanted whitespace
        if "NAME_LATN" in props:
            props["NAME_LATN"] = props["NAME_LATN"].strip()
        if "NUTS_NAME" in props:
            props["NUTS_NAME"] = props["NUTS_NAME"].strip()
        feat["properties"] = props
        clean_features.append(feat)

ireland_geo = {
    "type": "FeatureCollection",
    "features": clean_features,
}

with dst.open("w", encoding="utf-8") as f:
    json.dump(ireland_geo, f, ensure_ascii=False)
