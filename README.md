# Valenbisi Bike Network Analysis

## Overview

This project presents an analysis of the Valenbisi bike-sharing system in Valencia, Spain, with the aim of improving user experience and operational efficiency. It explores spatial and temporal usage patterns and investigates how external factors like weather, holidays, and events influence demand.

The analysis is based on data collected from December 2022 to February 2024 and includes clustering methods to identify station-level behaviors and challenges.

## Authors

- **Anna Kapitánová** – Czech Technical University in Prague  
- **Pablo Díaz-Masa** – Universitat Politècnica de València  
- 📧 kapitann@fit.cvut.cz  
- 📧 pdiamas@etsinf.upv.es

## Full Report

The full technical report with detailed analysis, figures, and references is available here:  
📄 [`text/RED_TEAM__Anna__Pablo.pdf`](text/RED_TEAM__Anna__Pablo.pdf)

## Objectives

- Evaluate historical bike usage trends
- Identify problematic stations and usage imbalances
- Analyze the impact of external factors (weather, holidays, events)
- Recommend improvements for station distribution and bike availability

## Data Sources

- **Valenbisi Usage Data** – 15-minute updates on station status  
- **Weather Data** – Hourly data on temperature, precipitation, etc.  
- **Festivities Data** – Public holidays and weekend classification

## Methodology

### Data Processing

- Standardized multiple data formats across time ranges
- Merged datasets using timestamp and location
- Calculated derived features: occupancy, vacancy, usage changes

### Clustering

- **Geographical Clustering** – Based on station coordinates  
- **Behavioral Clustering** – Based on hourly usage patterns

### Analysis Dimensions

- Station size vs. usage
- Hourly, daily, monthly variation
- Holiday vs. working day impact
- Weather impact (temperature, sky condition, rain)

## Visualization Highlights

- Cluster maps (location & behavior)
- Time-based and weather-based usage trends
- Occupancy/vacancy indicators for individual stations

## Conclusion

The study suggests that Valencia’s Valenbisi system can benefit from:
- Redistributing bikes based on behavioral clusters
- Expanding capacity in high-demand zones
- Adjusting supply dynamically based on weather and calendar data

These insights lay the groundwork for smarter, more adaptive urban mobility solutions.



## License

This project is intended for academic and urban planning purposes. Contact the authors for other use cases.
