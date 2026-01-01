import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Scientific Visualization", layout="wide")
st.title("Scientific Visualization Dashboard")

# --- Debug: list files in the repo ---
st.write("Files in current folder:", os.listdir())

# --- Load CSV ---
try:
    df = pd.read_csv("cleaned_student_study_dataset_FINAL.csv")
    st.success("CSV loaded successfully!")
except FileNotFoundError:
    st.error("CSV not found! Make sure cleaned_student_study_dataset_FINAL.csv is in the same folder as app.py")

# --- Create 3 tabs ---
tab1, tab2, tab3 = st.tabs(["Page 1: Study Techniques", "Page 2: Stress & Motivation", "Page 3: Learning Obstacles & Support"])

# ================= PAGE 1 =================
with tab1:
    st.header("Page 1 Visualizations - Study Techniques")
    freq_cols = ["freq_reading","freq_videos","freq_practice","freq_group",
                 "freq_summary","freq_flashcards","freq_teaching"]
    freq_means = df[freq_cols].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(9,5))
    ax.bar(freq_means.index, freq_means.values)
    ax.set_ylabel("Mean Frequency Score (1–5)")
    ax.set_xticklabels(freq_means.index, rotation=45, ha="right")
    st.pyplot(fig)

    eff_cols = ["eff_reading","eff_practice","eff_group","eff_flashcards","eff_videos"]
    eff_means = df[eff_cols].mean().sort_values(ascending=False)
    fig2, ax2 = plt.subplots(figsize=(8,5))
    ax2.bar(eff_means.index, eff_means.values)
    ax2.set_ylabel("Mean Effectiveness Score (1–5)")
    ax2.set_xticklabels(eff_means.index, rotation=45, ha="right")
    st.pyplot(fig2)

# ================= PAGE 2 =================
with tab2:
    st.header("Page 2 Visualizations - Stress & Motivation")
    st.write("Add your page 2 visualizations here (bar charts, heatmaps, boxplots)")

# ================= PAGE 3 =================
with tab3:
    st.header("Page 3 Visualizations - Learning Obstacles & Support")
    st.write("Add your page 3 visualizations here (bar, pie, scatter, boxplots)")
