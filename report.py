from pathlib import Path
from utils import create_output_folder
def generate_report(original_columns,
    final_columns,
    output_dataset_path):
    create_output_folder()
    report_path = Path("outputs") / "feature_engineering_report.txt"
    with open(report_path, "w") as file:
        report = f"""
        =====================================
        FEATURE ENGINEERING REPORT
        =====================================

        Original Columns : {original_columns}
        Final Columns    : {final_columns}
        Features Added   : {final_columns - original_columns}

        Output Dataset:
        {output_dataset_path}
        """

        file.write(report)
        