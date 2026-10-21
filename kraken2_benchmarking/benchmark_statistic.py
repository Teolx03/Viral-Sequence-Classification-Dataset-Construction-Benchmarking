import pandas as pd
import numpy as np
import math

# ===== 1. Load Kraken result CSV =====
df = pd.read_csv("TESTING_1000bp_18000_per_read_summary.csv")

print(f"Dataset size: {df.shape}")
print(f"Columns: {list(df.columns)}")

print("\nFirst 5 rows:")
print(df.head())

# Keep only rows where true_label is 'virus' or 'bacteria'
df = df[df["true_label"].isin(["virus", "bacteria"])].copy()

print(f"\nNumber of virus sequences: {(df['true_label'] == 'virus').sum()}")
print(f"Number of bacteria sequences: {(df['true_label'] == 'bacteria').sum()}")

# ===== 2. Compute Confusion Matrix =====
TP = TN = FP = FN = 0

for _, row in df.iterrows():
    t = row["true_label"]
    p = row["pred_label"]

    if t == "virus" and p == "virus":
        TP += 1
    elif t == "bacteria" and p == "bacteria":
        TN += 1
    elif t == "bacteria" and p == "virus":
        FP += 1
    elif t == "virus" and p == "bacteria":
        FN += 1
    # Handle 'other' predictions: treat them as incorrect predictions
    elif t == "virus" and p == "other":
        FN += 1
    elif t == "bacteria" and p == "other":
        FP += 1

# Classification metrics
def safe_divide(a, b):
    return a / b if b != 0 else 0

accuracy    = safe_divide(TP + TN, TP + TN + FP + FN)
precision   = safe_divide(TP, TP + FP)
recall      = safe_divide(TP, TP + FN)          # sensitivity
specificity = safe_divide(TN, TN + FP)
f1          = safe_divide(2 * precision * recall, precision + recall)

denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
mcc = (TP * TN - FP * FN) / denominator if denominator > 0 else 0


# ===== 3. Print Results =====
print("\n" + "="*60)
print("Kraken Benchmark Results")
print("="*60)

print("\nDataset Statistics:")
print(f"Total sequences: {len(df)}")
print(f"Virus sequences: {(df['true_label'] == 'virus').sum()}")
print(f"Bacteria sequences: {(df['true_label'] == 'bacteria').sum()}")

print("\nConfusion Matrix:")
print("+" + "-"*23 + "+")
print("|         Predicted      |")
print("|  bacteria  |   virus   |")
print("+" + "-"*23 + "+")
print(f"|   {TN:6d}    |   {FP:6d}   |  bacteria")
print("+" + "-"*23 + "+")
print(f"|   {FN:6d}    |   {TP:6d}   |  virus")
print("+" + "-"*23 + "+")

print("\nPerformance Metrics:")
print("-" * 40)
print(f"Accuracy:           {accuracy:.4f} ({accuracy*100:.1f}%)")
print(f"Precision:          {precision:.4f} ({precision*100:.1f}%)")
print(f"Recall (Sensitivity): {recall:.4f} ({recall*100:.1f}%)")
print(f"Specificity:        {specificity:.4f} ({specificity*100:.1f}%)")
print(f"F1 Score:           {f1:.4f}")


print("\nDetailed Statistics:")
print("-" * 40)
print(f"True Positives (TP):  {TP}")
print(f"True Negatives (TN):  {TN}")
print(f"False Positives (FP): {FP}")
print(f"False Negatives (FN): {FN}")
print(f"False Positive Rate:  {FP/(TN+FP) if (TN+FP)>0 else 0:.4f}")
print(f"False Negative Rate:  {FN/(TP+FN) if (TP+FN)>0 else 0:.4f}")
