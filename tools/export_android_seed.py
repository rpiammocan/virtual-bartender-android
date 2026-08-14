import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "build-source" / "backend" / "app"
OUTPUT = ROOT / "build-source" / "frontend" / "src" / "androidSeed.ts"


def assignments(path: Path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    values = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                values[node.targets[0].id] = ast.literal_eval(node.value)
            except Exception:
                pass
    return values


seed = assignments(SOURCE / "seed.py")
v2 = assignments(SOURCE / "catalog_v2.py")
v3 = assignments(SOURCE / "catalog_v3.py")
v4 = assignments(SOURCE / "catalog_v4.py")
v5 = assignments(SOURCE / "catalog_v5.py")

units = seed["BUILTIN_UNITS"]
ingredient_rows = seed["BASE_INGREDIENTS"] + v2["INGREDIENTS_V2"]
recipes_raw = seed["BASE_RECIPES"] + v2["RECIPES_V2"] + v3["RECIPES_V3"] + v4["RECIPES_V4"] + v5["RECIPES_V5"]
substitutions_raw = v2["SUBSTITUTIONS_V2"]
image_metadata = seed.get("IMAGE_METADATA", {})

# Stable deterministic IDs inside the Android edition.
ingredients = []
ingredient_id = {}
for name, category in ingredient_rows:
    if name in ingredient_id:
        continue
    iid = len(ingredients) + 1
    ingredient_id[name] = iid
    ingredients.append({"id": iid, "name": name, "category": category, "is_user_created": False, "is_active": True})

unit_by_abbr = {u["abbreviation"]: {**u, "id": i + 1} for i, u in enumerate(units)}
recipe_id_by_key = {r["key"]: i + 1 for i, r in enumerate(recipes_raw)}
recipes = []
for raw in recipes_raw:
    rid = recipe_id_by_key[raw["key"]]
    ingredients_out = []
    for idx, (name, quantity, unit, optional) in enumerate(raw["ingredients"], 1):
        ingredients_out.append({
            "id": idx,
            "ingredient_id": ingredient_id[name],
            "ingredient_name": name,
            "quantity": quantity,
            "unit": unit,
            "is_optional": optional,
            "notes": None,
        })
    meta = image_metadata.get(raw["key"], {})
    recipes.append({
        "id": rid,
        "built_in_key": raw["key"],
        "name": raw["name"],
        "description": raw.get("description"),
        "recipe_type": raw.get("type", "cocktail"),
        "source_type": "built_in",
        "instructions": raw.get("instructions"),
        "image_path": meta.get("image_path"),
        "image_ai_generated": meta.get("image_ai_generated", False),
        "parent_recipe_id": recipe_id_by_key.get(raw.get("parent")) if raw.get("parent") else None,
        "active": True,
        "ingredients": ingredients_out,
    })

substitutions = []
for required, substitute, priority in substitutions_raw:
    substitutions.append({
        "required_ingredient_id": ingredient_id[required],
        "substitute_ingredient_id": ingredient_id[substitute],
        "priority": priority,
    })

payload = {
    "schemaVersion": 1,
    "ingredients": ingredients,
    "recipes": recipes,
    "substitutions": substitutions,
    "units": list(unit_by_abbr.values()),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text("const androidSeed = " + json.dumps(payload, ensure_ascii=False) + " as const;\nexport default androidSeed;\n", encoding="utf-8")
print(f"Generated {len(recipes)} recipes and {len(ingredients)} ingredients -> {OUTPUT}")
