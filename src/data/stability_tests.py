import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing

from evidently import ColumnMapping

from evidently.report import Report
from evidently.metrics.base_metric import generate_column_metrics
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset
from evidently.metrics import *

from evidently.test_suite import TestSuite
from evidently.tests.base_test import generate_column_tests
from evidently.test_preset import DataStabilityTestPreset, NoTargetPerformanceTestPreset
from evidently.tests import *

#"TestColumnsType, TestNumberOfDriftedColumns"

df_current = pd.read_csv("../../data/processed/current_data.csv",index_col=0)

df_reference = pd.read_csv("../../data/processed/reference_data.csv",index_col=0)

tests = TestSuite(tests=[
    TestColumnsType(),
    TestNumberOfDriftedColumns()
])

tests.run(reference_data=df_reference, current_data=df_current)
tests.save_html("../../reports/stability_report.html")