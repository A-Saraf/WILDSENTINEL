from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import os
import json
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "static", "data", "MASTER_TRAINING_DATA.csv")

MASTER = pd.read_csv(csv_path)
UNIQUE_COUNTRIES = sorted(MASTER["Country"].dropna().unique().tolist())


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/risk")
def analytics_page():
    return render_template("prediction.html", countries=UNIQUE_COUNTRIES)  # Your input + heatmap page

@app.route("/predict_policy", methods=["POST"])
def predict_policy():
    try:
        country = request.form["country"]
        forest_pct = float(request.form["forest_pct"])
        urban_pct  = float(request.form["urban_pct"])
        import_pct = float(request.form["import_pct"])
        export_pct = float(request.form["export_pct"])

        # Filter master dataset
        df = MASTER[(MASTER["Country"] == country) & (MASTER["Year"] == 2024)].copy()
        if df.empty:
            return jsonify({"error": "No 2024 data found for this country"}), 400

        # Apply % modifications
        df["percent_forest"] *= (1 + forest_pct/100)
        df["percent_urban"]  *= (1 + urban_pct/100)

        df["total_import_events"] *= (1 + import_pct/100)
        df["total_live_imports"]  *= (1 + import_pct/100)

        df["total_export_events"] *= (1 + export_pct/100)
        df["total_live_exports"]  *= (1 + export_pct/100)

        df["percent_forest"] = df["percent_forest"].clip(0,100)
        df["percent_urban"]  = df["percent_urban"].clip(0,100)

        # Load XGB model (matches dataset)
        model = joblib.load(
            r"C:\Users\gopal\Desktop\WILDSENTINEL\model\new_model\trained_model_xgb.joblib"
        )

        FEATURES = [
            "percent_forest", "percent_urban",
            "forest_change_rate", "urban_change_rate",
            "species_richness", "zoonotic_host_count",
            "total_import_events", "total_live_imports",
            "total_export_events", "total_live_exports"
        ]

        df = df.dropna(subset=FEATURES)

        df["prob"] = model.predict_proba(df[FEATURES])[:, 1]

        result = df[["lat","lon","prob"]].to_dict(orient="records")
        return jsonify(result)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

  



@app.route("/genai")
def genai():
    return render_template("genai.html")

@app.route("/about")
def about_us_page():
    return render_template("about_us.html")


# -----------------------------
# MAIN ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
