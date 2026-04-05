# WildSentinel – Predictive Zoonotic Spillover Risk Analysis

## Overview
WildSentinel is a data-driven bio-surveillance system designed to predict zoonotic disease spillover risks at the human–wildlife interface. The system integrates ecological, environmental, and trade-related datasets to identify high-risk regions and provide early warning insights for potential outbreaks.

By combining machine learning, geospatial analysis, and network-based modeling, WildSentinel enables proactive monitoring and supports data-driven decision-making aligned with the One Health approach.

---

## Key Features
- Geospatial risk mapping of zoonotic spillover hotspots  
- Integration of multi-source datasets (trade, biodiversity, land use, outbreaks)  
- Machine learning-based risk prediction (low, moderate, high risk classification)  
- Network-based modeling of wildlife–human interactions  
- Scenario simulation using Monte Carlo methods  
- Data-driven insights for biosurveillance and policy  

---

## System Architecture

### Data Layer
- Wildlife trade data (CITES)  
- Species distribution data (GBIF)  
- Satellite imagery (NASA MODIS)  
- Historical outbreak data (WHO / WAHIS)  

### Data Processing
- Data cleaning and normalization  
- Geospatial alignment and raster processing  
- Feature engineering (trade intensity, forest fragmentation, biodiversity indices)  

### Modeling
- Machine learning model (XGBoost classifier)  
- Network-based analytical framework  
- Temporal training (pre-2020) and testing (2021–2024)  

### Simulation
- Monte Carlo-based scenario simulations  
- Trade reduction, forest restoration, biosurveillance improvements  

### Visualization
- Interactive heatmaps using Leaflet.js  
- Risk probability mapping  
- Temporal analysis across multiple years  

---

## Technologies Used

- Programming: Python  
- Libraries: Pandas, NumPy, Scikit-learn  
- Machine Learning: XGBoost  
- Geospatial: Google Earth Engine, GeoJSON, Raster Processing  
- Visualization: Leaflet.js  
- Data Sources: CITES, GBIF, NASA MODIS, WHO  

---

## How It Works
1. Multi-source datasets are collected and preprocessed  
2. Key features such as trade intensity, forest loss, and species richness are extracted  
3. A machine learning model predicts spillover probability  
4. Results are mapped as geospatial heatmaps  
5. Scenario simulations evaluate the impact of interventions  

---

## Results
- AUC-ROC Score: 0.87  
- AUC-PR Score: 0.67  
- Strong detection of outbreak-prone regions  

Key contributing factors:
- Wildlife trade intensity  
- Deforestation rate  
- Species richness  

---

## Insights
- High spillover risk is strongly linked to habitat destruction and wildlife trade  
- Regions with high human–animal interaction show elevated risk  
- Preventive measures like trade reduction and forest restoration significantly reduce predicted risk  

---

## Future Work
- Integration with real-time data sources  
- Advanced machine learning models  
- Cloud deployment for scalability  
- Enhanced decision-support tools  

---

## Publication
WildSentinel: Safeguarding the Human–Wildlife Interface  
International Journal of Advanced Research (IJAR), 2026  

DOI: http://dx.doi.org/10.21474/IJAR01/22705  

---

## Contributors
- Gopal Bansal  
- Avyav Saraf  
- Amogh S  
- Namitha G  
- Dayakara Sharvani  
- Harsh Jain
