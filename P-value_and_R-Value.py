# Importing packages
import pandas as pd
from scipy import stats

df = pd.read_csv("BoxPlotStats2.0.csv")
HeaderName = df.head

#Heading names
Name = df["TubeName"]
TubeType = df["TubeType"]
SameTube = df["SameTube"]
PeakWidth = df["PeakWidth"]
Absolute = df["Absolute"]
SN = df["SN"]
Intensity = df["Intensity"]
BLN = df["BaselineNoise"]
Quality = df["Quality"]
TubeTypeNum = df["TubeTypeNum"]
Cost = df["Cost"]
DO = df["DiameterOuter"]
MOEO = df["MOEO"]
DI = df["DiameterInner"]
MOEI = df["MOEI"]
Concentricity = df["Concentricity"]
Camber = df["Camber"]
Freq = df["Frequency"]
ThickWall = df["ThicknessWall"]
QualityTube = df["QualityTube"]
CostvsQuality = df["CostvsQuality"]


print("-----------------------------------------------------------")
corr_PeakWidth_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_Absolute_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_SN_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_Intensity_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_BLN_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_Quality_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_TubeTypeNum_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_Cost_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_DO_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_MOEO_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_DI_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_MOEI_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_Concentricity_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_Camber_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_Freq_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_ThickWall_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_QualityTube_df = pd.DataFrame(columns=['correlation', 'pvalue'])
corr_CostvsQuality_df = pd.DataFrame(columns=['correlation', 'pvalue'])


# PeakWidth
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(PeakWidth, df[col])
        corr_PeakWidth_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Peak Width of acetone correlation and p-values___","\n",corr_PeakWidth_df,"\n\n")

# Absolute
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(Absolute, df[col])
        corr_Absolute_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Absolute correlation and p-values___","\n",corr_Absolute_df,"\n\n")

# Signal to Noise
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(SN, df[col])
        corr_SN_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Signal to Noise correlation and p-values___ \n", corr_SN_df, "\n\n")

# Intensity
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(Intensity, df[col])
        corr_Intensity_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Intensity correlation and p-values___ \n", corr_Intensity_df, "\n\n")

# BLN
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(BLN, df[col])
        corr_BLN_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Base Line Noise correlation and p-values___", "\n",corr_BLN_df,"\n\n")

# Quality
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(Quality, df[col])
        corr_Quality_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Quality correlation and p-values___","\n",corr_Quality_df, "\n\n")

# TubeTypeNum
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(TubeTypeNum, df[col])
        corr_TubeTypeNum_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___TubeTypeNum correlation and p-values___","\n",corr_TubeTypeNum_df, "\n\n")


# Cost
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(Cost, df[col])
        corr_Cost_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___cost of tube correlation and p-values___","\n",corr_Cost_df, "\n\n")

# DO
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(DO, df[col])
        corr_DO_df.loc[col] = [round(correlation, 6), round(pvalue, 6)]
print("___Diameter outer correlation and p-values___","\n",corr_DO_df,"\n\n")


# MOEO
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(MOEO, df[col])
        corr_MOEO_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Margin of error of outer diameter correlation and p-values___ \n",corr_MOEO_df, "\n\n")

# DI
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(DI, df[col])
        corr_DI_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Diameter inner correlation and p-values___\n", corr_DI_df, "\n\n")

# MOEI
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(MOEI, df[col])
        corr_MOEI_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Margin of error of inner diameter correlation and p-values___\n", corr_MOEI_df, "\n\n")

# Concentricity
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(Concentricity, df[col])
        corr_Concentricity_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Concentricity correlation and p-values___ \n", corr_Concentricity_df, "\n\n")

# Camber
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(Camber, df[col])
        corr_Camber_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Camber correlation and p-values___ \n", corr_Camber_df, "\n\n")

#  Frequency
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(Freq, df[col])
        corr_Freq_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Frequency of Tubes correlation and p-values___ \n",corr_Freq_df, "\n\n")

# Thickeness of Wall
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(ThickWall, df[col])
        corr_ThickWall_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___Thickness of Wall correlation and p-values___ \n",corr_ThickWall_df,"\n\n")


# QualityTube
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(QualityTube, df[col])
        corr_QualityTube_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("QualityTube Correlation and p-values___ \n",corr_QualityTube_df,"\n\n")




# CostvsQuality
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]):
        correlation, pvalue = stats.pearsonr(CostvsQuality, df[col])
        corr_CostvsQuality_df.loc[col] = [round(correlation, 5), round(pvalue, 5)]
print("___ CostvsQuality Correlation and p-values___ \n",corr_CostvsQuality_df,"\n\n")


