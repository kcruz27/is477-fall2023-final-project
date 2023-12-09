# Snakefile

rule all:
  input:
    "results/alcohol_distribution.png",
    "results/classification_results.txt",
    "results/summary_statistics.csv"

rule prepare_data:
  output:
    "data/wine+quality.zip",
    "data/winequality-red.csv",
    "data/winequality-white.csv",
    "data/winequality.names"
  shell:
    "python scripts/prepare_data.py"

rule profile_data:
  input:
    "data/winequality-red.csv"
  output:
    "profiling/report.html"
  shell:
    "python scripts/profile.py"

rule analyze_data:
  input:
    "data/winequality-red.csv"
  output:
    "results/alcohol_distribution.png",
    "results/classification_results.txt",
    "results/summary_statistics.csv"
  shell:
    "python scripts/analysis.py"